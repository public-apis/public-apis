const compare = require('./compare')
const compareLoose = (a, b) => compare(a, b, true)
module.exports = compareLoose
