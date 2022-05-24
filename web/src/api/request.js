import axios from 'axios'
import { ElMessage } from 'element-plus'
import { diffTokenTime } from '@/utils/auth'
import store from '@/store'
import qs from 'qs'
const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // 每个接口都添加 VUE_APP_BASE_API 的值,build打包的时候可以选择不同环境变量中的VUE_APP_BASE_API的值
  timeout: 5000
})
// 取消重复请求 start
// 声明一个Map用于存储每个请求的标识和取消函数
const pending = new Map()
/**
 * 添加请求
 * @param {Object} config
 */
const addPending = (config) => {
  const url = [
    config.method,
    config.url,
    // qs.stringify()是将对象 序列化成URL的形式，以&进行拼接
    qs.stringify(config.params),
    qs.stringify(config.data)
  ].join('&') // join 把数组合成一个字符串 以 & 连接  // url 是以 & 拼接的字符串，存放在map 中当作key
  // console.log(url)
  // cancelToken自定义的，名字可以随便换；一开始请求config中是没有 cancelToken 的
  // cancelToken 是唯一的，每个请求cancelToken都不一样；
  config.cancelToken =
    config.cancelToken ||
    new axios.CancelToken((cancel) => { // axios.CancelToken构造函数生成取消函数
      if (!pending.has(url)) {
        // 如果pending中不存在当前请求
        pending.set(url, cancel) // 每个请求都对应一个 cancel
      }
    })
}
/**
 * 移除请求
 * @param {Object} config
 */
const removePending = (config) => {
  const url = [
    config.method,
    config.url,
    qs.stringify(config.params),
    qs.stringify(config.data)
  ].join('&')
  if (pending.has(url)) {
    // 如果pending中存在当前请求标识，需要取消当前请求，并移除
    const cancel = pending.get(url) // 获取这个url 对应的cancel
    cancel(url) // 取消请求
    pending.delete(url)
  }
}
/**
 * 清空pending中的请求（在路由跳转时调用）
 */
// clearPending 在路由前置守卫 router.beforeEach 那使用，跳转url了，取消之前的所有请求，把pending 清空
export const clearPending = () => {
  for (const [url, cancel] of pending) {
    cancel(url)
  }
  pending.clear()
}

// 取消重复请求 end

// 请求拦截器 //校验 token 本地是否存在 //每个接口请求 后端api 都添加 token 信息
service.interceptors.request.use(
   // onfulfiled函数：成功的回调函数 （value）=> { }
   // onrejected函数：失败的回调函数 (reason ) => { }
   // 请求成功执行下面的代码
  // config 是 axios 请求前传入的信息，比如 请求的url、请求的method 方式 等的信息
  (config) => { // 这个函数就是 service.interceptors.request.use 成功请求的回调函数 // config 就是axios 获取到的 请求的相关信息
    removePending(config) // 请求开始前，对之前的请求做检查取消操作
    addPending(config) // 将当前请求添加到pending中
    if (localStorage.getItem('token')) {
      // 每次请求接口的时候，都会去校验 登录时间是否大于定义的超时时间
      if (diffTokenTime()) { // 校验token 是否过期
        // 执行 退出登录 操作
        store.dispatch('app/logout')
        return Promise.reject(new Error('token 失效了'))
      }
    }
    // Authorization 是自己随便定义的
    config.headers.Authorization = localStorage.getItem('token')
    // console.log(config)
    return config
  },
  // 请求失败执行下面的代码
  (error) => {
    return Promise.reject(new Error(error))
  }
)

 // 响应拦截器
 // response 是请求返回的信息  response 是Promise.resolve(结果)简写
service.interceptors.response.use(
  (response) => {
    // 在请求结束后，移除本次请求
    removePending(response)
    const { data, meta } = response.data
    // 请求正常相应就行执行下面的代码  // 相当于 Promise 中  then
    if (meta.status === 200 || meta.status === 201) {
      return data
    } else {
      console.log(response)
      ElMessage.error(meta.msg)
      return Promise.reject(new Error(meta.msg))
    }
  }, // 如果访问出错，比如500错误，就会执行下面的 // 相当于 Promise 中 catch    //error 是其他未知 返回的结果
  (error) => {
    console.log(error.response)
    // error.response  存在  就弹窗提示 response.data 中的错误信息
    error.response && ElMessage.error(error.response.data)
    return Promise.reject(new Error(error.response.data))
  }
)
export default service
