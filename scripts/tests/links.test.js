"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { findLinksInText, checkDuplicateLinks, getHostFromLink } = require("../links");
const { extractAddedLines, extractRemovedLines, findNewLinksInDiff } = require("../check-pr-links");

test("finds links in text", () => {
  const text = "| [Cats](https://example.com/cats) | Pictures | No | Yes | No |";
  assert.deepEqual(findLinksInText(text), ["https://example.com/cats"]);
});

test("flags the second occurrence of a duplicate link, ignoring trailing slash", () => {
  const links = ["https://a.com", "https://a.com/", "https://b.com"];
  const { hasDuplicates, duplicates } = checkDuplicateLinks(links);
  assert.equal(hasDuplicates, true);
  assert.deepEqual(duplicates, ["https://a.com"]);
});

test("does not flag links that only appear once", () => {
  const links = ["https://a.com", "https://b.com"];
  const { hasDuplicates } = checkDuplicateLinks(links);
  assert.equal(hasDuplicates, false);
});

test("extracts the host from a link", () => {
  assert.equal(getHostFromLink("https://example.com/path?x=1"), "example.com");
  assert.equal(getHostFromLink("example.com/path"), "example.com");
});

test("extractAddedLines only keeps real additions, not the +++ file header", () => {
  const diff = [
    "--- a/README.md",
    "+++ b/README.md",
    "@@ -1,2 +1,3 @@",
    " unchanged line",
    "+| [New](https://example.com/new) | Desc | No | Yes | No |",
    "-| [Old](https://example.com/old) | Desc | No | Yes | No |",
  ].join("\n");

  const added = extractAddedLines(diff);
  assert.deepEqual(added, ["| [New](https://example.com/new) | Desc | No | Yes | No |"]);
});

test("extractRemovedLines only keeps real removals, not the --- file header", () => {
  const diff = [
    "--- a/README.md",
    "+++ b/README.md",
    "@@ -1,2 +1,2 @@",
    "-| [Old](https://example.com/old) | Old description | No | Yes | No |",
    "+| [Old](https://example.com/old) | New description | No | Yes | No |",
  ].join("\n");

  assert.deepEqual(extractRemovedLines(diff), [
    "| [Old](https://example.com/old) | Old description | No | Yes | No |",
  ]);
});

test("does not treat moved or edited existing links as new", () => {
  const diff = [
    "--- a/README.md",
    "+++ b/README.md",
    "@@ -1,2 +1,3 @@",
    "-| [Old](https://example.com/old/) | Old description | No | Yes | No |",
    "+| [Old](https://example.com/old) | New description | No | Yes | No |",
    "+| [New](https://example.com/new) | New API | No | Yes | No |",
  ].join("\n");

  const { addedLinks, newLinks } = findNewLinksInDiff(diff);
  assert.deepEqual(addedLinks, ["https://example.com/old", "https://example.com/new"]);
  assert.deepEqual(newLinks, ["https://example.com/new"]);
});

test("ignores links changed outside README.md", () => {
  const diff = [
    "diff --git a/scripts/example.js b/scripts/example.js",
    "--- a/scripts/example.js",
    "+++ b/scripts/example.js",
    "@@ -0,0 +1 @@",
    "+const url = 'https://example.com/not-readme';",
    "diff --git a/README.md b/README.md",
    "--- a/README.md",
    "+++ b/README.md",
    "@@ -0,0 +1 @@",
    "+| [New](https://example.com/readme) | New API | No | Yes | No |",
  ].join("\n");

  assert.deepEqual(extractAddedLines(diff), [
    "| [New](https://example.com/readme) | New API | No | Yes | No |",
  ]);
});
