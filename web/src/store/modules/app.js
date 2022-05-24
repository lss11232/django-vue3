import { login as loginApi } from '@/api/login'
import router from '@/router'
import { setTokenTime } from '@/utils/auth'
export default {
  namespaced: true,
  state: () => ({
    token: localStorage.getItem('token') || '',
    siderType: true,
    lang: localStorage.getItem('lang') || 'zh'
  }),
  mutations: {
    setToken(state, token) { // 第一个参数接受的是 state
      // 下面这行不写，url 不会跳转，因为 router/permission.js 中 会对state.token 做判断
      state.token = token // 这里更改的是 store 中 state 下token 的值
      localStorage.setItem('token', token) // 这里更改的是浏览器中存储 的token 信息
    },
    changeSiderType(state) {
      state.siderType = !state.siderType
    },
    changLang (state, lang) {
      state.lang = lang
    }
  },
  actions: {
    login({ commit }, userInfo) { // 第一个参数接受的是 store，  userInfo 是浏览器中输入的账号密码
      return new Promise((resolve, reject) => {
        loginApi(userInfo) // 这里执行 axios 请求
          .then((res) => {
            // console.log(res)
            commit('setToken', res.token) // 调用mutations的setToken 方法 存储token  // 获取data.token  信息
            // 把登录时间放到 localStorage 中
            setTokenTime()
            router.replace('/') // 重定向到首页
            resolve()
          })
          .catch((err) => {
            reject(err)
          })
      })
    },
    // 退出
    logout({ commit }) {
      commit('setToken', '')
      localStorage.clear()
      router.replace('/login')
    }
  }
}
