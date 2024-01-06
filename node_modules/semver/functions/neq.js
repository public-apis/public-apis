const compare = require('./compare')
const neq = (a, b, loose) => compare(a, b, loose) !== 0
module.exports = neq
