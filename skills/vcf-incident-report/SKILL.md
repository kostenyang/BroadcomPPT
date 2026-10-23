---
name: "vcf-incident-report"
description: "產出 Broadcom CXS 格式的 VCF 事故報告簡報 (事件發生報告 / incident report / RCA / 事後檢討 .pptx)：封面、事故時間軌跡、影響範圍、根本原因、解決方案、Thank You。"
---

# VCF 事故報告簡報 (CXS Incident Report)

以 CXS「事件發生報告」範本 (中華外雲 2025-09-10 NSX Edge uplink 事件) 的版面與報告方式，產出新的事故報告 .pptx。
使用者說「事故報告」「事件報告」「事件發生報告」「incident report」「RCA 簡報」「事後檢討」「postmortem 簡報」「客戶事件說明」時使用。

## 1. 範本 (一律以範本為底，不從零建立)

依序尋找，找到即停：
1. 對話上傳檔中的 `incident-report-template.pptx`，或任何 `*issue_report*.pptx` (原始事件報告也可直接當範本，腳本會清掉舊內容)。
2. `curl -fsSLo template.pptx https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/templates/incident-report-template.pptx`
3. 都沒有 → 請使用者附上範本，停下來等。

範本必須含以下版型 (腳本以名稱查找)：`Title Slide – Leaf` (封面)、`空白` (時間軸)、`Diagram with Outcome, Benefit` (影響範圍/解決方案)、`Outcome / Benefit` (根本原因)、`Thank You / Closing - Plum` (結尾)。
右側兩個面板的 placeholder idx：17 = 上方標題、20 = 上方內容、19 = 下方標題、21 = 下方內容；0 = 標題、10 = 副標題。

## 2. 報告方式 (敘事結構固定)

對象是客戶主管 + 維運人員，繁體中文、白話，技術名詞用頁尾「註:」解釋 (例：`註: NSX Edge 為虛擬路由器`、`註: AVI LB 為虛擬負載平衡器`)。

| # | 頁 | 版型 | 內容規則 |
|---|---|---|---|
| 1 | 封面 | Title Slide – Leaf | 標題 = 客戶/環境名 (例「中華外雲」)；副標 = `YYYY MMDD 事件發生報告`；`CXS Team`；日期 `YYYY M` |
| 2 | 事故時間軌跡 | 空白 + 自繪時間軸 | 左→右箭頭時間軸；每個節點 = 日期 + 時間 + 2–4 條短 bullet (誰做了什麼、看到什麼)。第一個節點標紅色「事故發生」(告警來源 + 確認事故)，最後一個節點標綠色「服務恢復」。上方用大括弧標出排查階段 (例「排查 AVI LB 問題」→「排查 NSX Edge 問題」)，誠實呈現排查方向的轉換。必含：case 編號與等級、CXS/GSS/客戶各方動作、重開機/切換等處置與結果。每頁最多 6 個節點，超過自動分頁 |
| 3 | 影響範圍 | Diagram with Outcome, Benefit | 左：拓撲圖，故障元件標紅。右上「影響範圍」= 哪些元件/租戶受影響；右下「發生症狀」= 使用者看到的現象 |
| 4 | 根本原因 | Outcome / Benefit | 標題 `根本原因：<一句話>`；副標 = 機制一句話 (例「實體網卡的連線狀態正常，但已無法傳送封包」)。左：故障點示意圖或證據截圖 + 紅字 callout。右上「現象」、右下「原因」— 必須說明為何既有 HA/監控沒有觸發 |
| 5+ | 解決方案 (可多頁) | Diagram with Outcome, Benefit | 標題 `解決方案：<措施>`；副標 = 目的 (例「強化告警機制」)。左：改善後架構 (新增機制標綠)。右上「解決方案」、右下「需要注意事項」(效能影響、誤切換等副作用) |
| 選 | 後續行動 | Diagram with Outcome, Benefit | 需要時加：右上「短期措施」、右下「長期改善 / 待辦」 |
| 末 | Thank You | Thank You / Closing - Plum | 不改 |

### 事實紀律
- 時間、case 編號、指令輸出、元件名稱只能來自使用者提供的資料 (對話、log、截圖、email)；缺的標 `[待確認]`，不可補想像值。
- 根因若尚未經 GSS / KB / 官方文件確認，副標或原因欄註明「初步判斷」，並在對話中標示哪些是推論。
- 截圖中的密碼、token、內部帳號一律不放入簡報。

