---
name: vcf-whats-new-911
description: |
  VCF 9.1.1 全端 "What's New" 技術簡報 skill。以官方 70 頁 `VCF 9.1.1 - Whats New Deck`
  為固定底版，涵蓋七大章節：VCF Networking (NSX / DTGW-EVPN / VPC)、Kubernetes (VKS 與
  Supervisor Services / Headlamp / Helm Controller / Gatekeeper / Cilium)、VCF Operations
  (OpenTelemetry 可觀測性、憑證與密碼集中管理、AI Assistant for VCF、Management Pack Builder、
  Bring Your Own LLM)、VCF Automation (Argo CD / 自助 GitOps)、VMware Data Services Manager
  (PostgreSQL / MySQL / SQL Server)、Private AI (Cloud LLM、多租戶 model serving、模型共享)、
  Protection and Recovery (Network Isolation 防火牆一鍵隔離)。
  當使用者要做 VCF 9.1.1 的 What's New / 新功能介紹 / release 技術簡報 / patch release 更新說明 /
  技術 enablement，或要從這 70 頁挑章節做客戶版、或問「9.1.1 有什麼新功能」時觸發。
  也在使用者提到 9.1.1、9.1.1 新功能、DTGW-EVPN、AI Assistant for VCF、Management Pack Builder、
  VLAN-backed VPC、Argo CD in VCF Automation 時觸發。
  另附 50 頁「Tech Tuesday / SRC 場次」精簡版底版 (templates/VCF_9_1_1_Whats_New_Tech_Tuesday_SRC_v3.pptx)：
  拿掉 VKS 與 AI Assistant/MPB/BYO LLM，VCF Operations 改以 Fleet Management (密碼 / 憑證 / 組態 / Identity) 開場；
  使用者提到 Tech Tuesday、SRC、精簡版、50 頁、Fleet Management 版時用它。
  一律以 templates/ 內兩份底版之一為底，不要從零開始。
---

# VCF 9.1.1 "What's New" 全端技術簡報

> ⚡ **固定底版**：`templates/VCF_9_1_1_Whats_New_Technical_Deck_v1.pptx`（70 頁、17.6MB、16:9）。
> 編輯流程、配色系統、字型與 clone-slide 手法先讀 `anthropic-skills:vcf-base`（別名 `broadcom-ppt-base`）。
> 新版本存成 `_v2`, `_v3`…，**永遠不要覆蓋或刪除 `_v1`**。

## 兩份底版：先選一份

> **GitHub repo 版本只附 SRC 精簡版底版 (`_v3`)**；70 頁完整版 `VCF_9_1_1_Whats_New_Technical_Deck_v1.pptx` 不在 repo 內，需自行放到 `templates/`。

| 底版 | 頁數 | 什麼時候用 |
|---|---|---|
| `templates/VCF_9_1_1_Whats_New_Technical_Deck_v1.pptx` | 70 | **全端完整版**（預設）。含 VKS / Supervisor Services、AI Assistant for VCF、Management Pack Builder、BYO LLM、IPv6 License Server |
| `templates/VCF_9_1_1_Whats_New_Tech_Tuesday_SRC_v3.pptx` | 50 | **Tech Tuesday / SRC 場次精簡版**。來源：`VCF 9.1.1 - Whats New Deck - Tech Tuesday - Edited copy for SRC.pptx`（已清機密字樣） |

判準：要講 VKS 或 AI Assistant → 完整版；Tech Tuesday 場次、聽眾已上過 enablement、或要以 Fleet Management 為主軸 → SRC 版。
兩份同 theme / 同 layout 體系（Leaf），可互相 clone 頁面補章節（例如 SRC 版補回 VKS 章節 → 從完整版 slide 9–17 複製）。
逐頁對照見 `references/deck-inventory-src.md`。

## 與其他 What's New skill 的分工

