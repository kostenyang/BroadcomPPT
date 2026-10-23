---
name: vcf-infographic-cards
description: "Two Broadcom/VMware-palette infographic layouts for 3–5 parallel items on a slide: staggered numbered circles (01–05, high/low along a dashed path) and arch-top cards (coloured semicircle header, grey body, tagged rows). Use for gates, phases, components, roles, or any left-to-right sequence on a VCF deck."
---

# VCF Infographic Cards

Two hand-built layouts for a row of 3–5 parallel items on a 960×540pt VMware 2025 Light slide. Both are drawn with `edit_slide_xml` (exact geometry), never Office.js, and both keep the slide's existing title / subtitle / footnote shapes and redraw everything else.

## When to use
- The user sends a reference image of numbered circles or arch-top ("tombstone") cards, or asks for 圓形 / 卡片 / infographic style.
- A slide lists 3–5 parallel things: Go/No-Go gates, upgrade phases, license-path components, team roles, options.
- Not for charts (use create_slide_chart) and not for more than 5 items (split the slide).

## Shared rules
- Colours per item, one each, from the deck palette: `005C8A` ocean, `007B8C` teal, `0098C7` sky, `6C4B94` plum, `61A60E` green; extras `F3BA16` gold, `E68C28` orange. If the slide already assigned colours (e.g. G0–G4), keep them.
- Text: 微軟正黑體 via `<a:latin/><a:ea/><a:cs typeface="微軟正黑體"/>`; title in item 14pt bold, body 11–12pt, grey `5A5F6B` for secondary lines, dark `1B1D36` for primary.
- Keep shapes: the title placeholder (id 2), any closing sentence and the source footnote. Remove all other shapes from `p:spTree` (skip `nvGrpSpPr`/`grpSpPr`), then insert new shapes before the footnote node so z-order stays below it.
- All text copied verbatim from the old slide; only the form changes.
- After drawing, run `verify_slide_visual`; typical fixes are orphaned single characters (shorten the line) and a bottom one-liner wrapping (shorten).
- Done when: verify_slide_visual returns `done` and every item shows name, body lines and colour.

## Layout A — Staggered numbered circles (reference: 01–05 circles)
Five circles alternating low/high along a dashed horizontal line; number tab on top; colour ring; white interior with title + 3 lines; coloured bottom segment holding an icon or a short bold action.

Geometry (5 items): `D=172, STEP=174, X0=44, yHi=104, yLo=196` (`y = i%2===0 ? yLo : yHi`). For 4 items use `STEP=215, X0=60`; for 3, `STEP=290, X0=100`.
Per item, in this order:
1. Dashed path once: `line` from `X0+D/2` to `X0+D/2+STEP*4`, y = `(yHi+yLo)/2+D/2`, colour `B5B9C0`, `prstDash sysDash`.
2. Ring: `ellipse` x,y,D,D filled with item colour.
3. Interior: `ellipse` x+7,y+7,D-14,D-14 white.
4. Bottom segment: `chord` same box as interior, item colour, `<a:gd name="adj1" fmla="val 2100000"/><a:gd name="adj2" fmla="val 8700000"/>` (these values put the segment at the bottom; 1200000/9600000 puts it on top — wrong).
5. Number tab: white `roundRect` (adj 50000) x+D/2-32, y-18, 64×34, text `01` / `G0` 22pt bold in item colour.
6. Title: rect x+20, y+24, D-40×22, 14pt bold centred.
7. Lines: rect x+18, y+50, D-36×72, anchor top, 3 × 12pt, spcAft 200.
8. In the segment: either a white 40pt `ellipse` at x+D/2-20, y+D-66 with a 26pt `insert_icon` in item colour centred in it, or two text lines (`不通過` 10pt + action 12pt bold, white) in a rect x+30, y+131, D-60×32.
Anything below (one-line note, closing sentence) goes at y ≥ 400.

## Layout B — Arch-top cards (reference: Mary Stark profile cards)
Five equal cards: coloured semicircle header with a white circle (icon or big label), grey body with name + role, dotted divider, 3 rows each with a small colour pill, optional coloured/pink strip at the foot.

