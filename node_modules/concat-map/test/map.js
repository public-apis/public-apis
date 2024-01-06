var concatMap = require('../');
var test = require('tape');

test('empty or not', function (t) {
    var xs = [ 1, 2, 3, 4, 5, 6 ];
    var ixes = [];
    var ys = concatMap(xs, function (x, ix) {
        ixes.push(ix);
        return x % 2 ? [ x - 0.1, x, x + 0.1 ] : [];
    });
    t.same(ys, [ 0.9, 1, 1.1, 2.9, 3, 3.1, 4.9, 5, 5.1 ]);
    t.same(ixes, [ 0, 1, 2, 3, 4, 5 ]);
    t.end();
});

test('always something', function (t) {
    var xs = [ 'a', 'b', 'c', 'd' ];
    var ys = concatMap(xs, function (x) {
        return x === 'b' ? [ 'B', 'B', 'B' ] : [ x ];
    });
    t.same(ys, [ 'a', 'B', 'B', 'B', 'c', 'd' ]);
    t.end();
});

test('scalars', function (t) {
    var xs = [ 'a', 'b', 'c', 'd' ];
    var ys = concatMap(xs, function (x) {
        return x === 'b' ? [ 'B', 'B', 'B' ] : x;
    });
    t.same(ys, [ 'a', 'B', 'B', 'B', 'c', 'd' ]);
    t.end();
});

test('undefs', function (t) {
    var xs = [ 'a', 'b', 'c', 'd' ];
    var ys = concatMap(xs, function () {});
    t.same(ys, [ undefined, undefined, undefined, undefined ]);
    t.end();
});
