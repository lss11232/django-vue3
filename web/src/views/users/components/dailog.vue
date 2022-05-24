<!-- close 是Dialog 关闭的回调，就是点击Dialog 右上角 x 时执行的 -->
<!-- model-value 是 element 自己封装的单向绑定， model-value / v-model 是否显示 Dialog -->
<!-- :model-value="dialogVisible"  根据 父组件中  v-model="dialogVisible"   的dialogVisible 的值 来判断是否显示 Dialog -->
<template>
  <el-dialog
    :model-value="dialogVisible"
    :title="dialogTitle"
    width="40%"
    @close="handleClose"
  >
    <!-- :model="form" 表单数据对象 -->
    <el-form  ref="formRef" :model="form" label-width="70px" :rules="rules">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item  label="密码"  prop="password" v-if="dialogTitle === '添加用户'" >
        <el-input v-model="form.password" type="password"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="手机" prop="mobile">
        <el-input v-model="form.mobile"></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleClose">取消</el-button>
        <el-button type="primary" @click="handleConfirm">确认</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { defineEmits, ref, defineProps, watch } from 'vue'
import { addUser, editUser } from '@/api/users'
import i18n from '@/i18n'
import { ElMessage } from 'element-plus'
const props = defineProps({
  dialogTitle: { // dialog的标题
    type: String,
    default: '',
    required: true // 父组件必须传入这个属性
  },
  dialogTableValue: {
    type: Object,
    default: () => {}
  }
})
// 组件间双向绑定 ,子组件 通过 $emit('update:modelValue', this.modelValue) 获取父组件中 v-model="xxxx" 的值
// 添加用户后，添加的信息不会立即渲染  所以需要重新获取下数据，来渲染  initUserList
const emit = defineEmits(['update:modelValue', 'initUserList'])
// formRef 用于表单验证  // 名字与标签 ref   ref="formRef"  的名字相等，这是固定写法
const formRef = ref(null)
const form = ref({
  username: '',
  password: '',
  email: '',
  mobile: ''
})
// model-value 是 element 的单向绑定
const handleClose = () => {
  // 修改父组件中 v-model="dialogVisible" 的dialogVisible 的值为 false
  emit('update:modelValue', false)
}
const handleConfirm = () => {
      //  formRef.value 获取 ref 有 formRef 的 dom 元素  //  validate 对整个表单的内容进行验证。 接收一个回调函数，或返回 Promise。
      //  validate校验通过,valid为true   validate校验不通过,valid为false
      formRef.value.validate(async (valid) => {
        if (valid) {
      props.dialogTitle === '添加用户'
        ? await addUser(form.value)
        : await editUser(form.value)
          ElMessage({
            message: i18n.global.t('message.updateSuccess'),
            type: 'success'
          })
          // 让父组件 执行方法 请求 后台api 获取数据
          emit('initUserList')
          handleClose()
        } else {
          console.log('error submit!!')
          return false
        }
     })
}
const rules = ref({
  username: [
    {
      required: true, // 是否必填
      message: 'Please input Activity name', // 提示信息
      trigger: 'blur' // 验证逻辑的触发方式
    }
  ],
  password: [
    {
      required: true,
      message: 'Please input Activity name',
      trigger: 'blur'
    }
  ],
  email: [
    {
      required: true,
      message: 'Please input Activity name',
      trigger: 'blur'
    },
    // email 额外的校验
    {
      type: 'email',
      message: '请输入正确邮箱',
      trigger: ['blur', 'change'] // 触发方式，blur失去焦点，change数据改变 // 没有进行任何输入时，不会触发change，但一定会触发blur事件
    }
  ],
  mobile: [
    {
      required: true,
      message: '请输入手机号',
      trigger: 'blur'
    },
   { pattern: /^1[3|5|7|8|9]\d{9}$/, message: '请输入正确的号码格式', trigger: 'change' }
  ]
})
watch(
  () => props.dialogTableValue,
  () => {
    // props.dialogTableValue  当 为添加用户的时候，props.dialogTableValue 为空，就是把空值 赋值给 form.value
    // 当为编辑用户 的时候，会把选中的一行（后台api返回的一行）信息 赋值给props.dialogTableValue， props.dialogTableValue  把值 又赋值给 form.value
    form.value = props.dialogTableValue
  },
  { deep: true, immediate: true }
)
</script>

<style lang="scss" scoped></style>
