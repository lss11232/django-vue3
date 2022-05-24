// store对象中getters就类似于计算属性，
// 若想获取state的变量，直接获取即可，
// 但很多时候获取的state变量需要经过一系列的加工或计算才是我们想要的，因此才有了getters
export default {
  token: (state) => state.app.token,
  siderType: (state) => state.app.siderType,
  lang: (state) => state.app.lang
}
