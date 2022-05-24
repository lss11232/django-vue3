<template>
  <router-view />
</template>

<style lang="scss">
  /* 用于 点击删除用户的时候， 提示图标和提示信息错位，不在一行的问题*/
  .el-message-box__status {
  position: absolute !important;
}
</style>
