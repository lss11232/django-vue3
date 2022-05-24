<!-- 全屏的时候，使用退出的图片；不是全屏的时候使用，全屏图标 -->
<template>
  <div @click="handleFullScreen" id="screenFul">
    <svg-icon :icon="icon ? 'exit-fullscreen' : 'fullscreen'"></svg-icon>
  </div>
</template>

<script setup>
// 使用 screenfull 这个插件
import screenfull from 'screenfull'
import { ref, onMounted, onBeforeMount } from 'vue'

// screenfull.isFullscreen 判断现在是否是全屏
const icon = ref(screenfull.isFullscreen)
const handleFullScreen = () => {
  // screenfull.isEnabled  判断浏览器是否支持全屏
  if (screenfull.isEnabled) {
    screenfull.toggle() // screenfull.toggle() 可以双向切换全屏与非全屏
  }
}

const changeIcon = () => {
  icon.value = screenfull.isFullscreen
}

// ref(screenfull.isFullscreen) 监听不到 screenfull.isFullscreen 值的变化，所以需要onMounted、onBeforeMount
onMounted(() => {
  // 这里写 screenfull.off('change')   onBeforeMount 中写 screenfull.on('change', changeIcon) 也可以
  // change 发生改变 是否全屏 的时候调用 changeIcon 方法 ， change是一个js的事件名称
  // 检测全屏变化
  screenfull.on('change', changeIcon)
})

onBeforeMount(() => {
  // 删除 监听器
  screenfull.off('change')
})
</script>

<style lang="scss" scoped></style>
