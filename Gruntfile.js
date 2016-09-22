module.exports = function(grunt) {

  grunt.initConfig({

    cacheBust: {
      assets: ['app/static/css/**', 'app/static/js/**']
    }

    taskName: {
      files: [{
        expand: true,
        src: ['app/templates/*/**.html']
      }]
    }

  });

  grunt.loadNpmTasks('grunt-cache-bust');

}
