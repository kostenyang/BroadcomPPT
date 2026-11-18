#!/usr/bin/env bash
# 移除 pptx 內所有 "Broadcom Proprietary and Confidential" 字樣（含 slides / layouts / masters / notes）。
# 保留 "Copyright © ... Broadcom. All Rights Reserved."。就地改檔，先自行備份。
set -euo pipefail
[ $# -eq 1 ] || { echo "usage: $0 <deck.pptx>"; exit 1; }
DECK=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
unzip -q "$DECK" -d "$TMP"
BEFORE=$( { grep -roh "Broadcom[ ,&]*Proprietary[ ,&a-z]*Confidential" "$TMP/ppt" 2>/dev/null || true; } | wc -l | tr -d ' ')
find "$TMP/ppt" -name '*.xml' -print0 | xargs -0 perl -CSD -pi -e \
  's/Broadcom[ ,&]{0,3}(?:and )?Proprietary[ ,&]{0,3}(?:and )?Confidential//gi'
AFTER=$( { grep -roh "Proprietary[ ,&a-z]*Confidential" "$TMP/ppt" 2>/dev/null || true; } | wc -l | tr -d ' ')
(cd "$TMP" && zip -q -r -X "$DECK.new" .)
mv "$DECK.new" "$DECK"
echo "cleaned: $BEFORE -> $AFTER  ($DECK)"
