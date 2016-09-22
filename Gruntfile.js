module.exports = function(grunt) {

  grunt.initConfig({
    cacheBust: {

      options: {
        assets: ['app/static/css/**', 'app/static/js/**'],
        baseDir: 'app/static/',
        jsonOutput: true
      },

      taskName: {
        files: [{
          expand: true,
          cwd: 'app/',
          src: ['templates/**/*.html']
        }]
      }
    }

  });

  grunt.loadNpmTasks('grunt-cache-bust');

}
