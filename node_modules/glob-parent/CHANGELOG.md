### [5.1.2](https://github.com/gulpjs/glob-parent/compare/v5.1.1...v5.1.2) (2021-03-06)


### Bug Fixes

* eliminate ReDoS ([#36](https://github.com/gulpjs/glob-parent/issues/36)) ([f923116](https://github.com/gulpjs/glob-parent/commit/f9231168b0041fea3f8f954b3cceb56269fc6366))

### [5.1.1](https://github.com/gulpjs/glob-parent/compare/v5.1.0...v5.1.1) (2021-01-27)


### Bug Fixes

* unescape exclamation mark ([#26](https://github.com/gulpjs/glob-parent/issues/26)) ([a98874f](https://github.com/gulpjs/glob-parent/commit/a98874f1a59e407f4fb1beb0db4efa8392da60bb))

## [5.1.0](https://github.com/gulpjs/glob-parent/compare/v5.0.0...v5.1.0) (2021-01-27)


### Features

* add `flipBackslashes` option to disable auto conversion of slashes (closes [#24](https://github.com/gulpjs/glob-parent/issues/24)) ([#25](https://github.com/gulpjs/glob-parent/issues/25)) ([eecf91d](https://github.com/gulpjs/glob-parent/commit/eecf91d5e3834ed78aee39c4eaaae654d76b87b3))

## [5.0.0](https://github.com/gulpjs/glob-parent/compare/v4.0.0...v5.0.0) (2021-01-27)


### ⚠ BREAKING CHANGES

* Drop support for node <6 & bump dependencies

### Miscellaneous Chores

* Drop support for node <6 & bump dependencies ([896c0c0](https://github.com/gulpjs/glob-parent/commit/896c0c00b4e7362f60b96e7fc295ae929245255a))

## [4.0.0](https://github.com/gulpjs/glob-parent/compare/v3.1.0...v4.0.0) (2021-01-27)


### ⚠ BREAKING CHANGES

* question marks are valid path characters on Windows so avoid flagging as a glob when alone
* Update is-glob dependency

### Features

* hoist regexps and strings for performance gains ([4a80667](https://github.com/gulpjs/glob-parent/commit/4a80667c69355c76a572a5892b0f133c8e1f457e))
* question marks are valid path characters on Windows so avoid flagging as a glob when alone ([2a551dd](https://github.com/gulpjs/glob-parent/commit/2a551dd0dc3235e78bf3c94843d4107072d17841))
* Update is-glob dependency ([e41fcd8](https://github.com/gulpjs/glob-parent/commit/e41fcd895d1f7bc617dba45c9d935a7949b9c281))

## [3.1.0](https://github.com/gulpjs/glob-parent/compare/v3.0.1...v3.1.0) (2021-01-27)


### Features

* allow basic win32 backslash use ([272afa5](https://github.com/gulpjs/glob-parent/commit/272afa5fd070fc0f796386a5993d4ee4a846988b))
* handle extglobs (parentheses) containing separators ([7db1bdb](https://github.com/gulpjs/glob-parent/commit/7db1bdb0756e55fd14619e8ce31aa31b17b117fd))
* new approach to braces/brackets handling ([8269bd8](https://github.com/gulpjs/glob-parent/commit/8269bd89290d99fac9395a354fb56fdcdb80f0be))
* pre-process braces/brackets sections ([9ef8a87](https://github.com/gulpjs/glob-parent/commit/9ef8a87f66b1a43d0591e7a8e4fc5a18415ee388))
* preserve escaped brace/bracket at end of string ([8cfb0ba](https://github.com/gulpjs/glob-parent/commit/8cfb0ba84202d51571340dcbaf61b79d16a26c76))


### Bug Fixes

* trailing escaped square brackets ([99ec9fe](https://github.com/gulpjs/glob-parent/commit/99ec9fecc60ee488ded20a94dd4f18b4f55c4ccf))

### [3.0.1](https://github.com/gulpjs/glob-parent/compare/v3.0.0...v3.0.1) (2021-01-27)


### Features

* use path-dirname ponyfill ([cdbea5f](https://github.com/gulpjs/glob-parent/commit/cdbea5f32a58a54e001a75ddd7c0fccd4776aacc))


### Bug Fixes

* unescape glob-escaped dirnames on output ([598c533](https://github.com/gulpjs/glob-parent/commit/598c533bdf49c1428bc063aa9b8db40c5a86b030))

## [3.0.0](https://github.com/gulpjs/glob-parent/compare/v2.0.0...v3.0.0) (2021-01-27)


### ⚠ BREAKING CHANGES

* update is-glob dependency

### Features

* update is-glob dependency ([5c5f8ef](https://github.com/gulpjs/glob-parent/commit/5c5f8efcee362a8e7638cf8220666acd8784f6bd))

## [2.0.0](https://github.com/gulpjs/glob-parent/compare/v1.3.0...v2.0.0) (2021-01-27)


### Features

* move up to dirname regardless of glob characters ([f97fb83](https://github.com/gulpjs/glob-parent/commit/f97fb83be2e0a9fc8d3b760e789d2ecadd6aa0c2))

## [1.3.0](https://github.com/gulpjs/glob-parent/compare/v1.2.0...v1.3.0) (2021-01-27)

## [1.2.0](https://github.com/gulpjs/glob-parent/compare/v1.1.0...v1.2.0) (2021-01-27)


### Reverts

* feat: make regex test strings smaller ([dc80fa9](https://github.com/gulpjs/glob-parent/commit/dc80fa9658dca20549cfeba44bbd37d5246fcce0))

## [1.1.0](https://github.com/gulpjs/glob-parent/compare/v1.0.0...v1.1.0) (2021-01-27)


### Features

* make regex test strings smaller ([cd83220](https://github.com/gulpjs/glob-parent/commit/cd832208638f45169f986d80fcf66e401f35d233))

## 1.0.0 (2021-01-27)

