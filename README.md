# BroadcomPPT — VMware by Broadcom 簡報技能套件

本 Repo 存放 Kosten Yang 專屬的 Claude Skill 套件，用於快速產生 Broadcom VCF 技術簡報。

## 官方範本

請將以下兩個範本 `.pptx` 上傳至本 Repo 根目錄：

- `VCF_5_2_Master_Technical_-_BC04.pptx` — VCF 5.2 深度技術範本
- `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` — VCF 9.1 升級路徑範本
- `VCF_Edge_Customer_Presentation.pptx` — VCF Edge 9.1 客戶簡報範本 (42 slides)

### 來源簡報 (Source Decks，下列 skill 以其為底版)

- `BOT - 原廠專業技術支援服務團隊與客戶成功案例分享_20241022_V9.0.pptx` — Broadcom CXS 原廠團隊與客戶成功案例 (27 slides)
- `VCF9 - EBC and Customer Deck.pptx` — VCF 9 EBC / 客戶高階簡報 (52 slides)
- `VMware Cloud Foundation - VCF9 - Summary_Final.pptx` — VCF 9 概覽摘要 (24 slides)
- `TECH_TUESDAY_Whats_New_with_vSphere_in_VCF_9_1.pptx` — VCF 9.1 vSphere「What's New」Tech Tuesday 範本 (29 slides)
- `TECH_TUESDAY_Whats_New_with_vSAN_in_VCF_9_1.pptx` — VCF 9.1 vSAN「What's New」Tech Tuesday 範本 (30 slides，Plum 視覺、左圖右文 diagram-led，L300)
- `VXD-VCF-910-PPT-v1_2-Taiwan.pptx` — VCF 9.1 Experience Day 工作坊 Master v1.2 台灣版 (144 slides，Sarah/OmniCorp 故事線 + Labs + Quiz，中文講者備註)

## Skill 套件（30 個 + 1 個 plugin）

### 基礎 / 分流

| Skill | 說明 | 適用情境 |
|-------|------|---------|
| `vcf-base` | 共用基礎 (donor slide 對照、版型解析、三層配色、字型、clone-slide 流程) | 所有 vcf-* 簡報 skill 共用 |
| `broadcom-ppt-base` | 同 `vcf-base`（別名，內容相同） | 舊名稱相容 |
| `vcf-router` | 分流總機：裁決該用哪個 vcf-* skill、怎麼組合，不產出檔案 | 需求模糊或同時命中多個 skill 時先讀 |

### 產業別簡報

| Skill | 說明 | 適用情境 |
|-------|------|---------|
| `vcf-semiconductor` | 半導體/晶圓廠 | TSMC、聯發科、VSMC、OA/MES |
| `vcf-financial` | 金融業 | CTBC、國泰世華、中信、富邦 |
| `vcf-telecom` | 電信/VCSP | CHT、OpenStack 遷移、VCD |
| `vcf-hybrid-cloud` | 混合雲/多站點 | GCVE、HCX、內雲/外雲/公雲 |
| `vcf-ai` | AI 基礎架構 | Private AI、GPU、VKS、GenAI |
| `vcf-edge` | 邊緣運算 | VCF Edge、零售門市、工廠、ZTP、邊緣 AI、上千站點 |

### 主題簡報

| Skill | 說明 | 適用情境 |
|-------|------|---------|
| `vcf-ebc` | VCF 9 EBC 高階簡報 (52 slides) | CIO/V-level pitch、私有雲價值、PCMO、Advanced Services |
| `vcf9-ebc-deck` | 同 `vcf-ebc`（別名） | — |
| `vcf-summary` | VCF 9 概覽摘要 (24 slides) | 快速 overview、產品摘要、30 分鐘介紹版 |
| `vcf9-summary` | 同 `vcf-summary`（別名） | — |
| `vcf-whats-new` | VCF「What's New」/ 技術概覽 (L200–L300) | 新功能介紹、Tech Tuesday、feature deep-dive、DEMO session、vSAN/儲存新功能 |
| `vcf-upgrade` | VCF 9.1 升級路徑 (APJ Upgrade Pathways 範本) | 5.2.1→9.1、vSphere→VCF、converge/import、IP/DNS 規劃 |
| `vcf-91-ppt` | 同 `vcf-upgrade`（別名） | — |
| `vcf-automation` | VCF 9.1 Automation (VCFA) 技術深入 | Consumption 層、VCD→VCFA 遷移、Quota、Placement Policy、Transit Gateway |
| `vcf-experience-day` | VCF 9.1 Experience Day (VXD) 工作坊 | 動手實作體驗日、Lab 導向訓練、模組化半天/一天場次 |
| `vcf-cxs` | 原廠服務團隊/客戶案例 | CXS 團隊介紹、公股金融業成功案例、PSO/顧問服務、數位韌性 |
| `cxs-success-stories` | 同 `vcf-cxs`（別名） | — |
| `vcf-project-status` | 單頁專案狀態報告 (1-page) | 週報/月報、治理會議、RAG 狀態、高管進度單頁 |
| `vcf-incident-report` | CXS 格式事故報告 | 事件發生報告、RCA、事後檢討 |

### 版面元件 (單頁 infographic)

