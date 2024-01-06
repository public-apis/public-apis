# ignore-by-default

This is a package aimed at Node.js development tools. It provides a list of
directories that should probably be ignored by such tools, e.g. when watching
for file changes.

It's used by [AVA](https://www.npmjs.com/package/ava) and
[nodemon](https://www.npmjs.com/package/nodemon).

[Please contribute!](./CONTRIBUTING.md)

## Installation

```
npm install --save ignore-by-default
```

## Usage

The `ignore-by-default` module exports a `directories()` function, which will
return an array of directory names. These are the ones you should ignore.

```js
// ['.git', '.sass_cache', …]
var ignoredDirectories = require('ignore-by-default').directories()
```
