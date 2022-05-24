import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/styles/index.scss'
import SvgIcon from '@/icons'
import 'element-plus/dist/index.css'
import '@/router/permission' // 这里就会使用这个 permission.ja，让没有登录只能访问特定 url
import * as ELIcons from '@element-plus/icons-vue' // element-plus 自带的图标
import i18n from '@/i18n'
// 导入全局属性
import filters from './utils/filters'

const app = createApp(App)

// 把图标 都注册为全局组件，ELIcons 相当于是个字典
for (const iconName in ELIcons) {
  app.component(iconName, ELIcons[iconName])
  // console.log(iconName + ' 图标呀11111111')
}

filters(app)
// 传递给 icons/index.js 中定义的函数，注册为全局组件
SvgIcon(app)
app.use(store).use(router).use(i18n).mount('#app')
