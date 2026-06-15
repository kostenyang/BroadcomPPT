---
name: vcf-project-status
description: |
  製作「單頁專案狀態報告」(Project 1-Page Status / One-Pager) 的通用 skill，輸出為 1 頁 PowerPoint 投影片。適用於任何 VCF / VMware / 基礎架構導入、升級、遷移專案的週報 / 月報 / 治理會議 / 高管匯報。一頁涵蓋：專案名稱與基本資訊、整體健康度 (RAG 紅黃綠燈)、進度百分比、里程碑時間軸、本期完成 (Accomplishments)、下期計畫 (Next Steps)、風險與議題 (Risks / Issues)、範圍與資源 / 預算狀態。當使用者要做「專案狀態」「專案一頁報告」「one page status」「status report」「週報 / 月報投影片」「專案儀表板單頁」「RAG status」「給高管的專案進度單頁」時觸發；不限定特定客戶或專案。需要做特定客戶整套故事 deck 時改用對應客戶 / 主題 skill (例如 vcf-foxconn)；需要完整甘特圖 Excel 時改用 wbs-gantt skill。一律套用 Broadcom 範本配色與字型，輸出單張投影片。
---

# VCF Project 1-Page Status (單頁專案狀態報告)

通用的「單頁專案狀態」投影片產生器。把一個專案的狀態濃縮到 **1 頁 PPTX**，
給專案週報 / 月報 / 治理會議 / 高管匯報使用。**不綁定特定客戶或專案**。

> ⚡ 編輯前先讀 `anthropic-skills:vcf-base` 取得 Broadcom 範本配色、字型、版面規格，
> 讓單頁狀態與其他 VCF 簡報視覺一致。實際做 / 改投影片用 `anthropic-skills:pptx` skill。

## 使用時機

- 專案週報 / 月報 / 雙週報的「一頁狀態」投影片
- 治理會議 (Steering Committee) / 高管 (Executive) 進度匯報單頁
- RAG (紅黃綠燈) 健康度狀態頁、專案儀表板單頁
- VCF / vSphere / NSX / vSAN / HCX 導入、升級、遷移專案的進度單頁

> 要做特定客戶整套故事 deck → 用對應 skill（如 `vcf-foxconn`）。
> 要做含日期排程、自動進度的甘特圖 Excel → 用 `wbs-gantt` skill。
> 要做人天估算 → 用 `manday-estimate` skill。

## 單頁版面 — 8 個固定區塊

一頁狀態報告建議固定包含以下區塊（缺資料時向使用者詢問，勿留 placeholder）：

| # | 區塊 | 內容 |
|---|------|------|
| 1 | **抬頭 (Header)** | 專案名稱、客戶 / 單位、PM / Owner、報告日期、報告期間 |
| 2 | **整體健康度 (Overall RAG)** | 🟢 On Track / 🟡 At Risk / 🔴 Off Track，一句話總評 |
| 3 | **進度 (Progress)** | 整體完成 %、本期 vs 計畫、目前階段 (Phase) |
| 4 | **里程碑 (Milestones)** | 3–6 個關鍵里程碑 + 日期 + 狀態 (✅完成 / ⏳進行 / ⬜未開始) |
| 5 | **本期完成 (Accomplishments)** | 本期 3–5 條重點成果 |
| 6 | **下期計畫 (Next Steps)** | 下期 3–5 條預計工作 |
| 7 | **風險與議題 (Risks / Issues)** | 各 2–3 條，含 owner / 對策 / 嚴重度 |
| 8 | **範圍 / 資源 / 預算 (Scope / Budget)** | 範圍變更、資源 / 人天、預算燒錄 (選填) |

### RAG 燈號慣例（沿用 Broadcom 配色，詳見 vcf-base）

| 燈號 | 意義 | 建議色 |
|------|------|--------|
| 🟢 Green | On Track — 進度 / 範圍 / 預算皆在控 | `#3BA55D` |
| 🟡 Amber | At Risk — 有風險但有對策 | `#E3A008` |
| 🔴 Red | Off Track — 需升級處理 / 決策 | `#D64545` |

## 建議版面配置 (16:9 單頁)

```
┌───────────────────────────────────────────────────────────┐
│ [專案名稱]        客戶 | PM | 期間 | 日期      [● RAG 大燈號]│  ← Header
├───────────────────────────┬───────────────────────────────┤
│ 進度 NN%  目前階段: Phase X │  里程碑 Milestones            │
│ ▓▓▓▓▓▓▓▓░░░░  本期 vs 計畫  │  ✅ M1 …  ⏳ M2 …  ⬜ M3 …      │
├───────────────────────────┼───────────────────────────────┤
│ 本期完成 Accomplishments    │  下期計畫 Next Steps           │
│ • …  • …  • …               │  • …  • …  • …                 │
├───────────────────────────┴───────────────────────────────┤
│ 風險/議題 Risks & Issues (含 owner/對策)  | 範圍/資源/預算   │  ← 底列
└───────────────────────────────────────────────────────────┘
```

左欄放量化（進度、完成、風險），右欄放時間軸（里程碑、下期），大 RAG 燈號放右上最醒目處。

## 製作流程

1. 讀 `anthropic-skills:vcf-base` 取得配色 / 字型 / 版面規格。
2. 向使用者蒐集 8 區塊缺少的資料（健康度、進度 %、里程碑日期、風險 owner…），**不要自行編造數字**。
3. 用 `anthropic-skills:pptx` skill 產生 **單張** 16:9 投影片：
   - 有底版範本 → unpack 既有 Broadcom 範本，保留一頁，填入狀態區塊。
   - 無範本 → 依上方版面用 pptx 建立單頁，套 Broadcom 配色 / 字型。
4. 視覺 QA：轉圖 + subagent 檢查重疊 / 溢出 / 對齊 / 對比（見 pptx skill QA 段落）。
5. 交付單頁 PPTX；要連續追蹤多期時，每期另存加版號 / 日期，**不要覆蓋舊報告**。

詳細欄位定義與填寫範例見 `references/one-page-status-spec.md`。
