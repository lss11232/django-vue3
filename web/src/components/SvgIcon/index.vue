<!-- :xlink:href 定义了到资源的链接-->
<template>
  <svg class="svg-icon" aria-hidden="true">
    <use :xlink:href="iconName"></use>
  </svg>
</template>

<script setup>
import { defineProps, computed } from 'vue'

// setup 中使用 父组件中定义的属性 ，需要用 defineProps 去接受同名的属性名称
const props = defineProps({
  icon: {
    type: String,
    required: true
  }
})

const iconName = computed(() => {
  return `#icon-${props.icon}` // # 是锚  icon- 是 vue.config.js 中定义的； 值为某个标签的id,这里会到  src/icons/svg/这个文件夹下去找相应的svg资源，路径是vue.config.js中定义的
})
</script>

<style lang="scss" scoped>
.svg-icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
</style>
