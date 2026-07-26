"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { parseReadme, githubSlug } = require("../generate");

test("parses a well-formed entry", () => {
  const readme = [
    "### Animals",
    "API | Description | Auth | HTTPS | CORS",
    "|:---|:---|:---|:---|:---|",
    "| [Cats](https://example.com/cats) | Pictures of cats | `apiKey` | Yes | No |",
  ].join("\n");

  const { apis, categories } = parseReadme(readme);

  assert.equal(apis.length, 1);
  assert.deepEqual(apis[0], {
    name: "Cats",
    description: "Pictures of cats",
    auth: "apiKey",
    https: true,
    cors: "No",
    url: "https://example.com/cats",
    category: "Animals",
  });
  assert.deepEqual(categories, [{ name: "Animals", slug: "animals", count: 1 }]);
});

test("tolerates a stray trailing empty cell", () => {
  const readme = [
    "### Animals",
    "API | Description | Auth | HTTPS | CORS",
    "|:---|:---|:---|:---|:---|",
    "| [Cats](https://example.com/cats) | Pictures of cats | No | Yes | No | |",
  ].join("\n");

  const { apis } = parseReadme(readme);
  assert.equal(apis.length, 1);
  assert.equal(apis[0].name, "Cats");
});

test("skips the header label row and divider row", () => {
  const readme = [
    "### Animals",
    "| API | Description | Auth | HTTPS | CORS |",
    "|---|:---|:---|:---|:---|",
    "| [Cats](https://example.com/cats) | Pictures of cats | No | Yes | No |",
  ].join("\n");

  const { apis } = parseReadme(readme);
  assert.equal(apis.length, 1);
});

test("counts entries per category correctly", () => {
  const readme = [
    "### Animals",
    "|:---|:---|:---|:---|:---|",
    "| [A](https://example.com/a) | Desc | No | Yes | No |",
    "| [B](https://example.com/b) | Desc | No | Yes | No |",
    "### Books",
    "|:---|:---|:---|:---|:---|",
    "| [C](https://example.com/c) | Desc | No | Yes | No |",
  ].join("\n");

  const { categories } = parseReadme(readme);
  assert.deepEqual(categories, [
    { name: "Animals", slug: "animals", count: 2 },
    { name: "Books", slug: "books", count: 1 },
  ]);
});

test("githubSlug matches GitHub's heading-anchor algorithm", () => {
  assert.equal(githubSlug("Animals"), "animals");
  assert.equal(githubSlug("Art & Design"), "art--design");
  assert.equal(githubSlug("Authentication & Authorization"), "authentication--authorization");
});
