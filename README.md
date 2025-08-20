# 🌟 果叔AI世界 - 个人博客与播客平台

基于Jekyll的现代化博客和播客平台，专注于分享AI出海干货和AI圈最新消息。

🌐 **在线访问**: https://mrzhangguoguo.github.io/

## ✨ 功能特性

### 核心功能
- 📝 **博客系统** - 支持Markdown写作，自动生成目录
- 🎙️ **播客平台** - 音频内容管理和RSS订阅
- 🏷️ **标签系统** - 文章分类和标签云
- 🔍 **SEO优化** - 元标签、结构化数据、站点地图
 - 💡 **语法高亮** - Rouge 高亮，清晰的代码块配色
 - 📈 **Mermaid 图表** - Markdown 中的 mermaid 代码块自动渲染

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
 - 🧭 **根域部署** - 使用用户站点仓库 `mrzhangguoguo.github.io`

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
或直接：
```bash
git add .
git commit -m "更新说明"
git push origin main
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
permalink: /posts/your-english-slug/   # 推荐：自定义英文URL，避免中文编码
redirect_from:                         # 可选：为历史URL保留跳转
  - "/posts/你的历史中文URL/"
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
说明：该预览不渲染 Jekyll 模板，仅用于快速查看样式（例如代码高亮、表格、Mermaid 效果）。

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

## 🌐 部署与域名

- 用户站点仓库：当前仓库已更名为 `mrzhangguoguo.github.io`，主页即根域。
- 站点配置：
  - `_config.yml`: `url: https://mrzhangguoguo.github.io`，`baseurl: ""`
  - `public/admin/config.yml`: `public_folder: "/assets/uploads"`，`backend.repo: mrzhangguoguo/mrzhangguoguo.github.io`
- 链接引用：页面/模板中优先使用 `| relative_url`，避免硬编码子路径。

## 🔗 URL 策略（重要）

- 文章与播客的 URL 通过 `permalink` 人工自定义（英文），与中文标题解耦。
- 已开启 `jekyll-redirect-from` 插件，可用 `redirect_from` 为旧链接提供 301 跳转。
- 全站文章默认路径：`/posts/:slug/`；播客：`/episodes/:slug/`。

## 🧩 富文本与可读性增强

- 代码高亮：使用 Rouge，高对比度配色；行内与块级代码均已优化。
- Mermaid：在 Markdown 使用围栏代码块标记 `mermaid`，前端自动渲染为图表。
- 表格：提供边框、表头底色、斑马纹与横向滚动，避免溢出。
- 长内容防溢出：对长链接、英文单词、内联 code 开启换行保护；图片/视频/iframe 限制 `max-width:100%`。

## 🧭 布局说明

- 文章页三栏布局采用 2:6:2（带最小宽度约束），中间主列严格占 60%。
- 目录仅抓取 H2 级标题，避免目录过长影响阅读。

## 📊 GA4 集成（可选）

1) 在 `_config.yml` 添加：`ga_measurement_id: G-XXXXXXXXXX`
2) 新建 `_includes/ga.html`（示例见下）：
```html
<script async src="https://www.googletagmanager.com/gtag/js?id={{ site.ga_measurement_id }}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);} gtag('js', new Date());
  gtag('config', '{{ site.ga_measurement_id }}', { anonymize_ip: true });
  // 自定义事件：gtag('event','name',{param:'value'})
</script>
```
3) 在 `_layouts/default.html` 的 `<head>` 中引入：
```liquid
{% raw %}{% if jekyll.environment == "production" and site.ga_measurement_id %}
  {% include ga.html %}
{% endif %}{% endraw %}
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
 - [x] URL 英文化与跳转（permalink + redirect_from）
 - [x] 代码高亮与 Mermaid 图表
 - [x] 三栏 2:6:2 布局与阅读体验优化

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
- **博客**: [果叔AI世界](https://mrzhangguoguo.github.io/)

## 📄 许可证

MIT License - 自由使用和修改

## 🙏 致谢

- Jekyll - 静态站点生成器
- GitHub Pages - 免费托管服务
- Claude Code - AI辅助开发

---

**最后更新**: 2025年8月16日
