import fs from 'fs';
import path from 'path';
import { API, Category, APIData } from './types';

function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/&/g, '-')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
}

function parseAuth(auth: string): API['auth'] {
  const cleaned = auth.trim().replace(/`/g, '');
  if (cleaned === 'No') return 'No';
  if (cleaned === 'apiKey') return 'apiKey';
  if (cleaned === 'OAuth') return 'OAuth';
  if (cleaned === 'X-Mashape-Key') return 'X-Mashape-Key';
  if (cleaned === 'User-Agent') return 'User-Agent';
  return 'No';
}

function parseCors(cors: string): API['cors'] {
  const cleaned = cors.trim();
  if (cleaned === 'Yes') return 'Yes';
  if (cleaned === 'No') return 'No';
  return 'Unknown';
}

function parseAPIRow(row: string): API | null {
  // Match: | [Name](URL) | Description | Auth | HTTPS | CORS |
  const linkMatch = row.match(/\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|/);
  if (!linkMatch) return null;

  const parts = row.split('|').filter(p => p.trim());
  if (parts.length < 5) return null;

  const name = linkMatch[1].trim();
  const url = linkMatch[2].trim();
  const description = parts[1]?.trim() || '';
  const auth = parts[2]?.trim() || 'No';
  const https = parts[3]?.trim().toLowerCase() === 'yes';
  const cors = parts[4]?.trim() || 'Unknown';

  return {
    name,
    url,
    description,
    auth: parseAuth(auth),
    https,
    cors: parseCors(cors),
  };
}

export function parseReadme(content: string): APIData {
  const lines = content.split('\n');
  const categories: Category[] = [];
  let currentCategory: Category | null = null;
  let totalApis = 0;

  for (const line of lines) {
    // Check for category header (### Category Name)
    const categoryMatch = line.match(/^###\s+(.+)$/);
    if (categoryMatch) {
      const categoryName = categoryMatch[1].trim();
      // Skip non-category headers
      if (categoryName.toLowerCase() === 'index' ||
          categoryName.toLowerCase().includes('apilayer')) {
        continue;
      }

      if (currentCategory && currentCategory.apis.length > 0) {
        categories.push(currentCategory);
      }

      currentCategory = {
        name: categoryName,
        slug: slugify(categoryName),
        apis: [],
      };
      continue;
    }

    // Check for API row
    if (currentCategory && line.startsWith('|') && line.includes('](')) {
      const api = parseAPIRow(line);
      if (api) {
        currentCategory.apis.push(api);
        totalApis++;
      }
    }
  }

  // Don't forget the last category
  if (currentCategory && currentCategory.apis.length > 0) {
    categories.push(currentCategory);
  }

  return {
    categories,
    totalApis,
    lastUpdated: new Date().toISOString(),
  };
}

export function loadAPIData(): APIData {
  const readmePath = path.join(process.cwd(), '..', 'README.md');
  const content = fs.readFileSync(readmePath, 'utf-8');
  return parseReadme(content);
}
