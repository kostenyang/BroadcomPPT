---
name: vcf-automation
description: Create Broadcom VCF 9.1 Automation (Consumption) technical deep-dive / enablement decks using the official WOE "VCF 9.1 Automation Technical Deep Dive" source deck. Trigger whenever the user wants a presentation, deep-dive, or enablement deck about VCF Automation, VCFA, the VCF self-service / Consumption layer, Appstack Formations, vSphere Namespace self-service, VM Apps vs All Apps, Project Content Libraries, VCD-to-VCF Automation migration, Cost Visibility, Organization/Region Quota, Infrastructure Placement Policies, Distributed Gateway / Transit Gateway networking, Container Service, VM Service (snapshots / VM Groups / Day-2 NIC), or Services Framework. Also trigger for VCF Automation 新功能, 自助式雲端消費層, VCFA deep dive, 自動化簡報, consumption layer 簡報. Always use Q3WOE021_-_VCF_9_1_Automation_Technical_Deep_Dive.pptx as the base template — never create from scratch.
---

# VCF 9.1 Automation (Consumption) Technical Deep-Dive Skill

Read `vcf-base` SKILL.md first for the general editing workflow, colors, and fonts.
（共用基礎：`skills/vcf-base/SKILL.md`）

> **⚡ 固定底版**：永遠使用 `Q3WOE021_-_VCF_9_1_Automation_Technical_Deep_Dive.pptx` (30 slides, 13MB)。
> 這是 **WOE (Week of Enablement) 技術 deep-dive** 範本，聚焦 **VCF Automation = VCF 的自助式雲端「消費層 (Consumption)」**（前身 Aria Automation / vRA、以及 VCD 的雲端體驗）。
> **白底 content 頁為主**；title 用 Plum、customer 章節用 Aqua、closing 用 Aqua。

Template GitHub URL：
`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/Q3WOE021_-_VCF_9_1_Automation_Technical_Deep_Dive.pptx`

或 session 上傳：`/mnt/user-data/uploads/Q3WOE021_-_VCF_9_1_Automation_Technical_Deep_Dive.pptx`

---

## When to use this vs other VCF skills

| 需求 | 用哪個 skill |
|------|-------------|
| **VCF Automation / VCFA / Consumption 消費層 deep-dive、自助式雲端、Namespace/Project/Appstack、VM Apps vs All Apps** | **vcf-automation** (本 skill) |
| vSphere / ESX 平台「What's New」、Tech Tuesday、feature 概覽 | `vcf-whats-new` |
| 升級路徑、5.2.1→9.1、IP/DNS 規劃、converge/import | `vcf-91-ppt` / `vcf-upgrade` |
| 特定客戶垂直故事 (金融/電信/半導體/AI/混合雲/邊緣) | `vcf-financial` / `vcf-telecom` / `vcf-semiconductor` / `vcf-ai` / `vcf-hybrid-cloud` / `vcf-edge` |
| VCF 9 高階主管 / CIO pitch、EBC | `vcf-ebc` / `vcf-summary` |
| 單頁專案狀態報告 | `vcf-project-status` |

> 判斷關鍵：只要主題是**「使用者怎麼自助消費基礎架構」**（self-service、catalog、blueprint、namespace、quota、cost、tenancy、TGW/VPC 消費）→ 用本 skill。
> 主題是**「平台本身有什麼新功能」**（ESX/vCenter/vSAN/NSX 底層）→ 用 `vcf-whats-new`。

---

## Template Specs

**File**：`Q3WOE021_-_VCF_9_1_Automation_Technical_Deep_Dive.pptx`（30 slides）
**Aspect ratio**：16:9（12188825 × 6858000 EMU）
**Fonts**：Arial（heading + body）。繁中渲染用 **微軟正黑體 (Microsoft JhengHei) + Arial**。
**Background default**：White `#FFFFFF`
**Content level**：L300 技術 deep-dive，預設 60 分鐘 enablement session
**Footer**：`vmware by Broadcom`（所有 content 頁固定）+ Broadcom 機密聲明

### Brand Colors（theme，與 vcf-base 一致）

