import { createI18n } from 'vue-i18n'
import EN from './en'
import ZH from './zh'
const messages = {
  // ... 是 es6的扩展运算符
  en: {
    // 相当于 把EN 这个对象 直接赋值给 en这个对象
    ...EN
  },
  zh: {
    ...ZH
  }
}
//
const getCurrentLanguage = () => {
  // 获取浏览器配置语言 // navigator 浏览器自带的方法 // zh-CN 是中国大陆地区 zh 是香港、新加坡浏览器中使用的
  const UAlang = navigator.language

  // UAlang.indexOf 检索 zh字符串是否在UAlang中出现，没找到会返回 -1
  // 包含 zh 就用zh ，不包含 zh 就用 en
  const langCode = UAlang.indexOf('zh') !== -1 ? 'zh' : 'en'
  // 第一次登录 setItem 中存一份，让 vuex store  第一次登录系统的时候获取
  localStorage.setItem('lang', langCode)
  return langCode // 返回的值 决定 用 zh 还是 en
}

const i18n = createI18n({
  legacy: false, // 必须指定为false
  globalInjection: true, // 全局模式，可以直接使用 $t
  locale: getCurrentLanguage() || 'zh', // getCurrentLanguage 方法执行错误， zh 赋值 给 locale
  messages: messages // 使用哪些文字
})

export default i18n
