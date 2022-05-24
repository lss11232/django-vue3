<!--@click.prevent.stop 是用了两个修饰符号，prevent、和stop；
 prevent 阻止默认行为修饰符，这里写没啥用，
 stop 是  阻止冒泡 ，也就是不触发父元素 的事件-->
<template>
  <div id="guide" @click.prevent.stop="handleGuide">
    <svg-icon icon="guide"></svg-icon>
  </div>
</template>

<script setup>
// 需要npm 安装   driver.js
import Driver from 'driver.js'
// 根据查找顺序，会去安装的 node_modules 下查找driver.js
import 'driver.js/dist/driver.min.css'
import { onMounted } from 'vue'
import { steps } from './steps'
import { watchLang } from '@/i18n/watchlang'
import i18n from '@/i18n'
// 这里导入  t = i18n.global.t 的话，在这个 template 模板里直接用 t 就行，不用$t 也可以
const t = i18n.global.t
let driver
onMounted(() => {
  initDriver()
})

const initDriver = () => {
  driver = new Driver({
    animate: false, // Whether to animate or not
    opacity: 0.75, // Background opacity (0 means only popovers and without overlay)
    padding: 10, // Distance of element from around the edges
    allowClose: true, // Whether the click on overlay should close or not
    overlayClickNext: false, // Whether the click on overlay should move next

    // 下面是按钮的名称
    // 完成
    doneBtnText: t('driver.doneBtnText'), // Text on the final button
    // 关闭
    closeBtnText: t('driver.closeBtnText'), // Text on the close button for this step
    // 背景颜色
    stageBackground: '#ffffff', // Background color for the staged behind highlighted element
    // 下一步
    nextBtnText: t('driver.nextBtnText'), // Next button text for this step
    // 上一步
    prevBtnText: t('driver.prevBtnText') // Previous button text for this step
  })
}

watchLang(initDriver)

// 点击按钮的事件,点击按钮的时候使用引导
const handleGuide = () => {
  driver.defineSteps(steps(t))
  driver.start()
}
</script>

<style lang="scss" scoped></style>
