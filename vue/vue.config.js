const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: 'http://localhost:8080/',
  outputDir: '../static/dist',
  indexPath: '../../templates/layout/base_vue.html',

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  },
  transpileDependencies: true
})
