#!/usr/bin/env node
var nopt = require("../lib/nopt")
  , types = { num: Number
            , bool: Boolean
            , help: Boolean
            , list: Array
            , "num-list": [Number, Array]
            , "str-list": [String, Array]
            , "bool-list": [Boolean, Array]
            , str: String }
  , shorthands = { s: [ "--str", "astring" ]
                 , b: [ "--bool" ]
                 , nb: [ "--no-bool" ]
                 , tft: [ "--bool-list", "--no-bool-list", "--bool-list", "true" ]
                 , "?": ["--help"]
                 , h: ["--help"]
                 , H: ["--help"]
                 , n: [ "--num", "125" ] }
  , parsed = nopt( types
                 , shorthands
                 , process.argv
                 , 2 )

console.log("parsed", parsed)

if (parsed.help) {
  console.log("")
  console.log("nopt cli tester")
  console.log("")
  console.log("types")
  console.log(Object.keys(types).map(function M (t) {
    var type = types[t]
    if (Array.isArray(type)) {
      return [t, type.map(function (type) { return type.name })]
    }
    return [t, type && type.name]
  }).reduce(function (s, i) {
    s[i[0]] = i[1]
    return s
  }, {}))
  console.log("")
  console.log("shorthands")
  console.log(shorthands)
}
