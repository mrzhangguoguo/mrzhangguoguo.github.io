# 果叔AI世界博客项目 - Claude AI上下文文档

## 项目概述

**项目名称**: 果叔AI世界（my-blog-podcast）
**项目类型**: Jekyll静态博客 + 播客平台
**部署平台**: GitHub Pages
**访问地址**: https://mrzhangguoguo.github.io/my-blog-podcast/
**开发状态**: 基础功能已完成，可正常使用

## 项目信息

- **所有者**: mrzhangguoguo
- **邮箱**: xjzzxwork@gmail.com
- **主题**: 分享AI出海干货，AI圈最新消息
- **语言**: 中文（zh-CN）
- **时区**: Asia/Shanghai

## 技术栈

- **静态生成器**: Jekyll 4.3
- **托管平台**: GitHub Pages
- **前端框架**: 原生HTML/CSS/JavaScript
- **CMS系统**: Decap CMS（原Netlify CMS）
- **版本控制**: Git
- **本地开发**: Python/Docker/rbenv（多种方案）

## 已完成功能 ✅

### 核心功能
1. **博客系统**
   - Markdown文章支持
   - 自动生成文章目录（TOC）
   - 标签分类系统
   - 文章摘要
   - 草稿功能

2. **播客系统**
   - 音频文件管理
   - 剧集列表
   - RSS订阅源
   - 播放器集成

3. **界面设计**
   - 响应式三栏布局（桌面端）
   - 左侧悬浮目录（文章页）
   - 右侧信息边栏（首页/文章页）
   - 深色/浅色主题切换
   - 移动端自适应

4. **侧边栏模块**
   - About介绍
   - 微信二维码
   - 邮箱联系
   - 推荐链接（Claude Code国内直连）
   - 热门标签云
   - 广告位
   - 相关文章

5. **SEO优化**
   - 中文语言设置
   - 元标签优化
   - Open Graph
   - JSON-LD结构化数据
   - XML站点地图
   - RSS订阅

6. **开发工具**
   - 快速创建文章脚本（new-post.sh）
   - 一键部署脚本（deploy.sh）
   - 本地预览服务器（test_server.py）
   - Docker环境配置
   - 代理配置支持

## 项目结构

```
blogs-for-github/
├── _posts/              # 博客文章
│   └── YYYY-MM-DD-title.md
├── _episodes/           # 播客剧集
├── _layouts/            # 页面模板
│   ├── default.html    # 基础模板
│   ├── post.html       # 文章模板
│   └── episode.html    # 播客模板
├── _includes/          # 可重用组件
│   ├── home-sidebar.html    # 首页侧边栏
│   ├── post-sidebar.html    # 文章侧边栏
│   ├── toc.html            # 目录组件
│   └── navigation.html     # 导航栏
├── assets/
│   ├── css/
│   │   └── style.css       # 主样式文件
│   └── images/
│       ├── wechat-qr.png   # 微信二维码（需替换）
│       └── default-ad.png  # 默认广告图（需替换）
├── pages/
│   └── about.md           # 关于页面
├── _config.yml           # Jekyll配置
├── index.md             # 首页
├── BLOG_GUIDE.md        # 使用指南
├── LOCAL_SETUP.md       # 本地环境说明
└── claude.md           # 本文档
```

## 文章格式规范

```markdown
---
layout: post
title: "文章标题"
date: 2025-08-16 10:30:00 +0800
tags: [AI, 教程, 技术]
excerpt: "文章摘要，150-160字符"
sidebar_ad: /assets/images/custom-ad.png  # 可选
draft: false  # 草稿状态
---

文章内容...
```

## 常用命令

```bash
# 创建新文章
./new-post.sh "文章标题"

# 本地预览
python3 test_server.py

# 部署到GitHub Pages
./deploy.sh "提交说明"

# Docker完整预览（需配置代理）
./docker-with-proxy.sh
```

## 待优化功能 🔧

1. **功能增强**
   - [ ] 站内搜索
   - [ ] 评论系统（Giscus/Disqus）
   - [ ] 访问统计（Google Analytics）
   - [ ] 相关文章智能推荐
   - [ ] 文章阅读进度条

2. **性能优化**
   - [ ] 图片懒加载
   - [ ] 资源压缩
   - [ ] PWA支持
   - [ ] CDN加速

3. **内容管理**
   - [ ] 分类系统
   - [ ] 文章系列
   - [ ] 作者系统
   - [ ] 多语言支持

## 已知问题

1. **Docker代理问题**
   - 需要配置socks5://127.0.0.1:1081代理
   - 或使用国内镜像源

2. **图片占位符**
   - wechat-qr.png需要替换为实际二维码
   - default-ad.png需要替换为实际广告图

3. **Jekyll本地安装**
   - 系统Ruby权限受限
   - 推荐使用Docker或Python预览

## 开发建议

### 下次迭代方向

1. **内容优先**
   - 定期发布高质量文章
   - 建立内容发布计划
   - 优化SEO关键词

2. **用户体验**
   - 添加搜索功能
   - 实现评论互动
   - 改进移动端体验

3. **商业化**
   - 接入广告系统
   - 添加赞助功能
   - 会员订阅系统

### 技术注意事项

1. **提交规范**
   - 使用中文commit信息
   - 包含emoji标识
   - 详细说明更改内容

2. **图片管理**
   - 按年月组织目录
   - 压缩图片大小
   - 使用描述性文件名

3. **SEO优化**
   - 每篇文章设置excerpt
   - 合理使用标签（3-5个）
   - 优化标题长度（60字符内）

## 环境配置

### Git配置
```bash
git config --global http.proxy socks5://127.0.0.1:1081
git config --global https.proxy socks5://127.0.0.1:1081
```

### Docker代理
在Docker Desktop中设置：
Settings → Resources → Proxies → socks5://127.0.0.1:1081

### Python服务器
无需配置，直接运行：
```bash
python3 test_server.py
```

## 联系支持

- **项目问题**: 提交Issue到GitHub仓库
- **技术咨询**: xjzzxwork@gmail.com
- **功能建议**: 通过邮箱或微信联系

## 更新历史

### 2025-08-16
- ✅ 初始化Jekyll博客框架
- ✅ 实现双侧边栏布局
- ✅ 添加响应式设计
- ✅ 配置中文语言
- ✅ 创建使用文档
- ✅ 添加快捷脚本
- ✅ 发布示例文章

## 原始需求文档

### 🎯 目标
- 托管：GitHub Pages（原生 Jekyll 构建）
- 页面：主页、About、标签页、文章、播客
- 风格：现代极简、艺术感、深浅色模式
- 后台：Decap CMS - 增删改查、草稿发布、自定义permalink、SEO字段
- Feed：RSS博客与播客订阅

### ✅ 验收标准
- GitHub Pages自动构建成功，主页/标签/详情可访问
- /feed.xml与/podcast.xml可被抓取
- /admin可创建/编辑内容；草稿不出现在站点，合并后即发布
- 自定义permalink、canonical、jsonld生效
- 标签页同时汇总文章与播客

---

**最后更新**: 2025-08-16
**下次对话重点**: 根据用户需求决定（内容发布/功能优化/问题修复）