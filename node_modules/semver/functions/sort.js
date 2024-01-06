const compareBuild = require('./compare-build')
const sort = (list, loose) => list.sort((a, b) => compareBuild(a, b, loose))
module.exports = sort
