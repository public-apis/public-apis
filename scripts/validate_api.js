#!/usr/bin/env node
/**
 * validate_api.js — Pre-submission validator for public-apis contributions
 * Run before opening a PR to catch common formatting issues.
 *
 * Usage: node scripts/validate_api.js [--fix] <api_name> <description> <auth> <https> <cors>
 * Or: node scripts/validate_api.js --table-row "| [Name](url) | Desc | Auth | Yes | Yes |"
 */

const FIX = process.argv.includes('--fix');

function error(msg) { console.error(`[ERROR] ${msg}`); }
function warn(msg) { console.warn(`[WARN]  ${msg}`); }
function info(msg) { console.log(`[INFO]  ${msg}`); }
function ok(msg) { console.log(`[OK]    ${msg}`); }

const VALID_AUTH = new Set(['OAuth', 'apiKey', 'X-Mashape-Key', 'No', 'User-Agent']);
const VALID_CORS = new Set(['Yes', 'No', 'Unknown']);
const VALID_HTTPS = new Set(['Yes', 'No']);
const MAX_DESC_LEN = 100;

let exitCode = 0;

if (process.argv.includes('--table-row')) {
  const rowIdx = process.argv.indexOf('--table-row') + 1;
  const row = process.argv[rowIdx];
  if (!row) { error('Missing table row after --table-row'); process.exit(1); }
  validateTableRow(row);
} else {
  // Arg mode: name, desc, auth, https, cors
  const args = process.argv.slice(2).filter(a => !a.startsWith('--'));
  if (args.length < 5) {
    console.log(`Usage: node scripts/validate_api.js [--fix] <name> <description> <auth> <https> <cors>
       node scripts/validate_api.js --table-row "| [Name](url) | Desc | Auth | Yes | Yes |"
       node scripts/validate_api.js --check-readme README.md`);
    process.exit(0);
  }
  const [name, desc, auth, https, cors] = args;
  validateFields({ name, desc, auth, https, cors });
}

function validateTableRow(row) {
  const cols = row.split('|').map(c => c.trim()).filter(Boolean);
  if (cols.length < 5) {
    error(`Expected 5+ columns, got ${cols.length}: "${row}"`);
    exitCode = 1;
    return;
  }

  const [nameLink, desc, auth, https, cors] = cols;
  const nameMatch = nameLink.match(/\[([^\]]+)\]\(([^)]+)\)/);
  if (!nameMatch) { error(`Invalid name link format: "${nameLink}"`); exitCode = 1; return; }

  const url = nameMatch[2];
  validateFields({ name: nameMatch[1], desc, auth, https, cors, url });
}

function validateFields({ name, desc, auth, https, cors, url }) {
  // Name checks
  if (name.endsWith(' API')) {
    error(`Name must not end with "API": "${name}"`);
    exitCode = 1;
  } else ok(`Name: ${name}`);

  if (name.includes('.com') || name.includes('.io') || name.includes('.org') || name.includes('www.')) {
    warn(`Name should not contain TLD: "${name}"`);
  }

  // URL check
  if (url) {
    try {
      new URL(url);
      ok(`URL: ${url}`);
    } catch {
      error(`Invalid URL: "${url}"`);
      exitCode = 1;
    }
  }

  // Description checks
  const descClean = desc.replace(/[`*_]/g, '');
  if (descClean.length > MAX_DESC_LEN) {
    error(`Description too long (${descClean.length}/${MAX_DESC_LEN}): "${descClean}"`);
    exitCode = 1;
  } else ok(`Description: ${descClean} (${descClean.length} chars)`);

  if (/[!?.]$/.test(descClean)) {
    warn(`Description should not end with punctuation: "${descClean}"`);
  }

  // Auth check
  const authClean = auth.replace(/`/g, '').trim();
  if (!VALID_AUTH.has(authClean)) {
    error(`Invalid Auth value "${authClean}". Must be one of: ${[...VALID_AUTH].join(', ')}`);
    exitCode = 1;
  } else ok(`Auth: ${authClean}`);

  // HTTPS check
  const httpsClean = https.toLowerCase();
  if (!VALID_HTTPS.has(httpsClean === 'ye' ? 'Yes' : httpsClean.charAt(0).toUpperCase() + httpsClean.slice(1))) {
    error(`Invalid HTTPS value "${https}". Must be Yes or No`);
    exitCode = 1;
  } else ok(`HTTPS: ${https}`);

  // CORS check
  const corsLower = cors.toLowerCase();
  const corsClean = cors.charAt(0).toUpperCase() + cors.slice(1).toLowerCase();
  if (['unkown', 'unknown'].includes(corsLower)) {
    warn(`CORS "Unkown" is a known typo in source data — will be normalized`);
  }
  if (!VALID_CORS.has(corsClean)) {
    error(`Invalid CORS value "${cors}". Must be Yes, No, or Unknown`);
    exitCode = 1;
  } else ok(`CORS: ${corsClean}`);

  if (exitCode === 0) {
    console.log('\n✓ All checks passed!');
  } else {
    console.log(`\n✗ ${exitCode} error(s) found. Fix above issues before submitting PR.`);
  }
}

process.exit(exitCode);
