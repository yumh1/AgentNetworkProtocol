import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Model Context Protocol",
  description: "A protocol that enables seamless integration between LLM applications and external data sources and tools",
  
  locales: {
    root: {
      label: 'English',
      lang: 'en'
    },
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      link: '/zh/'
    }
  },

  // 主题相关配置
  appearance: true,
  lastUpdated: true,
  
  themeConfig: {
    logo: '/logo.png',
    nav: [
      { text: 'Guide', link: '/guide/' },
      { text: 'Specification', link: '/specification/' },
      { text: 'Blog', link: '/blog/' },
      {
        text: 'Resources',
        items: [
          { text: 'GitHub', link: 'https://github.com/chgaowei/AgentNetworkProtocol' }
        ]
      }
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Introduction',
          items: [
            { text: 'What is MCP?', link: '/guide/what-is-mcp' },
            { text: 'Getting Started', link: '/guide/getting-started' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/chgaowei/AgentNetworkProtocol' }
    ],

    // 搜索配置
    search: {
      provider: 'local'
    },
    
    // 文档页脚配置
    docFooter: {
      prev: '上一页',
      next: '下一页'
    },
    
    // 大纲配置
    outline: {
      level: [2, 3],
      label: {
        'zh': '页面导航',
        'en': 'On this page'
      }
    },
    
    // 页脚配置
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024-present Model Context Protocol'
    }
  }
})
