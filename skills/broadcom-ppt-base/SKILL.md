---
name: broadcom-ppt-base
description: Core Broadcom/VMware by Broadcom PowerPoint template knowledge. Use this as a shared reference for all VCF presentation skills. Contains template specs, slide layouts, color system, font rules, and upgrade path conventions for VCF 5.2 and VCF 9.1 templates.
---

# Broadcom PPT Base Template Knowledge

This is the shared reference for all Broadcom VCF vertical presentation skills.
Always read this alongside the vertical skill (semiconductor / financial / telecom / hybrid-cloud / ai).

---

## Template Files

Two official templates exist. **Always use one of these as the base — never create from scratch.**

| Template | File | When to use |
|----------|------|-------------|
| VCF 5.2 Master Technical | `VCF_5_2_Master_Technical_-_BC04.pptx` | Deep technical / architecture deep-dive |
| APJ Upgrade Pathways to VCF 9.1 | `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` | Upgrade planning, modernization pitch |

Download from GitHub: `https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/<filename>`
Or use uploaded file directly from `/mnt/user-data/uploads/` if available in session.

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

---

## Fonts

| Template | Heading Font | Body Font |
|----------|-------------|-----------|
| VCF 5.2 Master | Metropolis / Camphor Std | Arial |
| APJ 9.1 Upgrade | NTR | Arial |

> Note: Metropolis must be installed locally. If unavailable, fall back to Arial.
> Never use Google Slides — it breaks fonts and spacing.

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
