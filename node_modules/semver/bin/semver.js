#!/usr/bin/env node
// Standalone semver comparison program.
// Exits successfully and prints matching version(s) if
// any supplied version is valid and passes all tests.

const argv = process.argv.slice(2)

let versions = []

const range = []

let inc = null

const version = require('../package.json').version

let loose = false

let includePrerelease = false

let coerce = false

let rtl = false

let identifier

let identifierBase

const semver = require('../')
const parseOptions = require('../internal/parse-options')

let reverse = false

let options = {}

const main = () => {
  if (!argv.length) {
    return help()
  }
  while (argv.length) {
    let a = argv.shift()
    const indexOfEqualSign = a.indexOf('=')
    if (indexOfEqualSign !== -1) {
      const value = a.slice(indexOfEqualSign + 1)
      a = a.slice(0, indexOfEqualSign)
      argv.unshift(value)
    }
    switch (a) {
      case '-rv': case '-rev': case '--rev': case '--reverse':
        reverse = true
        break
      case '-l': case '--loose':
        loose = true
        break
      case '-p': case '--include-prerelease':
        includePrerelease = true
        break
      case '-v': case '--version':
        versions.push(argv.shift())
        break
      case '-i': case '--inc': case '--increment':
        switch (argv[0]) {
          case 'major': case 'minor': case 'patch': case 'prerelease':
          case 'premajor': case 'preminor': case 'prepatch':
            inc = argv.shift()
            break
          default:
            inc = 'patch'
            break
        }
        break
      case '--preid':
        identifier = argv.shift()
        break
      case '-r': case '--range':
        range.push(argv.shift())
        break
      case '-n':
        identifierBase = argv.shift()
        if (identifierBase === 'false') {
          identifierBase = false
        }
        break
      case '-c': case '--coerce':
        coerce = true
        break
      case '--rtl':
        rtl = true
        break
      case '--ltr':
        rtl = false
        break
      case '-h': case '--help': case '-?':
        return help()
      default:
        versions.push(a)
        break
    }
  }

  options = parseOptions({ loose, includePrerelease, rtl })

  versions = versions.map((v) => {
    return coerce ? (semver.coerce(v, options) || { version: v }).version : v
  }).filter((v) => {
    return semver.valid(v)
  })
  if (!versions.length) {
    return fail()
  }
  if (inc && (versions.length !== 1 || range.length)) {
    return failInc()
  }

  for (let i = 0, l = range.length; i < l; i++) {
    versions = versions.filter((v) => {
      return semver.satisfies(v, range[i], options)
    })
    if (!versions.length) {
      return fail()
    }
  }
  return success(versions)
}

const failInc = () => {
  console.error('--inc can only be used on a single version with no range')
  fail()
}

const fail = () => process.exit(1)

const success = () => {
  const compare = reverse ? 'rcompare' : 'compare'
  versions.sort((a, b) => {
    return semver[compare](a, b, options)
  }).map((v) => {
    return semver.clean(v, options)
  }).map((v) => {
    return inc ? semver.inc(v, inc, options, identifier, identifierBase) : v
  }).forEach((v, i, _) => {
    console.log(v)
  })
}

const help = () => console.log(
`SemVer ${version}

A JavaScript implementation of the https://semver.org/ specification
Copyright Isaac Z. Schlueter

Usage: semver [options] <version> [<version> [...]]
Prints valid versions sorted by SemVer precedence

Options:
-r --range <range>
        Print versions that match the specified range.

-i --increment [<level>]
        Increment a version by the specified level.  Level can
        be one of: major, minor, patch, premajor, preminor,
        prepatch, or prerelease.  Default level is 'patch'.
        Only one version may be specified.

--preid <identifier>
        Identifier to be used to prefix premajor, preminor,
        prepatch or prerelease version increments.

-l --loose
        Interpret versions and ranges loosely

-p --include-prerelease
        Always include prerelease versions in range matching

-c --coerce
        Coerce a string into SemVer if possible
        (does not imply --loose)

--rtl
        Coerce version strings right to left

--ltr
        Coerce version strings left to right (default)

-n <base>
        Base number to be used for the prerelease identifier.
        Can be either 0 or 1, or false to omit the number altogether.
        Defaults to 0.

Program exits successfully if any valid version satisfies
all supplied ranges, and prints all satisfying versions.

If no satisfying versions are found, then exits failure.

Versions are printed in ascending order, so supplying
multiple versions to the utility will just sort them.`)

main()
