import request from './request'
// 获取用户数据
export const getUser = (params) => {
  return request({ url: '/users', params })
}

// 更改 用户的 状态
export const changeUserState = (uId, type) => {
  return request({
    url: `users/${uId}/state/${type}`,
    method: 'put'
  })
}

// 增加用户
export const addUser = (data) => {
  return request({ url: 'users', method: 'post', data })
}

// 编辑用户
export const editUser = (data) => {
  return request({ url: `users/${data.id}`, method: 'put', data })
}

export const deleteUser = (id) => {
  return request({ url: `users/${id}`, method: 'delete' })
}
