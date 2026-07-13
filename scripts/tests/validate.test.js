"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { validateReadme } = require("../validate");

function withCategory(rows) {
  return [
    "## Index",
    "* [Animals](#animals)",
    "### Animals",
    "|:---|:---|:---|:---|:---|",
    ...rows,
  ].join("\n");
}

function threeValidRows() {
  return [
    "| [A](https://example.com/a) | Desc one | No | Yes | No |",
    "| [B](https://example.com/b) | Desc two | No | Yes | No |",
    "| [C](https://example.com/c) | Desc three | No | Yes | No |",
  ];
}

test("valid file produces no errors", () => {
  assert.deepEqual(validateReadme(withCategory(threeValidRows())), []);
});

test("does not crash on an empty description", () => {
  const rows = [...threeValidRows(), "| [D](https://example.com/d) |  | No | Yes | No |"];
  assert.ok(validateReadme(withCategory(rows)).some((e) => e.includes("description is empty")));
});

test("flags the last category in the file", () => {
  const rows = ["| [A](https://example.com/a) | Only one | No | Yes | No |"];
  assert.ok(validateReadme(withCategory(rows)).some((e) => e.includes("minimum 3")));
});

test("flags API as the last word but allows API as part of a brand name", () => {
  const rows = [
    "| [Gmail API](https://example.com/a) | Desc one | No | Yes | No |",
    "| [FastAPI](https://example.com/b) | Desc two | No | Yes | No |",
    "| [ip-api](https://example.com/c) | Desc three | No | Yes | No |",
  ];
  const errors = validateReadme(withCategory(rows));
  assert.ok(errors.some((e) => e.includes('"Gmail API"')));
  assert.ok(!errors.some((e) => e.includes('"FastAPI"')));
  assert.ok(!errors.some((e) => e.includes('"ip-api"')));
});

test("flags an auth value missing backticks", () => {
  const rows = [
    "| [A](https://example.com/a) | Desc one | apiKey | Yes | No |",
    "| [B](https://example.com/b) | Desc two | No | Yes | No |",
    "| [C](https://example.com/c) | Desc three | No | Yes | No |",
  ];
  assert.ok(validateReadme(withCategory(rows)).some((e) => e.includes("not enclosed in backticks")));
});

test("flags a description over 100 characters", () => {
  const rows = [
    `| [A](https://example.com/a) | ${"D".repeat(101)} | No | Yes | No |`,
    "| [B](https://example.com/b) | Desc two | No | Yes | No |",
    "| [C](https://example.com/c) | Desc three | No | Yes | No |",
  ];
  assert.ok(validateReadme(withCategory(rows)).some((e) => e.includes("should not exceed 100 characters")));
});

test("flags a duplicate name and URL entry", () => {
  const rows = [...threeValidRows(), "| [A](https://example.com/a) | Again | No | Yes | No |"];
  assert.equal(validateReadme(withCategory(rows)).filter((e) => e.includes("duplicate entry")).length, 2);
});

test("flags duplicate entries across categories", () => {
  const readme = [
    "## Index",
    "* [Animals](#animals)",
    "* [Books](#books)",
    "### Animals",
    "|:---|:---|:---|:---|:---|",
    ...threeValidRows(),
    "### Books",
    "|:---|:---|:---|:---|:---|",
    "| [A](https://example.com/a) | Duplicate | No | Yes | No |",
    "| [D](https://example.com/d) | Desc four | No | Yes | No |",
    "| [E](https://example.com/e) | Desc five | No | Yes | No |",
  ].join("\n");

  assert.equal(validateReadme(readme).filter((e) => e.includes("duplicate entry")).length, 2);
});

test("flags a category missing from the Index", () => {
  const readme = ["## Index", "### Animals", "|:---|:---|:---|:---|:---|", ...threeValidRows()].join("\n");
  assert.ok(validateReadme(readme).some((e) => e.includes("missing from the ## Index")));
});

test("allows a trailing empty table cell", () => {
  const rows = [
    "| [A](https://example.com/a) | Desc one | No | Yes | No | |",
    "| [B](https://example.com/b) | Desc two | No | Yes | No |",
    "| [C](https://example.com/c) | Desc three | No | Yes | No |",
  ];
  assert.ok(!validateReadme(withCategory(rows)).some((e) => e.includes("columns")));
});

test("flags a populated extra table column", () => {
  const rows = [
    "| [A](https://example.com/a) | Desc one | No | Yes | No | Extra |",
    "| [B](https://example.com/b) | Desc two | No | Yes | No |",
    "| [C](https://example.com/c) | Desc three | No | Yes | No |",
  ];
  assert.ok(validateReadme(withCategory(rows)).some((e) => e.includes("columns")));
});

test("allows promoted rows above an alphabetized organic list", () => {
  const rows = [
    "| [Zebra](https://example.com/z?utm_campaign=Public-apis-repo-Best-sellers) | Paid | No | Yes | No |",
    ...threeValidRows(),
  ];
  assert.deepEqual(validateReadme(withCategory(rows)), []);
});

test("flags a promoted row below an organic entry", () => {
  const rows = [
    "| [A](https://example.com/a) | Desc one | No | Yes | No |",
    "| [Zebra](https://example.com/z?utm_campaign=Public-apis-repo-Best-sellers) | Paid | No | Yes | No |",
    "| [B](https://example.com/b) | Desc two | No | Yes | No |",
  ];
  assert.ok(validateReadme(withCategory(rows)).some((e) => e.includes("promoted entry below organic")));
});

test("does not exempt an unrelated UTM link from alphabetical order", () => {
  const rows = [
    "| [Zebra](https://example.com/z?utm_source=public-apis) | Organic | No | Yes | No |",
    ...threeValidRows(),
  ];
  assert.ok(validateReadme(withCategory(rows)).some((e) => e.includes("not in alphabetical order")));
});
