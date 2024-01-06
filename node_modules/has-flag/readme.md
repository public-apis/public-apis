# has-flag [![Build Status](https://travis-ci.org/sindresorhus/has-flag.svg?branch=master)](https://travis-ci.org/sindresorhus/has-flag)

> Check if [`argv`](https://nodejs.org/docs/latest/api/process.html#process_process_argv) has a specific flag

Correctly stops looking after an `--` argument terminator.


## Install

```
$ npm install has-flag
```


## Usage

```js
// foo.js
const hasFlag = require('has-flag');

hasFlag('unicorn');
//=> true

hasFlag('--unicorn');
//=> true

hasFlag('f');
//=> true

hasFlag('-f');
//=> true

hasFlag('foo=bar');
//=> true

hasFlag('foo');
//=> false

hasFlag('rainbow');
//=> false
```

```
$ node foo.js -f --unicorn --foo=bar -- --rainbow
```


## API

### hasFlag(flag, [argv])

Returns a boolean for whether the flag exists.

#### flag

Type: `string`

CLI flag to look for. The `--` prefix is optional.

#### argv

Type: `string[]`<br>
Default: `process.argv`

CLI arguments.


## License

MIT © [Sindre Sorhus](https://sindresorhus.com)
