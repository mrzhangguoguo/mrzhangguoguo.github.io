#!/bin/bash
# 使用代理启动Docker Jekyll服务器

echo "🐳 配置Docker使用代理"
echo "======================"
echo ""

# 设置代理
export HTTP_PROXY=socks5://127.0.0.1:1081
export HTTPS_PROXY=socks5://127.0.0.1:1081
export ALL_PROXY=socks5://127.0.0.1:1081

echo "📍 代理设置: socks5://127.0.0.1:1081"
echo ""

# 拉取Jekyll镜像
echo "📦 下载Jekyll Docker镜像..."
docker pull jekyll/jekyll:latest

if [ $? -eq 0 ]; then
    echo "✅ 镜像下载成功！"
    echo ""
    echo "🚀 启动Jekyll服务器..."
    
    # 启动Jekyll服务器
    docker run --rm \
      --volume="$PWD:/srv/jekyll" \
      --publish 4000:4000 \
      --publish 35729:35729 \
      jekyll/jekyll:latest \
      jekyll serve --livereload --baseurl '' --host 0.0.0.0 --force_polling
else
    echo "❌ 镜像下载失败"
    echo ""
    echo "可能的解决方案："
    echo "1. 检查代理是否运行: curl --proxy socks5://127.0.0.1:1081 https://google.com"
    echo "2. 使用Docker Desktop配置代理"
    echo "3. 使用国内镜像源"
fi