| Skill | 說明 | 適用情境 |
|-------|------|---------|
| `vcf-hex-cluster` | 蜂巢式：中心六角 + 3–6 個彩色六角 | 六步驟 / 六大面向 / 六個元件 |
| `vcf-infographic-cards` | 錯位編號圓 (01–05) 與拱頂卡片 | 關卡、階段、元件、角色等 3–5 個平行項目 |
| `vcf-pillar-cards` | 2–4 欄漸層 header 卡 + 3 列 icon | 倡議、支柱、use case、工作流 |

### 交付文件 / 估算

| Skill | 說明 | 適用情境 |
|-------|------|---------|
| `vcf-delivery-docs` | PSO 官方交付套件為底的交付文件 | 前置檢查、HLD/LLD、安裝手冊、驗收、SOP、As-Built、升級計畫 |
| `manday-estimate` | 人天估算 Excel (WBS + 小計 + 總人天，整數) | 售前 scoping、VCF / HCX / 遷移案估人天 |
| `wbs-gantt` | WBS 進度表 + 自動更新甘特圖 Excel | 專案進度、里程碑、升級/遷移排程 |

### 工作流程

| Skill | 說明 | 適用情境 |
|-------|------|---------|
| `session-state` | 把目標/決策/進度寫進 `dev-docs/`，對抗 context 壓縮失憶 (INIT / CHECKPOINT / RESUME / CLOSE) | 長任務、接續上次、handoff |
| `lab-env` | Lab 環境事實的單一來源 + DNS/NTP/憑證 preflight | 任何 lab 部署/除錯前，絕不憑印象填 IP/FQDN |

### Plugin

| Plugin | 說明 |
|--------|------|
| `plugins/vcf-tech-deck` | VCF 9.1 General Overview Tech Deck (150 slides) — 技術總覽、部署規劃、客戶 pitch、升級遷移；Plum 配色、中英雙語標題。內含 41MB 範本 `assets/VCF_General_Overview_Tech_Deck_9_1.pptx` |

## 工具

| 檔案 | 用途 |
|------|------|
| `scripts/clone-slide.py` | 從範本複製整頁、只換文字（`list` / `clone` / `settext` / `keep`）。一張官方內容頁 XML 約 293,000 字元、純文字只有約 950 —— 複製整頁是「照官方美術又不燒 token」的做法。 |
| `scripts/gen-layout-map.py` | 產生版型對照表；範本換版時重跑 |
| `skills/vcf-whats-new/references/layout-map.md` | 兩份 Tech Tuesday 範本全部 268 個版型的 名稱 → 檔案 → master → 幾何 對照 |

## 目錄結構

```
BroadcomPPT/
├── *.pptx                    # 官方範本 / 來源簡報
├── scripts/                  # clone-slide.py、gen-layout-map.py
├── skills/                   # 30 個 Skill 原始檔 (SKILL.md + references/assets/scripts)
│   ├── vcf-base/  broadcom-ppt-base/  vcf-router/
│   ├── vcf-semiconductor/  vcf-financial/  vcf-telecom/
│   ├── vcf-hybrid-cloud/  vcf-ai/  vcf-edge/
│   ├── vcf-ebc/  vcf9-ebc-deck/  vcf-summary/  vcf9-summary/
│   ├── vcf-whats-new/  vcf-upgrade/  vcf-91-ppt/  vcf-automation/
│   ├── vcf-experience-day/  vcf-cxs/  cxs-success-stories/
│   ├── vcf-project-status/  vcf-incident-report/
│   ├── vcf-hex-cluster/  vcf-infographic-cards/  vcf-pillar-cards/
│   ├── vcf-delivery-docs/  manday-estimate/  wbs-gantt/
│   └── session-state/  lab-env/
├── skills-pkg/               # 每個 skill 對應一個 .skill 安裝檔 (zip)
├── plugins/
│   └── vcf-tech-deck/        # Claude plugin (.claude-plugin/plugin.json + skills/)
└── vcf-delivery-examples/    # vcf-delivery-docs 引用的實際交付範例
```

## 使用方式

下載 `skills-pkg/` 下的 `.skill` 檔，安裝到 Claude 後即可使用。`skills-pkg/` 由 `skills/` 原始檔直接打包，兩邊內容一致。

觸發範例：
- 「幫我做一份給 CTBC 的 VCF 升級提案」→ `vcf-financial`
- 「CHT OpenStack 遷移簡報」→ `vcf-telecom`
- 「VSMC 半導體客戶架構提案」→ `vcf-semiconductor`
- 「混合雲 GCVE + HCX 簡報」→ `vcf-hybrid-cloud`
- 「Private AI 基礎架構簡報」→ `vcf-ai`
- 「VCF Edge 零售門市/工廠邊緣簡報」→ `vcf-edge`
- 「原廠技術團隊介紹 / 客戶成功案例分享」→ `vcf-cxs`
- 「VCF 9 EBC 高階主管簡報 / 私有雲價值 pitch」→ `vcf-ebc`
- 「VCF 9 快速概覽 / 產品摘要」→ `vcf-summary`
- 「VCF 9 What's New / 新功能介紹 / Tech Tuesday」→ `vcf-whats-new`
- 「專案一頁狀態報告 / 週報月報投影片 / RAG status」→ `vcf-project-status`
- 「VCF 9.1 Experience Day / 體驗日工作坊 / 半天 Lab 場」→ `vcf-experience-day`
