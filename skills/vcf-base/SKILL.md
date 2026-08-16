---
name: vcf-base
description: Core Broadcom/VMware by Broadcom PowerPoint template knowledge. Use this as a shared reference for all VCF presentation skills. Contains template specs, slide layouts, color system, font rules, and upgrade path conventions for VCF 5.2 and VCF 9.1 templates.
---

# Broadcom PPT Base Template Knowledge

This is the shared reference for all Broadcom VCF vertical presentation skills.
Always read this alongside the vertical skill (semiconductor / financial / telecom / hybrid-cloud / ai).

---

## Template Files

Two official templates exist. **Always use one of these as the base — never create from scratch.**

> **⚡ 預設永遠先用最小的白底範本**。只有在使用者明確要求時才改用其他範本。

| 優先順序 | Template | File | Size | When to use |
|---------|----------|------|------|-------------|
| ✅ **預設 (Default)** | VCF 9.1 Getting Started | `Getting_Started_with_VCF_9_1__Upgrade_Paths__and_What_to_Expect.pptx` | 2.4MB | **所有情境的預設底版** — 白底、輕量 |
| 🔁 備用 | APJ Upgrade Pathways to VCF 9.1 | `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` | 3.8MB | 升級路徑詳細場景 |
| 🔁 備用 | Tech Tuesday — vSphere in VCF 9.1 | `TECH_TUESDAY_Whats_New_with_vSphere_in_VCF_9_1.pptx` | 8.5MB | 功能概覽 (icon-led) → 走 `vcf-whats-new` |
| 🔁 備用 | Tech Tuesday — vSAN in VCF 9.1 | `TECH_TUESDAY_Whats_New_with_vSAN_in_VCF_9_1.pptx` | 12.2MB | 功能概覽 (diagram-led, Plum) → 走 `vcf-whats-new` |
| 🔁 備用 (On request only) | VCF 5.2 Master Technical | `VCF_5_2_Master_Technical_-_BC04.pptx` | 97MB | 僅當使用者明確指定時 |

Download from GitHub (預設):
`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/Getting_Started_with_VCF_9_1__Upgrade_Paths__and_What_to_Expect.pptx`

Or use uploaded file directly from `/mnt/user-data/uploads/` if available in session.

---

## Background Color Rule

**白底 (White Background) 為所有投影片的預設底色。**

- Content slides: 白底 `#FFFFFF` + 深色文字 `#000000` / `#1B1E35`
- Section headers: 可用品牌色 (Teal `#007A86` / Navy `#1B1E35`) 作深色背景
- Title slide & closing: 可用深色背景增加視覺層次
- **不得使用米色、米黃、淺橘等暖色背景** (`#FAF0E6`, `#FFF8E1`, `#F5F5DC` 等)
- 圖表、diagram 區塊：白底或極淺灰 `#F2F2F2`

---

## Brand Colors

Both templates share the same Broadcom color system:

| Role | Hex | Usage |
|------|-----|-------|
| Dark Navy | `#1B1E35` / `#1B1D36` | Slide backgrounds (dark sections) |
| Teal (Primary) | `#007A86` / `#007B8C` | Accent1 — primary highlights, icons |
| Ocean Blue | `#005B84` / `#005C8A` | Accent2 — secondary, links |
| Sky Blue | `#0193C2` / `#0098C7` | Accent3 — supporting color |
| Green | `#61A00A` / `#61A60E` | Accent4 — positive/success indicators |
| Plum | `#6C4B8F` / `#6C4B94` | Accent5 — variety/alternating sections |
| Gold | `#EDB516` / `#F3BA16` | Accent6 — callouts, warnings, highlight |
| White | `#FFFFFF` | Text on dark backgrounds |
| Off-white | `#F2F2F2` / `#EEEEEE` | Light background slides |
| Black | `#000000` | Body text on light backgrounds |

**Color scheme nickname: Leaf = Teal/Green, Aqua = Teal/Blue, Plum = Purple**

### Theme 名稱對照（新一代 VCF 9 範本）

VCF 9 世代的範本（Tech Tuesday 系列）帶兩個 master / 兩套 theme：

