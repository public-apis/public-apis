# yallist

Yet Another Linked List

There are many doubly-linked list implementations like it, but this
one is mine.

For when an array would be too big, and a Map can't be iterated in
reverse order.


[![Build Status](https://travis-ci.org/isaacs/yallist.svg?branch=master)](https://travis-ci.org/isaacs/yallist) [![Coverage Status](https://coveralls.io/repos/isaacs/yallist/badge.svg?service=github)](https://coveralls.io/github/isaacs/yallist)

## basic usage

```javascript
var yallist = require('yallist')
var myList = yallist.create([1, 2, 3])
myList.push('foo')
myList.unshift('bar')
// of course pop() and shift() are there, too
console.log(myList.toArray()) // ['bar', 1, 2, 3, 'foo']
myList.forEach(function (k) {
  // walk the list head to tail
})
myList.forEachReverse(function (k, index, list) {
  // walk the list tail to head
})
var myDoubledList = myList.map(function (k) {
  return k + k
})
// now myDoubledList contains ['barbar', 2, 4, 6, 'foofoo']
// mapReverse is also a thing
var myDoubledListReverse = myList.mapReverse(function (k) {
  return k + k
}) // ['foofoo', 6, 4, 2, 'barbar']

var reduced = myList.reduce(function (set, entry) {
  set += entry
  return set
}, 'start')
console.log(reduced) // 'startfoo123bar'
```

## api

The whole API is considered "public".

Functions with the same name as an Array method work more or less the
same way.

There's reverse versions of most things because that's the point.

### Yallist

Default export, the class that holds and manages a list.

Call it with either a forEach-able (like an array) or a set of
arguments, to initialize the list.

The Array-ish methods all act like you'd expect.  No magic length,
though, so if you change that it won't automatically prune or add
empty spots.

### Yallist.create(..)

Alias for Yallist function.  Some people like factories.

#### yallist.head

The first node in the list

#### yallist.tail

The last node in the list

#### yallist.length

The number of nodes in the list.  (Change this at your peril.  It is
not magic like Array length.)

#### yallist.toArray()

Convert the list to an array.

#### yallist.forEach(fn, [thisp])

Call a function on each item in the list.

#### yallist.forEachReverse(fn, [thisp])

Call a function on each item in the list, in reverse order.

#### yallist.get(n)

Get the data at position `n` in the list.  If you use this a lot,
probably better off just using an Array.

#### yallist.getReverse(n)

Get the data at position `n`, counting from the tail.

#### yallist.map(fn, thisp)

Create a new Yallist with the result of calling the function on each
item.

#### yallist.mapReverse(fn, thisp)

Same as `map`, but in reverse.

#### yallist.pop()

Get the data from the list tail, and remove the tail from the list.

#### yallist.push(item, ...)

Insert one or more items to the tail of the list.

#### yallist.reduce(fn, initialValue)

Like Array.reduce.

#### yallist.reduceReverse

Like Array.reduce, but in reverse.

#### yallist.reverse

Reverse the list in place.

#### yallist.shift()

Get the data from the list head, and remove the head from the list.

#### yallist.slice([from], [to])

Just like Array.slice, but returns a new Yallist.

#### yallist.sliceReverse([from], [to])

Just like yallist.slice, but the result is returned in reverse.

#### yallist.toArray()

Create an array representation of the list.

#### yallist.toArrayReverse()

Create a reversed array representation of the list.

#### yallist.unshift(item, ...)

Insert one or more items to the head of the list.

#### yallist.unshiftNode(node)

Move a Node object to the front of the list.  (That is, pull it out of
wherever it lives, and make it the new head.)

If the node belongs to a different list, then that list will remove it
first.

#### yallist.pushNode(node)

Move a Node object to the end of the list.  (That is, pull it out of
wherever it lives, and make it the new tail.)

If the node belongs to a list already, then that list will remove it
first.

#### yallist.removeNode(node)

Remove a node from the list, preserving referential integrity of head
and tail and other nodes.

Will throw an error if you try to have a list remove a node that
doesn't belong to it.

### Yallist.Node

The class that holds the data and is actually the list.

Call with `var n = new Node(value, previousNode, nextNode)`

Note that if you do direct operations on Nodes themselves, it's very
easy to get into weird states where the list is broken.  Be careful :)

#### node.next

The next node in the list.

#### node.prev

The previous node in the list.

#### node.value

The data the node contains.

#### node.list

The list to which this node belongs.  (Null if it does not belong to
any list.)
