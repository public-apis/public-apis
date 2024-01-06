{
  "name": "debug",
  "version": "4.3.4",
  "repository": {
    "type": "git",
    "url": "git://github.com/debug-js/debug.git"
  },
  "description": "Lightweight debugging utility for Node.js and the browser",
  "keywords": [
    "debug",
    "log",
    "debugger"
  ],
  "files": [
    "src",
    "LICENSE",
    "README.md"
  ],
  "author": "Josh Junon <josh.junon@protonmail.com>",
  "contributors": [
    "TJ Holowaychuk <tj@vision-media.ca>",
    "Nathan Rajlich <nathan@tootallnate.net> (http://n8.io)",
    "Andrew Rhyne <rhyneandrew@gmail.com>"
  ],
  "license": "MIT",
  "scripts": {
    "lint": "xo",
    "test": "npm run test:node && npm run test:browser && npm run lint",
    "test:node": "istanbul cover _mocha -- test.js",
    "test:browser": "karma start --single-run",
    "test:coverage": "cat ./coverage/lcov.info | coveralls"
  },
  "dependencies": {
    "ms": "2.1.2"
  },
  "devDependencies": {
    "brfs": "^2.0.1",
    "browserify": "^16.2.3",
    "coveralls": "^3.0.2",
    "istanbul": "^0.4.5",
    "karma": "^3.1.4",
    "karma-browserify": "^6.0.0",
    "karma-chrome-launcher": "^2.2.0",
    "karma-mocha": "^1.3.0",
    "mocha": "^5.2.0",
    "mocha-lcov-reporter": "^1.2.0",
    "xo": "^0.23.0"
  },
  "peerDependenciesMeta": {
    "supports-color": {
      "optional": true
    }
  },
  "main": "./src/index.js",
  "browser": "./src/browser.js",
  "engines": {
    "node": ">=6.0"
  }
}
