import SvgIcon from '@/components/SvgIcon'

// 调用webpack  从一个文件夹引入模块  // 检索 当前目录下的 svg 目录，不检索 子目录， 匹配svg 结尾的文件
const svgRequired = require.context('./svg', false, /\.svg$/)
svgRequired.keys().forEach((item) => svgRequired(item))

// 注册为全局组件，这里只是声明；调用需要传入vue 实例才会执行
export default (app) => {
  app.component('svg-icon', SvgIcon)
}
