#!/bin/bash
# 使用用户目录安装Jekyll（完全不需要sudo）

echo "🔧 设置用户级Jekyll环境"
echo "========================"
echo ""

# 设置GEM环境变量
export GEM_HOME="$HOME/.gem"
export PATH="$GEM_HOME/bin:$PATH"

echo "📍 设置GEM_HOME: $GEM_HOME"
echo "📍 Ruby版本: $(ruby --version)"
echo ""

# 安装bundler到用户目录
echo "💎 安装Bundler到用户目录..."
gem install bundler --user-install

# 添加到PATH
export PATH="$HOME/.gem/ruby/2.6.0/bin:$PATH"

# 配置bundle使用本地vendor目录
echo "📦 配置项目依赖..."
bundle config set --local path 'vendor/bundle'

# 创建最小化Gemfile
cat > Gemfile.minimal << 'EOF'
source "https://rubygems.org"

gem "jekyll", "~> 3.9.0"  # 使用3.9版本，兼容Ruby 2.6
gem "jekyll-feed"
gem "jekyll-sitemap"
gem "webrick"
EOF

# 安装依赖
echo "📦 安装Jekyll（到项目vendor目录）..."
BUNDLE_GEMFILE=Gemfile.minimal bundle install --path vendor/bundle

echo ""
echo "✅ 设置完成！"
echo ""
echo "启动服务器命令："
echo "  export PATH=\"\$HOME/.gem/ruby/2.6.0/bin:\$PATH\""
echo "  BUNDLE_GEMFILE=Gemfile.minimal bundle exec jekyll serve --baseurl ''"
echo ""
echo "或使用快捷脚本："
echo "  ./run-jekyll.sh"

# 创建启动脚本
cat > run-jekyll.sh << 'EOF'
#!/bin/bash
export PATH="$HOME/.gem/ruby/2.6.0/bin:$PATH"
export GEM_HOME="$HOME/.gem"
BUNDLE_GEMFILE=Gemfile.minimal bundle exec jekyll serve --baseurl '' --host 0.0.0.0
EOF

chmod +x run-jekyll.sh

echo ""
echo "已创建 run-jekyll.sh 启动脚本"