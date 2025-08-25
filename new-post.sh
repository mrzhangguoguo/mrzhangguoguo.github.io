#!/bin/bash
# 快速创建新文章

if [ -z "$1" ]; then
    echo "使用方法: ./new-post.sh \"文章标题\""
    exit 1
fi

TITLE="$1"
DATE=$(date +%Y-%m-%d)
TIME=$(date +"%Y-%m-%d %H:%M:%S %z")
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g')
FILENAME="_posts/${DATE}-${SLUG}.md"

cat > "$FILENAME" << EOF
---
layout: post
title: "$TITLE"
date: $TIME
tags: []
excerpt: ""
---

## 介绍

在这里写你的文章内容...

## 主要内容

### 小标题1

内容...

### 小标题2

内容...

## 总结

总结内容...
EOF

echo "✅ 创建成功: $FILENAME"
echo ""
echo "下一步："
echo "1. 编辑文章: code $FILENAME"
echo "2. 本地预览: python3 test_server.py"
echo "3. 提交发布: git add . && git commit -m \"发布文章：$TITLE\" && git push"