import request from './request'
// 获取平台数据
export const getPlatform = (params) => {
  return request({ url: '/Platform/', params })
}

// 更改 平台状态
// export const changeUserState = (uId, type) => {
//   return request({
//     url: `users/${uId}/state/${type}`,
//     method: 'put'
//   })
// }

// 增加 平台信息
export const addPlatform = (data) => {
  return request({ url: 'Platform/', method: 'post', data })
}

// 编辑平台信息
export const editPlatform = (data) => {
  return request({ url: `Platform/${data.id}/`, method: 'put', data })
}

// 删除平台信息
export const deletePlatform = (id) => {
  return request({ url: `Platform/${id}/`, method: 'delete' })
}
