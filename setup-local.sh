#!/bin/bash
# 使用Bundler创建本地隔离环境（不需要rbenv）

echo "🔧 设置本地Jekyll环境"
echo "====================="
echo ""

# 检查Ruby版本
echo "📍 Ruby版本: $(ruby --version)"
echo ""

# 配置Bundler使用本地路径
echo "📦 配置Bundler使用本地vendor目录..."
bundle config set --local path 'vendor/bundle'

# 安装Jekyll和依赖到本地目录
echo "💎 安装Jekyll到本地目录（vendor/bundle）..."
echo "   这不会影响系统的gem..."

# 创建简化的Gemfile
cat > Gemfile.local << 'EOF'
source "https://rubygems.org"

gem "jekyll", "~> 4.3.0"
gem "jekyll-feed"
gem "jekyll-sitemap"
gem "minima"
gem "webrick"
EOF

# 使用本地Gemfile安装
BUNDLE_GEMFILE=Gemfile.local bundle install

echo ""
echo "✅ 安装完成！"
echo ""
echo "所有gem都安装在: vendor/bundle/"
echo "这个目录可以随时删除，不会影响系统"
echo ""
echo "启动Jekyll服务器："
echo "  BUNDLE_GEMFILE=Gemfile.local bundle exec jekyll serve --baseurl ''"
echo ""