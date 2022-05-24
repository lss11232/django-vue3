// 需要安装第三方库 dayjs
const dayjs = require('dayjs')

const filterTimes = (val, format = 'YYYY-MM-DD') => {
  if (!isNull(val)) {
    val = parseInt(val) * 1000
    return dayjs(val).format(format)
  } else {
    return '--'
  }
}

// 判断 date 时间 是否为空
export const isNull = (date) => {
  if (!date) return true
  if (JSON.stringify(date) === '{}') return true
  if (JSON.stringify(date) === '[]') return true
}

// 添加全局属性 $filters
export default (app) => {
  app.config.globalProperties.$filters = {
    filterTimes
  }
}
