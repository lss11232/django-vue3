<template>
  <!-- unique-opened 是否只保持一个子菜单的展开 、  collapse 是否水平折叠 -->
  <el-menu
    active-text-color="#ffd04b"
    :background-color="variables.menuBg"
    class="el-menu-vertical-demo"
    :default-active="defaultActive"
    text-color="#fff"
    router
    unique-opened
    :collapse="!$store.getters.siderType"
  >
    <!-- 这里  使用 elment ，相当于el-sub-menu  是子组件，这里父组件使用el-sub-menu 子组件，index 是 elment 定义需要的-->
    <!-- 下面el-sub-menu 实现父级 菜单的显示 -->
    <el-sub-menu
      :index="item.id"
      v-for="(item, index) in menusList"
      :key="item.id"
    >
      <template #title>
        <el-icon>
          <!-- 动态组件实际上就是一个 component 标签，通过is属性来决定这个显示的是哪个组件-->
          <component :is="iconList[index]"></component>
        </el-icon>
        <span>{{ item.authName }}</span>
      </template>
      <!-- index 就是路由到哪个url ,下面是子菜单-->
      <el-menu-item
        :index="'/' + it.path"
        v-for="it in item.children"
        :key="it.id"
        @click="savePath(it.path)"
      >
        <template #title>
          <el-icon>
            <component :is="icon"></component>
          </el-icon>
          <span>{{ $t(`menus.${it.path}`) }}</span>
        </template>
      </el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<script setup>
import { menuList } from '@/api/menu'
import { ref } from 'vue'
import variables from '@/styles/variables.scss'

const iconList = ref(['user', 'setting', 'shop', 'tickets', 'pie-chart'])
const icon = ref('menu')

// 因为 路由中访问 /  默认访问 /users，所以为了保持一致，这里 users需要被选中
const defaultActive = ref(sessionStorage.getItem('path') || '/platform')
const menusList = ref([])
const initMenusList = async () => {
  menusList.value = await menuList()
  menusList.value = menusList.value.data
  // console.log('6666666666666666888888888888888888888888888888888888888888888', menusList.value.data)
}
initMenusList()

const savePath = (path) => {
  sessionStorage.setItem('path', `/${path}`)
}
</script>

<style lang="scss" scoped></style>
