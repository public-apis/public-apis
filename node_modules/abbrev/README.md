# abbrev-js

Just like [ruby's Abbrev](http://apidock.com/ruby/Abbrev).

Usage:

    var abbrev = require("abbrev");
    abbrev("foo", "fool", "folding", "flop");
    
    // returns:
    { fl: 'flop'
    , flo: 'flop'
    , flop: 'flop'
    , fol: 'folding'
    , fold: 'folding'
    , foldi: 'folding'
    , foldin: 'folding'
    , folding: 'folding'
    , foo: 'foo'
    , fool: 'fool'
    }

This is handy for command-line scripts, or other cases where you want to be able to accept shorthands.
