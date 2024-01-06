{
  "name": "picomatch",
  "description": "Blazing fast and accurate glob matcher written in JavaScript, with no dependencies and full support for standard and extended Bash glob features, including braces, extglobs, POSIX brackets, and regular expressions.",
  "version": "2.3.1",
  "homepage": "https://github.com/micromatch/picomatch",
  "author": "Jon Schlinkert (https://github.com/jonschlinkert)",
  "funding": "https://github.com/sponsors/jonschlinkert",
  "repository": "micromatch/picomatch",
  "bugs": {
    "url": "https://github.com/micromatch/picomatch/issues"
  },
  "license": "MIT",
  "files": [
    "index.js",
    "lib"
  ],
  "main": "index.js",
  "engines": {
    "node": ">=8.6"
  },
  "scripts": {
    "lint": "eslint --cache --cache-location node_modules/.cache/.eslintcache --report-unused-disable-directives --ignore-path .gitignore .",
    "mocha": "mocha --reporter dot",
    "test": "npm run lint && npm run mocha",
    "test:ci": "npm run test:cover",
    "test:cover": "nyc npm run mocha"
  },
  "devDependencies": {
    "eslint": "^6.8.0",
    "fill-range": "^7.0.1",
    "gulp-format-md": "^2.0.0",
    "mocha": "^6.2.2",
    "nyc": "^15.0.0",
    "time-require": "github:jonschlinkert/time-require"
  },
  "keywords": [
    "glob",
    "match",
    "picomatch"
  ],
  "nyc": {
    "reporter": [
      "html",
      "lcov",
      "text-summary"
    ]
  },
  "verb": {
    "toc": {
      "render": true,
      "method": "preWrite",
      "maxdepth": 3
    },
    "layout": "empty",
    "tasks": [
      "readme"
    ],
    "plugins": [
      "gulp-format-md"
    ],
    "lint": {
      "reflinks": true
    },
    "related": {
      "list": [
        "braces",
        "micromatch"
      ]
    },
    "reflinks": [
      "braces",
      "expand-brackets",
      "extglob",
      "fill-range",
      "micromatch",
      "minimatch",
      "nanomatch",
      "picomatch"
    ]
  }
}