| 需求 | 用哪個 |
|---|---|
| **VCF 9.1.1 全端**新功能（NSX + VKS + Ops + Automation + DSM + Private AI + Protection） | **本 skill** |
| vSphere / ESX / vCenter 為主的 L200 Tech Tuesday 場次（9.1） | `anthropic-skills:vcf-whats-new`（Plum、29 頁、DEMO 頁模型） |
| 怎麼升上 9.1 / 5.2.1→9.1 / converge / import | `vcf-upgrade` |
| 大範圍技術總覽、要從官方 150 頁挑章節 | `vcf-tech-deck:vcf-tech-deck` |

判準：**講「9.1.1 這個 release 多了什麼」→ 本 skill；講「vSphere 這個產品有什麼」→ `vcf-whats-new`。**

## 底版規格

- **檔案**：`VCF_9_1_1_Whats_New_Technical_Deck_v1.pptx`，70 slides / 56 layouts / 1 master
- **尺寸**：16:9，12188825 × 6858000 EMU
- **Theme**：`VMware 2025 Light`（與 Tech Tuesday 同一套 theme，配色可互通）
- **字型**：Arial（heading + body）。繁中渲染用 **微軟正黑體 (Microsoft JhengHei) + Arial**
- **色系家族**：本 deck 走 **Leaf**（`Title Slide – Leaf` / `Section Header – Leaf` / `Thank You / Closing - Leaf`）。
  同 master 另有 Aqua / Plum 平行版型，**整份要一致，不要混用家族**。

### Theme 配色（accent1–6，與 vcf-base 相同）

| Role | Hex | 用途 |
|---|---|---|
| Teal | `#007B8C` | accent1，主要強調 |
| Ocean Blue | `#005C8A` | accent2 |
| Sky Blue | `#0098C7` | accent3、hyperlink |
| Green | `#61A60E` | accent4，正面 / new |
| Plum | `#6C4B94` | accent5、followed link |
| Gold | `#F3BA16` | accent6，callout |
| Navy | `#1B1D36` | dk2，深底頁 |
| White | `#FFFFFF` | 內容頁預設底色 |

## 核心內容模型：`Diagram with Outcome, Benefit`

70 頁中有 **39 頁**用這個版型（含 `1_`–`6_` 變體），是本 deck 的骨幹。照抄這個 pattern：

```
Title        ← 功能名（產品術語，如 "DHCP Relay on Virtual Network Appliances"）
Subtitle     ← 一句話講「這是什麼」（如 "New centralized service offered by VNAs for..."）
┌ Customer Benefits ─────────┬ Capabilities ──────────────┐
│ • 客戶得到什麼（2–3 點）    │ • 技術能力 / 規模上限（2–4 點） │
└────────────────────────────┴────────────────────────────┘
[ 架構圖 or 產品 UI 截圖 ]
```

Placeholder 對應（`Diagram with Outcome, Benefit`）：
`title` → 標題；`subTitle` idx=10 → 副標；
body idx=17 → 固定字串 **"Customer Benefits"**；idx=20 → benefits bullets；
body idx=19 → 固定字串 **"Capabilities"**；idx=21 → capabilities bullets。

> `1_`–`6_` 變體是同版型的 Google Slides 匯入複本（placeholder idx 為 1–5，非 17/19/20/21）。
> **clone slide 時直接複製最接近的既有頁再改字**，不要自己新接 layout — idx 對不上會掉版。
> 部分頁另有 `Requirements` 區塊（寫在 capabilities bullets 尾端），需要時沿用同一區。

### 其他會用到的版型

| 用途 | Layout |
|---|---|
| 封面 | `Title Slide – Leaf`（slideLayout1） |
| 議程 | `Agenda`（slideLayout4） |
| 章節分隔 | `Section Header – Leaf`（slideLayout5）— 全 deck 7 張 |
| 圖在左、要點在右 | `Diagram with Content on Right`（24 / 46 / 54） |
| 標題+副標+內文 | `Title, Subtitle and Content`（16 / 45） |
| icon 列 | `Three Icon`(27) / `Four Icon`(28) / `Five Icon`(29) |
| 大數字 | `Big Statistic`(39) |
| 結尾 | `Thank You / Closing - Leaf`（slideLayout41） |

## 原始 deck 章節結構（可直接沿用為骨架）

