#!/bin/bash
# 使用Docker启动Jekyll服务器

echo "🐳 使用Docker启动Jekyll服务器"
echo "=============================="
echo ""
echo "首次运行会下载Jekyll镜像（约200MB）"
echo ""

# 启动Jekyll服务器
docker run --rm \
  --volume="$PWD:/srv/jekyll:Z" \
  --publish 4000:4000 \
  jekyll/jekyll:latest \
  jekyll serve --baseurl '' --host 0.0.0.0

# 如果失败，提供备选方案
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Jekyll启动失败"
    echo ""
    echo "备选方案："
    echo "1. 使用Python查看静态预览："
    echo "   python3 test_server.py"
    echo "   访问: http://localhost:8000/preview.html"
    echo ""
    echo "2. 检查Docker是否运行："
    echo "   docker ps"
fi