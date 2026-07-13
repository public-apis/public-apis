#!/usr/bin/env node
// Parses README.md's category tables into the website backend's JSON datasets.
"use strict";

const fs = require("fs");
const path = require("path");
const {
  CATEGORY_RE,
  LINK_CELL_RE,
  SEPARATOR_CELL_RE,
  stripBackticks,
  parseBool,
  splitRow,
} = require("./row-parser");

const README_PATH = process.argv[2] || path.join(__dirname, "..", "README.md");
const OUT_DIR = process.argv[3] || path.join(__dirname, "..", "data");

// Mirrors GitHub's markdown heading-anchor algorithm, so a category's slug
// matches the #anchor the README's own "## Index" section links to
// (e.g. "Art & Design" -> "art--design").
function githubSlug(title) {
  return title
    .toLowerCase()
    .replace(/[^a-z0-9 -]/g, "")
    .replace(/ /g, "-");
}

function parseReadme(text) {
  const lines = text.split("\n");
  const apis = [];
  const categoryCounts = new Map(); // name -> entry count, insertion order = README order

  let currentCategory = null;

  for (const line of lines) {
    const catMatch = CATEGORY_RE.exec(line.trim());
    if (catMatch) {
      currentCategory = catMatch[1].trim();
      if (!categoryCounts.has(currentCategory)) categoryCounts.set(currentCategory, 0);
      continue;
    }
    if (!currentCategory || !line.trim().startsWith("|")) continue;

    const cells = splitRow(line);
    if (cells.length < 5) continue;
    if (SEPARATOR_CELL_RE.test(cells[1])) continue; // header divider row

    const linkMatch = LINK_CELL_RE.exec(cells[0]);
    if (!linkMatch) continue;

    const [, name, url] = linkMatch;
    const [, description, auth, https, cors] = cells;

    categoryCounts.set(currentCategory, categoryCounts.get(currentCategory) + 1);
    apis.push({
      name: name.trim(),
      description: description.trim(),
      auth: stripBackticks(auth),
      https: parseBool(https),
      cors: cors.trim(),
      url: url.trim(),
      category: currentCategory,
    });
  }

  const categories = Array.from(categoryCounts.entries())
    .map(([name, count]) => ({ name, slug: githubSlug(name), count }))
    .sort((a, b) => a.name.localeCompare(b.name));

  return { apis, categories };
}

function main() {
  const readme = fs.readFileSync(README_PATH, "utf8");
  const { apis, categories } = parseReadme(readme);

  if (apis.length === 0) {
    console.error("No APIs parsed — README format may have changed. Aborting.");
    process.exit(1);
  }

  fs.mkdirSync(OUT_DIR, { recursive: true });

  const apisJson = JSON.stringify({ count: apis.length, entries: apis }, null, 2);
  const categoriesJson = JSON.stringify(
    { count: categories.length, totalApis: apis.length, categories },
    null,
    2
  );

  fs.writeFileSync(path.join(OUT_DIR, "apis.json"), apisJson + "\n");
  fs.writeFileSync(path.join(OUT_DIR, "categories.json"), categoriesJson + "\n");

  console.log(`Parsed ${apis.length} APIs across ${categories.length} categories.`);
  console.log(`Wrote apis.json and categories.json to ${OUT_DIR}`);
}

if (require.main === module) main();

module.exports = { parseReadme, githubSlug };
