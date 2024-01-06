'use strict'

exports.directories = function () {
  return [
    '.git', // Git repository files, see <https://git-scm.com/>
    '.nyc_output', // Temporary directory where nyc stores coverage data, see <https://github.com/bcoe/nyc>
    '.sass-cache', // Cache folder for node-sass, see <https://github.com/sass/node-sass>
    'bower_components', // Where Bower packages are installed, see <http://bower.io/>
    'coverage', // Standard output directory for code coverage reports, see <https://github.com/gotwarlost/istanbul>
    'node_modules' // Where Node modules are installed, see <https://nodejs.org/>
  ]
}