### 文字長度 (避免溢出)
- 時間軸 bullet：每條 ≤ 40 字，每節點 ≤ 4 條。
- 右側面板：每區 2–3 條，每條 ≤ 45 字。
- 標題 ≤ 22 字，副標 ≤ 30 字。

## 3. 流程

1. 收集事實：告警時間/來源、處理時序、case 編號、影響元件與租戶、症狀、根因證據、修復動作、改善方案與副作用。
2. 先在對話中給出結論先行的大綱 (每頁標題 + 重點)，一輪確認後再生成檔案。
3. 撰寫 `spec.json` (格式見下)，存在工作目錄。
4. 把下方腳本存成 `build_incident_report.py`，執行：
   `python3 build_incident_report.py template.pptx spec.json <客戶>_<YYYYMMDD>_incident_report.pptx`
   (需 `python-pptx`、`Pillow`；沒有就 `pip install python-pptx pillow --break-system-packages`)
5. QA：`soffice --headless --convert-to pdf` → `pdftoppm -r 60 -png` 逐頁看圖，檢查文字溢出、重疊、時間軸節點擠壓；有問題就縮短文字或調 `max_per_slide` 後重跑。
6. 交付 .pptx (SendUserFile)，一句話說明內容與 `[待確認]` 項目。

## 4. spec.json 格式

```json
{
  "cover": {"customer": "中華外雲", "title": "2025 0910 事件發生報告", "team": "CXS Team", "author": "", "date": "2025 9"},
  "timeline": {
    "title": "事故時間軌跡",
    "max_per_slide": 6,
    "events": [
      {"date": "9/10", "time": "5:45 PM", "label": "事故發生", "incident": true, "bullets": ["中華 eyesee 發出告警", "確認事故發生"]},
      {"date": "9/10", "time": "6:00 PM", "bullets": ["Broadcom CXS 接到通知", "開立最高等級 Case#36583560"]},
      {"date": "9/10", "time": "9:45 PM", "label": "服務恢復", "resolved": true, "bullets": ["切換實體連線後恢復正常"]}
    ],
    "phases": [{"from": 1, "to": 2, "label": "排查 AVI LB 問題"}],
    "notes": ["AVI LB 為虛擬負載平衡器", "NSX Edge 為虛擬路由器"]
  },
  "impact": {
    "title": "影響範圍", "subtitle": "",
    "upper": {"heading": "影響範圍", "items": ["..."]},
    "lower": {"heading": "發生症狀", "items": ["..."]},
    "diagram": [
      {"label": "實體網路", "boxes": [{"text": "Router 1"}, {"text": "Router 2"}]},
      {"label": "NSX", "boxes": [{"text": "Edge Cluster", "fault": true}, {"text": "AVI Service Engine"}]},
      {"label": "租戶", "boxes": [{"text": "租戶 1 VM"}, {"text": "租戶 2 VM"}]}
    ],
    "notes": ["NSX Edge 為虛擬路由器"]
  },
  "root_cause": {
    "title": "根本原因：網路連線問題", "subtitle": "實體網卡的連線狀態正常，但已無法傳送封包",
    "upper": {"heading": "現象", "items": ["..."]},
    "lower": {"heading": "原因", "items": ["..."]},
    "diagram": [
      {"label": "ESXi uplink", "boxes": [{"text": "uplink1 (Active)", "fault": true, "callout": "Uplink1 有連線但已無法傳送封包"}, {"text": "uplink2 (Standby)"}]}
    ]
  },
  "solutions": [
    {"title": "解決方案：開啟 Edge 及實體交換機的 BFD", "subtitle": "強化告警機制",
     "upper": {"heading": "解決方案", "items": ["..."]},
     "lower": {"heading": "需要注意事項", "items": ["..."]},
     "diagram": [{"label": "Edge", "boxes": [{"text": "Edge Node 1 + BFD", "fix": true}]}]}
  ],
  "extra": []
}
```

左側視覺 (每個 section 擇一)：
- `"diagram"`：由上而下的分層拓撲，每層一個灰底帶 + 方塊，上下層自動連線。`fault: true` 紅色 (故障點)、`fix: true` 綠色 (新增/改善)、其餘 teal。`callout` 在方塊左側加紅字 + 紅箭頭。
- `"image": "path.png"`：使用者提供的架構圖或證據截圖 (例 CLI 輸出看到 MAC 00:00:00:00:00:00)，等比置中於左側區域。可再加 `"callouts": [{"text": "...", "x": 0.0, "y": 0.4}]` (x/y 為左側區域的相對比例)。
- 使用者提供原始 Visio/簡報圖時優先用 `image`，比自動拓撲更貼近實況。

