---
name: vcf-pillar-cards
description: "Broadcom/VMware \"three pillar\" layout (reference: Business Initiatives and Use Cases): 2–4 columns, each a rounded gradient header card (plum / teal-blue / teal-green) with white title and hero illustration, followed by 3 tinted rows with a gradient circle icon and one short line. Use for initiatives, pillars, use cases, workstreams or any parallel columns of 2–4 bullets each on a VCF deck."
---

# VCF Pillar Cards (gradient header + icon rows)

Companion to `vcf-infographic-cards` (Layouts A/B). This is **Layout C**: the Broadcom "Business Initiatives and Use Cases" look — a row of 2–4 pillar columns on a 960×540pt VMware 2025 Light slide. Read `vcf-base` / `broadcom-ppt-base` first for the palette and clone-slide rules. Drawn with `edit_slide_xml` (exact geometry), never Office.js.

## When to use
- The user sends the pillar-card reference image, or asks for 三大支柱 / 三欄卡片 / use-case 欄位 / "像 Business Initiatives 那頁".
- A slide has 2–4 parallel themes, each with 2–4 short points (initiatives, modernization tracks, workstreams, risk categories, 三工法比較).
- Not for sequences with order (use Layout A/B chevrons) and not for more than 4 columns or more than 4 rows (split the slide).

## Visual spec (from the reference)
- Slide title: keep the template title placeholder (template blue, Arial), no subtitle.
- **Header card**: rounded rect (`roundRect`, adj ≈ 6000), height 159pt, **linear gradient at 45° (`a:lin ang="2700000"`)**. One gradient per column, from the deck palette:
  - Column 1 plum: `6C4B94` → `3B4A8C`
  - Column 2 teal-blue: `0098C7` → `005C8A`
  - Column 3 teal-green: `007B8C` → `61A60E`
  - Column 4 (if needed) ocean: `005C8A` → `1B1D36`
- Inside the header: hero illustration in the upper ~60% (cloud + themed icon), **white bold 20–22pt title, 1–2 lines, centred, bottom 40% of the card** (微軟正黑體 for Chinese, Arial for English).
- **Rows** (3 per column, 69pt each, no gap): each row is a rect with a vertical gradient from a light tint of the column colour at the top to white at the bottom (`a:lin ang="5400000"`): plum tint `EFEAF5`, blue tint `E9F3FA`, green tint `EDF5EA`, ocean tint `E6EEF4`. A 0.75pt divider line in the column's light tone (`B9A9D1` / `9CCBE3` / `B8D89A`) between rows, none under the last.
- **Row icon**: 37pt circle filled with the column gradient (same two stops, 45°), left inset 16pt, vertically centred; white 20pt `insert_icon` centred in it.
- **Row text**: 12pt dark `1B1D36`, left-aligned, anchor centre, rect starts 63pt from the column's left edge, width `CW-70`, up to 3 lines. Bold the 1–3 words that carry the point only if the deck already does that.
- Footer (logo, confidentiality line, page number) comes from the master; do not redraw.

## Geometry (pt)
- 3 columns: `CW=250, GAP=61, X0=47`, `x = X0 + i*(CW+GAP)`. 2 columns: `CW=380, GAP=100, X0=50`. 4 columns: `CW=204, GAP=20, X0=44`.
- `Y_HDR=58, H_HDR=159` → rows start at `Y_ROW=221`, `H_ROW=69`, rows end at 428. Leave ≥ 40pt above the footer band (footer starts ~480).
- With 4 rows use `H_ROW=56` and 11pt text; with 2 rows use `H_ROW=90`.
- Header title rect: `x+16, Y_HDR+100, CW-32 × 50`. Illustration box: `x+CW/2-55, Y_HDR+14, 110 × 80`.

## Steps
1. `list_slide_shapes` → note ids of the title placeholder and footnote/source to keep. Read every body text with `read_slide_text`; copy wording verbatim (only the form changes). **Done when:** a keep-list of ids and a column→rows text map exist.
2. One `edit_slide_xml` pass: remove all non-kept shapes from `p:spTree` (skip `nvGrpSpPr`/`grpSpPr`), then insert, per column: header roundRect (gradFill), title text rect, 3 row rects (gradFill), 2 divider lines, 3 icon circles (gradFill), 3 text rects. Insert before the footnote node so z-order stays below it. `bodyPr` insets 0, `anchor="ctr"`, `<a:normAutofit/>` off (`noAutofit`). **Done when:** slide re-imports without error and `list_slide_shapes` shows 3×(1+1+3+2+3)+kept shapes.
3. Icons last (the XML pass deletes everything else): `search_icons` one literal noun each (cloud, server, gauge, kubernetes→"container", brain, shield, lock, lifebuoy→"life preserver") and `insert_icon` with `color:"#FFFFFF"`, 20×20 at circle centre −10. Hero illustrations: `insert_icon` 56pt white (cloud / monitor / shield) at the illustration box; a second small icon (24pt, `F3BA16` gold) offset top-left gives the reference's "floating squares" feel — optional. **Done when:** every row and header has an icon.
4. `verify_slides` then `verify_slide_visual` with expected_changes "3 gradient pillar headers + 9 tinted icon rows". Typical fixes: row text wrapping to 4 lines (shorten or drop to 11pt), header title wrapping to 3 lines (shorten). **Done when:** verdict `done`.

## Gradient snippet (OOXML)
```xml
<a:gradFill rotWithShape="1"><a:gsLst>
  <a:gs pos="0"><a:srgbClr val="6C4B94"/></a:gs>
  <a:gs pos="100000"><a:srgbClr val="3B4A8C"/></a:gs>
</a:gsLst><a:lin ang="2700000" scaled="0"/></a:gradFill>
```
Row tint: `pos 0 = EFEAF5`, `pos 100000 = FFFFFF`, `ang="5400000"`.

## Examples
- 玉山/兆豐 三大現代化：Infrastructure / Application / Security Modernization, 3 use cases each → 3 columns, hero icons cloud+server / monitor / shield.
- 元大 三工法比較 (In-place upgrade / Converge / Rebuild) → 3 columns, rows = 時程、風險、回退.
- 授權風險四類 → 4 columns with `CW=204`, rows = 3 facts, 11pt.
