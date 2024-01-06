# lru cache

A cache object that deletes the least-recently-used items.

[![Build Status](https://travis-ci.org/isaacs/node-lru-cache.svg?branch=master)](https://travis-ci.org/isaacs/node-lru-cache) [![Coverage Status](https://coveralls.io/repos/isaacs/node-lru-cache/badge.svg?service=github)](https://coveralls.io/github/isaacs/node-lru-cache)

## Installation:

```javascript
npm install lru-cache --save
```

## Usage:

```javascript
var LRU = require("lru-cache")
  , options = { max: 500
              , length: function (n, key) { return n * 2 + key.length }
              , dispose: function (key, n) { n.close() }
              , maxAge: 1000 * 60 * 60 }
  , cache = new LRU(options)
  , otherCache = new LRU(50) // sets just the max size

cache.set("key", "value")
cache.get("key") // "value"

// non-string keys ARE fully supported
// but note that it must be THE SAME object, not
// just a JSON-equivalent object.
var someObject = { a: 1 }
cache.set(someObject, 'a value')
// Object keys are not toString()-ed
cache.set('[object Object]', 'a different value')
assert.equal(cache.get(someObject), 'a value')
// A similar object with same keys/values won't work,
// because it's a different object identity
assert.equal(cache.get({ a: 1 }), undefined)

cache.reset()    // empty the cache
```

If you put more stuff in it, then items will fall out.

If you try to put an oversized thing in it, then it'll fall out right
away.

## Options

* `max` The maximum size of the cache, checked by applying the length
  function to all values in the cache.  Not setting this is kind of
  silly, since that's the whole purpose of this lib, but it defaults
  to `Infinity`.  Setting it to a non-number or negative number will
  throw a `TypeError`.  Setting it to 0 makes it be `Infinity`.
* `maxAge` Maximum age in ms.  Items are not pro-actively pruned out
  as they age, but if you try to get an item that is too old, it'll
  drop it and return undefined instead of giving it to you.
  Setting this to a negative value will make everything seem old!
  Setting it to a non-number will throw a `TypeError`.
* `length` Function that is used to calculate the length of stored
  items.  If you're storing strings or buffers, then you probably want
  to do something like `function(n, key){return n.length}`.  The default is
  `function(){return 1}`, which is fine if you want to store `max`
  like-sized things.  The item is passed as the first argument, and
  the key is passed as the second argumnet.
* `dispose` Function that is called on items when they are dropped
  from the cache.  This can be handy if you want to close file
  descriptors or do other cleanup tasks when items are no longer
  accessible.  Called with `key, value`.  It's called *before*
  actually removing the item from the internal cache, so if you want
  to immediately put it back in, you'll have to do that in a
  `nextTick` or `setTimeout` callback or it won't do anything.
* `stale` By default, if you set a `maxAge`, it'll only actually pull
  stale items out of the cache when you `get(key)`.  (That is, it's
  not pre-emptively doing a `setTimeout` or anything.)  If you set
  `stale:true`, it'll return the stale value before deleting it.  If
  you don't set this, then it'll return `undefined` when you try to
  get a stale entry, as if it had already been deleted.
* `noDisposeOnSet` By default, if you set a `dispose()` method, then
  it'll be called whenever a `set()` operation overwrites an existing
  key.  If you set this option, `dispose()` will only be called when a
  key falls out of the cache, not when it is overwritten.
* `updateAgeOnGet` When using time-expiring entries with `maxAge`,
  setting this to `true` will make each item's effective time update
  to the current time whenever it is retrieved from cache, causing it
  to not expire.  (It can still fall out of cache based on recency of
  use, of course.)

## API

* `set(key, value, maxAge)`
* `get(key) => value`

    Both of these will update the "recently used"-ness of the key.
    They do what you think. `maxAge` is optional and overrides the
    cache `maxAge` option if provided.

    If the key is not found, `get()` will return `undefined`.

    The key and val can be any value.

* `peek(key)`

    Returns the key value (or `undefined` if not found) without
    updating the "recently used"-ness of the key.

    (If you find yourself using this a lot, you *might* be using the
    wrong sort of data structure, but there are some use cases where
    it's handy.)

* `del(key)`

    Deletes a key out of the cache.

* `reset()`

    Clear the cache entirely, throwing away all values.

* `has(key)`

    Check if a key is in the cache, without updating the recent-ness
    or deleting it for being stale.

* `forEach(function(value,key,cache), [thisp])`

    Just like `Array.prototype.forEach`.  Iterates over all the keys
    in the cache, in order of recent-ness.  (Ie, more recently used
    items are iterated over first.)

* `rforEach(function(value,key,cache), [thisp])`

    The same as `cache.forEach(...)` but items are iterated over in
    reverse order.  (ie, less recently used items are iterated over
    first.)

* `keys()`

    Return an array of the keys in the cache.

* `values()`

    Return an array of the values in the cache.

* `length`

    Return total length of objects in cache taking into account
    `length` options function.

* `itemCount`

    Return total quantity of objects currently in cache. Note, that
    `stale` (see options) items are returned as part of this item
    count.

* `dump()`

    Return an array of the cache entries ready for serialization and usage
    with 'destinationCache.load(arr)`.

* `load(cacheEntriesArray)`

    Loads another cache entries array, obtained with `sourceCache.dump()`,
    into the cache. The destination cache is reset before loading new entries

* `prune()`

    Manually iterates over the entire cache proactively pruning old entries