| Role | Hex | Usage |
|------|-----|-------|
| Teal | `#007B8C` | Primary accent、icon |
| Ocean Blue | `#005C8A` | Secondary、links |
| Sky Blue | `#0098C7` | Supporting、icon |
| Green | `#61A60E` | Positive /「new」/ checkmark |
| Plum | `#6C4B94` | Title slide、alternating accent |
| Gold | `#F3BA16` | Callout、警示 badge |
| Navy | `#1B1D36` | 深色背景（title / divider） |
| White | `#FFFFFF` | 預設 content 底色 |
| Off-white | `#EEEEEE` | 淺底區塊 / 截圖底 |

---

## Signature Layouts（本範本特色頁）

| 用途 | Layout 名稱 | Layout 檔 | 說明 |
|------|------------|-----------|------|
| **★ Feature 頁（核心）** | `Diagram with Content on Right` | slideLayout41 | 左截圖/架構圖 + 右 3–5 點能力清單。**deep-dive 主力版型，slide 7–18 全用這個** |
| **封面** | `2_Title Slide – Plum` | slideLayout2 | 紫色封面 + 標題 + 講者 + 日期 |
| **What's New 總覽** | `Title and Subtitle` | slideLayout35 | 三欄分類（Deploy / Lifecycle / Governance）總覽 |
| **Takeaways / 資源** | `1_Title, Subtitle and Content` | slideLayout47 | 條列連結 / 影片 / 文件 |
| **客戶章節封面** | `1_Title Slide – Aqua` | slideLayout48 | 藍色封面，customer case 開場 |
| **客戶成功案例** | `Customer Success` | slideLayout50 | Challenge / Solution / Impact 結構 |
| **結尾** | `Thank You / Closing - Aqua` | slideLayout25 | Thank You + CTA |
| **WOE 房務頁** | `Title Only` | slideLayout3 | Housekeeping（Chat/Q&A/Recording/Materials） |
| **滿版圖 / pillar** | `Blank` | slideLayout1 | VCF 9.1 三大價值支柱、滿版視覺 |

> 範本共 256 個 layout 可用；上表是這份 deck 實際用到、要優先沿用的版型。

---

## Feature-Slide 內容模型（★ 核心 pattern）

每張 deep-dive 功能頁（slideLayout41）固定三層結構，照抄：

```
┌─ Benefit Headline（上方，價值陳述句） ────────────────────────┐
│  例：Create reusable sandbox environments with Appstack Formations │
├─ Feature / Action 副標 ──────────────────────────────────────┤
│  例：Capture a running namespace as an application blueprint        │
├──────────────────────┬───────────────────────────────────────┤
│  [左] 產品截圖 / 架構圖 │  [右] 3–5 點能力 bullet                 │
│   (UI screenshot 或   │   • 能力點一（具體做得到什麼）          │
│    networking diagram) │   • 能力點二                            │
│                        │   • 能力點三                            │
└──────────────────────┴───────────────────────────────────────┘
```

規則：
- **Headline 講「客戶/管理員得到什麼好處」**，不是功能名本身；功能/動作放副標。
- 右側 bullet **3–5 個**；超過 5 個拆兩頁或合併同類。
- 左側一定要有視覺：UI 截圖（多數頁）或 networking diagram（TGW/VPC/VLAN 類頁）。
- **conclusion-first**：每點 bullet 第一句就講結果，再補細節。
- 英文技術名詞 + 中文敘述；繁中客戶版可在 headline 下加一行中文副標。

---

## Standard Deck Structure（照搬參考 deck 30 頁骨架）

| # | 段落 | 頁 | Layout | 內容 |
|---|------|----|--------|------|
| 1 | **WOE 平台 / Housekeeping** | 1–2 | Title Only / Blank | Zoom Events 操作、Chat/Q&A/Recording/Materials（對內 enablement 才保留；對客戶版刪掉） |
| 2 | **Title** | 3 | Title – Plum | VCF 9.1 Automation Technical Deep Dive + 講者 + 日期 |
| 3 | **VCF 9.1 價值支柱** | 4–5 | Blank | 三大支柱：Efficient Infra & Ops / High-Velocity App Delivery / Cyber Resilience；+ Open Platform |
| 4 | **What's New: VCF Automation 總覽** | 6 | Title and Subtitle | 三欄：Fast-Track Deployment / App & Workload Lifecycle / Governance & Cost Visibility |
| 5 | **★ Feature Deep-Dive** | 7–18 | Diagram with Content on Right | 每張一個 9.1 Automation 功能（見下方素材庫） |
| 6 | **Takeaways / 資源** | 19 | Title, Subtitle and Content | 影片系列、release replay、demo 連結 |
| 7 | **Customer Case（選用）** | 20–24 | Aqua / Customer Success | 客戶 VCF Automation 演進故事（參考：Rogers VCF 4→9） |
| 8 | **Enablement 資源 / Field Guide** | 25–29 | Title Only 系列 | Field Guide 更新、Upgrade Readiness（PCMO v5 / Upgrade Planner）、Frontier AI、HOL、Next Steps CTA |
| 9 | **Thank You** | 30 | Thank You – Aqua | 收尾 + CTA |

