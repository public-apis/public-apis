{
  "name": "simple-update-notifier",
  "version": "2.0.0",
  "description": "Simple update notifier to check for npm updates for cli applications",
  "main": "build/index.js",
  "types": "build/index.d.ts",
  "repository": {
    "type": "git",
    "url": "https://github.com/alexbrazier/simple-update-notifier.git"
  },
  "homepage": "https://github.com/alexbrazier/simple-update-notifier.git",
  "author": "alexbrazier",
  "license": "MIT",
  "engines": {
    "node": ">=10"
  },
  "scripts": {
    "test": "jest src --noStackTrace",
    "build": "rollup -c rollup.config.js --bundleConfigAsCjs",
    "prettier:check": "prettier --check src/**/*.ts",
    "prettier": "prettier --write src/**/*.ts",
    "eslint": "eslint src/**/*.ts",
    "lint": "yarn prettier:check && yarn eslint",
    "prepare": "yarn lint && yarn build",
    "release": "release-it"
  },
  "dependencies": {
    "semver": "^7.5.3"
  },
  "devDependencies": {
    "@babel/preset-env": "^7.22.5",
    "@babel/preset-typescript": "^7.22.5",
    "@release-it/conventional-changelog": "^5.1.1",
    "@types/jest": "^29.5.2",
    "@types/node": "^20.3.1",
    "@typescript-eslint/eslint-plugin": "^5.60.0",
    "@typescript-eslint/parser": "^5.60.0",
    "eslint": "^8.43.0",
    "eslint-config-prettier": "^8.8.0",
    "eslint-plugin-prettier": "^4.0.0",
    "jest": "^29.5.0",
    "prettier": "^2.8.8",
    "release-it": "^15.11.0",
    "rollup": "^3.25.2",
    "rollup-plugin-ts": "^3.2.0",
    "typescript": "^5.1.3"
  },
  "resolutions": {
    "semver": "^7.5.3"
  },
  "publishConfig": {
    "registry": "https://registry.npmjs.org/"
  },
  "files": [
    "build",
    "src"
  ],
  "release-it": {
    "git": {
      "commitMessage": "chore: release ${version}",
      "tagName": "v${version}"
    },
    "npm": {
      "publish": true
    },
    "github": {
      "release": true
    },
    "plugins": {
      "@release-it/conventional-changelog": {
        "preset": "angular",
        "infile": "CHANGELOG.md"
      }
    }
  },
  "eslintConfig": {
    "plugins": [
      "@typescript-eslint",
      "prettier"
    ],
    "extends": [
      "prettier",
      "eslint:recommended",
      "plugin:@typescript-eslint/recommended"
    ],
    "parser": "@typescript-eslint/parser",
    "rules": {
      "prettier/prettier": [
        "error",
        {
          "quoteProps": "consistent",
          "singleQuote": true,
          "tabWidth": 2,
          "trailingComma": "es5",
          "useTabs": false
        }
      ]
    }
  }
}
