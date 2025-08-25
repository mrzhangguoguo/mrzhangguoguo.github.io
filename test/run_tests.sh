#!/bin/bash

# Jekyll 博客和播客平台测试脚本
echo "🚀 开始测试 Jekyll 博客和播客平台..."
echo "=================================="

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 测试结果统计
PASSED=0
FAILED=0
TOTAL=0

# 测试函数
run_test() {
    local test_name="$1"
    local test_command="$2"
    
    echo -e "${BLUE}测试: ${test_name}${NC}"
    
    if eval "$test_command" &> /dev/null; then
        echo -e "${GREEN}✅ PASSED${NC}: $test_name"
        ((PASSED++))
    else
        echo -e "${RED}❌ FAILED${NC}: $test_name"
        ((FAILED++))
    fi
    ((TOTAL++))
    echo ""
}

# 检查必要文件
run_test "检查 _config.yml 配置文件" "[ -f _config.yml ]"
run_test "检查 Gemfile" "[ -f Gemfile ]"
run_test "检查首页文件" "[ -f index.md ]"
run_test "检查关于页面" "[ -f pages/about.md ]"
run_test "检查默认布局" "[ -f _layouts/default.html ]"
run_test "检查文章布局" "[ -f _layouts/post.html ]"
run_test "检查播客布局" "[ -f _layouts/episode.html ]"

# 检查内容文件
run_test "检查示例文章" "[ -f _posts/2025-08-16-welcome-to-your-new-blog.md ]"
run_test "检查示例播客" "[ -f _episodes/welcome-episode.md ]"

# 检查 Feed 文件
run_test "检查博客 RSS" "[ -f rss.xml ]"
run_test "检查播客 RSS" "[ -f podcast.xml ]"

# 检查 CMS 文件
run_test "检查 CMS 入口页面" "[ -f public/admin/index.html ]"
run_test "检查 CMS 配置" "[ -f public/admin/config.yml ]"

# 检查样式文件
run_test "检查主样式文件" "[ -f assets/css/style.css ]"

# 检查 includes 文件
run_test "检查 SEO includes" "[ -f _includes/head-seo.html ]"
run_test "检查导航 includes" "[ -f _includes/navigation.html ]"

# 验证配置文件语法
echo -e "${BLUE}验证配置文件语法...${NC}"

# 检查 YAML 语法
run_test "验证 _config.yml YAML 语法" "ruby -ryaml -e 'YAML.load_file(\"_config.yml\")'"
run_test "验证 CMS config.yml YAML 语法" "ruby -ryaml -e 'YAML.load_file(\"public/admin/config.yml\")'"

# 检查 Front Matter 语法
echo -e "${BLUE}检查 Front Matter 语法...${NC}"

check_frontmatter() {
    local file="$1"
    if [ -f "$file" ]; then
        # 提取 front matter 并验证
        if head -n 20 "$file" | grep -q "^---$"; then
            echo "✅ $file front matter 格式正确"
            return 0
        else
            echo "❌ $file front matter 格式错误"
            return 1
        fi
    else
        echo "❌ 文件不存在: $file"
        return 1
    fi
}

run_test "验证文章 Front Matter" "check_frontmatter '_posts/2025-08-16-welcome-to-your-new-blog.md'"
run_test "验证播客 Front Matter" "check_frontmatter '_episodes/welcome-episode.md'"

# 检查关键内容
echo -e "${BLUE}检查内容完整性...${NC}"

run_test "检查 _config.yml 包含 title" "grep -q 'title:' _config.yml"
run_test "检查 _config.yml 包含 collections" "grep -q 'collections:' _config.yml"
run_test "检查 _config.yml 包含 episodes" "grep -q 'episodes:' _config.yml"

# 检查 CSS 基础语法
run_test "检查 CSS 文件非空" "[ -s assets/css/style.css ]"
run_test "检查 CSS 包含主题变量" "grep -q ':root' assets/css/style.css"
run_test "检查 CSS 包含深色主题" "grep -q 'data-theme=\"dark\"' assets/css/style.css"

# 检查 JavaScript 功能
run_test "检查主题切换 JS" "grep -q 'toggleTheme' _layouts/default.html"

# 生成测试报告
echo "=================================="
echo -e "${BLUE}📊 测试报告${NC}"
echo "=================================="
echo -e "总测试数: ${TOTAL}"
echo -e "${GREEN}通过: ${PASSED}${NC}"
echo -e "${RED}失败: ${FAILED}${NC}"

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 所有测试通过！${NC}"
    echo ""
    echo "✅ 项目结构完整"
    echo "✅ 配置文件正确"
    echo "✅ 内容文件存在"
    echo "✅ 样式和脚本就绪"
    echo ""
    echo "🚀 现在可以运行以下命令启动本地开发:"
    echo "   bundle install"
    echo "   bundle exec jekyll serve"
    exit 0
else
    echo -e "${RED}❌ 有 ${FAILED} 个测试失败，请检查上述错误。${NC}"
    exit 1
fi