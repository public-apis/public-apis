const SemVer = require('../classes/semver')
const patch = (a, loose) => new SemVer(a, loose).patch
module.exports = patch
