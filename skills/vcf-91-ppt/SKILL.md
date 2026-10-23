---
name: vcf-91-ppt
description: Create Broadcom VCF 9.1 upgrade and technical presentation decks using the official APJ Upgrade Pathways to VCF 9.1 template. Trigger whenever the user wants a presentation on VCF 9.1 upgrade paths, VCF 5.2.1 to 9.1 migration, vSphere to VCF conversion, upgrade prerequisites, IP/DNS planning, or any VCF 9.1 technical topic. Also trigger for 升級路徑, 升級規劃, upgrade scenarios, converge/import flows, or any 9.1 upgrade簡報. Always use APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx as the base template — never create from scratch.
---

# VCF 9.1 Presentation Skill

Read `broadcom-ppt-base` SKILL.md first for general editing workflow.
Location: `/home/claude/broadcom-ppt-skills/broadcom-ppt-base/SKILL.md`

> **⚡ 固定底版**：永遠使用 `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` (3.8MB)。
> **白底 content slides 為主**，section header 可用品牌深色背景。

Template GitHub URL:
`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx`

Or from session uploads: `/mnt/user-data/uploads/APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx`

---

## Template Specs

**File**: `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` (60 slides)
**Aspect ratio**: 16:9
**Fonts**: NTR (heading), Arial (body)
**Background default**: White `#FFFFFF`

### Brand Colors

| Role | Hex | Usage |
|------|-----|-------|
| Teal | `#007B8C` | Primary accent, icons, highlights |
| Ocean Blue | `#005C8A` | Secondary, links |
| Sky Blue | `#0098C7` | Supporting color |
| Green | `#61A60E` | Positive/checkmark indicators |
| Plum | `#6C4B94` | Alternating sections |
| Gold | `#F3BA16` | Callouts, warnings |
| Navy | `#1B1D36` | Dark backgrounds |
| White | `#FFFFFF` | Default slide background |

---

## Slide Layouts (59 layouts available)

### Title / Cover
- `Title Slide – Leaf` (Layout 24)
- `Title Slide – Aqua` (Layout 25) ← **預設封面**
- `Title Slide – Plum` (Layout 26)
- `1_Title Slide – Aqua` (Layout 23) — with VCF 9.1 badge graphic

### Agenda
- `Agenda` (Layout 3 / Layout 48)
- `1_Agenda` (Layout 2)

### Section Headers
- `Section Header – Aqua` (Layout 4 / Layout 50) ← **預設 section header**
- `Section Header – Leaf` (Layout 5 / Layout 51)
- `Section Header – Plum` (Layout 6 / Layout 52)
- `Section Header – Photo` (Layout 7 / Layout 53)

### Content Layouts
- `Title and Subtitle` (Layout 29)
- `Title, Subtitle and Content` (Layout 30 / Layout 59)
- `Two-Content Balanced` (Layout 31)
- `Two-Content Balanced Color on Right` (Layout 32)
- `Two-Content Balanced Color on Left` (Layout 33)
- `Comparison` (Layout 34) ← 用於 Current vs Future State
- `Three-Content Comparison` (Layout 35)
- `Two Content Dynamic – Left` (Layout 36)
- `Two Content Dynamic – Right` (Layout 11)
- `Diagram with Content on Right` (Layout 37) ← 用於架構圖
- `Diagram with Outcome, Benefit` (Layout 38)

### Icon / Visual
- `Three Icon` (Layout 40)
- `Four Icon` (Layout 41)
- `Five Icon` (Layout 42)
- `Five Numbered` (Layout 12) ← 用於升級步驟 (9步驟流程)
- `Chart` (Layout 43)
- `Big Statistic` (Layout 45)

### Quote / Statement
- `Quote – Leaf` (Layout 27 / Layout 54)
- `Quote – Aqua` (Layout 8 / Layout 55)
- `Quote – Plum` (Layout 28 / Layout 56)
- `Big Statement - Leaf` (Layout 13)
- `Big Statement - Aqua` (Layout 14)
- `Big Statement - Plum` (Layout 15)
- `Big Statement 2 - Leaf` (Layout 16)
- `Big Statement - Customer Story` (Layout 9 / Layout 57)
- `Customer Success` (Layout 39)

### Closing
- `Thank You / Closing - Leaf` (Layout 19)
- `Thank You / Closing - Aqua` (Layout 20)
- `Thank You / Closing - Plum` (Layout 21)

### Utility
- `Blank` (Layout 46)
- `Title Only` (Layout 1 / Layout 49)

---

## VCF 9.1 Upgrade Scenarios (核心知識)

### What's New in VCF 9.1 Upgrades

