import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default {
  ...DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      // 这里可以自定义布局组件
    })
  },
  enhanceApp({ app, router, siteData }) {
    // 注册自定义组件
  }
}
