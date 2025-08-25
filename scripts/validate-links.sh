#!/usr/bin/env bash
set -euo pipefail

# Validate that no local/temporary file paths are referenced in site content.
# Fails if any forbidden patterns are found.

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

TARGETS=(
  "_posts"
  "pages"
  "_episodes"
)

# Forbidden patterns (extended regex)
PATTERN='(/Users/|com\.tencent\.xinWeChat|xwechat_files|RWTemp|file://|\\\\|[A-Za-z]:\\\\|/var/folders/|/private/var/|AppData/Local/Temp)'

found=0
for dir in "${TARGETS[@]}"; do
  [ -d "$ROOT_DIR/$dir" ] || continue
  if grep -REn --binary-files=without-match "$PATTERN" "$ROOT_DIR/$dir" >/tmp/validate-links.out 2>/dev/null; then
    echo "❌ 检测到禁止的本地路径/临时文件引用（请修复后再发布）："
    cat /tmp/validate-links.out
    found=1
  fi
done

if [ "$found" -ne 0 ]; then
  exit 2
fi

echo "✅ 链接校验通过：未发现本地路径或临时文件引用"

