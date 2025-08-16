#!/bin/bash
# 快速部署到GitHub Pages

if [ -z "$1" ]; then
    COMMIT_MSG="更新博客内容"
else
    COMMIT_MSG="$1"
fi

echo "📦 准备部署..."
echo ""

# 添加所有更改
git add -A

# 显示更改
echo "📝 更改的文件："
git status --short
echo ""

# 提交
git commit -m "$COMMIT_MSG

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# 推送
echo "🚀 推送到GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 部署成功！"
    echo ""
    echo "⏱️  等待几分钟让GitHub Pages构建..."
    echo "🌐 访问: https://mrzhangguoguo.github.io/my-blog-podcast/"
else
    echo "❌ 部署失败，请检查网络连接"
fi