const compare = require('./compare')
const lt = (a, b, loose) => compare(a, b, loose) < 0
module.exports = lt
