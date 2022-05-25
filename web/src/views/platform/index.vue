<template>
  <el-card>
    <el-row :gutter="20" class="header">
      <el-col :span="4">
        <el-autocomplete
          :fetch-suggestions="queryItem"
          :placeholder="$t('table.placeholder')"
          clearable
          v-model="queryFrom.platform_name"
          value-key="platform_name"
          @select="handleSelect"
        ></el-autocomplete>

      </el-col>
      <!-- 搜索的时候从第一页返回 -->
      <el-button type="primary" :icon="Search" @click="initGetPlatformList(1)">{{
        $t('table.search')
      }}</el-button>
      <!-- @click="handleDialogValue" 与 @click="handleDialogValue()" ;  如果不加括号，函数的第一个参数为event   如果加了括号，需要手动传入$event才能获得事件对象。-->
      <!-- 这里要传入一个空,而不是$event 所以handleDialogValue 事件 需要添加() -->
      <el-button type="primary" @click="handleDialogValue()">{{
        $t('table.addplaceholder')
      }}</el-button>
    </el-row>
    <!-- prop 是对应 tableData  中的字段名；   字段名称 对应列内容的字段名，-->
    <el-table :data="tableData" stripe style="width: 100%">
      <el-table-column
        :width="item.width"
        :prop="item.prop"
        :label="$t(`table.${item.label}`)"
        v-for="(item, index) in options"
        :key="index"
      >
        <!-- #default="scope" 作用域插槽； v-slot="{ row }" 的row就是从scope 解构出来的  -->
        <!-- element 中tables 表格，自定义列需要使用 slot  -->
        <!-- 因为这里 不仅仅用到了后台接口的数据，还用到了 el-switch 标签，所以需要自定义列 -->
        <!-- change switch 状态发生变化时的回调函数 -->
        <template v-slot="{ row }" v-if="item.prop === 'mg_state'">
          <el-switch
            v-model="row.mg_state"
            @change="changeState(row)"
          ></el-switch>
        </template>
        <!-- 需要对时间进行加工处理， 所以需要自定义列 -->
        <template v-slot="{ row }" v-else-if="item.prop === 'create_time'">
          {{ $filters.filterTimes(row.create_time) }}
        </template>
        <!-- 默认插槽 v-slot:的语法糖是#，但后面必须有插槽名，例如v-slot:default 等价于 #default  -->
        <!-- 自定义列需要使用 slot -->
        <!--  这里用到了el-button， 所以需要自定义列-->
        <!-- 注意，这里的row，不是取展示页面上一行的信息，而是取后台api返回的一行的信息；
        所以这里row 可以取到虽然页面上没展示，但是后台api返回的字段的信息 -->
        <template #default="{ row }" v-else-if="item.prop === 'action'">
          <el-button type="primary" size="small" :icon="Edit" @click="handleDialogValue(row)"></el-button>
          <!-- <el-button type="warning" size="small" :icon="Setting"></el-button> -->
          <el-button type="danger"  size="small" :icon="Delete" @click="delPlatform(row)" ></el-button>
        </template>
      </el-table-column>
    </el-table>
    <!--  分页-->
    <!-- size-change 新每页条数   pageSize 改变时触发  -->
    <!-- current-change 新当前页    current-change 改变时触发-->
    <el-pagination
        v-model:currentPage="queryFrom.page"
        v-model:page-size="queryFrom.limit"
        :page-sizes="[2, 5, 10, 15]"
        :small="small"
        :disabled="disabled"
        :background="background"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      >
      </el-pagination>
  </el-card>
  <!-- model-value / v-model 是否显示 Dialog,element 自带的写法 -->
  <!-- v-if 解决重新点击添加用户的时候，form表单里数据要是空的 -->
  <!-- initUserList 是子组件 添加用户 确认按钮，传过来的事件，解决用户添加信息后页面不渲染刚添加的用户信息-->
  <Dialog
    v-model="dialogVisible"
    :dialogTitle="dialogTitle"
    v-if="dialogVisible"
    @initPlatformList="initGetPlatformList"
    :dialogTableValue="dialogTableValue"
  ></Dialog>
