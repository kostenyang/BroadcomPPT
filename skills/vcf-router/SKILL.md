---
name: vcf-router
description: VCF / Broadcom 交付物「分流總機」(router)。使用者的 skill 庫中有多個重複與觸發重疊的 vcf-* 簡報 skills — 本 skill 負責裁決該用哪一個、怎麼組合，不產出任何檔案。只要使用者要做任何 VCF / VMware / Broadcom 相關的簡報、deck、提案、估算、專案文件，就先讀本 skill 再選定目標 skill — 即使需求看起來已經明確命中某個 skill 也一樣，因為多個 skills 的觸發條件互相重疊（例如升級簡報、EBC、summary、產業別簡報都可能同時匹配）。尤其當需求同時涉及「產業客戶 + 技術主題」（如：銀行的升級簡報）、或用詞模糊（「幫我做個 VCF 簡報」）時，一定先經過本 skill 裁決。本 skill 不修改、不取代任何現有 skill。
---

# VCF Skill Router（分流總機）

這個 skill 庫是同一位使用者長期累積的，存在**兩組平行複本**與多處**觸發重疊**。
本 skill 的工作：先裁決路由，再讓目標 skill 做事。**本 skill 自己不產出任何檔案。**

裁決完成後：讀取目標 skill 的 SKILL.md 並照其執行。若需要組合多個 skills，按「組合規則」一節處理。

---

## 第 0 步：正名表（重複組裁決）

以下每對 skills 內容完全相同（僅名稱與內部交叉引用不同）。**一律使用左欄的正名版**；
只有在正名版不存在或無法讀取時，才改用右欄別名版（兩者可互換，內容一致）：

| ✅ 正名（使用這個） | ❌ 別名（不要主動選它） | 用途 |
|---|---|---|
| `vcf-base` | `broadcom-ppt-base` | 共用範本知識（顏色/字型/底版） |
| `vcf-upgrade` | `vcf-91-ppt` | 9.1 升級路徑簡報 |
| `vcf-ebc` | `vcf9-ebc-deck` | 52-slide EBC 高階簡報 |
| `vcf-summary` | `vcf9-summary` | 24-slide 概覽簡報 |
| `vcf-cxs` | `cxs-success-stories` | 原廠服務團隊 + 成功案例 |

注意：正名版的 SKILL.md 內部若引用 `vcf-base`，別名版內部引用 `broadcom-ppt-base` — 跟著所選版本的內部引用走即可，不要混用兩個家族的引用。

---

## 第 1 步：交付物類型分流

先看使用者要的**東西**是什麼，不是主題是什麼：

| 使用者要的 | 目標 skill |
|---|---|
| 簡報 / deck / slides / 提案投影片 | → 第 2 步簡報選型 |
| 人天 / 工時估算（Excel，無日期） | `manday-estimate` |
| 專案時程 / 甘特圖 / WBS（Excel，有日期） | `wbs-gantt` |
| 單頁專案狀態（1 頁 PPT、RAG 燈號） | `vcf-project-status` |
| 安裝/升級案交付文件：前置檢查表、HLD/LLD 設計書、安裝手冊、測試驗收/UAT、SOP/維運手冊、竣工 As-Built、升級計畫/Gap 分析 | `vcf-delivery-docs`（以官方 PSO delivery kit 為底） |
| 一般 Word / PDF / Excel（非 VCF 情境） | `docx` / `pdf` / `xlsx` |

「估人天**順便**排時程」= 兩個交付物 = `manday-estimate` + `wbs-gantt` 各做一份，不要硬塞進同一張表。

---

## 第 2 步：簡報選型決策樹

依序問三個問題：

**Q1 — 聽眾與深度？**

| 情境 | 目標 skill |
|---|---|
| CIO / 高階主管、完整價值論述、EBC、whiteboard | `vcf-ebc`（52p） |
| 30 分鐘快速介紹、概覽、入門 | `vcf-summary`（24p） |
| L200 新功能介紹 / What's New / Tech Tuesday | `vcf-whats-new` |
| L300 技術 deep-dive（依主題見 Q2） | 主題 skill |
| 大範圍技術總覽、要從官方 150 頁挑章節、Plum 配色雙語 | `vcf-tech-deck:vcf-tech-deck`（plugin） |
| 原廠服務 / PSO 提案 / 客戶成功案例 | `vcf-cxs` |

**Q2 — 技術主題？**（deep-dive 或主題明確時）

| 主題 | 目標 skill |
|---|---|
| 升級路徑、5.2→9.1、vSphere 轉 VCF、converge/import | `vcf-upgrade` |
| VCF Automation / VCFA / 自助消費層 | `vcf-automation` |
| Private AI / GPU / VKS / NVIDIA | `vcf-ai` |
| 邊緣 / 門市 / 工廠 / ROBO / edge AI | `vcf-edge` |
| 混合雲 / GCVE / AVS / HCX 跨雲 / 多站點 | `vcf-hybrid-cloud` |