> **客製給特定客戶時**：保留 2→3→4→5（核心技術），刪 1（WOE 房務）、25–28（內部 enablement 資源），customer case 換成該客戶情境。

---

## 參考 Deck 功能素材庫（VCF 9.1 Automation / Consumption，可直接當 feature 頁內容）

> 這是這份 deck 最有價值的部分 —— VCF 9.1 Automation 全部新功能。挑使用者需要的組成 deep-dive。

### A. Fast-Track Deployment（快速佈署 / 服務擴充）
- **Appstack Formations** — 把執行中的 vSphere Namespace 連同基礎架構（disks / networks）擷取成 application blueprint，可發佈到 catalog、跨 project 重複佈署。支援 **Labs-as-a-Service**、沙箱環境、一致性與品保。
- **Container Service / Container Deployment** — 透過 VCF Services UI + Blueprints 直接跑 container，**不需自建/維運完整 Kubernetes**；以 vSphere Namespace 為界，具備平台層 security / visibility / governance。
- **Services Framework** — region 層級的服務管理框架：佈署、升級、發佈服務到 organization 或整個 VCF Fleet；標準化整合 VMware 與 partner 服務，新服務上線通知。

### B. App & Workload Lifecycle Management（應用與工作負載生命週期）
- **Project Content Libraries** — 新型態 content library，可限定只給 organization 內特定 project 與其使用者；管理員精準控管 VM Image 的可見範圍。
- **Self-Service vSphere Namespace Creation** — Org Admin 授權 Project Admin 自助建立 vSphere Namespace，仍保有細粒度治理；可關聯 Regions / Namespace Classes / Connectivity Profiles / Subnets / Infra Policies / VPCs / Service Engine Groups。打破 Project team 對 Org Admin 的相依。
- **VM Service 強化** — UI 內支援 **VM Snapshots、VM Groups（一起管理的 VM 群組）、Day-2 NIC 變更**。
- **VCD Migration Path to VCF Automation** — VCD 客戶轉用新 VCF Cloud Experience 的路徑：OrgVDC Resource Pool 的 VM 匯入 Namespace；Supervisor / Clusters / Regions / Projects / Namespaces 自動建立並對應既有 VCD 結構；OrgVDC 網路界線遷移到 **NSX VPC**。

### C. Governance & Cost Visibility（治理與成本可視性）
- **Cost Visibility & Pricing** — 從 Organization Overview 頁看 Project / Namespace 成本；Org 與 Project 總成本；可寄報表 / 告警給 Admin；使用者從 catalog 申請（VM / VKS）時即顯示預估成本。
- **Organization Region Quota** — 可把整個 region quota 或部分分享給一或多個 organization；Day 0 quota 設定大幅簡化，Admin 不必煩惱 reservation。
- **Infrastructure Placement Policies** — 治理 VM 在 region 內的放置；policy 可強制或選用；依放置需求指派給 namespace；支援 **license 最佳化（依 OS 放置）、DR 預留、合規**。

### D. Networking（自助式網路消費）
- **Distributed Gateway / Distributed VLAN Connections** — VPC 對外連線只需一個 **VLAN + Gateway CIDR**，透過實體網路 VLAN 定義外部連通，**不需 NSX Tier-0 gateway**；簡化 organization TGW 連外。
- **Transit Gateway Advanced Networking** — organization 自助管理 **VPN（Policy-Based / Route-Based）、NAT（DNAT/SNAT）、Static Routes、TGW/VPC 上的 Firewall**。

---

## VCF Automation 定位與術語（重要：consumption 模型）

VCF Automation = VCF 的**自助式雲端消費層**。9.x 有兩種消費模型，常被客戶問差異：

