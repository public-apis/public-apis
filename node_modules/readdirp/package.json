{
  "name": "readdirp",
  "description": "Recursive version of fs.readdir with streaming API.",
  "version": "3.6.0",
  "homepage": "https://github.com/paulmillr/readdirp",
  "repository": {
    "type": "git",
    "url": "git://github.com/paulmillr/readdirp.git"
  },
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/paulmillr/readdirp/issues"
  },
  "author": "Thorsten Lorenz <thlorenz@gmx.de> (thlorenz.com)",
  "contributors": [
    "Thorsten Lorenz <thlorenz@gmx.de> (thlorenz.com)",
    "Paul Miller (https://paulmillr.com)"
  ],
  "main": "index.js",
  "engines": {
    "node": ">=8.10.0"
  },
  "files": [
    "index.js",
    "index.d.ts"
  ],
  "keywords": [
    "recursive",
    "fs",
    "stream",
    "streams",
    "readdir",
    "filesystem",
    "find",
    "filter"
  ],
  "scripts": {
    "dtslint": "dtslint",
    "nyc": "nyc",
    "mocha": "mocha --exit",
    "lint": "eslint --report-unused-disable-directives --ignore-path .gitignore .",
    "test": "npm run lint && nyc npm run mocha"
  },
  "dependencies": {
    "picomatch": "^2.2.1"
  },
  "devDependencies": {
    "@types/node": "^14",
    "chai": "^4.2",
    "chai-subset": "^1.6",
    "dtslint": "^3.3.0",
    "eslint": "^7.0.0",
    "mocha": "^7.1.1",
    "nyc": "^15.0.0",
    "rimraf": "^3.0.0",
    "typescript": "^4.0.3"
  },
  "nyc": {
    "reporter": [
      "html",
      "text"
    ]
  },
  "eslintConfig": {
    "root": true,
    "extends": "eslint:recommended",
    "parserOptions": {
      "ecmaVersion": 9,
      "sourceType": "script"
    },
    "env": {
      "node": true,
      "es6": true
    },
    "rules": {
      "array-callback-return": "error",
      "no-empty": [
        "error",
        {
          "allowEmptyCatch": true
        }
      ],
      "no-else-return": [
        "error",
        {
          "allowElseIf": false
        }
      ],
      "no-lonely-if": "error",
      "no-var": "error",
      "object-shorthand": "error",
      "prefer-arrow-callback": [
        "error",
        {
          "allowNamedFunctions": true
        }
      ],
      "prefer-const": [
        "error",
        {
          "ignoreReadBeforeAssign": true
        }
      ],
      "prefer-destructuring": [
        "error",
        {
          "object": true,
          "array": false
        }
      ],
      "prefer-spread": "error",
      "prefer-template": "error",
      "radix": "error",
      "semi": "error",
      "strict": "error",
      "quotes": [
        "error",
        "single"
      ]
    }
  }
}
