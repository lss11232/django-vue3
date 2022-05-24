// 定义引导步骤
// 因为 vue 是单页面的，也就是只有一个html， 所以 指定 元素的id 都可以找的到
// 这里的 i18n形参，就是 driver/index.vue 中 传入的 i18n.global.t 这个实参
export const steps = (i18n) => [
  {
    // element 是个id 元素
    element: '#guide',
    popover: {
      // 标题
      title: i18n('driver.guideBtn'),
      // 描述
      description: 'Body of the popover',
      // 弹窗出现的位置
      position: 'left'
    }
  },
  {
    element: '#hamburger',
    popover: {
      title: i18n('driver.hamburgerBtn'),
      description: '这个是汉堡按钮',
      position: 'bottom'
    }
  },
  {
    element: '#screenFul',
    popover: {
      title: i18n('driver.fullScreen'),
      description: 'Body of the popover',
      position: 'left'
    }
  }
]
