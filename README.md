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

## Skill 套件

| Skill | 說明 | 適用情境 |
|-------|------|---------|
| `vcf-base` | 共用基礎 (顏色/字體/Layout) | 所有垂直 skill 共用 |
| `vcf-semiconductor` | 半導體/晶圓廠 | TSMC、聯發科、VSMC、OA/MES |
| `vcf-financial` | 金融業 | CTBC、國泰世華、中信、富邦 |
| `vcf-telecom` | 電信/VCSP | CHT、OpenStack 遷移、VCD |
| `vcf-hybrid-cloud` | 混合雲/多站點 | GCVE、HCX、內雲/外雲/公雲 |
| `vcf-ai` | AI 基礎架構 | Private AI、GPU、VKS、GenAI |
| `vcf-edge` | 邊緣運算 | VCF Edge、零售門市、工廠、ZTP、邊緣 AI、上千站點 |
| `vcf-cxs` | 原廠服務團隊/客戶案例 | CXS 團隊介紹、公股金融業成功案例、PSO/顧問服務、數位韌性 |
| `vcf-ebc` | VCF 9 EBC 高階簡報 | CIO/V-level pitch、私有雲價值、PCMO、Advanced Services |
| `vcf-summary` | VCF 9 概覽摘要 | 快速 overview、產品摘要、30 分鐘介紹版 |
| `vcf-whats-new` | VCF「What's New」/ 技術概覽 (L200–L300) | 新功能介紹、Tech Tuesday、feature deep-dive、DEMO session、vSAN/儲存新功能 |
| `vcf-project-status` | 單頁專案狀態報告 (1-page) | 週報/月報、治理會議、RAG 狀態、高管進度單頁 |

## 工具

| 檔案 | 用途 |
|------|------|
| `scripts/clone-slide.py` | 從範本複製整頁、只換文字（`list` / `clone` / `settext` / `keep`）。一張官方內容頁 XML 約 293,000 字元、純文字只有約 950 —— 複製整頁是「照官方美術又不燒 token」的做法。 |
| `scripts/gen-layout-map.py` | 產生版型對照表；範本換版時重跑 |
| `skills/vcf-whats-new/references/layout-map.md` | 兩份 Tech Tuesday 範本全部 268 個版型的 名稱 → 檔案 → master → 幾何 對照 |

## 目錄結構

```
BroadcomPPT/
├── skills/              # Skill 原始檔 (SKILL.md)
│   ├── vcf-base/
│   ├── vcf-semiconductor/
│   ├── vcf-financial/
│   ├── vcf-telecom/
│   ├── vcf-hybrid-cloud/
│   ├── vcf-ai/
│   ├── vcf-edge/
│   ├── vcf-cxs/
│   ├── vcf-ebc/
│   ├── vcf-summary/
│   ├── vcf-whats-new/
│   └── vcf-project-status/
└── skills-pkg/          # 打包好的 .skill 安裝檔
    ├── vcf-base.skill
    ├── vcf-semiconductor.skill
    ├── vcf-financial.skill
    ├── vcf-telecom.skill
    ├── vcf-hybrid-cloud.skill
    ├── vcf-ai.skill
    ├── vcf-edge.skill
    ├── vcf-cxs.skill
    ├── vcf-ebc.skill
    ├── vcf-summary.skill
    ├── vcf-whats-new.skill
    └── vcf-project-status.skill
```

## 使用方式

下載 `skills-pkg/` 下的 `.skill` 檔，安裝到 Claude 後即可使用。

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