Geometry (5 items): `CW=158, GAP=20, X0=45, Y=86..110, H=284..300`, `x = X0 + i*(CW+GAP)`. For 4 items `CW=200, GAP=22`; for 3 `CW=270, GAP=30` (scale the white circle to ~0.65·CW).
Per item:
1. Arch: `ellipse` x,Y,CW,CW item colour, then `rect` x,Y+CW/2,CW,52 item colour.
2. Body: `rect` x,Y+131,CW,H-131 fill `EEEEEE` (covers the ellipse's lower half).
3. White circle: `ellipse` x+27,Y+21,104,104. Put either an `insert_icon` (48pt, item colour, at x+55,Y+49) or a big label (G0, 32pt bold, item colour) in a no-fill ellipse of the same box.
4. Name: rect x+6,Y+140,CW-12×24, 14pt bold. Role: rect x+6,Y+164,CW-12×18, 11pt grey.
5. Divider: `line` x+10,Y+190,CW-20, colour `9AA0AA`, w 15875, `prstDash sysDot` (thinner/lighter is invisible).
6. Rows: for j in 0..2, `ry=Y+200+j*24`; pill `roundRect` x+12,ry+6,18×8 item colour; text rect x+36,ry,CW-42×20, 11pt left.
7. Optional foot strip: `rect` x,Y+H-26,CW,26 fill `FBE9EC`, text 11pt bold `A6192E` (for 不通過 actions), or item colour with white text.
8. Chevron between cards: `chevron` x+CW+5,Y+66,10×14 fill `B5B9C0`.
Move any closing sentence to `Y+H+14`.

## Code skeleton (edit_slide_xml)
```js
const xml=await zip.file("ppt/slides/slide1.xml").async("string");
const doc=new DOMParser().parseFromString(xml,"text/xml");
const NS_P="http://schemas.openxmlformats.org/presentationml/2006/main",NS_A="http://schemas.openxmlformats.org/drawingml/2006/main";
const spTree=doc.getElementsByTagNameNS(NS_P,"spTree")[0];
const keep=["2","28","29"]; // title, closing line, footnote — read ids from list_slide_shapes first
for(const s of Array.from(spTree.childNodes)){if(s.nodeType!==1||s.localName==="nvGrpSpPr"||s.localName==="grpSpPr")continue;const c=s.getElementsByTagNameNS(NS_P,"cNvPr")[0];if(!c||!keep.includes(c.getAttribute("id")))spTree.removeChild(s);}
const E=v=>Math.round(v*12700);
const FONT='<a:latin typeface="微軟正黑體"/><a:ea typeface="微軟正黑體"/><a:cs typeface="微軟正黑體"/>';
const P=(t,o={})=>`<a:p><a:pPr algn="${o.al||'ctr'}"><a:spcBef><a:spcPts val="0"/></a:spcBef><a:spcAft><a:spcPts val="${o.aft||0}"/></a:spcAft><a:buNone/></a:pPr><a:r><a:rPr lang="zh-TW" sz="${o.sz||1200}" b="${o.b?1:0}" dirty="0"><a:solidFill><a:srgbClr val="${o.c||'1B1D36'}"/></a:solidFill>${FONT}</a:rPr><a:t>${escapeXml(t)}</a:t></a:r></a:p>`;
let nid=700; const anchor=/* footnote shape node */;
function sp(x,y,w,h,prst,fill,ln,paras,o={}){ /* build <p:sp> with xfrm, prstGeom (+avLst for chord/roundRect), fill, ln, bodyPr lIns/tIns/rIns/bIns=0 anchor ctr, noAutofit; parse and insertBefore(anchor) */ }
// ...draw per layout above...
zip.file("ppt/slides/slide1.xml",new XMLSerializer().serializeToString(doc)); markDirty();
```
Icons: after the XML pass, `search_icons` one noun each (cloud, shield, key, television, database…) and `insert_icon` with `color` = item hex at the centres given above. Insert icons last; the XML pass deletes non-kept shapes.

## Examples
- Go/No-Go gates G0–G4 → Layout B with G-labels in the circles, rows = pass conditions, pink foot strip = 不通過 action. Or Layout A with the action in the bottom segment.
- License path Broadcom 雲端 → Proxy → VCF Operations → vCenter → ESX → Layout B with icons, rows = 3 facts each, offline-mode one-liner under the cards.
