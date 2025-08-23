---
layout: post
title: "博客使用教程：如何发布你的第一篇文章"
date: 2025-08-16 23:30:00 +0800
tags: [教程, 博客, 入门]
excerpt: "详细介绍如何在果叔AI世界发布文章、管理图片和优化SEO。"
sidebar_ad: /assets/images/default-ad.png
permalink: /posts/how-to-use-blog/
---

## 欢迎使用果叔AI世界博客

这是一篇示例文章，展示了所有常用的Markdown语法和功能。

## 基础语法演示

### 文字样式

这是**粗体文字**，这是*斜体文字*，这是~~删除线文字~~。

你也可以使用`行内代码`来标记代码片段。

### 列表

**无序列表：**
- AI技术分享
- 出海经验总结
- 工具推荐

**有序列表：**
1. 第一步：创建文章文件
2. 第二步：编写内容
3. 第三步：发布到GitHub

### 引用

> 人工智能不是要取代人类，而是要增强人类的能力。
> 
> —— 某位智者

## 插入图片

图片可以这样插入（请替换为实际图片）：

![示例图片](/assets/images/placeholder.html)

或使用HTML控制大小：

<div style="text-align: center;">
  <img src="/assets/images/placeholder.html" alt="示例" style="max-width: 500px;">
</div>

## 代码展示

### Python代码示例

```python
def hello_ai():
    """AI世界的问候"""
    print("欢迎来到果叔AI世界！")
    return "Let's explore AI together!"

# 调用函数
message = hello_ai()
print(message)
```

### JavaScript代码示例

```javascript
// 获取文章列表
async function fetchPosts() {
  const response = await fetch('/api/posts');
  const posts = await response.json();
  return posts;
}

// 显示文章
fetchPosts().then(posts => {
  console.log('文章数量:', posts.length);
});
```

## 表格展示

| 功能 | 免费版 | 专业版 | 企业版 |
|------|--------|--------|--------|
| 文章发布 | ✅ | ✅ | ✅ |
| 图片上传 | 10张/月 | 无限 | 无限 |
| SEO优化 | 基础 | 高级 | 定制 |
| 技术支持 | 社区 | 邮件 | 专属客服 |

## 链接示例

- [访问果叔AI世界主页](/)
- [Claude Code 国内直连](https://code.yoretea.com)
- [GitHub项目地址](https://github.com/mrzhangguoguo/my-blog-podcast)

## 任务列表

- [x] 学习Markdown语法
- [x] 创建第一篇文章
- [ ] 添加自定义图片
- [ ] 分享到社交媒体

## 数学公式（需要插件支持）

行内公式：$E = mc^2$

独立公式：
$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

## 提示框（使用HTML）

<div style="background: #e3f2fd; border-left: 4px solid #2196F3; padding: 15px; margin: 20px 0;">
  <strong>💡 提示：</strong> 记得在发布前本地预览你的文章！
</div>

<div style="background: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; margin: 20px 0;">
  <strong>⚠️ 注意：</strong> 文件名必须使用英文或拼音。
</div>

<div style="background: #e8f5e9; border-left: 4px solid #4caf50; padding: 15px; margin: 20px 0;">
  <strong>✅ 成功：</strong> 你已经掌握了基本的博客写作技巧！
</div>

## 嵌入视频

可以嵌入YouTube视频（替换VIDEO_ID）：

<div style="text-align: center; margin: 20px 0;">
  <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
    frameborder="0" 
    allowfullscreen>
  </iframe>
</div>

## 总结

现在你已经了解了所有基础功能，可以开始创作了！记住：

1. 📝 使用 `./new-post.sh "标题"` 快速创建文章
2. 👀 使用 `python3 test_server.py` 本地预览
3. 🚀 使用 `./deploy.sh` 发布到线上

祝你写作愉快！如有问题，欢迎通过邮箱联系：xjzzxwork@gmail.com

---

*本文是示例文章，展示博客的各种功能。*
