# Color and style rules (Plum scheme + bilingual)

The bundled template carries Broadcom's official Plum colour scheme. Stick to it — do not mix Leaf or Aqua variants into the same deck.

## Plum colour palette

| Role | Hex | Used for |
|---|---|---|
| Plum (Primary) | `#6C4B8F` | Section header backgrounds, Big Statement Plum slides, closing slide, accent shapes |
| Plum Dark | `#5A3F77` | Plum shape outlines, hover/active states |
| Plum Tint | `#E8DDEE` | Light fill for callout boxes on white slides |
| Dark Navy | `#1B1E35` | Body text on white slides |
| White | `#FFFFFF` | Content slide backgrounds, text on Plum |
| Off-white | `#F2F2F2` | Diagram backgrounds, very subtle dividers |
| Gold (accent only) | `#EDB516` | Warnings, callouts, "what's new" badges |
| Teal/Green/Sky | _do not use as primary_ | Reserved for the Leaf/Aqua decks — avoid here |

## Layout picks (Plum-only)

When inserting new structural slides, pick Plum-named layouts:

- Section divider: `1_Section Header – Plum` (preferred, matches the 9-chapter rhythm of the template) or `Section Header – Plum`
- Big takeaway: `Big Statement - Plum` or `Big Statement 2 - Plum`
- Cover slide: `Title Slide – Plum` (NOT Leaf or Aqua)
- Closing: `Thank You / Closing - Plum`

Content slides have no colour variant — use layouts like:
- `1_Title and Subtitle`, `Title and Subtitle`
- `1_Diagram with Content on Right`, `Diagram with Content on Right`
- `Two-Content Balanced`, `1_Two-Content Balanced Color on Left/Right`
- `Three/Four/Five Icon`, `Five Numbered`, `Customer Success`, `Big Statistic`, `Chart`

## Fonts

The template ships with the Broadcom font stack:

- Headings: NTR (falls back to Arial)
- Body: Arial
- Code/mono: Consolas

Do NOT swap to other fonts. If you must add text via python-pptx, set the run font to `Arial` for safety — Office will substitute NTR on hosts that have it installed.

## Background rule

- Content slides: **white** background. Never beige (`#FAF0E6`), cream (`#FFF8E1`), or any warm colour.
- Section headers, title slide, big-statement, closing: Plum (`#6C4B8F`) background with white text.
- Diagram callouts: white or very light grey (`#F2F2F2`). Never tinted with Leaf green or Aqua blue.

## Bilingual labeling rules

### Cover slide (1)

- Title (large): English product/topic, e.g. `VMware Cloud Foundation 9.1 — Deployment Planning`
- Subtitle: Traditional Chinese, e.g. `VCF 9.1 部署規劃 — 資源 / IP / FQDN`
- Presenter / date line: bilingual ok — `Kosten Yang  ·  2026-06-18  ·  玉山銀行`

### Content slide titles

Pattern: `English headline` (top, sentence case) + `中文副標` (below).

Examples:
```
✔  Title:    VCF Operations 9.1 — Fleet Management
    Subtitle: Fleet 級集中管理 — 跨多 Instance 統一治理

✔  Title:    NSX networking in VMware Cloud Foundation
    Subtitle: NSX 虛擬網路 — VCF 內建 SDN

✘  Title:    VCF Operations 9.1 - 艦隊管理     ← never put Chinese in the English title
✘  Title:    VCF OPERATIONS 9.1                  ← never ALL CAPS
✘  Title:    VCF Operations 9.1 — Fleet Management.  ← no trailing period
```

### Body content

- Primary language: English (mirrors the original Broadcom template wording).
- Add Chinese annotation in parentheses for jargon that Taiwan customers may not recognize:
  - `Fleet Management (集中艦隊管理)`
  - `vSAN ESA (新世代儲存架構)`
  - `VCF Identity Broker (統一身份驗證入口)`
- For numbered lists / bullet groups: keep the English bullet on top; you may add a one-line Chinese summary at the end.

### Section header text

Do NOT translate the English section header text. The bundled deck uses:

- "Build and Deploy Private Cloud Infrastructure On-Premises"
- "Optimize Infrastructure and Operations"
- "Modernize Infrastructure"
- "Extend Data Center to the Edge"
- "Enable Self-Service Infrastructure"
- "Build, Run and Manage Kubernetes"
- "Build, Run and Manage Private AI Apps"
- "Strengthen Compliance and Harden Infrastructure"
- "Accelerate Recovery from Ransomware and Other Disasters"

Keep them as-is. A small Chinese tagline UNDER the English header is acceptable (use the layout's existing subtitle placeholder).

### Speaker notes

- Always Traditional Chinese.
- Format: 1–3 sentences per slide describing what to say aloud.
- Include any numerical proof-points (TCO %, latency ms, IP counts) explicitly.

## Customer-name placement

When customizing for a specific customer:

- Title slide subtitle: add `for {Customer 中文名}` (e.g. `for 玉山銀行`)
- Page footer (bottom-left or bottom-right): you may add `{Customer}  ·  Broadcom Proprietary and Confidential` — keep the Broadcom confidentiality string intact.
- Customer logos: ONLY if the customer has granted Broadcom permission. Otherwise omit.

## Date and version

- Footer date format: `Month YYYY` (e.g. `June 2026`) or `YYYY-MM` for internal versioning.
- Version stamp: `V1.0` on cover, increment minor for content edits, major for restructure.
