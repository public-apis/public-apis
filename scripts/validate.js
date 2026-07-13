#!/usr/bin/env node
// Validates README.md's category tables against CONTRIBUTING.md rules.
// Includes checks for trailing "API" names, empty descriptions, final-category
// entry counts, and duplicate name-and-URL entries.
"use strict";

const fs = require("fs");
const path = require("path");
const {
  CATEGORY_RE,
  LINK_CELL_RE,
  SEPARATOR_CELL_RE,
  stripBackticks,
  splitRow,
  splitRowRaw,
  isPromotedUrl,
} = require("./row-parser");

const README_PATH = process.argv[2] || path.join(__dirname, "..", "README.md");

const AUTH_KEYS = ["apiKey", "OAuth", "X-Mashape-Key", "User-Agent", "No"];
const HTTPS_KEYS = ["Yes", "No"];
const CORS_KEYS = ["Yes", "No", "Unknown"];
const MIN_ENTRIES_PER_CATEGORY = 3;
const MAX_DESCRIPTION_LENGTH = 100;
// "()" is temporarily allowed at the end of a description (upstream's own
// carve-out — many descriptions end with a parenthetical).
const END_PUNCTUATION_RE = /[!"#$%&'*+,\-./:;<=>?@[\\\]^_`{|}~]$/;
// NOTE: CONTRIBUTING.md also says not to tack a TLD onto a name (e.g.
// "Gmail.com" -> "Gmail"), but that's intentionally NOT checked here: too
// many real API names legitimately end in .io/.com/.net as their actual
// registered brand (File.io, RAWG.io, Battle.net, Host.io, ...). A regex
// on the suffix can't distinguish "lazy TLD suffix" from "that's the name" —
// flagging it produced dozens of false positives on the real README, which
// is worse than not checking it at all. Left to human review.
//
// The trailing-"API" check below intentionally only matches a *space*
// before "api" (mirroring CONTRIBUTING.md's own example: "Gmail API" ->
// "Gmail"), not a hyphen or no separator at all — "ip-api", "weather-api",
// "ExchangeRate-API", and "Pokéapi" are each the service's actual
// registered/repo name, not a contributor redundantly appending "API".
// The upstream check already narrowly targets the space-separated case;
// this only fixes its robustness (it broke on trailing punctuation like
// "Gmail API."), it doesn't widen what counts as a violation.
const TRAILING_API_RE = /\sapi[.!?,;:'")\]]*\s*$/i;
const INDEX_ANCHOR_RE = /^\*\s\[(.*)\]\(#/;

function fmt(lineNum, message) {
  return `L${lineNum + 1}: ${message}`;
}

// Index section runs from "## Index" up to the first "### Category" header.
function collectIndexCategories(lines) {
  const names = new Set();
  let inIndex = false;
  for (const line of lines) {
    if (/^## Index/.test(line)) {
      inIndex = true;
      continue;
    }
    if (inIndex && CATEGORY_RE.test(line)) break;
    if (!inIndex) continue;
    const m = INDEX_ANCHOR_RE.exec(line);
    if (m) names.add(m[1].trim());
  }
  return names;
}

function checkTitle(lineNum, cell) {
  const errors = [];
  const linkMatch = LINK_CELL_RE.exec(cell);
  if (!linkMatch) {
    errors.push(fmt(lineNum, 'title syntax should be "[TITLE](LINK)"'));
    return { errors, title: null };
  }
  const title = linkMatch[1];

  if (TRAILING_API_RE.test(title)) {
    errors.push(
      fmt(lineNum, `title "${title}" should not end with "API" — every entry here is an API`)
    );
  }
  return { errors, title };
}

function checkDescription(lineNum, description) {
  const errors = [];
  if (description.length === 0) {
    errors.push(fmt(lineNum, "description is empty"));
    return errors;
  }

  const firstChar = description[0];
  if (firstChar.toUpperCase() !== firstChar && firstChar.toLowerCase() !== firstChar) {
    // not a letter at all (e.g. starts with a digit/symbol) — not an error on its own
  } else if (firstChar.toUpperCase() !== firstChar) {
    errors.push(fmt(lineNum, "first character of description is not capitalized"));
  }

  const lastChar = description[description.length - 1];
  if (END_PUNCTUATION_RE.test(lastChar)) {
    errors.push(fmt(lineNum, `description should not end with "${lastChar}"`));
  }

  if (description.length > MAX_DESCRIPTION_LENGTH) {
    errors.push(
      fmt(
        lineNum,
        `description should not exceed ${MAX_DESCRIPTION_LENGTH} characters (currently ${description.length})`
      )
    );
  }
  return errors;
}

function checkAuth(lineNum, auth) {
  const errors = [];
  if (auth !== "No" && !(auth.startsWith("`") && auth.endsWith("`") && auth.length > 1)) {
    errors.push(fmt(lineNum, `auth value "${auth}" is not enclosed in backticks`));
  }
  if (!AUTH_KEYS.includes(stripBackticks(auth))) {
    errors.push(fmt(lineNum, `"${auth}" is not a valid Auth option`));
  }
  return errors;
}

function checkHttps(lineNum, https) {
  if (!HTTPS_KEYS.includes(https)) {
    return [fmt(lineNum, `"${https}" is not a valid HTTPS option`)];
  }
  return [];
}

function checkCors(lineNum, cors) {
  if (!CORS_KEYS.includes(cors)) {
    return [fmt(lineNum, `"${cors}" is not a valid CORS option`)];
  }
  return [];
}

function checkSpacing(lineNum, rawCells) {
  const errors = [];
  for (const cell of rawCells) {
    const leading = cell.length - cell.trimStart().length;
    const trailing = cell.length - cell.trimEnd().length;
    if (leading !== 1 || trailing !== 1) {
      errors.push(fmt(lineNum, "each table cell must have exactly one space on either side"));
      break;
    }
  }
  return errors;
}

function validateReadme(text) {
  const lines = text.split("\n");
  const errors = [];
  const indexCategories = collectIndexCategories(lines);

  let currentCategory = null;
  let currentCategoryLine = 0;
  let entriesInCategory = [];
  let sawDividerRow = false; // the "| API | Description | ... |" header row precedes the divider and isn't data
  const entryOccurrences = new Map(); // `${name.toLowerCase()}::${url}` -> README locations

  function flushCategory() {
    if (currentCategory === null) return;
    if (entriesInCategory.length < MIN_ENTRIES_PER_CATEGORY) {
      errors.push(
        fmt(
          currentCategoryLine,
          `category "${currentCategory}" has only ${entriesInCategory.length} entries (minimum ${MIN_ENTRIES_PER_CATEGORY})`
        )
      );
    }
    const firstOrganic = entriesInCategory.findIndex((entry) => !entry.promoted);
    if (
      firstOrganic !== -1 &&
      entriesInCategory.slice(firstOrganic + 1).some((entry) => entry.promoted)
    ) {
      errors.push(
        fmt(currentCategoryLine, `category "${currentCategory}" has a promoted entry below organic entries`)
      );
    }
    const titles = entriesInCategory
      .filter((entry) => !entry.promoted)
      .map((entry) => entry.title.toLowerCase());
    const sorted = [...titles].sort();
    if (JSON.stringify(titles) !== JSON.stringify(sorted)) {
      errors.push(fmt(currentCategoryLine, `category "${currentCategory}" is not in alphabetical order`));
    }
  }

  lines.forEach((line, lineNum) => {
    const catMatch = CATEGORY_RE.exec(line.trim());
    if (catMatch) {
      flushCategory(); // validate the category we're leaving, including the last one at EOF
      currentCategory = catMatch[1].trim();
      currentCategoryLine = lineNum;
      entriesInCategory = [];
      sawDividerRow = false;
      if (!indexCategories.has(currentCategory)) {
        errors.push(fmt(lineNum, `category "${currentCategory}" is missing from the ## Index section`));
      }
      return;
    }

    if (!currentCategory || !line.trim().startsWith("|")) return;

    const rawCells = splitRowRaw(line);
    const cells = splitRow(line);
    if (cells.length < 2 || SEPARATOR_CELL_RE.test(cells[1])) {
      sawDividerRow = true; // this line itself is the "|---|:---|...|" row
      return;
    }
    if (!sawDividerRow) return; // the "| API | Description | ... |" label row, not data

    // A stray trailing "| |" (empty extra cell) is a widespread pre-existing
    // formatting quirk in this file, not a real extra data column — only
    // flag when there are too few cells, or extra cells actually hold content.
    if (cells.length < 5 || cells.slice(5).some((c) => c.length > 0)) {
      errors.push(fmt(lineNum, `entry has ${cells.length} columns, needs 5`));
      return;
    }

    errors.push(...checkSpacing(lineNum, rawCells));

    const { errors: titleErrors, title } = checkTitle(lineNum, cells[0]);
    errors.push(...titleErrors);

    const [, description, auth, https, cors] = cells;
    errors.push(...checkDescription(lineNum, description));
    errors.push(...checkAuth(lineNum, auth));
    errors.push(...checkHttps(lineNum, https));
    errors.push(...checkCors(lineNum, cors));

    if (title) {
      const linkMatch = LINK_CELL_RE.exec(cells[0]);
      const url = linkMatch ? linkMatch[2].trim() : "";
      entriesInCategory.push({ title, promoted: isPromotedUrl(url) });
      const key = `${title.toLowerCase()}::${url}`;
      const occurrences = entryOccurrences.get(key) || [];
      occurrences.push({ lineNum, title, url });
      entryOccurrences.set(key, occurrences);
    }
  });

  flushCategory(); // the final category in the file, otherwise never checked

  // Report every copy so a newly inserted duplicate is still attached to the
  // changed line even when the original entry appears later in the README.
  for (const occurrences of entryOccurrences.values()) {
    if (occurrences.length < 2) continue;
    for (const { lineNum, title, url } of occurrences) {
      errors.push(fmt(lineNum, `duplicate entry "${title}" (${url})`));
    }
  }

  return errors;
}

function main() {
  const readme = fs.readFileSync(README_PATH, "utf8");
  const errors = validateReadme(readme);

  if (errors.length > 0) {
    for (const e of errors) console.error(e);
    console.error(`\n${errors.length} validation error(s) found in ${README_PATH}`);
    process.exit(1);
  }

  console.log(`${README_PATH} is valid.`);
}

if (require.main === module) main();

module.exports = { validateReadme };
