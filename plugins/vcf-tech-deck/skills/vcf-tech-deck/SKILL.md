---
name: vcf-tech-deck
description: Build Broadcom VCF 9.1 presentations from the official 150-slide General Overview Tech Deck (VCF General Overview Tech Deck - Updated for 9.1). Trigger when the user asks for a VCF 9.1 deck, VCF 技術簡報, VCF Overview, VCF Tech Deck, VCF General Overview, VCF 部署規劃簡報, VCF 客戶簡報, VCF customer pitch, VCF EBC briefing, VCF Tech Tuesday style deck, VCF 升級路徑簡報, VCF upgrade pathways, vSphere/Aria/HCX/NSX 整合簡報, or any 投影片/deck/slides/pptx request about VCF 9.x topics including private cloud, vSAN ESA, NSX networking, HCX mobility, fleet management, VCF Operations, VCF Automation, VKS Kubernetes, Private AI, security/compliance, VCF Live Recovery, License Hub, vDefend, edge deployment. Always uses Plum color scheme and bilingual English title + Chinese subtitle. Never create slides from scratch — always start from the bundled 150-slide template.
---

# VCF Tech Deck (Broadcom VCF 9.1)

Build VCF 9.1 presentations by selecting and customizing slides from the official 150-slide **VCF General Overview Tech Deck — Updated for 9.1**. The full template is bundled at `${CLAUDE_PLUGIN_ROOT}/skills/vcf-tech-deck/assets/VCF_General_Overview_Tech_Deck_9_1.pptx`.

## Mandatory rules

1. **Never create slides from scratch.** Always copy the bundled template, then delete/edit slides. The template carries 64 official Broadcom layouts (Title Slide – Leaf/Aqua/Plum, Section Header – Leaf/Aqua/Plum/Photo, Big Statement, Diagram with Content on Right, Two-Content Balanced, Three/Four/Five Icon, Five Numbered, Chart, Customer Success, Big Statistic, Thank You / Closing, etc.). Recreating these layouts by hand loses the brand fidelity.

2. **Plum color scheme.** This deck uses Plum (`#6C4B8F`/`#6C4B94`) for all section headers and accent elements. Do NOT swap section headers to Leaf or Aqua variants. When inserting new section headers, pick the `1_Section Header – Plum` layout. Big Statement closing slides should be `Big Statement - Plum` or `Big Statement 2 - Plum`. Closing slide is `Thank You / Closing - Plum`.

3. **Bilingual labeling.** Every new content slide must carry an English title and a Chinese subtitle:
   - Slide title (top): English (e.g. "VCF Operations 9.1 — Fleet Management")
   - Slide subtitle (under title): Traditional Chinese (e.g. "Fleet 級別集中管理 — 跨 Instance 統一治理")
   - Body content: English primary, Chinese annotation in parentheses or bullet sub-points when helpful
   - Speaker notes: Traditional Chinese (for internal Taiwan briefings)
   - Section headers: Keep the English headline; do NOT translate the section header text.

4. **White background.** Content slides stay white. Only section headers, title slide, big statements, and closing slide use the Plum dark background. Never use beige/cream/orange backgrounds.

5. **Sentence case.** Slide titles use sentence case ("Private cloud constructs within VMware Cloud Foundation"), never Title Case, never ALL CAPS. Chinese subtitles do not need case rules.

## Workflow

### Step 1 — Discovery: confirm the use case

Ask the user (use AskUserQuestion) which use case fits, unless already obvious from the request:

- **General technical overview** — covering the whole VCF 9.1 stack (compute, storage, network, mobility, operations, automation, VKS, AI, security). Audience: technical decision makers, infra architects. Length: 25–50 slides.
- **Deployment planning** — Resources / IP / FQDN / network / firewall / DNS for a Greenfield bring-up. Audience: infra engineers, PMO. Length: 30–45 slides. See `references/deployment-planning.md`.
- **Customer pitch / EBC** — Executive briefing, value proposition, business outcomes, customer success. Audience: CIO/CTO/business stakeholders. Length: 20–35 slides. See `references/customer-pitch.md`.
- **Upgrade / migration** — VCF 5.x → 9.1, vSphere → VCF Import, Converge flow. Audience: existing customers, ops teams. Length: 20–30 slides. See `references/upgrade-migration.md`.

A deck can combine use cases (e.g., customer pitch + deployment planning).

### Step 2 — Slide selection from the 150-slide catalog

Read `references/slide-catalog.md` for the full 150-slide inventory grouped by 9 chapters. Pick slides relevant to the use case. The catalog also lists "must-have" anchor slides per use case.

### Step 3 — Read the format skill

Before manipulating the pptx, read `/var/folders/jh/mlkw7x193gg10t4h4vqftqlc0000gn/T/claude-hostloop-plugins/86389155adc3e66f/skills/pptx/SKILL.md` for the proper unpack/edit/pack workflow. Use the unpack scripts at `/sessions/jolly-festive-fermi/mnt/.claude/skills/xlsx/scripts/office/` (despite the path, the office helpers work for pptx too) or `python-pptx` directly.

### Step 4 — Edit workflow

1. Copy the bundled template to `outputs/`.
2. Delete unwanted slides (keep only those picked in Step 2).
3. Re-title and re-content the kept slides for the customer/situation:
   - Replace English title (sentence case)
   - Add Chinese subtitle (Traditional)
   - Update body content while preserving the layout placeholders
4. For tables: replace cell text only, never restructure the table.
5. Insert new section headers using `1_Section Header – Plum` layout if you need a chapter divider not in the original 9 chapters.
6. Update the title slide (slide 1) with customer name, presenter, date.
7. Update the closing slide (slide 150) with contact info.

### Step 5 — Save deliverables

Save the output to the workspace folder with a filename pattern:
`{date}-{customer}-{topic}-VCF9.1.pptx`

Examples:
- `20260618-EsunBank-VCF9.1-DeploymentPlanning.pptx`
- `20260618-Foxconn-VCF9.1-EBC.pptx`
- `20260618-CTBC-VCF9.1-UpgradeFrom5.2.pptx`

Then present the file with `present_files` and a short one-paragraph summary of what you built.

## Use-case quick reference

| Use case | Anchor slides (catalog #) | Color | Reference |
|---|---|---|---|
| General technical overview | 1, 3, 5, 8, 21–32, 35–42, 49–55, 66–73, 78, 119, 124, 134, 143, 150 | Plum | `references/slide-catalog.md` |
| Deployment planning | 1, 3, 5–12, 13, 22–32, 37–48, 58–62, 78, 86, 150 | Plum | `references/deployment-planning.md` |
| Customer pitch / EBC | 1, 3, 5, 24–28, 31–32, 36–40, 63–64, 92–94, 119, 124, 132, 134, 140, 143, 150 | Plum | `references/customer-pitch.md` |
| Upgrade / migration | 1, 7, 8, 11, 12, 14–20, 50–55, 78, 150 | Plum | `references/upgrade-migration.md` |

## Reference files

- `references/slide-catalog.md` — Full 150-slide inventory by chapter, with layout types
- `references/color-and-style.md` — Plum color hex codes, font rules, bilingual labeling examples
- `references/deployment-planning.md` — Slide picks + content recipe for deployment-planning decks
- `references/customer-pitch.md` — Slide picks + content recipe for customer pitch / EBC decks
- `references/upgrade-migration.md` — Slide picks + content recipe for VCF 5.x → 9.1 upgrade decks
