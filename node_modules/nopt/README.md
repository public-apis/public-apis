If you want to write an option parser, and have it be good, there are
two ways to do it.  The Right Way, and the Wrong Way.

The Wrong Way is to sit down and write an option parser.  We've all done
that.

The Right Way is to write some complex configurable program with so many
options that you go half-insane just trying to manage them all, and put
it off with duct-tape solutions until you see exactly to the core of the
problem, and finally snap and write an awesome option parser.

If you want to write an option parser, don't write an option parser.
Write a package manager, or a source control system, or a service
restarter, or an operating system.  You probably won't end up with a
good one of those, but if you don't give up, and you are relentless and
diligent enough in your procrastination, you may just end up with a very
nice option parser.

## USAGE

    // my-program.js
    var nopt = require("nopt")
      , Stream = require("stream").Stream
      , path = require("path")
      , knownOpts = { "foo" : [String, null]
                    , "bar" : [Stream, Number]
                    , "baz" : path
                    , "bloo" : [ "big", "medium", "small" ]
                    , "flag" : Boolean
                    , "pick" : Boolean
                    , "many" : [String, Array]
                    }
      , shortHands = { "foofoo" : ["--foo", "Mr. Foo"]
                     , "b7" : ["--bar", "7"]
                     , "m" : ["--bloo", "medium"]
                     , "p" : ["--pick"]
                     , "f" : ["--flag"]
                     }
                 // everything is optional.
                 // knownOpts and shorthands default to {}
                 // arg list defaults to process.argv
                 // slice defaults to 2
      , parsed = nopt(knownOpts, shortHands, process.argv, 2)
    console.log(parsed)

This would give you support for any of the following:

```bash
$ node my-program.js --foo "blerp" --no-flag
{ "foo" : "blerp", "flag" : false }

$ node my-program.js ---bar 7 --foo "Mr. Hand" --flag
{ bar: 7, foo: "Mr. Hand", flag: true }

$ node my-program.js --foo "blerp" -f -----p
{ foo: "blerp", flag: true, pick: true }

$ node my-program.js -fp --foofoo
{ foo: "Mr. Foo", flag: true, pick: true }

$ node my-program.js --foofoo -- -fp  # -- stops the flag parsing.
{ foo: "Mr. Foo", argv: { remain: ["-fp"] } }

$ node my-program.js --blatzk 1000 -fp # unknown opts are ok.
{ blatzk: 1000, flag: true, pick: true }

$ node my-program.js --blatzk true -fp # but they need a value
{ blatzk: true, flag: true, pick: true }

$ node my-program.js --no-blatzk -fp # unless they start with "no-"
{ blatzk: false, flag: true, pick: true }

$ node my-program.js --baz b/a/z # known paths are resolved.
{ baz: "/Users/isaacs/b/a/z" }

# if Array is one of the types, then it can take many
# values, and will always be an array.  The other types provided
# specify what types are allowed in the list.

$ node my-program.js --many 1 --many null --many foo
{ many: ["1", "null", "foo"] }

$ node my-program.js --many foo
{ many: ["foo"] }
```

Read the tests at the bottom of `lib/nopt.js` for more examples of
what this puppy can do.

## Types

The following types are supported, and defined on `nopt.typeDefs`

* String: A normal string.  No parsing is done.
* path: A file system path.  Gets resolved against cwd if not absolute.
* url: A url.  If it doesn't parse, it isn't accepted.
* Number: Must be numeric.
* Date: Must parse as a date. If it does, and `Date` is one of the options,
  then it will return a Date object, not a string.
* Boolean: Must be either `true` or `false`.  If an option is a boolean,
  then it does not need a value, and its presence will imply `true` as
  the value.  To negate boolean flags, do `--no-whatever` or `--whatever
  false`
* NaN: Means that the option is strictly not allowed.  Any value will
  fail.
* Stream: An object matching the "Stream" class in node.  Valuable
  for use when validating programmatically.  (npm uses this to let you
  supply any WriteStream on the `outfd` and `logfd` config options.)
* Array: If `Array` is specified as one of the types, then the value
  will be parsed as a list of options.  This means that multiple values
  can be specified, and that the value will always be an array.

If a type is an array of values not on this list, then those are
considered valid values.  For instance, in the example above, the
`--bloo` option can only be one of `"big"`, `"medium"`, or `"small"`,
and any other value will be rejected.

When parsing unknown fields, `"true"`, `"false"`, and `"null"` will be
interpreted as their JavaScript equivalents, and numeric values will be
interpreted as a number.

You can also mix types and values, or multiple types, in a list.  For
instance `{ blah: [Number, null] }` would allow a value to be set to
either a Number or null.

To define a new type, add it to `nopt.typeDefs`.  Each item in that
hash is an object with a `type` member and a `validate` method.  The
`type` member is an object that matches what goes in the type list.  The
`validate` method is a function that gets called with `validate(data,
key, val)`.  Validate methods should assign `data[key]` to the valid
value of `val` if it can be handled properly, or return boolean
`false` if it cannot.

You can also call `nopt.clean(data, types, typeDefs)` to clean up a
config object and remove its invalid properties.

## Error Handling

By default, nopt outputs a warning to standard error when invalid
options are found.  You can change this behavior by assigning a method
to `nopt.invalidHandler`.  This method will be called with
the offending `nopt.invalidHandler(key, val, types)`.

If no `nopt.invalidHandler` is assigned, then it will console.error
its whining.  If it is assigned to boolean `false` then the warning is
suppressed.

## Abbreviations

Yes, they are supported.  If you define options like this:

```javascript
{ "foolhardyelephants" : Boolean
, "pileofmonkeys" : Boolean }
```

Then this will work:

```bash
node program.js --foolhar --pil
node program.js --no-f --pileofmon
# etc.
```

## Shorthands

Shorthands are a hash of shorter option names to a snippet of args that
they expand to.

If multiple one-character shorthands are all combined, and the
combination does not unambiguously match any other option or shorthand,
then they will be broken up into their constituent parts.  For example:

```json
{ "s" : ["--loglevel", "silent"]
, "g" : "--global"
, "f" : "--force"
, "p" : "--parseable"
, "l" : "--long"
}
```

```bash
npm ls -sgflp
# just like doing this:
npm ls --loglevel silent --global --force --long --parseable
```

## The Rest of the args

The config object returned by nopt is given a special member called
`argv`, which is an object with the following fields:

* `remain`: The remaining args after all the parsing has occurred.
* `original`: The args as they originally appeared.
* `cooked`: The args after flags and shorthands are expanded.

## Slicing

Node programs are called with more or less the exact argv as it appears
in C land, after the v8 and node-specific options have been plucked off.
As such, `argv[0]` is always `node` and `argv[1]` is always the
JavaScript program being run.

That's usually not very useful to you.  So they're sliced off by
default.  If you want them, then you can pass in `0` as the last
argument, or any other number that you'd like to slice off the start of
the list.
