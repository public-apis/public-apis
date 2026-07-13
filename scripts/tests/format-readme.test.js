"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { sortCategoryRows } = require("../format-readme");

const unsorted = [
  "Intro",
  "### Animals",
  "API | Description | Auth | HTTPS | CORS |",
  "|:---|:---|:---|:---|:---|",
  "| [Zebra](https://example.com/z) | Zebra data | No | Yes | No |",
  "| [Ant](https://example.com/a) | Ant data | No | Yes | No |",
  "",
  "Back to index",
].join("\n");

test("sorts API rows by title inside a category", () => {
  const formatted = sortCategoryRows(unsorted);
  assert.ok(formatted.indexOf("[Ant]") < formatted.indexOf("[Zebra]"));
});

test("preserves Markdown outside API rows", () => {
  const formatted = sortCategoryRows(unsorted);
  assert.ok(formatted.startsWith("Intro\n### Animals"));
  assert.ok(formatted.endsWith("\nBack to index"));
});

test("formatting is idempotent", () => {
  const once = sortCategoryRows(unsorted);
  assert.equal(sortCategoryRows(once), once);
});

test("pins promoted rows in their configured order and sorts only organic rows", () => {
  const readme = [
    "### Animals",
    "API | Description | Auth | HTTPS | CORS |",
    "|:---|:---|:---|:---|:---|",
    "| [Zebra](https://example.com/z?utm_campaign=Public-apis-repo-Best-sellers) | Paid one | No | Yes | No |",
    "| [Yak](https://example.com/y?utm_campaign=Public-apis-repo-Best-sellers) | Paid two | No | Yes | No |",
    "| [Wolf](https://example.com/w) | Organic two | No | Yes | No |",
    "| [Ant](https://example.com/a) | Organic one | No | Yes | No |",
  ].join("\n");
  const formatted = sortCategoryRows(readme);

  assert.ok(formatted.indexOf("[Zebra]") < formatted.indexOf("[Yak]"));
  assert.ok(formatted.indexOf("[Yak]") < formatted.indexOf("[Ant]"));
  assert.ok(formatted.indexOf("[Ant]") < formatted.indexOf("[Wolf]"));
});

test("does not pin unrelated UTM links", () => {
  const readme = unsorted.replace("https://example.com/z", "https://example.com/z?utm_source=public-apis");
  const formatted = sortCategoryRows(readme);
  assert.ok(formatted.indexOf("[Ant]") < formatted.indexOf("[Zebra]"));
});
