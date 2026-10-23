# VCF Tech Deck plugin

Build Broadcom VMware Cloud Foundation 9.1 presentations from the official 150-slide **VCF General Overview Tech Deck — Updated for 9.1** template.

## What this plugin does

When you ask for a VCF 9.1 presentation — technical overview, deployment planning, customer pitch, or upgrade migration — this plugin copies the bundled 150-slide official Broadcom template, picks the right slides for your use case, and customizes them for your customer. The output is always:

- **Plum color scheme** (matches the bundled template)
- **Bilingual** — English title + Traditional Chinese subtitle
- **White content background** (Broadcom brand rule)
- **Sentence case** titles (not Title Case, not ALL CAPS)

## Use cases supported

| Use case | Length | When to use |
|---|---|---|
| General technical overview | 25–50 slides | Architect briefings, full stack tour |
| Deployment planning | 30–45 slides | Greenfield bring-up, resource/IP/FQDN planning |
| Customer pitch / EBC | 20–35 slides | CIO/CTO briefings, value proposition |
| Upgrade / migration | 20–30 slides | VCF 5.x → 9.1, Import, Converge flows |

## What's included

- `skills/vcf-tech-deck/SKILL.md` — Skill instructions for Claude
- `skills/vcf-tech-deck/assets/VCF_General_Overview_Tech_Deck_9_1.pptx` — Official 150-slide Broadcom template (42 MB)
- `skills/vcf-tech-deck/references/`
  - `slide-catalog.md` — Full 150-slide inventory grouped by 9 chapters
  - `color-and-style.md` — Plum palette, font rules, bilingual labeling rules
  - `deployment-planning.md` — Slide picks + content recipe for deployment-planning decks
  - `customer-pitch.md` — Slide picks + content recipe for customer pitch / EBC
  - `upgrade-migration.md` — Slide picks + content recipe for upgrade migration

## How to trigger

Examples of phrases that trigger this skill:

- "幫我做 VCF 9.1 技術簡報"
- "VCF deployment planning deck"
- "Make a VCF customer pitch for 玉山銀行"
- "VCF 5.2 升級到 9.1 的簡報"
- "VCF Tech Tuesday style overview"
- "VCF General Overview deck"

## Requirements

The skill expects access to file I/O tools (Read, Write, Bash) to copy and modify the template. python-pptx is sufficient for most operations; for complex layout work, use the bundled pptx unpack/pack helpers.

## Author

Kosten Yang
