const compare = require('./compare')
const eq = (a, b, loose) => compare(a, b, loose) === 0
module.exports = eq