| Theme | clrScheme | 用途 |
|-------|-----------|------|
| `VMware 2025 Light` | `VMware-Light` | 預設白底 content 頁（上表色票即為此組）|
| `VMware-dark` | `Custom 8` | 深底 section / DEMO / 封面頁 |

深底頁**不要**沿用淺底 accent（對比不足），改用 dark 版：
accent1 `#0088EF`、accent2 `#01B9C6`、accent3 `#0098C7`、accent4 `#61A60E`、accent5 `#A468EE`、accent6 `#F3BA16`。

**架構圖線條 / 元件框線固定用 `#717074`**（Broadcom 圖示灰），不要用純黑。

---

## Fonts

| Template | Heading Font | Body Font |
|----------|-------------|-----------|
| VCF 5.2 Master | Metropolis / Camphor Std | Arial |
| APJ 9.1 Upgrade | NTR | Arial |
| Tech Tuesday (VCF 9.1) | Arial（theme）+ 內嵌 Metropolis / Metropolis Light / Arial Rounded MT Bold | Arial |

> Note: Metropolis must be installed locally. If unavailable, fall back to Arial.
> Tech Tuesday 範本已 **embed** 這幾套字型，改檔時不要刪 `ppt/fonts/*.fntdata` 與 `presentation.xml` 的 `<p:embeddedFont>`。
> 繁中一律 **微軟正黑體 (Microsoft JhengHei)**（theme 已把 Hant script 指過去）。
> Never use Google Slides — it breaks fonts and spacing.

---

## ⚠️ Layout 用「名稱」解析，不要用編號

`slideLayoutNN.xml` 的編號**是每份 deck 各自的**，同名版型在不同範本編號完全不同
（`slideLayout92` 在 vSphere Tech Tuesday 是 `Section Header 2 - VCF 9`，在 vSAN Tech Tuesday 是 `Section - Availability`）。

改檔前先建對照表：

```bash
for f in unpacked/ppt/slideLayouts/slideLayout*.xml; do
  printf '%s | %s\n' "$(basename $f)" \
    "$(sed -n 's/.*<p:cSld[^>]*name="\([^"]*\)".*/\1/p' $f | head -1)"
done | sort -t'|' -k2
```

同理，**多 master 的範本**要確認 slide 掛在哪個 master 底下（`ppt/slides/_rels/*.rels` → layout → master），
否則同名版型會套到錯的 theme 色。

---

## Slide Layouts (VCF 5.2 Master — primary template)

### Title / Cover Slides
- `Title Slide – Leaf` (Layout 1) — Green/Teal cover, use for most decks
- `Title Slide – Aqua` (Layout 2) — Blue cover
- `Title Slide – Plum` (Layout 3) — Purple cover
- `Title Slide – Leaf with Circle` (Layout 47) — With circular graphic

### Section Headers
- `Section Header – Leaf` (Layout 5)
- `Section Header – Aqua` (Layout 6)
- `Section Header – Plum` (Layout 7)
- `Section Header – Photo 4` (Layout 8) — With background photo

### Content Layouts
- `Agenda` (Layout 4)
- `Title and Subtitle` (Layout 13)
- `Title, Subtitle and Content` (Layout 14)
- `Two-Content Balanced` (Layout 15)
- `Two-Content Balanced Color on Right` (Layout 16)
- `Two-Content Balanced Color on Left` (Layout 17)
- `Comparison` (Layout 18)
- `Three-Content Comparison` (Layout 19)
- `Two Content Dynamic – Left` (Layout 20)
- `Two Content Dynamic – Right` (Layout 21)
- `Diagram with Content on Right` (Layout 22)
- `Diagram with Outcome, Benefit` (Layout 23)

### Icon / Visual Layouts
- `Three Icon` (Layout 25)
- `Four Icon` (Layout 26)
- `Five Icon` (Layout 27)
- `Five Numbered` (Layout 28)
- `Chart` (Layout 29)
- `Customer Success` (Layout 24)
- `Big Statistic` (Layout 37)