| Feature | 9.0.x | 9.1.x |
|---------|-------|-------|
| NSX Convert and Import | ✔ | ✔ |
| NSX Federation Support | ✔ | ✔ |
| Can Upgrade Operations / Automation / Ops for Networks | ✔ | ✔ |
| NSX Bare Metal Edges Import & Convert | ✘ | ✔ |
| New VCF Management Services deployed during upgrade | ✘ | ✔ |
| VCF Operations Fleet Management is a Service | ✘ | ✔ |
| VCF Operations for Logs is a Service | ✘ | ✔ |
| VIDB deployed Day 0 | ✘ | ✔ |

### Not Supported in 9.1

| Component | 限制說明 |
|-----------|---------|
| Enhanced Linked Mode (ELM) | vSphere 客戶須將所有 vCenter 升至 9.0 再 break ELM；vSphere+NSX 客戶須先 Converge/Import 再離開 ELM |
| VXRail | 現有 VCF 客戶可升級；vSphere 客戶的 VXRail 不支援 |

---

## Upgrade Path 1 — vSphere 8.x (+Ops) → vSphere 8.x + VCF Operations 9.1

**Current State**: vCenter 8.0u3a (有或無 Aria Operations 8.18.x)
**Future State**: vCenter 8.0u3a + VCF Operations 9.1
**Minimum version**: vCenter 8.0u3a, Aria Operations 8.18.x

**New Components & IP/DNS**:
| New Component | Simple | HA |
|--------------|--------|-----|
| License Server | 1 IP, 1 DNS | 1 IP, 1 DNS |

**Steps** (use Five Numbered layout):
1. Design and Plan
2. Deploy VCF Installer
3. Prepare Prerequisites
4. Install or Upgrade Aria Operations → VCF Operations 9.1
5. License VCF Operations 9.1

---

## Upgrade Path 2 — vSphere 8.x (+Ops) → vSphere 9.1 + VCF Operations 9.1

**Current State**: vCenter 8.0u3a (有或無 Aria Operations 8.18.x)
**Future State**: vCenter 9.1 + VCF Operations 9.1

**Upgrade sequence**:
1. Upgrade Aria Operations 8.18.x → VCF Operations 9.1
2. Upgrade vCenter 8.0u3a → vCenter 9.1

**New Components**: License Server (1 IP, 1 DNS)

---

## Upgrade Path 3 — vSphere 8.x + NSX → VCF 9.1 (Converge)

**Current State**: vCenter 8.0u3a + NSX 4.2.x (有或無 NSX Federation / Bare Metal Edges)
**Future State**: Full VCF 9.1 stack

**New Components & IP/DNS**:
| Component | Simple | HA |
|-----------|--------|-----|
| VCF Management Services | 1 IP, 1 DNS | 1 IP, 1 DNS |
| VCF Fleet Services | 1 IP, 1 DNS | 1 IP, 1 DNS |
| VCF Instance Services | 1 IP, 1 DNS | 1 IP, 1 DNS |
| License Server | 1 IP, 1 DNS | 1 IP, 1 DNS |
| VCF Identity Broker | 1 IP, 1 DNS | 1 IP, 1 DNS |
| VCF Mgmt Services IP Pool | Min 6 IPs | Min 8 IPs |
| SDDC Manager | 1 IP, 1 DNS | — |
| NSX Manager | — | — |
| VCF Ops Cloud Proxy | 1 IP, 1 DNS | — |
| VCF Automation | 1 IP (VIP+NodeA) | 3 IPs |

**Steps** (9步驟, use Five Numbered layout):
1. Design and Plan 9.0 (Sizing, IPs, DNS)
2. Prepare all Prerequisites
3. Deploy VCF Installer
4. Configure Depot and Download Binaries
5. Download NSX/vCenter/ESX Binaries
6. Upgrade NSX, vCenter, ESX
7. Converge vSphere with NSX to VCF Instance
8. Configure VCF Operations Licensing
9. (Optional) Import Workload Domain vCenter

---

## Upgrade Path 4 — VCF 5.2 / VCF 5.2.1 → VCF 9.1

**Current State**:
- VCF 5.2 without Aria, OR
- VCF 5.2 with Aria, OR
- VCF 9.0.x

**Minimum version**: Management Domain 5.2, Workload Domain 5.2

**Future State**: VCF 9.1 full stack (SDDC Manager 9.1, vCenter 9.1, NSX 9.1, VCF Management Services, VCF Operations 9.1, VCF License Server, VCF Ops Cloud Proxy, VCF Automation 9.1)

