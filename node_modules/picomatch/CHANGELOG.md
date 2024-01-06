# Release history

**All notable changes to this project will be documented in this file.**

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<details>
  <summary><strong>Guiding Principles</strong></summary>

- Changelogs are for humans, not machines.
- There should be an entry for every single version.
- The same types of changes should be grouped.
- Versions and sections should be linkable.
- The latest version comes first.
- The release date of each versions is displayed.
- Mention whether you follow Semantic Versioning.

</details>

<details>
  <summary><strong>Types of changes</strong></summary>

Changelog entries are classified using the following labels _(from [keep-a-changelog](http://keepachangelog.com/)_):

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

</details>

## 2.3.1 (2022-01-02)

### Fixed

* Fixes bug when a pattern containing an expression after the closing parenthesis (`/!(*.d).{ts,tsx}`) was incorrectly converted to regexp ([9f241ef](https://github.com/micromatch/picomatch/commit/9f241ef)).

### Changed

* Some documentation improvements ([f81d236](https://github.com/micromatch/picomatch/commit/f81d236), [421e0e7](https://github.com/micromatch/picomatch/commit/421e0e7)).

## 2.3.0 (2021-05-21)

### Fixed

* Fixes bug where file names with two dots were not being matched consistently with negation extglobs containing a star ([56083ef](https://github.com/micromatch/picomatch/commit/56083ef))

## 2.2.3 (2021-04-10)

### Fixed

* Do not skip pattern seperator for square brackets ([fb08a30](https://github.com/micromatch/picomatch/commit/fb08a30)).
* Set negatedExtGlob also if it does not span the whole pattern ([032e3f5](https://github.com/micromatch/picomatch/commit/032e3f5)).

## 2.2.2 (2020-03-21)

### Fixed

* Correctly handle parts of the pattern after parentheses in the `scan` method ([e15b920](https://github.com/micromatch/picomatch/commit/e15b920)).

## 2.2.1 (2020-01-04)

* Fixes [#49](https://github.com/micromatch/picomatch/issues/49), so that braces with no sets or ranges are now propertly treated as literals.

## 2.2.0 (2020-01-04)

* Disable fastpaths mode for the parse method ([5b8d33f](https://github.com/micromatch/picomatch/commit/5b8d33f))
* Add `tokens`, `slashes`, and `parts` to the object returned by `picomatch.scan()`.

## 2.1.0 (2019-10-31)

* add benchmarks for scan ([4793b92](https://github.com/micromatch/picomatch/commit/4793b92))
* Add eslint object-curly-spacing rule ([707c650](https://github.com/micromatch/picomatch/commit/707c650))
* Add prefer-const eslint rule ([5c7501c](https://github.com/micromatch/picomatch/commit/5c7501c))
* Add support for nonegate in scan API ([275c9b9](https://github.com/micromatch/picomatch/commit/275c9b9))
* Change lets to consts. Move root import up. ([4840625](https://github.com/micromatch/picomatch/commit/4840625))
* closes https://github.com/micromatch/picomatch/issues/21 ([766bcb0](https://github.com/micromatch/picomatch/commit/766bcb0))
* Fix "Extglobs" table in readme ([eb19da8](https://github.com/micromatch/picomatch/commit/eb19da8))
* fixes https://github.com/micromatch/picomatch/issues/20 ([9caca07](https://github.com/micromatch/picomatch/commit/9caca07))
* fixes https://github.com/micromatch/picomatch/issues/26 ([fa58f45](https://github.com/micromatch/picomatch/commit/fa58f45))
* Lint test ([d433a34](https://github.com/micromatch/picomatch/commit/d433a34))
* lint unit tests ([0159b55](https://github.com/micromatch/picomatch/commit/0159b55))
* Make scan work with noext ([6c02e03](https://github.com/micromatch/picomatch/commit/6c02e03))
* minor linting ([c2a2b87](https://github.com/micromatch/picomatch/commit/c2a2b87))
* minor parser improvements ([197671d](https://github.com/micromatch/picomatch/commit/197671d))
* remove eslint since it... ([07876fa](https://github.com/micromatch/picomatch/commit/07876fa))
* remove funding file ([8ebe96d](https://github.com/micromatch/picomatch/commit/8ebe96d))
* Remove unused funks ([cbc6d54](https://github.com/micromatch/picomatch/commit/cbc6d54))
* Run eslint during pretest, fix existing eslint findings ([0682367](https://github.com/micromatch/picomatch/commit/0682367))
* support `noparen` in scan ([3d37569](https://github.com/micromatch/picomatch/commit/3d37569))
* update changelog ([7b34e77](https://github.com/micromatch/picomatch/commit/7b34e77))
* update travis ([777f038](https://github.com/micromatch/picomatch/commit/777f038))
* Use eslint-disable-next-line instead of eslint-disable ([4e7c1fd](https://github.com/micromatch/picomatch/commit/4e7c1fd))

## 2.0.7 (2019-05-14)

* 2.0.7 ([9eb9a71](https://github.com/micromatch/picomatch/commit/9eb9a71))
* supports lookbehinds ([1f63f7e](https://github.com/micromatch/picomatch/commit/1f63f7e))
* update .verb.md file with typo change ([2741279](https://github.com/micromatch/picomatch/commit/2741279))
* fix: typo in README ([0753e44](https://github.com/micromatch/picomatch/commit/0753e44))

## 2.0.4 (2019-04-10)

### Fixed

- Readme link [fixed](https://github.com/micromatch/picomatch/pull/13/commits/a96ab3aa2b11b6861c23289964613d85563b05df) by @danez.
- `options.capture` now works as expected when fastpaths are enabled. See https://github.com/micromatch/picomatch/pull/12/commits/26aefd71f1cfaf95c37f1c1fcab68a693b037304. Thanks to @DrPizza.

## 2.0.0 (2019-04-10)

### Added

- Adds support for `options.onIgnore`. See the readme for details
- Adds support for `options.onResult`. See the readme for details

### Breaking changes

- The unixify option was renamed to `windows`
- caching and all related options and methods have been removed

## 1.0.0 (2018-11-05)

- adds `.onMatch` option
- improvements to `.scan` method
- numerous improvements and optimizations for matching and parsing
- better windows path handling

## 0.1.0 - 2017-04-13

First release.


[keep-a-changelog]: https://github.com/olivierlacan/keep-a-changelog
