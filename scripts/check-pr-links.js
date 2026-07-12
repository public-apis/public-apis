#!/usr/bin/env node
// JS port of `scripts/github_pull_request.sh`: fetches a PR's raw diff,
// extracts only the *added* lines, and runs the duplicate + liveness link
// check scoped to just those new links — cheap enough to run on every PR
// without hitting rate limits, unlike checking all ~1,400 existing links.
"use strict";

const { findLinksInText, checkDuplicateLinks, checkLinksWorking } = require("./links");

function parseArgs(argv) {
  const [repo, prNumber] = argv;
  if (!repo || !prNumber) {
    console.error("Usage: node check-pr-links.js <owner/repo> <pull-number>");
    process.exit(1);
  }
  if (!/^\d+$/.test(prNumber)) {
    console.error(`Invalid pull request number: "${prNumber}"`);
    process.exit(1);
  }
  return { repo, prNumber };
}

async function fetchDiff(repo, prNumber) {
  const url = `https://patch-diff.githubusercontent.com/raw/${repo}/pull/${prNumber}.diff`;
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch diff for PR #${prNumber}: HTTP ${response.status}`);
  }
  return response.text();
}

// Real added lines only: "+" at the very start, excluding the "+++ b/..."
// file-header line diff itself uses.
function extractAddedLines(diffText) {
  return diffText
    .split("\n")
    .filter((line) => line.startsWith("+") && !line.startsWith("+++"))
    .map((line) => line.slice(1));
}

async function main() {
  const { repo, prNumber } = parseArgs(process.argv.slice(2));

  console.log(`Fetching diff for ${repo}#${prNumber}...`);
  const diffText = await fetchDiff(repo, prNumber);
  const addedLines = extractAddedLines(diffText);
  const links = findLinksInText(addedLines.join("\n"));

  console.log(`Found ${links.length} link(s) in the added lines.`);
  if (links.length === 0) return;

  const { hasDuplicates, duplicates } = checkDuplicateLinks(links);
  if (hasDuplicates) {
    console.error("Found duplicate links in this PR's additions:");
    for (const link of duplicates) console.error(link);
    process.exit(1);
  }

  console.log(`Checking if ${links.length} newly-added link(s) are working...`);
  const errors = await checkLinksWorking(links);
  if (errors.length > 0) {
    console.error(`${errors.length} newly-added link(s) are not working:`);
    for (const error of errors) console.error(error);
    process.exit(1);
  }
  console.log("All newly-added links are working.");
}

if (require.main === module) {
  main().catch((error) => {
    console.error(error.message);
    process.exit(1);
  });
}

module.exports = { extractAddedLines };