### Statement / Closing
- `Big Statement - Leaf` (Layout 30)
- `Big Statement - Aqua` (Layout 31)
- `Big Statement - Plum` (Layout 32)
- `Big Statement with Photo` (Layout 36)
- `Big Statement – Blue` (Layout 54)
- `Thank You / Closing - Leaf` (Layout 39)
- `Thank You / Closing - Aqua` (Layout 40)
- `Thank You / Closing - Plum` (Layout 41)

### VCF 9 世代新增版型（Tech Tuesday master，僅列名稱）

- 封面 / 結尾：`vcf-title-a` / `VCF-light-title-a` / `VCF-title-b` / `vcf-close-a` / `vcf-close-b` / `vcf-med-close-a`
- **主題式 section divider**（不必自己改字，直接挑主題）：
  `Section - Storage` / `Section - Networking` / `Section - VKS` / `Section - DPU` / `Section - AI` /
  `Section - Lifecycle` / `Section - Workloads` / `Section - Resource Mgmt` / `Section - Availability` /
  `Section - Developer` / `Section - Wrap Up`
- 內容頁強化版：`Three/Four/Five Icon - Fancy`（+ `- RBLF` 變體）、`Four Square 1`、
  `Three Icon - Horizontal - Green/Teal`、`Big Statement with Icon - Indigo/Ocean/Plum`、
  `Big Statement 2 - Leaf/Aqua/Plum`、`Definition`、`Important`、`Screenshot`、`QR`、`Additional Resources`
- 免責 / 警語：`Blank`（Do Not Distribute）、`Actually Blank`（PowerPoint-only 警語）、
  `Disclaimer - Regulatory`、`Disclaimer - RevRec`

> **RBLF** = Right Body Left Footer：icon 列 + 右側補充說明，適合每個 icon 要展開 1–2 句時。

---

## Standard Deck Structure

Every Broadcom VCF presentation follows this slide order:

1. **Title Slide** — Topic, presenter name, date, customer name
2. **Agenda** — 4–6 agenda items matching section headers
3. **Section Header** (per major topic)
4. **Content slides** — 2–5 per section
5. **Big Statement** — Key takeaway / value proposition
6. **Thank You / Closing** — Contact info, QR code, next steps
7. **(Optional) Appendix** — Detailed technical reference slides

---

## VCF Naming Conventions (VCF 9.x)

Always use the following product names in VCF 9.x decks:

| Old Name | New Name (VCF 9.x) |
|----------|-------------------|
| VMware Aria Operations | VCF Operations |
| VMware Aria Automation | VCF Automation |
| VMware Aria Operations for Networks | VCF Operations for Networks |
| VMware Aria Operations for Logs | VCF Operations for Logs |
| vSphere with Tanzu / TKG | VKS (vSphere Kubernetes Service) |
| NSX-T | NSX |
| VCDA (Cloud Director Availability) | Live Recovery |
| vDefend Firewall | vDefend |

For VCF 5.2 decks, use the 5.x naming (Aria Operations, Aria Automation, etc.)

---

## Upgrade Path Conventions

When presenting upgrade scenarios, always show:
- **Current State** (left) → **Upgrade Path** (arrow) → **Future State** (right)
- Minimum supported version table
- IP / DNS requirements for new components
- What's not supported (clearly called out in red/gold callout box)

Common upgrade scenarios to include:
- vSphere 8.x → VCF 9.1
- VCF 5.2 → VCF 9.1
- Aria Operations 8.18.x → VCF Operations 9.1

---

## Bilingual Labeling (中英雙語)

For Taiwan customer-facing decks:
- Slide titles: English primary, Chinese subtitle optional
- Architecture diagrams: English labels + Chinese annotation in speaker notes
- Section headers: English
- Speaker notes: Chinese preferred for internal briefing

---

## Editing Workflow

1. Copy the template to `/home/claude/` — never edit the original
2. Unpack: `python3 /mnt/skills/public/pptx/scripts/office/unpack.py template.pptx unpacked/`
3. Add/edit slides by manipulating XML in `unpacked/ppt/slides/`
4. Pack: `python3 /mnt/skills/public/pptx/scripts/office/pack.py unpacked/ output.pptx`
5. QA: `extract-text output.pptx` + visual check

Read `/mnt/skills/public/pptx/editing.md` for full XML editing details.
