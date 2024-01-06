'use strict'

const EE = require('events').EventEmitter
const cons = require('constants')
const fs = require('fs')

module.exports = (f, options, cb) => {
  if (typeof options === 'function')
    cb = options, options = {}

  const p = new Promise((res, rej) => {
    new Touch(validOpts(options, f, null))
      .on('done', res).on('error', rej)
  })

  return cb ? p.then(res => cb(null, res), cb) : p
}

module.exports.sync = module.exports.touchSync = (f, options) =>
  (new TouchSync(validOpts(options, f, null)), undefined)

module.exports.ftouch = (fd, options, cb) => {
  if (typeof options === 'function')
    cb = options, options = {}

  const p = new Promise((res, rej) => {
    new Touch(validOpts(options, null, fd))
      .on('done', res).on('error', rej)
  })

  return cb ? p.then(res => cb(null, res), cb) : p
}

module.exports.ftouchSync = (fd, opt) =>
  (new TouchSync(validOpts(opt, null, fd)), undefined)

const validOpts = (options, path, fd) => {
  options = Object.create(options || {})
  options.fd = fd
  options.path = path

  // {mtime: true}, {ctime: true}
  // If set to something else, then treat as epoch ms value
  const now = parseInt(new Date(options.time || Date.now()).getTime() / 1000)
  if (!options.atime && !options.mtime)
    options.atime = options.mtime = now
  else {
    if (true === options.atime)
      options.atime = now

    if (true === options.mtime)
      options.mtime = now
  }

  let oflags = 0
  if (!options.force)
    oflags = oflags | cons.O_RDWR

  if (!options.nocreate)
    oflags = oflags | cons.O_CREAT

  options.oflags = oflags
  return options
}

class Touch extends EE {
  constructor (options) {
    super(options)
    this.fd = options.fd
    this.path = options.path
    this.atime = options.atime
    this.mtime = options.mtime
    this.ref = options.ref
    this.nocreate = !!options.nocreate
    this.force = !!options.force
    this.closeAfter = options.closeAfter
    this.oflags = options.oflags
    this.options = options

    if (typeof this.fd !== 'number') {
      this.closeAfter = true
      this.open()
    } else
      this.onopen(null, this.fd)
  }

  emit (ev, data) {
    // we only emit when either done or erroring
    // in both cases, need to close
    this.close()
    return super.emit(ev, data)
  }

  close () {
    if (typeof this.fd === 'number' && this.closeAfter)
      fs.close(this.fd, () => {})
  }

  open () {
    fs.open(this.path, this.oflags, (er, fd) => this.onopen(er, fd))
  }

  onopen (er, fd) {
    if (er) {
      if (er.code === 'EISDIR')
        this.onopen(null, null)
      else if (er.code === 'ENOENT' && this.nocreate)
        this.emit('done')
      else
        this.emit('error', er)
    } else {
      this.fd = fd
      if (this.ref)
        this.statref()
      else if (!this.atime || !this.mtime)
        this.fstat()
      else
        this.futimes()
    }
  }

  statref () {
    fs.stat(this.ref, (er, st) => {
      if (er)
        this.emit('error', er)
      else
        this.onstatref(st)
    })
  }

  onstatref (st) {
    this.atime = this.atime && parseInt(st.atime.getTime()/1000, 10)
    this.mtime = this.mtime && parseInt(st.mtime.getTime()/1000, 10)
    if (!this.atime || !this.mtime)
      this.fstat()
    else
      this.futimes()
  }

  fstat () {
    const stat = this.fd ? 'fstat' : 'stat'
    const target = this.fd || this.path
    fs[stat](target, (er, st) => {
      if (er)
        this.emit('error', er)
      else
        this.onfstat(st)
    })
  }

  onfstat (st) {
    if (typeof this.atime !== 'number')
      this.atime = parseInt(st.atime.getTime()/1000, 10)

    if (typeof this.mtime !== 'number')
      this.mtime = parseInt(st.mtime.getTime()/1000, 10)

    this.futimes()
  }

  futimes () {
    const utimes = this.fd ? 'futimes' : 'utimes'
    const target = this.fd || this.path
    fs[utimes](target, ''+this.atime, ''+this.mtime, er => {
      if (er)
        this.emit('error', er)
      else
        this.emit('done')
    })
  }
}

class TouchSync extends Touch {
  open () {
    try {
      this.onopen(null, fs.openSync(this.path, this.oflags))
    } catch (er) {
      this.onopen(er)
    }
  }

  statref () {
    let threw = true
    try {
      this.onstatref(fs.statSync(this.ref))
      threw = false
    } finally {
      if (threw)
        this.close()
    }
  }

  fstat () {
    let threw = true
    const stat = this.fd ? 'fstatSync' : 'statSync'
    const target = this.fd || this.path
    try {
      this.onfstat(fs[stat](target))
      threw = false
    } finally {
      if (threw)
        this.close()
    }
  }

  futimes () {
    let threw = true
    const utimes = this.fd ? 'futimesSync' : 'utimesSync'
    const target = this.fd || this.path
    try {
      fs[utimes](target, this.atime, this.mtime)
      threw = false
    } finally {
      if (threw)
        this.close()
    }
    this.emit('done')
  }

  close () {
    if (typeof this.fd === 'number' && this.closeAfter)
      try { fs.closeSync(this.fd) } catch (er) {}
  }
}
