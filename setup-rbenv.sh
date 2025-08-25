#!/bin/bash
# 使用rbenv设置隔离的Ruby环境（不影响系统Ruby）

echo "🔧 设置隔离的Ruby环境"
echo "====================="
echo ""

# 检查是否已安装Homebrew
if ! command -v brew &> /dev/null; then
    echo "📦 安装Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# 安装rbenv
if ! command -v rbenv &> /dev/null; then
    echo "📦 安装rbenv..."
    brew install rbenv ruby-build
    
    # 添加到shell配置
    echo "" >> ~/.zshrc
    echo '# rbenv配置' >> ~/.zshrc
    echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
    
    echo "" >> ~/.bash_profile
    echo '# rbenv配置' >> ~/.bash_profile
    echo 'eval "$(rbenv init - bash)"' >> ~/.bash_profile
fi

# 初始化rbenv
eval "$(rbenv init -)"

# 安装Ruby 3.0.0（Jekyll推荐版本）
echo "📦 安装Ruby 3.0.0（隔离版本）..."
rbenv install -s 3.0.0

# 设置项目Ruby版本
echo "📍 设置当前项目使用Ruby 3.0.0..."
rbenv local 3.0.0

# 安装bundler和jekyll
echo "💎 安装Jekyll（仅在项目环境）..."
gem install bundler jekyll

# 安装项目依赖
echo "📦 安装项目依赖..."
bundle install

echo ""
echo "✅ 设置完成！"
echo ""
echo "环境信息："
echo "  Ruby版本: $(ruby -v)"
echo "  Jekyll版本: $(jekyll -v)"
echo "  安装位置: $(rbenv prefix)"
echo ""
echo "这个Ruby环境完全独立于系统Ruby，不会影响其他项目。"
echo ""
echo "启动服务器："
echo "  bundle exec jekyll serve --baseurl ''"
echo ""
echo "提示：每次打开新终端需要运行 'eval \"\$(rbenv init -)\"' 来激活rbenv"