# Release history

All notable changes to this project will be documented in this file.

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

## [3.0.0] - 2018-04-08

v3.0 is a complete refactor, resulting in a faster, smaller codebase, with fewer deps, and a more accurate parser and compiler. 

**Breaking Changes**

- The undocumented `.makeRe` method was removed

**Non-breaking changes**

- Caching was removed

## [2.3.2] - 2018-04-08

- start refactoring
- cover sets
- better range handling

## [2.3.1] - 2018-02-17

- Remove unnecessary escape in Regex. (#14)

## [2.3.0] - 2017-10-19

- minor code reorganization
- optimize regex
- expose `maxLength` option

## [2.2.1] - 2017-05-30

- don't condense when braces contain extglobs

## [2.2.0] - 2017-05-28

- ensure word boundaries are preserved
- fixes edge case where extglob characters precede a brace pattern

## [2.1.1] - 2017-04-27

- use snapdragon-node
- handle edge case
- optimizations, lint

## [2.0.4] - 2017-04-11

- pass opts to compiler
- minor optimization in create method
- re-write parser handlers to remove negation regex

## [2.0.3] - 2016-12-10

- use split-string
- clear queue at the end
- adds sequences example
- add unit tests

## [2.0.2] - 2016-10-21

- fix comma handling in nested extglobs

## [2.0.1] - 2016-10-20

- add comments
- more tests, ensure quotes are stripped

## [2.0.0] - 2016-10-19

- don't expand braces inside character classes
- add quantifier pattern

## [1.8.5] - 2016-05-21

- Refactor (#10)

## [1.8.4] - 2016-04-20

- fixes https://github.com/jonschlinkert/micromatch/issues/66

## [1.8.0] - 2015-03-18

- adds exponent examples, tests
- fixes the first example in https://github.com/jonschlinkert/micromatch/issues/38

## [1.6.0] - 2015-01-30

- optimizations, `bash` mode:
- improve path escaping

## [1.5.0] - 2015-01-28

- Merge pull request #5 from eush77/lib-files

## [1.4.0] - 2015-01-24

- add extglob tests
- externalize exponent function
- better whitespace handling

## [1.3.0] - 2015-01-24

- make regex patterns explicity

## [1.1.0] - 2015-01-11

- don't create a match group with `makeRe`

## [1.0.0] - 2014-12-23

- Merge commit '97b05f5544f8348736a8efaecf5c32bbe3e2ad6e'
- support empty brace syntax
- better bash coverage
- better support for regex strings

## [0.1.4] - 2014-11-14

- improve recognition of bad args, recognize mismatched argument types
- support escaping
- remove pathname-expansion
- support whitespace in patterns

## [0.1.0]

- first commit

[2.3.2]: https://github.com/micromatch/braces/compare/2.3.1...2.3.2
[2.3.1]: https://github.com/micromatch/braces/compare/2.3.0...2.3.1
[2.3.0]: https://github.com/micromatch/braces/compare/2.2.1...2.3.0
[2.2.1]: https://github.com/micromatch/braces/compare/2.2.0...2.2.1
[2.2.0]: https://github.com/micromatch/braces/compare/2.1.1...2.2.0
[2.1.1]: https://github.com/micromatch/braces/compare/2.1.0...2.1.1
[2.1.0]: https://github.com/micromatch/braces/compare/2.0.4...2.1.0
[2.0.4]: https://github.com/micromatch/braces/compare/2.0.3...2.0.4
[2.0.3]: https://github.com/micromatch/braces/compare/2.0.2...2.0.3
[2.0.2]: https://github.com/micromatch/braces/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/micromatch/braces/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/micromatch/braces/compare/1.8.5...2.0.0
[1.8.5]: https://github.com/micromatch/braces/compare/1.8.4...1.8.5
[1.8.4]: https://github.com/micromatch/braces/compare/1.8.0...1.8.4
[1.8.0]: https://github.com/micromatch/braces/compare/1.6.0...1.8.0
[1.6.0]: https://github.com/micromatch/braces/compare/1.5.0...1.6.0
[1.5.0]: https://github.com/micromatch/braces/compare/1.4.0...1.5.0
[1.4.0]: https://github.com/micromatch/braces/compare/1.3.0...1.4.0
[1.3.0]: https://github.com/micromatch/braces/compare/1.2.0...1.3.0
[1.2.0]: https://github.com/micromatch/braces/compare/1.1.0...1.2.0
[1.1.0]: https://github.com/micromatch/braces/compare/1.0.0...1.1.0
[1.0.0]: https://github.com/micromatch/braces/compare/0.1.4...1.0.0
[0.1.4]: https://github.com/micromatch/braces/compare/0.1.0...0.1.4

[Unreleased]: https://github.com/micromatch/braces/compare/0.1.0...HEAD
[keep-a-changelog]: https://github.com/olivierlacan/keep-a-changelog