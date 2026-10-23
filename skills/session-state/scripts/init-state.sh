#!/usr/bin/env bash
# init-state.sh — 在目標專案建立 dev-docs/ 狀態檔（不覆蓋既有檔案）
# usage: bash init-state.sh [project-dir]
set -euo pipefail

PROJECT_DIR="${1:-.}"
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$PROJECT_DIR/dev-docs"

mkdir -p "$DEST"

for f in plan.md context.md tasks.md; do
  if [[ -e "$DEST/$f" ]]; then
    echo "skip (exists): dev-docs/$f"
  else
    cp "$SKILL_DIR/assets/$f" "$DEST/$f"
    echo "created:       dev-docs/$f"
  fi
done

echo
echo "下一步："
echo "  1. 填寫 dev-docs/plan.md 的目標 / in-scope / out-of-scope / done-when / 驗證指令"
echo "  2. 把 $SKILL_DIR/assets/claude-md-snippet.md 貼進 project-root 的 CLAUDE.md"
echo "     （這是壓縮後能自動想起狀態檔的關鍵，沒有它整套機制不會啟動）"