<!--  <div>平台信息</div>-->
</template>

<script setup>
import { Search, Edit, Delete } from '@element-plus/icons-vue'
import { onMounted, ref } from 'vue'
import { getPlatform, deletePlatform } from '@/api/platform.js'
import { options } from './options'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useI18n } from 'vue-i18n'
import Dialog from './components/dailog.vue'
import { isNull } from '@/utils/filters'
const i18n = useI18n()
const dialogTableValue = ref({})

const field = ref({
    field: 'platform_name'
  }
)
const queryFrom = ref({
    platform_name: '', // 后端定义的参数名，查询参数
    // service_name: '', // 后端定义的参数名，查询参数
    // pagenum: 1, // 后端定义的参数名，当前页码
    page: 1,
    // pagesize: 10 // 后端定义的参数名，每页显示条数
    limit: 10
})
const tableData = ref([])
const total = ref(0)
const dialogVisible = ref(false)
const dialogTitle = ref('')
const links = ref([])
const items = ref([])
// ***** 远程搜索
    let itemList = []
  onMounted(async() => {
    links.value = await getPlatform(field.value)
    itemList = links.value.data
    items.value = itemList
  })

    /** 需求条目模糊查询逻辑 */
    const queryItem = (queryString, cb) => {
      const results = queryString ? items.value.filter(createFilter(queryString)) : items.value
      cb(results)
    }
    const createFilter = (queryString) => {
      return (item) => {
        return (
          item.platform_name.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        )
      }
    }
// ******

const initGetPlatformList = async (page) => {
  // 当 page 传值的时候 当前页等于 page；  只有搜索的时候传值
  page && (queryFrom.value.page = page)
  // queryFrom.value.page = page?queryFrom.value.page
  const result = await getPlatform(queryFrom.value)
  // console.log(result, '00000000000000000000')
  total.value = result.total
  tableData.value = result.data
}
initGetPlatformList()

const handleSizeChange = (limit) => {
  // 更改 新每页条数，都从第一页 开始展示
  queryFrom.value.page = 1
  queryFrom.value.limit = limit
  initGetPlatformList()
}

// Go to 跳转到 哪一页
const handleCurrentChange = (page) => {
  queryFrom.value.page = page
  initGetPlatformList()
}

// const changeState = async (info) => {
//   // 调用 后台接口，更改数据库中 mg_state 的值
//   await changeUserState(info.id, info.mg_state)
//   // 更新完成后的消息提示
//   ElMessage({
//     message: i18n.t('message.updateSuccess'),
//     type: 'success'
//   })
// }

const handleDialogValue = (row) => {
    if (isNull(row)) {
        dialogTitle.value = '添加平台信息'
        // 用 dialogTableValue 来区分 是添加用户 还是 编辑用户
        dialogTableValue.value = {}
      } else {
      dialogTitle.value = '编辑平台信息'
      // console.log(row)
      // JSON.parse() 把JSON字符串 转换为 JavaScript值或对象
      // JSON.stringify  把 JavaScript 对象或值转换为 JSON 字符串
      dialogTableValue.value = JSON.parse(JSON.stringify(row))
      console.log(dialogTableValue.value)
  }
        dialogVisible.value = true // 显示dialog 对话框
}

// 删除用户
const delPlatform = (row) => {
  ElMessageBox.confirm(i18n.t('dialog.deleteTitle'), 'Warning', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    type: 'warning'
  })
     // 点击确认执行下面的代码
    .then(async () => {
      await deletePlatform(row.id)
      ElMessage({
        type: 'success',
        message: 'Delete completed'
      })
      initGetPlatformList()
    })
     //  点击 取消 按钮 执行下面的代码
    .catch(() => {
      ElMessage({
        type: 'info',
        message: 'Delete canceled'
      })
    })
}
</script>

<style lang="scss" scoped>
.header {
  padding-bottom: 16px;
  box-sizing: border-box;
}

::v-deep .el-input__suffix {
  align-items: center;
}
/* 分页放到 右边 */
::v-deep .el-pagination {
  padding-top: 16px;
  box-sizing: border-box;
  text-align: right;
}
</style>
