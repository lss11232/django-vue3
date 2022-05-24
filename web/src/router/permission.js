import router from './index'
import store from '@/store'
import { clearPending } from '@/api/request'

const whiteList = ['/login']
router.beforeEach((to, from, next) => {
  clearPending()
  if (store.getters.token) { // 这里会判断 store 下的token 是否有值
    if (to.path === '/login') {
      next('/')
    } else {
      next()
    }
  } else { // includes 判断 要去的  路由 是否在 whiteList 白名单中
    if (whiteList.includes(to.path)) {
      next()
    } else {
      next('/login')
    }
  }
})
