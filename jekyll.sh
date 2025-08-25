#!/bin/bash
# Jekyll Docker 启动脚本
# 完全隔离的Jekyll环境，不会污染系统

echo "🐳 Jekyll Docker 环境"
echo "================================"
echo "此脚本使用Docker运行Jekyll，不会影响您的系统环境"
echo ""

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker未安装。请先安装Docker Desktop："
    echo "   https://www.docker.com/products/docker-desktop"
    exit 1
fi

# 检查Docker是否运行
if ! docker info &> /dev/null; then
    echo "❌ Docker未运行。请启动Docker Desktop"
    exit 1
fi

echo "请选择操作："
echo "1) 启动Jekyll服务器 (http://localhost:4000)"
echo "2) 构建站点"
echo "3) 创建新文章"
echo "4) 安装/更新依赖"
echo "5) 清理Docker容器"
echo ""
read -p "选择 (1-5): " choice

case $choice in
    1)
        echo "🚀 启动Jekyll服务器..."
        docker run --rm \
            -v "$PWD:/srv/jekyll" \
            -p 4000:4000 \
            -p 35729:35729 \
            jekyll/jekyll:latest \
            jekyll serve --livereload --baseurl ''
        ;;
    2)
        echo "🔨 构建Jekyll站点..."
        docker run --rm \
            -v "$PWD:/srv/jekyll" \
            jekyll/jekyll:latest \
            jekyll build
        echo "✅ 构建完成！站点文件在 _site 目录"
        ;;
    3)
        read -p "文章标题: " title
        slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g')
        date=$(date +%Y-%m-%d)
        filename="_posts/${date}-${slug}.md"
        
        docker run --rm \
            -v "$PWD:/srv/jekyll" \
            jekyll/jekyll:latest \
            sh -c "cat > $filename << 'EOF'
---
layout: post
title: \"$title\"
date: $(date +%Y-%m-%d\ %H:%M:%S)
tags: []
---

在这里写你的内容...
EOF"
        echo "✅ 创建新文章: $filename"
        ;;
    4)
        echo "📦 安装/更新依赖..."
        docker run --rm \
            -v "$PWD:/srv/jekyll" \
            jekyll/jekyll:latest \
            bundle install
        echo "✅ 依赖安装完成"
        ;;
    5)
        echo "🧹 清理Docker容器..."
        docker system prune -f
        echo "✅ 清理完成"
        ;;
    *)
        echo "❌ 无效选择"
        exit 1
        ;;
esac