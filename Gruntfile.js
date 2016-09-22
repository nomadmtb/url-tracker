module.exports = function(grunt) {

  grunt.initConfig({

    cacheBust: {
      options: {
        assets: ['/static/**/*.css', '/static/**/*.js'],
        baseDir: 'app'
      },

      taskName: {
        files: [{
          expand: true,
          cwd: 'app/templates',
          src: ['*.html']
        }]
      }
    }

  });

  grunt.loadNpmTasks('grunt-cache-bust');

}