## 5. 產生器腳本 (build_incident_report.py)

把以下內容原樣寫入檔案再執行。保留範本的封面與結尾頁，中間內容頁全部以範本版型重建，舊事件內容不會殘留。

```python
#!/usr/bin/env python3
"""Build an incident report (事故報告) deck from the CXS issue-report template.

Usage: python3 build_incident_report.py <template.pptx> <spec.json> <out.pptx>

The template is the CXS issue report (Title Slide – Leaf / 空白 timeline /
Diagram with Outcome, Benefit / Outcome / Benefit / Thank You / Closing - Plum).
Only the cover and closing slides are kept; every content slide is rebuilt from
the template's own layouts so nothing from the previous incident leaks through.
"""
import json, sys
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

FONT = "Microsoft YaHei UI"
NAVY = RGBColor(0x00, 0x2E, 0x45)      # accent2 @ 50% — dates / bullets
LINE = RGBColor(0x00, 0x20, 0x60)      # timeline arrow
DOT = RGBColor(0x1B, 0x1D, 0x36)       # dk2 — timeline nodes
RED = RGBColor(0xFF, 0x00, 0x00)       # 事故發生 / fault point
TEAL = RGBColor(0x00, 0x7B, 0x8C)      # accent1
GREEN = RGBColor(0x61, 0xA6, 0x0E)     # accent4 — fix / recovered
GREY_BG = RGBColor(0xF2, 0xF2, 0xF2)
SLIDE_W = 12188825

LAYOUT_TIMELINE = "空白"
LAYOUT_PANEL = "Diagram with Outcome, Benefit"
LAYOUT_ROOTCAUSE = "Outcome / Benefit"


def layout(prs, name):
    for l in prs.slide_layouts:
        if l.name == name:
            return l
    raise SystemExit(f"layout not found in template: {name}")


def drop_slide(prs, slide):
    sldIdLst = prs.slides._sldIdLst
    for sldId in list(sldIdLst):
        if prs.slides.part.related_part(sldId.rId) is slide.part:
            prs.part.drop_rel(sldId.rId)
            sldIdLst.remove(sldId)
            return


def move_to_end(prs, slide):
    sldIdLst = prs.slides._sldIdLst
    for sldId in list(sldIdLst):
        if prs.slides.part.related_part(sldId.rId) is slide.part:
            sldIdLst.remove(sldId)
            sldIdLst.append(sldId)
            return


def style_run(run, size, bold=False, color=NAVY):
    f = run.font
    f.size = Pt(size)
    f.bold = bold
    f.color.rgb = color
    f.name = FONT
    rPr = run._r.get_or_add_rPr()
    ea = rPr.find(qn("a:ea"))
    if ea is None:
        ea = rPr.makeelement(qn("a:ea"), {})
        rPr.append(ea)
    ea.set("typeface", FONT)


def textbox(slide, x, y, w, h, lines, size=10, bold=False, color=NAVY,
            align=PP_ALIGN.LEFT, bullets=False):
    tb = slide.shapes.add_textbox(Emu(x), Emu(y), Emu(w), Emu(h))
    tf = tb.text_frame
    tf.word_wrap = True
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, 0)
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(6)
        if bullets:
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", "171450"); pPr.set("indent", "-171450")
            bu = pPr.makeelement(qn("a:buChar"), {"char": "•"})
            pPr.append(bu)
        r = p.add_run(); r.text = line
        style_run(r, size, bold, color)
    return tb


def set_ph(slide, idx, value):
    """value: str or list[str] (one paragraph per item)."""
    ph = slide.placeholders[idx]
    items = value if isinstance(value, list) else [value]
    tf = ph.text_frame
    tf.text = items[0] if items else ""
    for it in items[1:]:
        tf.add_paragraph().text = it


def notes_block(slide, notes, x=1950805, y_bottom=6380000):
    """Glossary footnotes, e.g. '註: NSX Edge 為虛擬路由器'."""
    for i, n in enumerate(reversed(notes)):
        textbox(slide, x, y_bottom - (i + 1) * 340000, 6000000, 330000,
                [n if n.startswith("註") else f"註: {n}"], size=14, color=RGBColor(0, 0, 0))


# ---------------------------------------------------------------- timeline
def timeline_slide(prs, title, events, phases, notes):
    s = prs.slides.add_slide(layout(prs, LAYOUT_TIMELINE))
    textbox(s, 211846, 343014, 6000000, 310000, [title], size=20, bold=True, color=DOT)
    n = len(events)
    left, right = 300000, SLIDE_W - 300000
    col_w = (right - left) // n
    line_y = 2560000
    # arrow
    ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Emu(left + col_w // 2), Emu(line_y),
                                Emu(right + 150000), Emu(line_y))
    ln.line.color.rgb = LINE; ln.line.width = Pt(2.25)
    ln.line._get_or_add_ln().append(ln.line._get_or_add_ln().makeelement(qn("a:tailEnd"), {"type": "triangle"}))
    centers = []
    for i, ev in enumerate(events):
        cx = left + col_w * i + col_w // 2
        centers.append(cx)
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Emu(cx - 107548), Emu(line_y - 120990),
                                 Emu(215097), Emu(241980))
        dot.fill.solid(); dot.fill.fore_color.rgb = RED if ev.get("incident") else DOT
        dot.line.color.rgb = NAVY
        textbox(s, cx - col_w // 2, 1960000, col_w, 450000,
                [ev.get("date", ""), ev.get("time", "")], size=12, bold=True, align=PP_ALIGN.CENTER)
        y = 2845000
        if ev.get("label"):
            textbox(s, cx - col_w // 2, y, col_w, 200000, [ev["label"]], size=12, bold=True,
                    color=RED if ev.get("incident") else GREEN if ev.get("resolved") else NAVY,
                    align=PP_ALIGN.CENTER)
            y += 300000
        textbox(s, cx - col_w // 2 + 40000, y, col_w - 80000, 2700000, ev.get("bullets", []),
                size=10, bold=True, bullets=True)
    # phase braces above the dates
    for ph in phases or []:
        a, b = centers[ph["from"]], centers[ph["to"]]
        span = max(b - a, 300000)
        brace = s.shapes.add_shape(MSO_SHAPE.LEFT_BRACE, Emu(a + span // 2 - 200000),
                                   Emu(1580000 - span // 2), Emu(400000), Emu(span))
        brace.rotation = 90
        brace.fill.background(); brace.line.color.rgb = RGBColor(0, 0, 0); brace.line.width = Pt(1)
        textbox(s, a, 1100000, span, 200000, [ph["label"]], size=10, bold=True,
                align=PP_ALIGN.CENTER, bullets=True)
    if notes:
        notes_block(s, notes)
    return s


# ---------------------------------------------------------------- diagram (left side)
DIAG = dict(x=450000, y=1400000, w=7400000, h=4500000)


def layered_diagram(slide, rows):
    """rows: [{"label": "實體網路", "boxes": [{"text": "Router 1", "fault": false, "fix": false, "callout": ""}]}]
    Draws top-to-bottom tiers; fault boxes red, fix boxes green, others teal."""
    n = len(rows)
    gap = 120000
    rh = (DIAG["h"] - gap * (n - 1)) // n
    prev = None
    for r_i, row in enumerate(rows):
        y = DIAG["y"] + r_i * (rh + gap)
        band = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Emu(DIAG["x"]), Emu(y), Emu(DIAG["w"]), Emu(rh))
        band.fill.solid(); band.fill.fore_color.rgb = GREY_BG; band.line.color.rgb = RGBColor(0xBF, 0xBF, 0xBF)
        band.adjustments[0] = 0.08
        textbox(slide, DIAG["x"] + 100000, y + 60000, 1500000, 250000, [row.get("label", "")],
                size=11, bold=True, color=RGBColor(0x40, 0x40, 0x40))
        boxes = row.get("boxes", [])
        m = max(len(boxes), 1)
        inner_x, inner_w = DIAG["x"] + 1650000, DIAG["w"] - 1800000
        bw = min(1800000, (inner_w - 150000 * (m - 1)) // m)
        total = bw * m + 150000 * (m - 1)
        start = inner_x + (inner_w - total) // 2
        bh = min(560000, rh - 200000)
        cur = []
        for b_i, b in enumerate(boxes):
            bx = start + b_i * (bw + 150000)
            by = y + (rh - bh) // 2
            shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Emu(bx), Emu(by), Emu(bw), Emu(bh))
            color = RED if b.get("fault") else GREEN if b.get("fix") else TEAL
            shp.fill.solid(); shp.fill.fore_color.rgb = color
            shp.line.color.rgb = color
            if b.get("fault"):
                shp.line.color.rgb = RGBColor(0x99, 0, 0); shp.line.width = Pt(2.5)
            tf = shp.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf.text = b.get("text", "")
            for p in tf.paragraphs:
                p.alignment = PP_ALIGN.CENTER
                for r in p.runs:
                    style_run(r, 11, True, RGBColor(0xFF, 0xFF, 0xFF))
            if b.get("callout"):  # red note + arrow pointing at this box (e.g. the fault point)
                textbox(slide, DIAG["x"] + 100000, by + 40000, inner_x - DIAG["x"] - 450000, bh,
                        [b["callout"]], size=10, bold=True, color=RED)
                arr = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Emu(bx - 330000), Emu(by + bh // 2 - 90000),
                                             Emu(300000), Emu(180000))
                arr.fill.solid(); arr.fill.fore_color.rgb = RED; arr.line.fill.background()
            cur.append((bx + bw // 2, by, by + bh))
        if prev and cur:
            for (px, _, pb) in prev:
                for (cx, ct, _) in cur:
                    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Emu(px), Emu(pb), Emu(cx), Emu(ct))
                    c.line.color.rgb = RGBColor(0x40, 0x40, 0x40); c.line.width = Pt(1)
        prev = cur or prev


def left_visual(slide, sec):
    if sec.get("image"):
        from PIL import Image
        iw, ih = Image.open(sec["image"]).size
        scale = min(DIAG["w"] / iw, DIAG["h"] / ih)
        w, h = int(iw * scale), int(ih * scale)
        slide.shapes.add_picture(sec["image"], Emu(DIAG["x"] + (DIAG["w"] - w) // 2),
                                 Emu(DIAG["y"] + (DIAG["h"] - h) // 2), Emu(w), Emu(h))
    elif sec.get("diagram"):
        layered_diagram(slide, sec["diagram"])
    for c in sec.get("callouts", []):  # free-positioned red callout text over an image
        textbox(slide, DIAG["x"] + int(c.get("x", 0) * DIAG["w"]), DIAG["y"] + int(c.get("y", 0) * DIAG["h"]),
                1800000, 500000, [c["text"]], size=11, bold=True, color=RED)


def panel_slide(prs, sec, layout_name=LAYOUT_PANEL):
    """Title + subtitle, diagram left, two titled panels right (idx 17/20 upper, 19/21 lower)."""
    s = prs.slides.add_slide(layout(prs, layout_name))
    set_ph(s, 0, sec["title"])
    set_ph(s, 10, sec.get("subtitle", ""))
    set_ph(s, 17, sec["upper"]["heading"]); set_ph(s, 20, sec["upper"]["items"])
    set_ph(s, 19, sec["lower"]["heading"]); set_ph(s, 21, sec["lower"]["items"])
    left_visual(s, sec)
    if sec.get("notes"):
        notes_block(s, sec["notes"], x=DIAG["x"] + 1300000)
    return s


def main(tpl, spec_path, out):
    spec = json.load(open(spec_path, encoding="utf-8"))
    prs = Presentation(tpl)
    slides = list(prs.slides)
    cover, closing = slides[0], slides[-1]
    old_middle = slides[1:-1]  # dropped AFTER new slides are added (avoids partname clashes)

    c = spec["cover"]
    set_ph(cover, 0, c["customer"])
    set_ph(cover, 10, c["title"])
    set_ph(cover, 11, c.get("team", "CXS Team"))
    set_ph(cover, 12, c.get("author", ""))
    set_ph(cover, 14, c["date"])

    tl = spec["timeline"]
    per = tl.get("max_per_slide", 6)
    ev = tl["events"]
    chunks = [ev[i:i + per] for i in range(0, len(ev), per)]
    for k, ch in enumerate(chunks):
        off = k * per
        phases = [dict(p, **{"from": max(p["from"], off) - off, "to": min(p["to"], off + len(ch) - 1) - off})
                  for p in tl.get("phases", []) if p["to"] >= off and p["from"] < off + len(ch)]
        title = tl.get("title", "事故時間軌跡") + (f" ({k + 1}/{len(chunks)})" if len(chunks) > 1 else "")
        timeline_slide(prs, title, ch, phases, tl.get("notes") if k == len(chunks) - 1 else None)

    panel_slide(prs, spec["impact"])
    panel_slide(prs, spec["root_cause"], LAYOUT_ROOTCAUSE)
    for sol in spec["solutions"]:
        panel_slide(prs, sol)
    for extra in spec.get("extra", []):
        panel_slide(prs, extra)

    for sl in old_middle:
        drop_slide(prs, sl)
    move_to_end(prs, closing)
    prs.save(out)
    print("saved", out, "slides:", len(prs.slides))


if __name__ == "__main__":
    main(*sys.argv[1:4])
```