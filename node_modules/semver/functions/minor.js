const SemVer = require('../classes/semver')
const minor = (a, loose) => new SemVer(a, loose).minor
module.exports = minor
