<!-- @command="handleCommand" 点击菜单项触发的事件回调-->
<!-- command="zh" 派发到command回调函数的指令参数 -->
<template>
  <el-dropdown @command="handleCommand">
    <svg-icon icon="language"></svg-icon>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item command="zh" :disabled="currentLanguage === 'zh'"
          >中文</el-dropdown-item
        >
        <el-dropdown-item command="en" :disabled="currentLanguage === 'en'"
          >English</el-dropdown-item
        >
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { computed } from 'vue'
import { useStore } from 'vuex'
const i18n = useI18n()
const store = useStore()
const currentLanguage = computed(() => {
  // 获取 i18n.locale.value  // 值是 src/i18n/index.js 中 指定的
  return i18n.locale.value
})

// var 就是 template 中command 属性的值
const handleCommand = (val) => {
  i18n.locale.value = val // i18n.locale 这个值必须更改，就是根据这个值来判断显示中文还是英文的
  store.commit('app/changLang', val) // 存store 中一份
  localStorage.setItem('lang', val) // 存localStorage 中一份
}
</script>

<style lang="scss" scoped></style>
