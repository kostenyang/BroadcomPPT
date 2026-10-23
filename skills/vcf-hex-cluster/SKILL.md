---
name: vcf-hex-cluster
description: "Broadcom/VMware honeycomb layout: a centre hexagon (theme label) ringed by 3–6 coloured pointy-top hexagons with a white numbered/icon circle, spokes to the centre, and a title + 1–2 line label beside each hexagon (left of the left-hand hexes, right of the right-hand ones). Use for 六步驟 / 六大面向 / 六個元件 or any 3–6 parallel items on a VCF deck."
---

## When to use
- User sends the hexagon-cluster reference (六角形蜂巢圖) or asks for 六步驟 / 六大面向 / 六角圖 / "像蜂巢那張".
- A slide has 3–6 parallel items, each with a short title and 1–2 lines. Numbers inside the hexes if the items are ordered; a white icon if not.
- Companion to `vcf-pillar-cards` (columns) and `vcf-infographic-cards` (chevrons). Not for more than 6 items (split the slide) or for a strict left-to-right process (use chevrons).

## Visual spec
- Keep the template title placeholder, subtitle text box, source line and master footer; delete everything else in the body.
- **Hexagons** are pointy-top: `prstGeom hexagon` with `rot="5400000"`. Circumradius `R=54pt` → width √3·R ≈ 94, height 2R = 108. Spacing factor `S=1.1`.
- **Positions** (centre `CX=480, CY=280`): left column at `(-W/2·S, -1.5R·S)`, `(-W·S, 0)`, `(-W/2·S, +1.5R·S)`; right column mirrored. Numbering runs 1–3 down the left, 4–6 down the right (reads left-to-right, top-to-bottom).
- **Colours** (deck palette, one per hex, left→right): `61A60E`, `007B8C`, `0098C7`, `005C8A`, `6C4B94`, `1B1D36`. 1pt white outline on each.
- **Centre hexagon**: white fill, `BFBFBF` 1pt outline, radius `0.95R`; label 13pt bold `1B1D36` + 11pt `6B6B6B` second line, centred, in a 90×52 rect.
- **Halo**: one pale hexagon `F3F3F3`, radius `2.45R`, behind everything. **Spokes**: 1.5pt `9A9A9A` lines from centre to each hex centre, drawn above the halo and below the hexes.
- **Number circle**: 30pt white ellipse at hex centre, number 14pt bold in the hex colour; for unordered items, `insert_icon` 20pt white instead.
- **Labels**: rect `80pt` tall, vertically centred on the hex; left labels right-aligned, right labels left-aligned. Inner edge = hex vertex ± 32pt, outer edge at x=43 / 917. First paragraph `"N  Title"` 12pt bold in the hex colour; body 10pt `1B1D36`, max 2 lines, each line must fit without an orphan (shorten wording rather than widen).
- Fonts: Arial latin, Microsoft JhengHei ea. `bodyPr` insets 0, `anchor="ctr"`, `noAutofit`.
- Any notes the slide already had (critical path, loop note) go at `y=444`, left and right of the cluster, 30pt tall.

## Steps
1. `list_slide_shapes` + read all text in one `edit_slide_xml` read pass. Build an ordered list of {number, title, body[]}; copy wording verbatim. **Done when:** the item list and the keep-ids (title, subtitle, source, any note boxes) exist.
2. One `edit_slide_xml` pass: remove non-kept shapes (skip `nvGrpSpPr`/`grpSpPr`), reposition kept notes, then append in z-order: halo → spokes → centre hex + label → per item: hex, number circle, label rect. Build rotated hexes with `off = (cx-r, cy-r·√3/2)`, `ext = (2r, √3·r)`, `rot=5400000`. **Done when:** import succeeds and `list_slide_shapes` shows kept + 3 + 3·N shapes.
3. If items are unordered: `search_icons` one noun each, `insert_icon` 20pt `#FFFFFF` at circle centre −10. **Done when:** every hex has a number or icon.
4. `verify_slides` then `verify_slide_visual` ("honeycomb: N coloured hexagons around centre hex, labels left/right, no orphans"). Typical fixes: a body line wrapping with a 1–2 word orphan → shorten that line (e.g. drop a vendor prefix, abbreviate "Protection and Recovery" → "P&R"); labels too close to hexes → increase the 32pt gap, never shrink the font. **Done when:** verdict `done`.

## Example
CTBC 方案一 執行流程 (6 steps): 全新建置 / 驗證就緒 / vCenter RDU / Import WLD / VCFA · ESXi / 拆舊→收尾 → centre label "先建後拆 / 六個步驟", numbers 1–3 on the left, 4–6 on the right, existing 關鍵路徑 and ↻ 步驟 3–5 notes moved to y=444.