| 章節 | 頁碼 | 內容重點 |
|---|---|---|
| 封面 + Agenda | 1–2 | — |
| **VCF Networking – NSX** | 3–8 | DHCP Relay on VNA、DTGW-EVPN（Centralized Services / Active-Active Route Controllers / Direct Prefix Routing）、VLAN-backed VPC for VCF Automation & VKS |
| **Kubernetes – VKS and Supervisor Services** | 9–17 | read-only node rollout、OS patch 快速修 CVE、Headlamp UI、Helm Controller、Gatekeeper (Policy-as-Code)、Cilium、Ubuntu images |
| **VCF Operations** | 18–38 | OpenTelemetry 可觀測性、社群 dashboard、Identity & Access、密碼與密碼政策、憑證集中管理與自動換發、大規模組態管理、IPv6 License Server、**AI Assistant for VCF**（Diagnostics / BYO LLM / tokenomics）、**AI-Driven Management Pack Builder** |
| **VCF Automation** | 39–46 | 自助 GitOps、集中式 Argo CD 管理與存取、使用者認證、無需提權的自助服務 |
| **VMware Data Services Manager** | 47–55 | DSM 以 VCF 服務形式執行、組態錯誤預檢、PostgreSQL idle overhead、MySQL、SQL Server 與可視性 |
| **Private AI** | 56–67 | Cloud LLM 支援、模型跨/內組織共享、多租戶 model serving、多重 auth provider、metrics & dashboards |
| **Protection and Recovery** | 68–69 | 一鍵 firewall policy 網路隔離 |
| 結尾 | 70 | Thank You / Closing – Leaf |

逐頁標題與副標見 `references/deck-inventory.md`（挑頁做客戶版時對照頁碼）。

## 作法：客製一份 9.1.1 What's New

1. 複製底版 → 依需求**刪頁**（保留封面 / Agenda / 用到的 section header / 結尾）。
2. 改封面標題、講者、日期；Agenda 刪掉已移除的章節。
3. 沿用留下的功能頁改字（Title / Subtitle / Customer Benefits / Capabilities）。
   需要新增功能頁 → **複製同章節既有頁**再改，不要新建。
4. 客戶版：刪 speaker notes、刪內部路線圖頁；對外只出 PDF。
5. **pack 前跑 `scripts/strip-confidential.sh`**（見下）。
6. QA：pack → LibreOffice 轉 PDF → `pdftoppm` 抽圖檢查頁尾與版面。

## ⚠️ 機密字樣（本底版有）

原始檔在 **layout 與 master 層**共 14 處 `Broadcom Proprietary and Confidential`
（`ppt/slides/*.xml` 內 0 處 — 只清 slides 會漏）：

- `ppt/slideMasters/slideMaster1.xml`
- `ppt/slideLayouts/slideLayout{1,2,3,8,9,10,11,13,39,41,42,43}.xml`
  （= Title Slide Leaf/Aqua/Plum、Section Header – Photo、Quote 四款、Big Statistic、Thank You 三款）

其中 **slideLayout1（封面）與 slideLayout41（結尾）本 deck 實際有用到** → 任何交付物產出前一律清掉。

```bash
scripts/strip-confidential.sh <deck.pptx>
```

`Copyright © … Broadcom. All Rights Reserved.` 預設保留。

## Speaker Notes 準則（中文）

- 每張功能頁：先一句「這功能解決客戶什麼痛點」，再 2–3 個技術細節。
- Networking 頁標註規模上限（如 DHCP relay 最多 8 台 server、最多 8 個 active/active RC）與前提（VNA + N/S services enabled）。
- AI Assistant / Private AI 頁註明 LLM 供應方式（BYO LLM / Cloud LLM）與 token 成本考量。
- 一律 conclusion-first、英文技術名詞 + 中文敘述。

## VCF 9.1 命名慣例（沿用）

Aria Operations → VCF Operations｜Aria Automation → VCF Automation｜
Aria Operations for Networks/Logs → VCF Operations for Networks/Logs｜
vSphere with Tanzu / TKG → VKS｜VCDA → Live Recovery｜NSX-T → NSX
