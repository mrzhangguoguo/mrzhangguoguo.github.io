# 📝 果叔AI世界博客使用指南

## 目录结构

```
blogs-for-github/
├── _posts/          # 博客文章目录
├── _episodes/       # 播客剧集目录
├── assets/          # 静态资源
│   ├── images/      # 图片
│   └── uploads/     # 上传的文件
└── pages/           # 静态页面
```

## 一、发布新文章

### 1. 创建文章文件

在 `_posts/` 目录下创建新文件，文件名格式：
```
YYYY-MM-DD-文章标题.md
```

例如：
```
2025-08-16-ai-chatgpt-tutorial.md
```

### 2. 文章格式

每篇文章开头必须包含Front Matter（头部信息）：

```markdown
---
layout: post
title: "ChatGPT提示词工程最佳实践"
date: 2025-08-16 10:30:00 +0800
tags: [AI, ChatGPT, 教程]
excerpt: "这篇文章介绍如何编写高质量的ChatGPT提示词..."
sidebar_ad: /assets/images/ad-example.png  # 可选：自定义广告图片
---

## 文章内容开始

这里写你的文章内容...

### 小标题

文章内容继续...
```

### 3. Front Matter字段说明

| 字段 | 必填 | 说明 | 示例 |
|------|------|------|------|
| layout | ✅ | 固定为`post` | `layout: post` |
| title | ✅ | 文章标题 | `title: "我的第一篇文章"` |
| date | ✅ | 发布时间 | `date: 2025-08-16 10:30:00 +0800` |
| tags | ❌ | 文章标签 | `tags: [AI, 技术, 创业]` |
| excerpt | ❌ | 文章摘要 | `excerpt: "文章简介..."` |
| sidebar_ad | ❌ | 侧边栏广告图片 | `sidebar_ad: /assets/images/ad.png` |
| draft | ❌ | 草稿状态 | `draft: true` |

## 二、图片管理

### 1. 图片存放位置

所有图片放在 `assets/images/` 目录下，建议按年月组织：

```
assets/
└── images/
    ├── 2025/
    │   ├── 08/
    │   │   ├── screenshot1.png
    │   │   └── diagram.jpg
    └── wechat-qr.png  # 微信二维码
```

### 2. 在文章中插入图片

```markdown
![图片描述](/assets/images/2025/08/screenshot1.png)

或使用HTML（可控制大小）：
<img src="/assets/images/2025/08/screenshot1.png" alt="描述" width="600">
```

### 3. 特殊图片

- **微信二维码**: `assets/images/wechat-qr.png`
- **默认广告图**: `assets/images/521431231.png`（全站侧栏推广位，点击跳转至 https://code.yoretea.com ）
- **文章自定义广告**: 在Front Matter中指定`sidebar_ad`（图片仍将链接到 https://code.yoretea.com）

## 三、发布播客

### 1. 创建剧集文件

在 `_episodes/` 目录下创建文件：

```
episode-001-ai-news.md
```

### 2. 剧集格式

```markdown
---
layout: episode
title: "第1期：AI出海最新动态"
date: 2025-08-16 20:00:00 +0800
audio_url: https://example.com/episode1.mp3
duration_sec: 1800  # 时长（秒）
tags: [AI, 出海, 新闻]
---

## 节目简介

本期节目我们讨论...

## 时间轴

- 00:00 开场
- 02:30 新闻速递
- 10:00 深度分析
```

## 四、常用操作

### 快速创建文章

```bash
# 使用脚本创建
cat > _posts/$(date +%Y-%m-%d)-新文章标题.md << 'EOF'
---
layout: post
title: "新文章标题"
date: $(date +"%Y-%m-%d %H:%M:%S %z")
tags: []
---

文章内容...
EOF
```

### 本地预览

```bash
# 方案1：Python静态预览
python3 test_server.py
# 访问 http://localhost:8000/preview.html

# 方案2：Docker完整预览（需配置代理）
./docker-with-proxy.sh
# 访问 http://localhost:4000
```

### 发布到GitHub

```bash
git add .
git commit -m "发布新文章：文章标题"
git push origin main
```

等待几分钟后访问：https://mrzhangguoguo.github.io/

## 五、Markdown语法参考

### 基础语法

```markdown
# 一级标题
## 二级标题
### 三级标题

**粗体文字**
*斜体文字*
~~删除线~~

> 引用文字

- 无序列表1
- 无序列表2

1. 有序列表1
2. 有序列表2

[链接文字](https://example.com)

`行内代码`

\```python
# 代码块
print("Hello World")
\```
```

### 表格

```markdown
| 列1 | 列2 | 列3 |
|-----|-----|-----|
| 内容1 | 内容2 | 内容3 |
| 内容4 | 内容5 | 内容6 |
```

## 六、SEO优化建议

1. **标题优化**
   - 包含关键词
   - 控制在60个字符以内
   - 吸引人点击

2. **摘要设置**
   - 设置excerpt字段
   - 150-160个字符
   - 包含核心信息

3. **标签使用**
   - 每篇文章3-5个标签
   - 使用热门关键词
   - 保持标签一致性

4. **图片优化**
   - 添加alt描述
   - 压缩图片大小
   - 使用描述性文件名

## 七、注意事项

1. ⚠️ 文件名必须是英文或拼音，不要用中文
2. ⚠️ 日期格式必须正确：YYYY-MM-DD
3. ⚠️ Front Matter的`---`必须在文件最开始
4. ⚠️ 图片路径使用绝对路径：`/assets/images/xxx.png`
5. ⚠️ 推送前先本地预览确认

## 八、常见问题

### Q: 文章不显示？
A: 检查：
- 文件名格式是否正确
- Front Matter是否完整
- date是否是未来时间（未来的文章不会显示）

### Q: 图片不显示？
A: 检查：
- 图片路径是否正确
- 图片文件是否已上传
- 使用绝对路径 `/assets/images/`

### Q: 如何置顶文章？
A: 在Front Matter添加：
```yaml
pinned: true
weight: 100  # 数字越大越靠前
```

### Q: 如何添加视频？
A: 使用iframe嵌入：
```html
<iframe width="560" height="315" 
  src="https://www.youtube.com/embed/VIDEO_ID" 
  frameborder="0" allowfullscreen>
</iframe>
```

## 九、快捷命令

```bash
# 创建今天的文章
./new-post.sh "文章标题"

# 启动本地预览
./start.sh

# 提交到GitHub
./deploy.sh "提交说明"
```

---

有问题随时查阅此指南，祝写作愉快！🚀
