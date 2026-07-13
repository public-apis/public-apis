# Public APIs scripts

This directory contains the JavaScript tools used to validate `README.md`, check links, and generate the JSON API files. The tools use Node.js built-ins and have no package dependencies.

## Commands

Run these commands from the repository root:

```bash
npm test
npm run format -- README.md
npm run validate -- README.md
npm run check-links -- README.md
npm run generate -- README.md data
```

To check only for duplicate links, without making HTTP requests to every API:

```bash
npm run check-links -- README.md --duplicates-only
```

## Files

- `validate.js` validates the README category tables.
- `validate-pr-readme.js` reports validation errors only for README lines changed by a pull request.
- `format-readme.js` sorts API rows inside each category without changing surrounding Markdown.
- `check-links.js` checks duplicate and unreachable links.
- `check-pr-links.js` checks links added by a pull request.
- `generate.js` writes the website backend datasets `data/apis.json` and `data/categories.json`.
- `links.js` and `row-parser.js` contain shared parsing and validation helpers.
- `tests/` contains the Node test suite.

GitHub Actions runs the same Node commands for pull requests, pushes to `master`, and scheduled link checks.

## Generated data

`README.md` remains the human-maintained source. After a README change is merged to
`master`, the build workflow regenerates and commits these stable backend inputs:

- `data/apis.json` contains the complete API records.
- `data/categories.json` contains category slugs and API counts.

The repository does not commit a separate minified copy. The website's HTTP layer
can compress `apis.json` when serving it.
