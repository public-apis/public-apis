var undefsafe = require('undefsafe');

var object = {
  a: {
    b: {
      c: 1,
      d: [1, 2, 3],
      e: 'remy'
    }
  }
};

console.log(undefsafe(object, 'a.b.e')); // "remy"
console.log(undefsafe(object, 'a.b.not.found')); // undefined
