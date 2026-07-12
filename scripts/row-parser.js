// Shared markdown-table parsing helpers used by generate.js and validate.js.
"use strict";

const CATEGORY_RE = /^### (.+)$/;
// First cell of a row must be a markdown link: [Name](url)
const LINK_CELL_RE = /^\[([^\]]+)\]\(([^)]+)\)$/;
const SEPARATOR_CELL_RE = /^:?-+:?$/;

function stripBackticks(s) {
  return s.replace(/`/g, "").trim();
}

function parseBool(s) {
  return s.trim().toLowerCase() === "yes";
}

// Splits a markdown table row into trimmed cells, dropping the empty
// leading/trailing cells produced by leading/trailing "|".
function splitRow(line) {
  const trimmed = line.trim().replace(/^\|/, "").replace(/\|$/, "");
  return trimmed.split("|").map((c) => c.trim());
}

// Same split, but without trimming each cell — needed to check the
// "exactly one space on each side" spacing rule from CONTRIBUTING.md.
function splitRowRaw(line) {
  const trimmed = line.trim().replace(/^\|/, "").replace(/\|$/, "");
  return trimmed.split("|");
}

module.exports = {
  CATEGORY_RE,
  LINK_CELL_RE,
  SEPARATOR_CELL_RE,
  stripBackticks,
  parseBool,
  splitRow,
  splitRowRaw,
};