**Q3 — 產業客戶？**（一律以通用產業別處理，不針對特定客戶名稱路由）

| 產業 | 目標 skill |
|---|---|
| 銀行 / 證券 / 保險 / 金融 | `vcf-financial` |
| 電信 / ISP / VCSP / 5G | `vcf-telecom` |
| 半導體 / 晶圓 / IC 設計 | `vcf-semiconductor` |
| 製造 / 工廠 / MES / OT | 廠務 IT/MES 域隔離 → `vcf-semiconductor`；分散式廠區/邊緣站點 → `vcf-edge` |

---

## 組合規則：產業 × 主題同時命中

最常見的衝突：「幫金融業客戶做一份 VCF 升級簡報」同時命中 `vcf-financial` 和 `vcf-upgrade`。
（半導體客戶的 AI 簡報、電信客戶的 Automation 簡報⋯⋯同理。）

裁決原則：**主題決定骨架，產業決定內容**。

1. **主 skill = 主題/深度 skill**（決定底版與章節結構）。上例中骨架用 `vcf-upgrade` 的 APJ 範本。
2. **副 skill = 產業 skill**，只讀取其 Industry Context / 法規 / 客戶痛點段落，把產業情境（如金融的法遵與 DR、半導體的 OT/IT 隔離、電信的多租戶）織進主 skill 的投影片裡。不要用副 skill 的底版。簡報內容保持通用產業寫法，除非使用者明確給了客戶名稱才帶入。
3. 若使用者**只給產業沒給主題**（「幫金融客戶做一份 VCF 簡報」）→ 產業 skill 就是主 skill。
4. 成功案例章節一律可搭 `vcf-cxs` 補強。

為什麼這樣分：主題 skills 各自綁定不同官方底版（升級=APJ、What's New=Tech Tuesday、Automation=WOE），底版選錯整份要重做；產業內容是文字層，織入任何底版都成立。

---

## Skill ↔ Git 底版對應

每個簡報 skill 綁定 GitHub repo（`github.com/kostenyang/BroadcomPPT`）中的官方底版檔。
**路由只選 skill，永遠不改底版對應** — 底版下載與細節以目標 skill 的 SKILL.md 為準：

| Skill | 綁定底版 |
|---|---|
| `vcf-upgrade` | `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx`（固定） |
| `vcf-whats-new` | `TECH_TUESDAY_Whats_New_with_vSphere_in_VCF_9_1.pptx`（固定） |
| `vcf-automation` | `Q3WOE021_-_VCF_9_1_Automation_Technical_Deep_Dive.pptx`（固定） |
| `vcf-ebc` | `VCF9 - EBC and Customer Deck.pptx`（52p） |
| `vcf-summary` | `VMware Cloud Foundation - VCF9 - Summary_Final.pptx`（24p） |
| `vcf-cxs` | `BOT - 原廠專業技術支援服務團隊與客戶成功案例分享_20241022_V9.0.pptx` |
| `vcf-edge` | `VCF_Edge_Customer_Presentation.pptx`（42p） |
| 產業/主題通用（financial / telecom / semiconductor / hybrid-cloud / ai） | 預設 `Getting_Started_with_VCF_9_1__Upgrade_Paths__and_What_to_Expect.pptx`（白底 2.4MB） |
| `vcf-tech-deck:vcf-tech-deck` | plugin 內建 150-slide General Overview Tech Deck |

---

## 易混淆對照（quick reference）

- 「新功能介紹」vs「升級規劃」：講**功能有什麼** → `vcf-whats-new`；講**怎麼升上去** → `vcf-upgrade`。
- 「概覽」vs「EBC」：時間短/入門 → `vcf-summary`；高階決策者/完整價值論述 → `vcf-ebc`。
- 「甘特圖」vs「單頁狀態」：Excel 排程追蹤 → `wbs-gantt`；1 頁 PPT 匯報 → `vcf-project-status`。
- 「估人天」vs「排時程」：只要工作量 → `manday-estimate`；要日期與進度 → `wbs-gantt`。
- 「升級**簡報**」vs「升級**計畫書/文件**」：給人看的投影片 → `vcf-upgrade`；正式交付的 Word/Excel 文件 → `vcf-delivery-docs`。
- AI 主題但在邊緣場域（門市推論、工廠 edge GPU）→ `vcf-edge` 為主，`vcf-ai` 補內容。

---

## 輸出習慣

裁決後，用一句話向使用者確認路由再動工，例如：
「這份我會用 `vcf-upgrade` 的 APJ 範本做骨架，並帶入 `vcf-financial` 的金融法規內容 — 開始做。」
需求明確時不必等回覆，講清楚即可直接進行。