| 模型 | 別名 | 適用 | 重點 |
|------|------|------|------|
| **VM Apps** | 傳統 VM 消費 | 既有 VM 投資、blueprint 自動化 | 成熟、tried-and-true 能力（vRA 沿襲） |
| **All Apps** | Cloud Native 消費 | 新雲原生工作負載（containers / VKS） | 新世代 self-service、Namespace 為核心；部分傳統 VM 能力仍在補齊 |

- **Mixed Tenancy Mode**：VM Apps 與 All Apps 可在「Share a WLD / Share a Cluster」模式下共存；但**無法共用同一 WLD**（各自需專屬 vCenter 與 NSX）。
- 常見 PSO 建議：既有 VM 投資先用 **VM Apps**，新能力用 **All Apps**，採 co-exist → pilot → migrate 漸進路徑。
- **Appstack Formation 被視為 VM Apps → All Apps 的未來遷移橋樑**。
- 設計參考：Broadcom TechDocs「VCF Automation Deployment Models / Multi-Tenancy Design Patterns / Shared Tenancy Design」。

---

## VCF 9.1 Naming Conventions

| Old Name | VCF 9.1 Name |
|----------|-------------|
| Aria Automation / vRA / vRealize Automation | **VCF Automation (VCFA)** |
| Aria Operations | VCF Operations |
| vSphere with Tanzu / TKG | **VKS** |
| Cloud Director (VCD) Org VDC | → 遷移到 **Projects / Namespaces + NSX VPC** |
| NSX-T | NSX |
| VCDA | Live Recovery |
| （新詞） | **Supervisor / Region / Project / vSphere Namespace / Appstack Formation / Transit Gateway (TGW) / NSX VPC** |

---

## Editing Workflow（沿用 vcf-base）

1. 複製範本到 `/home/claude/` —— 永遠不要改原檔。
2. Unpack：`python3 /mnt/skills/public/pptx/scripts/office/unpack.py <template>.pptx unpacked/`
3. 改 / 增 feature 頁：複製 slideLayout41 結構的既有 feature slide，換 headline / 副標 / 右側 bullet / 左側截圖。
4. Pack：`python3 /mnt/skills/public/pptx/scripts/office/pack.py unpacked/ output.pptx`
5. QA：`extract-text output.pptx` + 視覺檢查（截圖是否仍對齊、右側 bullet 是否溢出框）。

讀 `/mnt/skills/public/pptx/editing.md` 取得完整 XML 編輯細節。

---

## ⚠️ Distribution / 機密性

- 範本含 **Broadcom 內部機密聲明** 與 WOE 房務頁（slide 1–2）。
- **對外（客戶 / VMUG / Explore）版本**：刪掉 WOE 房務頁、內部 enablement 資源頁（Field Guide / HOL / Odyssey），移除 speaker notes，輸出 PDF。
- **內部 enablement**：保留全部頁與 speaker notes。
- 客製給特定客戶時，先換封面標題 / 講者 / 日期，刪不相關功能頁。

---

## Speaker Notes Guidelines（中文）

- **每張 feature 頁**：1 句帶「這功能解決客戶什麼痛點」，再講 2–3 個技術細節（誰能自助、治理邊界、相依被打破）。
- **VM Apps vs All Apps 頁**：務必講清楚「不能共用 WLD」、Mixed Tenancy 的限制，以及 co-exist/pilot/migrate 建議。
- **Networking 頁（TGW / Distributed VLAN）**：強調「不需 Tier-0」「只要 VLAN + CIDR」這類 opex 降低點。
- **Cost / Quota / Placement Policy 頁**：對金融/公股客戶強調 governance、license 最佳化、合規。
- **VCD Migration 頁**：對電信 / VCSP 客戶（如 CHT）特別相關，連結 OrgVDC → NSX VPC 對應。
- 一律 **conclusion-first**，英文技術名詞 + 中文敘述。

---

## Token / 成本最佳化（沿用既有規則）

- **內容草稿與檔案生成分開**：先在對話確認所有 feature 頁文字（挑哪些功能、headline、bullet），再一次生成 .pptx。
- 大型 deck（>20 頁）分多個對話產出，避免單次 token 爆量。
- **Front-load 需求**：一開始講清楚 —— 要哪些功能段（Deployment / Lifecycle / Governance / Networking）、對內或對外版、要不要 customer case、要不要 enablement 資源頁。
- 模板型 deck 用標準 chat + 本 skill，**不要用 Cowork**。
