# is-binary-path [![Build Status](https://travis-ci.org/sindresorhus/is-binary-path.svg?branch=master)](https://travis-ci.org/sindresorhus/is-binary-path)

> Check if a file path is a binary file


## Install

```
$ npm install is-binary-path
```


## Usage

```js
const isBinaryPath = require('is-binary-path');

isBinaryPath('source/unicorn.png');
//=> true

isBinaryPath('source/unicorn.txt');
//=> false
```


## Related

- [binary-extensions](https://github.com/sindresorhus/binary-extensions) - List of binary file extensions
- [is-text-path](https://github.com/sindresorhus/is-text-path) - Check if a filepath is a text file


## License

MIT © [Sindre Sorhus](https://sindresorhus.com), [Paul Miller](https://paulmillr.com)
