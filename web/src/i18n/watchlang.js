import { watch } from 'vue'
import store from '@/store'

// 引导页 按钮文字使用， 当切换语言的时候， 引导页 按钮文字（上一步、下一步、完成、关闭）语言， 也相应的替换为中文 或 英文

// ... 相当于接受多个参数
export const watchLang = function (...cbs) {
   // 这里的 ... 会自动给传递的参数添加上 []， 相当于 cbs = [...cbs]的结果，这里cbs 实际是  [initDriver()] 注意，会自动添加上函数的()
  // console.log(arguments, '111111111111')
  // console.log(cbs, '555555555555555555555555555555555555555555555555')
  watch(
    // 监听 store.getters.lang 值发生改变的时候
    // 监听 reactive 这样的数据，watch 的第一个参数，要用 箭头函数 的形式
    () => store.getters.lang,
    // ()是空，不用当前值和原始值
    () => {
      // 传入 store.getters.lang 没啥用，initDriver 中不会使用这个参数，因为initDriver中就没有形参接受
      // cbs 是 [initDriver()]  ,cb 也就是initDriver()
      cbs.forEach((cb) => cb(store.getters.lang))
      // 写成下面这样也可以
      // cbs.forEach((cb) => cb)
    },
    { deep: true } // deep 深度监视
  )
}
