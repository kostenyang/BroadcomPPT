#!/usr/bin/env python3
"""set-hant-font.py — 把 pptx 所有 theme 的繁中字型 (script="Hant") 改成微軟正黑體。

為什麼：部分官方 deck（例如 VCF_9.1_Whats_New_Sales_09.30.26.pptx）theme 的 Hant 字型是
新細明體，換成中文後在 PowerPoint 會以新細明體顯示。vcf-base 規定繁中一律微軟正黑體。
官方範本本身不動，產出 deck 後跑一次即可。

用法
----
  set-hant-font.py in.pptx out.pptx                     # 預設 微軟正黑體
  set-hant-font.py in.pptx out.pptx --font "Microsoft JhengHei"

in 與 out 可以是同一個檔。只改 ppt/theme/theme*.xml 的 <a:font script="Hant" …/>，
其他 part（含內嵌字型 ppt/fonts/*.fntdata）原封不動。
"""

import argparse
import re
import shutil
import zipfile


def main():
    ap = argparse.ArgumentParser(description="pptx theme 繁中字型改成微軟正黑體")
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--font", default="微軟正黑體")
    a = ap.parse_args()

    pat = re.compile(rb'<a:font script="Hant" typeface="[^"]*"/>')
    rep = ('<a:font script="Hant" typeface="%s"/>' % a.font).encode("utf-8")
    tmp = a.dst + ".tmp"
    n = 0
    with zipfile.ZipFile(a.src) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            b = zi.read(it.filename)
            if re.match(r"ppt/theme/theme\d+\.xml$", it.filename):
                b, k = pat.subn(rep, b)
                n += k
            zo.writestr(it, b)
    shutil.move(tmp, a.dst)
    print("已把 %d 處 theme Hant 字型改成 %s → %s" % (n, a.font, a.dst))


if __name__ == "__main__":
    main()
