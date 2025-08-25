#!/bin/bash
# 一键启动Jekyll开发服务器（使用Docker，不污染系统）

echo "🚀 启动Jekyll开发服务器"
echo "========================"
echo ""

# 检查Docker
if ! command -v docker &> /dev/null; then
    echo "❌ 需要先安装Docker Desktop"
    echo "   下载地址: https://www.docker.com/products/docker-desktop"
    echo ""
    echo "或者使用其他方式："
    echo "1. 使用rbenv管理Ruby版本（不污染系统Ruby）"
    echo "2. 使用Python服务器查看静态预览"
    exit 1
fi

# 使用Docker运行Jekyll
echo "🐳 使用Docker运行Jekyll（完全隔离环境）"
echo "📍 访问地址: http://localhost:4000"
echo "📍 实时刷新: 已启用"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "------------------------"

docker run --rm \
    --volume="$PWD:/srv/jekyll" \
    --publish 4000:4000 \
    --publish 35729:35729 \
    -it jekyll/jekyll:latest \
    jekyll serve --livereload --baseurl ''