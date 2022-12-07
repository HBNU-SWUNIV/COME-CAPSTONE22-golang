const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer:{ //api 요청이 있을때 어디에서 처리할지
    proxy:{
      '/api':{
        target:"http://localhost:3000/api",
        changeOrigin:true,
        pathRewrite:{
          '^/api': ''
        }
      }
    }
  },
  outputDir : "../back/public", // 배포 파일의 위치를 지정
}

