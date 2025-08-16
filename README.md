# 🌟 果叔AI世界 - 个人博客与播客平台

基于Jekyll的现代化博客和播客平台，专注于分享AI出海干货和AI圈最新消息。

🌐 **在线访问**: https://mrzhangguoguo.github.io/my-blog-podcast/

## ✨ 功能特性

### 核心功能
- 📝 **博客系统** - 支持Markdown写作，自动生成目录
- 🎙️ **播客平台** - 音频内容管理和RSS订阅
- 🏷️ **标签系统** - 文章分类和标签云
- 🔍 **SEO优化** - 元标签、结构化数据、站点地图

### 界面设计
- 🎨 **响应式布局** - 完美适配桌面、平板、手机
- 🌓 **深色模式** - 自动切换明暗主题
- 📊 **双侧边栏** - 左侧目录导航，右侧广告位
- 💬 **联系模块** - 微信二维码、邮箱联系

### 技术特点
- ⚡ **静态站点** - 基于Jekyll，GitHub Pages托管
- 🚀 **快速部署** - Git推送自动构建
- 🔧 **易于维护** - 简单的Markdown文件管理
- 🌍 **中文优化** - 完全中文界面和日期格式

## 🚀 快速开始

### 1. 创建新文章
```bash
./new-post.sh "文章标题"
```

### 2. 本地预览
```bash
python3 test_server.py
# 访问: http://localhost:8000/preview.html
```

### 3. 发布到线上
```bash
./deploy.sh "更新说明"
```

## 📁 项目结构

```
blogs-for-github/
├── _posts/          # 博客文章
├── _episodes/       # 播客剧集
├── _layouts/        # 页面模板
├── _includes/       # 可重用组件
├── assets/          # 静态资源
│   ├── css/        # 样式文件
│   └── images/     # 图片资源
├── pages/          # 静态页面
├── _config.yml     # Jekyll配置
└── index.md        # 首页
```

## 📝 文章格式

```markdown
---
layout: post
title: "文章标题"
date: 2025-08-16 10:30:00 +0800
tags: [AI, 教程, 技术]
excerpt: "文章摘要..."
sidebar_ad: /assets/images/ad.png  # 可选
---

文章内容...
```

## 🖼️ 图片管理

- **微信二维码**: `assets/images/wechat-qr.png`
- **默认广告图**: `assets/images/default-ad.png`
- **文章图片**: `assets/images/YYYY/MM/图片名.png`

## 🛠️ 本地开发

### 方案1: Python预览（最简单）
```bash
python3 test_server.py
```

### 方案2: Docker运行（完整功能）
```bash
# 配置Docker代理后运行
./docker-with-proxy.sh
```

### 方案3: Jekyll本地安装
```bash
# 使用rbenv安装隔离环境
./setup-rbenv.sh
```

## 🎯 核心功能实现

### 已完成功能 ✅
- [x] 基础Jekyll博客框架
- [x] 首页右侧边栏（About、微信、邮箱、推荐）
- [x] 文章页双侧边栏（目录+广告）
- [x] 响应式移动端适配
- [x] 深色模式切换
- [x] 中文语言设置
- [x] SEO基础优化
- [x] 标签系统
- [x] RSS订阅
- [x] Decap CMS配置

### 待优化功能 🔧
- [ ] 搜索功能
- [ ] 评论系统
- [ ] 访问统计
- [ ] 相关文章推荐算法
- [ ] 图片懒加载
- [ ] PWA支持

## 📖 使用文档

- **使用指南**: [BLOG_GUIDE.md](BLOG_GUIDE.md)
- **本地环境**: [LOCAL_SETUP.md](LOCAL_SETUP.md)
- **项目规划**: [claude.md](claude.md)

## 🤝 联系方式

- **邮箱**: xjzzxwork@gmail.com
- **GitHub**: [mrzhangguoguo](https://github.com/mrzhangguoguo)
- **博客**: [果叔AI世界](https://mrzhangguoguo.github.io/my-blog-podcast/)

## 📄 许可证

MIT License - 自由使用和修改

## 🙏 致谢

- Jekyll - 静态站点生成器
- GitHub Pages - 免费托管服务
- Claude Code - AI辅助开发

---

**最后更新**: 2025年8月16日