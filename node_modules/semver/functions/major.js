const SemVer = require('../classes/semver')
const major = (a, loose) => new SemVer(a, loose).major
module.exports = major
