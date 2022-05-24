<!-- separator 分隔符 -->
<!-- 下面 template 中 breadcrumbList  可以直接替换为 route.matched，也就是 script 中可以不定义breadcrumbList。下面这样写是为了好看点把-->
<template>
  <el-breadcrumb separator="/">
    <el-breadcrumb-item v-for="(item, index) in breadcrumbList" :key="index">
      <span class="no-redirect" v-if="index === breadcrumbList.length - 1">{{
        $t(`menus.${item.name}`)
      }}</span>
      <span class="redirect" v-else @click="handleRedirect(item.path)">{{
        $t(`menus.${item.name}`)
      }}</span>
    </el-breadcrumb-item>
  </el-breadcrumb>
</template>

<script setup>
import { watch, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
// route对象表示当前的路由信息，包含了当前 URL 解析得到的信息。包含当前的路径，参数，query对象等。
const route = useRoute()
// router对象是全局路由的实例，是router构造方法的实例。 可以用router 来改变当前的 路由url
const router = useRouter()

const breadcrumbList = ref([])

// 注意initBreadcrumbList 方法需要写在 watch 上面，因为watch定义immediate 一开始就会执行一次
const initBreadcrumbList = () => {
  breadcrumbList.value = route.matched
  // console.log(route.matched)
}
const handleRedirect = (path) => {
  router.push(path)
}

watch(
  route,
  () => {
    initBreadcrumbList()
  },
  { deep: true, immediate: true } // immediate 一开始就会执行一次，不管监听的数据是否更新   // deep 深度监视
)
</script>

<style lang="scss" scoped>
.no-redirect {
  color: #97a8be;
  cursor: text;
}
.redirect {
  color: #666;
  font-weight: 600;
  cursor: pointer;
  &:hover {
    color: $menuBg;
  }
}
</style>
