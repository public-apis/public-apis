#!/usr/bin/env node
// Finds every link in the README (from "## Index" onward), flags
// duplicates, and — unless
// --duplicates-only is passed — live-checks each one over HTTP.
"use strict";

const path = require("path");
const { findLinksInFile, checkDuplicateLinks, checkLinksWorking } = require("./links");

function parseArgs(argv) {
  const positional = argv.filter((a) => !a.startsWith("--"));
  const duplicatesOnly = argv.includes("--duplicates-only") || argv.includes("-odlc");
  const filename = positional[0] || path.join(__dirname, "..", "README.md");
  return { filename, duplicatesOnly };
}

async function main() {
  const { filename, duplicatesOnly } = parseArgs(process.argv.slice(2));
  const links = findLinksInFile(filename);

  console.log(`Checking for duplicate links among ${links.length} found...`);
  const { hasDuplicates, duplicates } = checkDuplicateLinks(links);
  if (hasDuplicates) {
    console.error("Found duplicate links:");
    for (const link of duplicates) console.error(link);
    process.exit(1);
  }
  console.log("No duplicate links.");

  if (duplicatesOnly) return;

  console.log(`Checking if ${links.length} links are working (this can take a while)...`);
  const errors = await checkLinksWorking(links);
  if (errors.length > 0) {
    console.error(`${errors.length} link(s) are not working properly:`);
    for (const error of errors) console.error(error);
    process.exit(1);
  }
  console.log("All links are working.");
}

if (require.main === module) main();

module.exports = { parseArgs };
