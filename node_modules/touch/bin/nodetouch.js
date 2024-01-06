#!/usr/bin/env node
const touch = require("../index.js")

const usage = code => {
  console[code ? 'error' : 'log'](
    'usage:\n' +
    'touch [-acfm] [-r file] [-t [[CC]YY]MMDDhhmm[.SS]] file ...'
  )
  process.exit(code)
}

const singleFlags = {
  a: 'atime',
  m: 'mtime',
  c: 'nocreate',
  f: 'force'
}

const singleOpts = {
  r: 'ref',
  t: 'time'
}

const files = []
const args = process.argv.slice(2)
const options = {}
for (let i = 0; i < args.length; i++) {
  const arg = args[i]
  if (!arg.match(/^-/)) {
    files.push(arg)
    continue
  }

  // expand shorthands
  if (arg.charAt(1) !== '-') {
    const expand = []
    for (let f = 1; f < arg.length; f++) {
      const fc = arg.charAt(f)
      const sf = singleFlags[fc]
      const so = singleOpts[fc]
      if (sf)
        expand.push('--' + sf)
      else if (so) {
        const soslice = arg.slice(f + 1)
        const soval = soslice.charAt(0) === '=' ? soslice : '=' + soslice
        expand.push('--' + so + soval)
        f = arg.length
      } else if (arg !== '-' + fc)
        expand.push('-' + fc)
    }
    if (expand.length) {
      args.splice.apply(args, [i, 1].concat(expand))
      i--
      continue
    }
  }

  const argsplit = arg.split('=')
  const key = argsplit.shift().replace(/^\-\-/, '')
  const val = argsplit.length ? argsplit.join('=') : null

  switch (key) {
    case 'time':
      const timestr = val || args[++i]
      // [-t [[CC]YY]MMDDhhmm[.SS]]
      const parsedtime = timestr.match(
        /^(([0-9]{2})?([0-9]{2}))?([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})(\.([0-9]{2}))?$/
      )
      if (!parsedtime) {
        console.error('touch: out of range or illegal ' +
                      'time specification: ' +
                      '[[CC]YY]MMDDhhmm[.SS]')
        process.exit(1)
      } else {
        const y = +parsedtime[1]
        const year = parsedtime[2] ? y
          : y <= 68 ? 2000 + y
          : 1900 + y

        const MM = +parsedtime[4] - 1
        const dd = +parsedtime[5]
        const hh = +parsedtime[6]
        const mm = +parsedtime[7]
        const ss = +parsedtime[8]

        options.time = new Date(Date.UTC(year, MM, dd, hh, mm, ss))
      }
      continue

    case 'ref':
      options.ref = val || args[++i]
      continue

    case 'mtime':
    case 'nocreate':
    case 'atime':
    case 'force':
      options[key] = true
      continue

    default:
      console.error('touch: illegal option -- ' + arg)
      usage(1)
  }
}

if (!files.length)
  usage()

process.exitCode = 0
Promise.all(files.map(f => touch(f, options)))
  .catch(er => process.exitCode = 1)
