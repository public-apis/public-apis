const compare = require('./compare')
const gte = (a, b, loose) => compare(a, b, loose) >= 0
module.exports = gte
