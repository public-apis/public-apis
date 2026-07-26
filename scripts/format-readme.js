#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const {
  CATEGORY_RE,
  LINK_CELL_RE,
  SEPARATOR_CELL_RE,
  splitRow,
  isPromotedRow,
} = require("./row-parser");

const README_PATH = process.argv[2] || path.join(__dirname, "..", "README.md");

function rowTitle(row) {
  const [titleCell = ""] = splitRow(row);
  const match = LINK_CELL_RE.exec(titleCell);
  return (match ? match[1] : titleCell).toLowerCase();
}

function compareRows(left, right) {
  const leftTitle = rowTitle(left);
  const rightTitle = rowTitle(right);
  if (leftTitle < rightTitle) return -1;
  if (leftTitle > rightTitle) return 1;
  return 0;
}

function sortCategoryRows(text) {
  const lines = text.split("\n");

  for (let index = 0; index < lines.length; index += 1) {
    if (!CATEGORY_RE.test(lines[index].trim())) continue;

    let divider = index + 1;
    while (divider < lines.length) {
      const cells = lines[divider].trim().startsWith("|") ? splitRow(lines[divider]) : [];
      if (cells.length > 1 && SEPARATOR_CELL_RE.test(cells[1])) break;
      if (CATEGORY_RE.test(lines[divider].trim())) break;
      divider += 1;
    }
    if (divider >= lines.length) continue;

    const start = divider + 1;
    let end = start;
    while (end < lines.length && lines[end].trim().startsWith("|")) end += 1;

    const rows = lines.slice(start, end);
    // Paid placements are intentionally pinned above the alphabetical list.
    // Array#filter preserves their configured order; only organic rows sort.
    const promoted = rows.filter(isPromotedRow);
    const sorted = [...promoted, ...rows.filter((row) => !isPromotedRow(row)).sort(compareRows)];
    lines.splice(start, sorted.length, ...sorted);
    index = end - 1;
  }

  return lines.join("\n");
}

function main() {
  const original = fs.readFileSync(README_PATH, "utf8");
  const formatted = sortCategoryRows(original);
  fs.writeFileSync(README_PATH, formatted);
  console.log(original === formatted ? `${README_PATH} is already sorted.` : `Sorted ${README_PATH}.`);
}

if (require.main === module) main();

module.exports = { compareRows, rowTitle, sortCategoryRows };
