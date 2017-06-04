var gulp     = require('gulp'),
    jsonLint = require('gulp-jsonlint');

gulp.task('lint', function() {
    gulp.src('apis.json')
        .pipe(jsonLint())
        .pipe(jsonLint.reporter());
});

gulp.task('default', ['lint']);