**New Components & IP/DNS**:
| Component | Simple | HA |
|-----------|--------|-----|
| VCF Management Services | 1 IP, 1 DNS | 1 IP, 1 DNS |
| VCF Fleet Services | 1 IP, 1 DNS | 1 IP, 1 DNS |
| VCF Instance Services | 1 IP, 1 DNS | 1 IP, 1 DNS |
| License Server | 1 IP, 1 DNS | 1 IP, 1 DNS |
| VCF Identity Broker | 1 IP, 1 DNS | 1 IP, 1 DNS |
| VCF Mgmt Services IP Pool | Min 6 IPs | Min 8 IPs |
| VCF Ops Cloud Proxy | 1 IP, 1 DNS | — |
| VCF Automation | 3 IPs (VIP+Instance Svc) | 6 IPs |

**Steps** (9步驟, use Five Numbered layout):
1. Design and Plan 9.0 (Sizing, IPs, DNS)
2. Prepare all Prerequisites
3. Download SDDC Binary / Upgrade SDDC Manager / Deploy VCF Services
4. Download Upgrade Binaries for NSX, vCenter, ESX
5. Upgrade VCF Operations 9.1
6. Upgrade Management Domain NSX
7. Deploy / Configure VCF SSO / Logs
8. Upgrade / Deploy / Configure VCF Automation
9. Upgrade Workload Domains

---

## Upgrade Path 5 — VCF 9.0.x → VCF 9.1

**Minimum version**: Management Domain 9.0.x, Workload Domain 9.0.x

**Steps** (9步驟, same as Path 4 with minor differences):
1. Design and Plan
2. Prepare all Prerequisites
3. Download SDDC Binary / Upgrade SDDC Manager / Deploy VCF Services
4. Download Upgrade Binaries for NSX, vCenter, ESX
5. Upgrade VCF Operations 9.1 / Move Fleet to Service
6. Upgrade Management Domain NSX
7. Deploy / Configure VCF SSO / Logs
8. Upgrade / Deploy / Configure VCF Automation
9. Upgrade Workload Domains

---

## Standard Deck Structure for Upgrade Presentation

1. **Title Slide** — `Title Slide – Aqua` (Layout 25) or `1_Title Slide – Aqua` (Layout 23)
2. **Agenda** — 列出升級情境章節
3. **Section: What's New in VCF 9.1** — `Section Header – Aqua` (Layout 4)
   - What's New 比較表 (Two-Content Balanced or Comparison)
   - Not Supported items (callout boxes)
4. **Section: 升級情境 (各 Path)** — 一個 section per path
   - Current State / Future State (Comparison layout)
   - IP & DNS Requirements (Title, Subtitle and Content)
   - Upgrade Steps (Five Numbered layout)
5. **Takeaway / Next Steps** — `Big Statement - Aqua` (Layout 14)
6. **Thank You / Closing** — `Thank You / Closing - Aqua` (Layout 20)

---

## Recommended Slide Colors per Section

| Section | Background | Layout |
|---------|-----------|--------|
| Title slide | Aqua deep (`#005C8A`) | Title Slide – Aqua |
| Section header | Aqua deep | Section Header – Aqua |
| Content / body | White `#FFFFFF` | Title, Subtitle and Content |
| Current vs Future | White, color on left/right | Two-Content Balanced Color |
| IP/DNS table | White | Title, Subtitle and Content |
| Steps flow | White | Five Numbered |
| Callout (Not Supported) | Gold `#F3BA16` box on white | Title, Subtitle and Content |
| Big Statement | Aqua or Leaf | Big Statement - Aqua |
| Closing | Aqua or Leaf | Thank You / Closing - Aqua |

---

## VCF 9.1 Naming Conventions

Always use these names in VCF 9.1 decks:

| Old Name | VCF 9.1 Name |
|----------|-------------|
| Aria Operations | VCF Operations |
| Aria Automation | VCF Automation |
| Aria Operations for Networks | VCF Operations for Networks |
| Aria Operations for Logs | VCF Operations for Logs |
| vSphere with Tanzu / TKG | VKS |
| VCDA | Live Recovery |
| SDDC Manager | SDDC Manager (unchanged) |
| NSX-T | NSX |

---

## Speaker Notes Guidelines (中文)

- **升級規劃章節**：強調 IP/DNS 規劃是升級前最常被忽略的步驟，建議客戶提前 2-3 週確認
- **VCF 5.2.1 升級**：5.2.1 = 5.2 base，升級路徑相同，直接走 Path 4
- **New Components**：VCF Management Services 是 9.1 新增的微服務架構，需額外 IP pool，Simple 最少 6 個 IP
- **ELM 限制**：Enhanced Linked Mode 必須在升級前 break，這是最常見的升級 blocker
- **VXRail**：提醒客戶 VXRail 限制，避免現場升級時才發現不支援
- **Fleet Management as Service**：9.1 的重大架構改變，VCF Operations 由 VM 變成 Service，升級後不需要維護額外 VM
