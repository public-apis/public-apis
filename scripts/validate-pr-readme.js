#!/usr/bin/env node
"use strict";

const fs = require("fs");
const { validateReadme } = require("./validate");
const { fetchDiff } = require("./check-pr-links");
const { CATEGORY_RE } = require("./row-parser");

const COMMENT_MARKER = "<!-- readme-diff-validation -->";
const INDEX_ENTRY_RE = /^\*\s\[([^\]]+)\]\(#/;

function parseReadmeDiff(diffText) {
  const touchedLines = new Set();
  const changedCategoryNames = new Set();
  let inReadme = false;
  let newLine = 0;
  let inHunk = false;

  for (const line of diffText.split("\n")) {
    if (line.startsWith("diff --git ")) {
      inReadme = line === "diff --git a/README.md b/README.md";
      inHunk = false;
      continue;
    }
    if (!inReadme) continue;

    const hunk = /^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@/.exec(line);
    if (hunk) {
      newLine = Number(hunk[1]);
      inHunk = true;
      continue;
    }
    if (!inHunk || line.startsWith("+++") || line.startsWith("---")) continue;

    if (line.startsWith("+")) {
      touchedLines.add(newLine);
      collectCategoryName(line.slice(1), changedCategoryNames);
      newLine += 1;
    } else if (line.startsWith("-")) {
      // A deletion affects the rows on either side in the proposed file.
      touchedLines.add(Math.max(1, newLine - 1));
      touchedLines.add(Math.max(1, newLine));
      collectCategoryName(line.slice(1), changedCategoryNames);
    } else if (line.startsWith(" ")) {
      newLine += 1;
    }
  }

  return { touchedLines, changedCategoryNames };
}

function collectCategoryName(line, names) {
  const category = CATEGORY_RE.exec(line.trim());
  if (category) names.add(category[1].trim());
  const indexEntry = INDEX_ENTRY_RE.exec(line.trim());
  if (indexEntry) names.add(indexEntry[1].trim());
}

function categoryAtLine(lines, oneBasedLine) {
  for (let index = Math.min(oneBasedLine - 1, lines.length - 1); index >= 0; index -= 1) {
    const match = CATEGORY_RE.exec(lines[index].trim());
    if (match) return match[1].trim();
  }
  return null;
}

function filterErrorsToDiff(errors, readmeText, diffText) {
  const { touchedLines, changedCategoryNames } = parseReadmeDiff(diffText);
  const lines = readmeText.split("\n");
  const touchedCategories = new Set(changedCategoryNames);

  for (const lineNumber of touchedLines) {
    const category = categoryAtLine(lines, lineNumber);
    if (category) touchedCategories.add(category);
  }

  return errors.filter((error) => {
    const parsed = /^L(\d+):\s*(.*)$/.exec(error);
    if (!parsed) return false;
    const lineNumber = Number(parsed[1]);
    const message = parsed[2];
    if (touchedLines.has(lineNumber)) return true;

    const categoryError = /^category "([^"]+)"/.exec(message);
    return Boolean(categoryError && touchedCategories.has(categoryError[1]));
  });
}

function errorKey(error) {
  return error.replace(/^L\d+:\s*/, "");
}

function escapeHtml(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function subtractBaselineErrors(proposedErrors, baselineErrors) {
  const baselineCounts = new Map();
  for (const error of baselineErrors) {
    const key = errorKey(error);
    baselineCounts.set(key, (baselineCounts.get(key) || 0) + 1);
  }

  return proposedErrors.filter((error) => {
    const key = errorKey(error);
    const remaining = baselineCounts.get(key) || 0;
    if (remaining === 0) return true;
    baselineCounts.set(key, remaining - 1);
    return false;
  });
}

function formatError(error, readmeUrl = "README.md") {
  const parsed = /^L(\d+):\s*(.*)$/.exec(error);
  if (!parsed) return `- <code>${escapeHtml(error)}</code>`;

  const [, lineNumber, message] = parsed;
  return `- [README.md line ${lineNumber}](${readmeUrl}#L${lineNumber}): <code>${escapeHtml(message)}</code>`;
}

function greeting(author) {
  return author ? `Hi @${author},` : "Hi there,";
}

function formatComment(errors, touchedReadme, author = "", links = {}) {
  const readmeUrl = links.readmeUrl || "README.md";
  const contributingUrl = links.contributingUrl || "CONTRIBUTING.md";
  if (!touchedReadme) {
    return `${COMMENT_MARKER}\n### Contribution check\n\n${greeting(author)}\n\nThanks for contributing! This pull request does not contain any README changes that need to be checked.`;
  }
  if (errors.length === 0) {
    return `${COMMENT_MARKER}\n### Contribution check\n\n${greeting(author)}\n\nThanks for contributing! ✅ Your README changes follow our contribution guidelines. One of our maintainers will review your pull request shortly. Thank you for your patience.`;
  }

  const details = errors.map((error) => formatError(error, readmeUrl)).join("\n");
  const issueLabel = errors.length === 1 ? "item" : "items";
  return `${COMMENT_MARKER}\n### Contribution check\n\n${greeting(author)}\n\nThanks a lot for contributing! Your pull request is nearly ready. We found ${errors.length} ${issueLabel} that could be improved to match our [contribution guidelines](${contributingUrl}):\n\n${details}\n\nPlease update the highlighted ${issueLabel}, and this check will run again automatically. If you believe a warning does not apply, feel free to explain why in a comment and a maintainer will take a look.`;
}

async function fetchReadme(repo, sha, label) {
  const url = `https://raw.githubusercontent.com/${repo}/${sha}/README.md`;
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Failed to fetch ${label} README: HTTP ${response.status}`);
  return response.text();
}

async function main() {
  const [readmePath, repo, prNumber, outputPath] = process.argv.slice(2);
  if (!readmePath || !repo || !prNumber || !outputPath) {
    throw new Error(
      "Usage: node validate-pr-readme.js <README> <owner/repo> <PR number> <comment output>"
    );
  }

  const diffText = await fetchDiff(repo, prNumber);
  const { touchedLines } = parseReadmeDiff(diffText);
  const readmeText = process.env.FETCH_HEAD_README === "true"
    ? await fetchReadme(process.env.HEAD_REPO, process.env.HEAD_SHA, "proposed")
    : fs.readFileSync(readmePath, "utf8");
  const baselineText = await fetchReadme(process.env.BASE_REPO, process.env.BASE_SHA, "base");
  const introducedErrors = subtractBaselineErrors(
    validateReadme(readmeText),
    validateReadme(baselineText)
  );
  const errors = filterErrorsToDiff(introducedErrors, readmeText, diffText);
  fs.writeFileSync(
    outputPath,
    `${formatComment(errors, touchedLines.size > 0, process.env.PR_AUTHOR, {
      readmeUrl: `https://github.com/${repo}/blob/${process.env.HEAD_SHA}/README.md`,
      contributingUrl: `https://github.com/${repo}/blob/${process.env.BASE_SHA}/CONTRIBUTING.md`,
    })}\n`
  );

  if (errors.length > 0) {
    for (const error of errors) console.error(error);
    process.exitCode = 1;
  } else {
    console.log(touchedLines.size > 0 ? "Changed README lines are valid." : "No README changes.");
  }
}

if (require.main === module) {
  main().catch((error) => {
    console.error(error.message);
    process.exit(1);
  });
}

module.exports = {
  COMMENT_MARKER,
  escapeHtml,
  filterErrorsToDiff,
  formatComment,
  formatError,
  parseReadmeDiff,
  subtractBaselineErrors,
};
