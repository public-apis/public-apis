"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const {
  COMMENT_MARKER,
  escapeHtml,
  filterErrorsToDiff,
  formatComment,
  formatError,
  parseReadmeDiff,
  subtractBaselineErrors,
} = require("../validate-pr-readme");

const readme = [
  "## Index",
  "* [Animals](#animals)",
  "### Animals",
  "|:---|:---|:---|:---|:---|",
  "| [Ant](https://example.com/a) | Good description | No | Yes | No |",
  "| [Bad](https://example.com/b) | bad description. | No | Yes | No |",
  "| [Cat](https://example.com/c) | Good description | No | Yes | No |",
].join("\n");

test("collects proposed README line numbers from a unified diff", () => {
  const diff = [
    "diff --git a/README.md b/README.md",
    "--- a/README.md",
    "+++ b/README.md",
    "@@ -4,2 +4,3 @@",
    " |:---|:---|:---|:---|:---|",
    "+| [Bad](https://example.com/b) | bad description. | No | Yes | No |",
    " | [Cat](https://example.com/c) | Good description | No | Yes | No |",
  ].join("\n");

  assert.deepEqual([...parseReadmeDiff(diff).touchedLines], [5]);
});

test("ignores legacy errors outside the diff", () => {
  const diff = [
    "diff --git a/README.md b/README.md",
    "--- a/README.md",
    "+++ b/README.md",
    "@@ -5,2 +5,2 @@",
    " | [Ant](https://example.com/a) | Good description | No | Yes | No |",
    "+| [Bad](https://example.com/b) | bad description. | No | Yes | No |",
  ].join("\n");
  const errors = [
    "L6: first character of description is not capitalized",
    'L6: description should not end with "."',
    "L99: unrelated legacy issue",
  ];

  assert.deepEqual(filterErrorsToDiff(errors, readme, diff), errors.slice(0, 2));
});

test("includes category-level errors when that category changed", () => {
  const diff = [
    "diff --git a/README.md b/README.md",
    "--- a/README.md",
    "+++ b/README.md",
    "@@ -5,2 +5,2 @@",
    "+| [Zoo](https://example.com/z) | Good description | No | Yes | No |",
    " | [Bad](https://example.com/b) | bad description. | No | Yes | No |",
  ].join("\n");

  const error = 'L3: category "Animals" is not in alphabetical order';
  assert.deepEqual(filterErrorsToDiff([error], readme, diff), [error]);
});

test("formats a stable success comment", () => {
  const comment = formatComment([], true, "octocat");
  assert.ok(comment.startsWith(COMMENT_MARKER));
  assert.ok(comment.includes("Hi @octocat"));
  assert.ok(comment.includes("follow our contribution guidelines"));
  assert.ok(comment.includes("maintainers will review"));
});

test("formats polite, actionable issue guidance", () => {
  const comment = formatComment(
    [
      "L42: description should not exceed 100 characters (currently 108)",
      'L43: title "Example API" should not end with "API" — every entry here is an API',
    ],
    true,
    "octocat",
    {
      readmeUrl: "https://github.com/example/repo/blob/abc123/README.md",
      contributingUrl: "https://github.com/example/repo/blob/def456/CONTRIBUTING.md",
    }
  );

  assert.ok(comment.includes("Thanks a lot for contributing"));
  assert.ok(comment.includes("2 items that could be improved"));
  assert.ok(comment.includes("README.md#L42"));
  assert.ok(comment.includes("CONTRIBUTING.md"));
  assert.ok(comment.includes("run again automatically"));
});

test("formats line-numbered errors as README links", () => {
  assert.equal(
    formatError("L12: description is empty"),
    "- [README.md line 12](README.md#L12): <code>description is empty</code>"
  );
});

test("escapes contributor-controlled text in validation comments", () => {
  assert.equal(escapeHtml('title "<img> & API"'), 'title "&lt;img&gt; &amp; API"');
});

test("subtracts legacy errors even when their line numbers move", () => {
  const baseline = [
    'L20: category "Finance" is not in alphabetical order',
    "L40: description is empty",
  ];
  const proposed = [
    'L21: category "Finance" is not in alphabetical order',
    "L41: description is empty",
    "L42: first character of description is not capitalized",
  ];

  assert.deepEqual(subtractBaselineErrors(proposed, baseline), [
    "L42: first character of description is not capitalized",
  ]);
});

test("preserves additional occurrences of an existing error", () => {
  const baseline = ["L10: description is empty"];
  const proposed = ["L10: description is empty", "L20: description is empty"];
  assert.deepEqual(subtractBaselineErrors(proposed, baseline), ["L20: description is empty"]);
});
