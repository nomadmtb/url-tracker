module.exports = function(grunt) {

  grunt.initConfig({
    cacheBust: {

      options: {
        assets: ['app/static/css/*', 'app/static/js/*'],
        baseDir: './static/'
      },

      taskName: {
        files: [{
          expand: true,
          cwd: 'app/templates'
        }]
      }

      taskName: {
        options: {
          assets: ['app/static/css/*', 'app/static/js/*'],
          baseDir: './static/'
        },
        src: ['app/templates/_base.html']
      }

    },
  });

  grunt.loadNpmTasks('grunt-cache-bust');

}
