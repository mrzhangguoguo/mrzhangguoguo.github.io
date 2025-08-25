#!/bin/bash
# 从Obsidian发布文章到Jekyll

echo "📝 从Obsidian发布文章到Jekyll"
echo "=============================="

# 检查Drafts目录
DRAFTS_DIR="Drafts"
if [ ! -d "$DRAFTS_DIR" ]; then
    echo "❌ 未找到Drafts目录"
    exit 1
fi

# 列出草稿文件
echo "📄 可发布的草稿："
ls -1 "$DRAFTS_DIR"/*.md 2>/dev/null | nl

if [ $? -ne 0 ]; then
    echo "❌ Drafts目录中没有markdown文件"
    exit 1
fi

# 选择要发布的文章
read -p "请输入要发布的文章编号: " choice
DRAFT_FILE=$(ls -1 "$DRAFTS_DIR"/*.md | sed -n "${choice}p")

if [ ! -f "$DRAFT_FILE" ]; then
    echo "❌ 无效的选择"
    exit 1
fi

# 提取文章标题
TITLE=$(grep "^title:" "$DRAFT_FILE" | sed 's/title: *"\?\([^"]*\)"\?/\1/')
DATE=$(date +%Y-%m-%d)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g')
POST_FILE="_posts/${DATE}-${SLUG}.md"

# 复制到_posts目录
cp "$DRAFT_FILE" "$POST_FILE"

echo "✅ 文章已发布: $POST_FILE"
echo ""

# 链接校验：拦截本地路径/临时文件引用
if [ -x ./scripts/validate-links.sh ]; then
    echo "🔎 正在执行链接校验（禁止本地/临时路径）..."
    if ! ./scripts/validate-links.sh; then
        echo "❌ 链接校验失败：发现本地路径/临时文件引用。已取消本次发布。"
        rm -f "$POST_FILE"
        exit 2
    fi
fi

# 询问是否立即部署
read -p "是否立即部署到GitHub Pages? (y/N): " deploy
if [ "$deploy" = "y" ] || [ "$deploy" = "Y" ]; then
    # 部署前再次执行校验，双保险
    if [ -x ./scripts/validate-links.sh ]; then
        ./scripts/validate-links.sh || { echo "❌ 链接校验失败，已中止部署"; exit 2; }
    fi
    ./deploy.sh "发布文章：$TITLE"
    echo "🚀 已部署到线上"
else
    echo "💡 可以稍后运行以下命令部署："
    echo "   ./deploy.sh \"发布文章：$TITLE\""
fi

# 询问是否移动原草稿
read -p "是否将草稿移动到Archive目录? (y/N): " archive
if [ "$archive" = "y" ] || [ "$archive" = "Y" ]; then
    mkdir -p Archive
    mv "$DRAFT_FILE" "Archive/"
    echo "📁 草稿已归档"
fi
