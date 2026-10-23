---
name: vcf-base
description: Core Broadcom/VMware by Broadcom PowerPoint template knowledge — the shared base for every VCF presentation skill. Default base deck is the Tech Tuesday vSAN in VCF 9.1 template (140 layouts, Plum, diagram-led). Contains the donor-slide map, layout resolution rules, the three-layer color system, font/embedding rules, deck structure, and the clone-slide editing workflow.
---

# Broadcom PPT Base — 所有 VCF 簡報的共用底版知識

這份是所有 `vcf-*` 簡報 skill 的共用基礎。做任何 Broadcom / VCF 簡報時，
**先讀這份，再讀該情境的垂直 skill**（financial / telecom / semiconductor / ai / edge / ebc / summary / whats-new / cxs / project-status）。

---

## ⚡ 預設底版

> **所有 VCF 簡報一律以 `TECH_TUESDAY_Whats_New_with_vSAN_in_VCF_9_1.pptx` 為底版開始。**
> 絕不從空白 pptx 或 python-pptx 從零建立。

| 優先順序 | Template | File | Size | 說明 |
|---------|----------|------|------|------|
| ✅ **預設 (Default)** | **Tech Tuesday — vSAN in VCF 9.1** | `TECH_TUESDAY_Whats_New_with_vSAN_in_VCF_9_1.pptx` | 12.2MB | **所有情境的預設底版**。30 頁、140 版型、雙 master、內嵌字型、Plum 視覺、diagram-led |
| 🔁 備用 | Tech Tuesday — vSphere in VCF 9.1 | `TECH_TUESDAY_Whats_New_with_vSphere_in_VCF_9_1.pptx` | 8.5MB | 需要大量 **icon 列**（Three/Four/Five Icon - Fancy）與 **DEMO 深底頁**時 |
| 🔁 備用 | VCF 9.1 Getting Started | `Getting_Started_with_VCF_9_1__Upgrade_Paths__and_What_to_Expect.pptx` | 2.4MB | 只要極輕量白底、不需要官方美術時 |
| 🔁 備用 | APJ Upgrade Pathways to VCF 9.1 | `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` | 3.8MB | 升級路徑詳細場景 → 走 `vcf-upgrade` |
| 🔁 僅指名時 | VCF 5.2 Master Technical | `VCF_5_2_Master_Technical_-_BC04.pptx` | 97MB | 使用者明確指定 5.2 世代時 |

取得方式（擇一）：

```bash
# 1) session 內已上傳
ls /mnt/user-data/uploads/TECH_TUESDAY_Whats_New_with_vSAN_in_VCF_9_1.pptx

# 2) 從 GitHub 抓（檔名有底線，URL 直接用）
curl -fsSLo base.pptx \
  https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/TECH_TUESDAY_Whats_New_with_vSAN_in_VCF_9_1.pptx
```

### 為什麼是這一份當預設

| 理由 | 具體內容 |
|------|---------|
| 版型最全 | 雙 master 共 **140 個版型**（M1 98 + M2 42），涵蓋封面 / 主題式 section / icon 列 / 四象限 / QR / Important / Screenshot / 免責頁 |
| 字型自帶 | 已內嵌 **Metropolis、Metropolis Light、Arial Rounded MT Bold**（`ppt/fonts/*.fntdata`），別台電腦開也不跑版 |
| 美術可直接複製 | 30 頁裡有 **16 頁成品級架構圖**（78 個 SVG + 76 個 PNG，10MB 媒體），是最好用的 donor 素材庫 |
| 結構完整 | 封面 → PowerPoint 警語 → 免責 → 總覽 → 4 章 → 收尾大字 → Thank You，一份 deck 該有的頁全在 |
| 語意色齊 | Plum 骨架 + 官方 extended palette，四章輪色不必自己配 |

---

## ⚠️ 三條不可違反的規則

1. **複製整頁換字，不要重畫。**
   一張官方內容頁 XML 約 293,000 字元、純文字只有約 950 —— 差 310 倍。
   複製整頁 = 用 1/300 的成本拿到 100% 官方美術。用 `scripts/clone-slide.py`。
2. **Layout 用「名稱」解析，永遠不要用編號。**
   `slideLayoutNN.xml` 的編號是每份 deck 各自的（`slideLayout92` 在 vSphere Tech Tuesday 是
   `Section Header 2 - VCF 9`，在 vSAN Tech Tuesday 是 `Section - Availability`）。
   查 `references/layout-map.md`，不要開檔掃 140 個 layout。
3. **挑 donor 頁要挑「圖已經對」的那一頁。**
   clone 只換 placeholder 文字，圖不會跟著標題改。
   拿壓縮示意圖的頁去講授權 = 圖文不符。donor 對照見 `references/donor-slides.md`。

---

## 預設底版規格

| 項目 | 值 |
|------|-----|
| 檔案 | `TECH_TUESDAY_Whats_New_with_vSAN_in_VCF_9_1.pptx` |
| 頁數 | 30 |
| 尺寸 | 16:9 — 12188825 × 6858000 EMU（13.33 × 7.5 in） |
| Master | M1 `VMware 2025 Light` (98 layouts) / M2 `VMware-dark` (42 layouts) |
| 內文字型 | Arial（theme）；內嵌 Metropolis / Metropolis Light / Arial Rounded MT Bold |
| 繁中字型 | 微軟正黑體 Microsoft JhengHei（theme 已把 Hant script 指過去） |
| 預設底色 | 白 `#FFFFFF` |
| 主視覺 | Plum `#6C4B94` |
| Footer | `vmware by Broadcom` |

---

## Donor-Slide Map（**做 deck 時第一個看的表**）

要哪種頁，就 clone 底版的哪一頁。完整版見 `references/donor-slides.md`。

| 你要做的頁 | clone 底版第幾頁 | 版型 | 可填欄位 |
|-----------|----------------|------|---------|
| **封面** | 1 | `Title Slide – Plum with Circle` | `title` / `subTitle:10` / `body:11` 講者 / `body:12` 部門 / `body:14` 日期 |
| PowerPoint-only 警語 | 2 | `Actually Blank` | （不改）|
| 免責 / About This Presentation | 3 | `Blank` | （文字為非 placeholder，需手改）|
| **四象限總覽**（What's New 全景）| 4 | `Title Only` | `title` + 4 組標題/清單文字方塊 |
| **章節分隔** | 5 / 11 / 15 / 22 | `Section Header – Plum` | `title` / `subTitle:10` |
| **架構圖頁（左圖右文）← 主力** | 6–10, 12, 14, 16–17, 19–20, 23–25, 29–30 | `Diagram with Content on Right` | `title` / `subTitle:10` / `body:17`（右欄 bullets）|
| **雙成果對照頁** | 18 | `Diagram with Outcome, Benefit` | `title` / `subTitle:10` / `body:17`+`body:20` 左組 / `body:19`+`body:21` 右組 |
| **三欄純文字頁**（無圖）| 13 / 21 / 26 | `Title, Subtitle and Content` | `title` / `subTitle:10` |
| 收尾大字 | 27 | `Blank` | （文字為非 placeholder）|
| **Thank You** | 28 | `Thank You / Closing - Plum` | （不改）|

> **主力版型是 `Diagram with Content on Right`** — 底版 30 頁裡佔 16 頁。
> 這是這份範本跟 vSphere Tech Tuesday（icon-led）最大的差別：**vSAN 這份是 diagram-led**。
> 幾何固定：title `L0.6 T0.5 W12.0 H0.4`、subtitle `L0.6 T0.9 W12.0 H0.3`、
> 右欄 body `L9.2 T1.8 W4.2 H5.0`，左側 `0.6–9.0 in` 全部留給圖。

---

## 內容頁三層文字模型

每張功能頁固定這個結構，照抄：

```
┌─ Title = Benefit Headline（客戶得到什麼好處，不是功能名）───────────┐
│  "Reduce Storage Costs with Lower Hardware Requirements for vSAN"  │
├─ Subtitle = Feature Name（產品/功能的正式名稱）────────────────────┤
│  "Lower hardware requirements for your vSAN powered VCF environment"│
├─ Body = 3–5 個 capability bullets（右欄）─────────────────────────┤
│  • Three profiles (small, medium & large)                          │
│  • Reduced TCO and design complexity                               │
└────────────────────────────────────────────────────────────────────┘
```

- **Title 講價值，Subtitle 才講功能名。** 反過來寫是最常見的錯。
- Bullets **3–5 個**；超過 5 個拆兩頁，不要塞。
- 需要「兩種成果並排」用 `Diagram with Outcome, Benefit`（底版第 18 頁）。

---

## 標準 Deck 結構

底版第 1–28 頁本身就是官方認證的骨架，直接沿用：

1. **封面**（`Title Slide – Plum with Circle`）— 主題 + 副標 + 講者 + 部門 + 日期
2. **PowerPoint-only 警語**（`Actually Blank`）— 內部版保留，對外版刪
3. **About This Presentation / 免責**（`Blank`）— 內部版保留，對外版刪
4. **總覽**（`Title Only` 四象限）— 4 大主題 × 每組 3–4 條 highlight，對應後面 4 章
5. **章節 1** section divider + 內容頁 3–6 張
6. **章節 2 / 3 / 4** 同上
7. **收尾大字**（`Blank`）— 一句話的價值主張
8. **Thank You**（`Thank You / Closing - Plum`）
9. （選用）**附錄** — 底版 29–30 頁後面

> 章節數建議 **3–4 章**、每章 3–6 張內容頁，全長 20–30 頁。
> 客製時：先換封面標題/講者/日期 → 用 `clone-slide.py keep` 砍掉不相關頁 → 再 clone 需要的 donor 頁。

---

## 配色（**避免單調 — 這是最常見的產出問題**）

只用 accent1 teal 會讓整份 deck 灰撲撲的。官方 deck 實際是**三層**在用色：

| 層 | 色 | 角色 |
|----|----|------|
| **骨架層** | theme accent1–6 | 封面 / section / 細色條 / icon 圈 — 決定「這一章是什麼顏色」 |
| **內容層** | 下面的 extended palette | 架構圖裡的元件、狀態、資料分類 — 決定「圖裡有幾種東西」 |
| **結構層** | `#717074` 灰、`#F2F2F2` / `#E8F0F4` 淺底 | 線條、分隔、襯底 — **不參與配色**，只負責讀得懂 |

### Theme accent（`VMware 2025 Light`，白底頁用）

| Role | Hex | Usage |
|------|-----|-------|
| Teal (accent1) | `#007B8C` | 主要重點、icon |
| Ocean Blue (accent2) | `#005C8A` | 次要、連結 |
| Sky Blue (accent3) | `#0098C7` | 輔助色、icon |
| Green (accent4) | `#61A60E` | 正向 / 新增 / 打勾 |
| **Plum (accent5)** | `#6C4B94` | **本底版主視覺** — 封面 / section / 收尾 |
| Gold (accent6) | `#F3BA16` | callout、CRITICAL 標籤 |
| Dark Navy (dk2) | `#1B1D36` | 深底頁背景 |
| Light (lt2) | `#EEEEEE` | 淺底區塊 |

### 深底頁（`VMware-dark` master）**不要沿用淺底 accent**（對比不足）

accent1 `#0088EF`、accent2 `#01B9C6`、accent3 `#0098C7`、accent4 `#61A60E`、accent5 `#A468EE`、accent6 `#F3BA16`

### Extended Palette（官方架構圖實際用色）

| Hex | 名稱 | 典型用途 |
|-----|------|---------|
| `#78BE20` | Bright Green | 新增 / 啟用 / 正向結果、資料節點 |
| `#316E60` | Deep Teal | 儲存層、持久化元件 |
| `#0091A0` | Teal Cyan | 服務層、中介元件 |
| `#0095D3` | Bright Blue | 網路 / 傳輸路徑 |
| `#1D428A` | Royal Blue | 管理平面、控制元件 |
| `#002142` | Midnight Navy | 深底區塊、外框容器 |
| `#A68CC2` | Lavender | 第二資料分類（與 Plum 同家族，圖裡好區分）|
| `#E68C28` | Orange | 注意 / 變更中 / 遷移中 |
| `#D58B3F` | Tan | Orange 的低彩度版，大面積填充用 |
| `#EC7700` | Vivid Orange | 單點強調（少量）|
| `#A6192E` | Crimson | 風險 / 不支援 / 舊架構 |
| `#CC092F` | Red | 錯誤 / 中斷（最少量）|
| `#79051B` | Deep Red | 紅底區塊 |
| `#E8F0F4` | Pale Blue Tint | 圖內分區襯底 |

**架構圖線條 / 元件框線固定用 `#717074`**（Broadcom 圖示灰），不要用純黑。

### 三條硬規則

1. **每一章換一個 accent** — section divider、該章內容頁細色條、icon 圈全部跟著該章的色走。
   底版是全 Plum；做多章 deck 時改配 **Plum → Teal → Sky Blue → Green**，一份 deck 至少四種主色。
2. **架構圖每頁 3–5 個彩色**，用來分類元件（運算 / 儲存 / 網路 / 管理），不是裝飾。
   同一種東西在不同頁用同一個色 — **跨頁一致比單頁好看重要**。
3. **語意色不可挪用**：綠=正向/新增、橘=注意/變更、紅=風險/不支援、灰=既有/背景。
   紅橘只做語意，不要拿來當分類色。

### 不要做的事

- ❌ 整份 deck 只有一種色 + 灰
- ❌ 單頁超過 6 個彩色（分類失效，變成色票展示）
- ❌ 深底頁沿用淺底 accent（見上面 dark 色盤）
- ❌ 用 extended palette 去塗標題文字或細色條（那是骨架層的事，只用 theme accent）
- ❌ 自己調 hex — 要新色就從上表挑
- ❌ 米色、米黃、淺橘等暖色背景（`#FAF0E6` / `#FFF8E1` / `#F5F5DC`）

---

## 字型

| Template | Heading | Body |
|----------|---------|------|
| **Tech Tuesday（預設底版）** | Arial（theme）+ 內嵌 Metropolis / Metropolis Light / Arial Rounded MT Bold | Arial |
| VCF 5.2 Master | Metropolis / Camphor Std | Arial |
| APJ 9.1 Upgrade | NTR | Arial |

- 改檔時**不要刪** `ppt/fonts/*.fntdata` 與 `presentation.xml` 的 `<p:embeddedFont>` — 刪了別台電腦就跑版。
- 繁中一律 **微軟正黑體 (Microsoft JhengHei)**。
- **絕不用 Google Slides 開** — 字型、間距、版型全毀（底版第 2 頁就是在講這件事）。

---

## Layout 解析規則

編號是每份 deck 各自的，**永遠用名稱查** `references/layout-map.md`。
若要現場產生對照表：

```bash
for f in unpacked/ppt/slideLayouts/slideLayout*.xml; do
  printf '%s | %s\n' "$(basename $f)" \
    "$(sed -n 's/.*<p:cSld[^>]*name="\([^"]*\)".*/\1/p' $f | head -1)"
done | sort -t'|' -k2
```

多 master 的範本要確認 slide 掛在哪個 master（`ppt/slides/_rels/*.rels` → layout → master），
否則同名版型會套到錯的 theme 色。

### 底版可用版型（依用途，名稱查表）

- **封面 / 結尾**：`Title Slide – Leaf/Aqua/Plum`（+ `with Circle`）、`VCF-light-title-a`、
  `vcf-title-a` / `VCF-title-b`、`vcf-close-a` / `vcf-close-b` / `vcf-med-close-a`、
  `Thank You / Closing - Leaf/Aqua/Plum`
- **主題式 section divider**（不必改字，直接挑主題）：
  `Section - Storage` / `Section - Networking` / `Section - VKS` / `Section - DPU` / `Section - AI` /
  `Section - Lifecycle` / `Section - Workloads` / `Section - Resource Mgmt` / `Section - Availability` /
  `Section - Developer` / `Section - Wrap Up`
- **通用 section**：`Section Header – Leaf/Aqua/Plum`、`Section Header – Photo`、`Section Header - Big Photo`
- **圖文頁**：`Diagram with Content on Right`（主力）、`Diagram with Outcome, Benefit`
- **文字頁**：`Title, Subtitle and Content`、`Title and Subtitle`、`Title Only`、
  `Two-Content Balanced`（+ `Color on Left/Right`）、`Comparison`、`Three-Content Comparison`
- **icon 列**：`Three/Four/Five Icon`、`Three/Four/Five Icon - Fancy`（+ `- RBLF`）、
  `Three Icon - Horizontal - Green/Teal`、`Four Square 1`、`Five Numbered`
- **強調頁**：`Big Statement - Leaf/Aqua/Plum`、`Big Statement 2 - *`、`Big Statement with Photo`、
  `Big Statement with Icon - Indigo/Ocean/Plum`、`Big Statistic`、`Quote – *`、`Definition`
- **功能頁**：`Chart`、`Screenshot`、`QR`（+ `- RBLF`）、`Q&A`、`Additional Resources`、
  `Important`（+ `- RBLF` / `- Red`）、`Customer Success`、`Agenda`
- **免責 / 警語**：`Blank`、`Actually Blank`、`Disclaimer - Regulatory`、`Disclaimer - RevRec`

> **RBLF** = Right Body Left Footer：icon 列 + 右側補充說明，適合每個 icon 要展開 1–2 句時。

---

## 編輯工作流程

### 首選：clone-slide.py（複製整頁換字）

```bash
> ⚠️ **順序：先 clone、後 keep。** `clone` 是在同一檔案內複製第 N 頁到最後，
> 先 `keep` 砍掉 donor 頁就再也 clone 不到它了。

```bash
# 1) 先看範本有哪些頁、什麼版型、有哪些欄位可填（最便宜，一定先做）
python3 scripts/clone-slide.py list base.pptx
python3 scripts/clone-slide.py list base.pptx --slide 6

cp base.pptx deck.pptx           # 永遠不要改原始範本

# 2) 在完整 30 頁底版上 clone donor 頁，新頁接在最後（31, 32, ...）
python3 scripts/clone-slide.py clone deck.pptx --slide 8 --out deck.pptx \
    --title "Reduce Storage Costs with Lower Hardware Requirements" \
    --subtitle "Lower hardware requirements for your vSAN powered VCF environment" \
    --bullets "三種 ReadyNode profile|降低 TCO 與設計複雜度|涵蓋 HCI / storage / cyber recovery"
# → 印出「新頁在第 31 頁」，記下來

# 3) 一次指定最終順序（骨架 + 新做的頁）
python3 scripts/clone-slide.py keep deck.pptx --slides 1,4,5,31,28 --out final.pptx

# 4) 換封面文字
python3 scripts/clone-slide.py settext final.pptx --slide 1 --out final.pptx \
    --title "VCF 9.1 技術簡報" --set 'body:14=2026 年 8 月'
```

已知限制（誠實說明）：

- 只換 **placeholder** 文字。圖裡的文字方塊不是 placeholder，不會被動到 —— 那正是要的（美術原封不動），
  但也代表**圖不會跟著新標題改**，所以 donor 頁要挑「圖已經對」的。
- **不支援 markdown**：寫 `**粗體**` 會原樣印出星號。局部粗體請在 PowerPoint 手動處理。
- 段落格式沿用原頁第一段的 `pPr`。

### 次選：unpack / pack XML（只在 clone 做不到時，例如要動 master 或圖形本身）

```bash
cp base.pptx work.pptx                      # 永遠不要改原始範本
python3 /mnt/skills/public/pptx/scripts/office/unpack.py work.pptx unpacked/
# 改 unpacked/ppt/slides/*.xml
python3 /mnt/skills/public/pptx/scripts/office/pack.py unpacked/ out.pptx
```

詳見 `/mnt/skills/public/pptx/editing.md`。

### QA（每次產出都要做）

```bash
soffice --headless --convert-to pdf --outdir qa out.pptx
pdftoppm -png -r 70 -f 4 -l 4 qa/out.pdf qa/slide    # 只渲染要看的那幾頁
```

檢查：字有沒有溢出框、圖文是否相符、章節色是否一致、footer 是否還在。

---

## VCF 9.x 產品命名

| 舊名 | VCF 9.x 正式名 |
|------|---------------|
| VMware Aria Operations | VCF Operations |
| VMware Aria Automation | VCF Automation |
| VMware Aria Operations for Networks | VCF Operations for Networks |
| VMware Aria Operations for Logs | VCF Operations for Logs |
| vSphere with Tanzu / TKG | VKS (vSphere Kubernetes Service) |
| NSX-T | NSX |
| VCDA (Cloud Director Availability) | Live Recovery |
| vDefend Firewall | vDefend |
| SDDC Manager | SDDC Manager（不變）|

VCF 5.2 世代的 deck 才用 5.x 舊名（Aria Operations / Aria Automation…）。

---

## 升級路徑頁慣例

- **Current State（左）→ Upgrade Path（箭頭）→ Future State（右）**
- 附最低支援版本表
- 新元件的 IP / DNS 需求
- 不支援的情境用紅 / 金色 callout 明確標出

常見情境：vSphere 8.x → VCF 9.1、VCF 5.2 → VCF 9.1、Aria Operations 8.18.x → VCF Operations 9.1

---

## 中英雙語（台灣客戶）

- 投影片標題：**英文為主**，中文副標選用
- 架構圖：英文標籤 + 中文註解寫在 speaker notes
- Section header：英文
- Speaker notes：內部簡報用中文，conclusion-first，英文技術名詞 + 中文敘述

---

## ⚠️ 對內 / 對外版本

底版第 2、3 頁是 Broadcom 內部聲明（PowerPoint-only 警語 + Do Not Distribute）。

- **對外**（客戶 / VMUG / Explore）：刪掉第 2、3 頁，**移除 speaker notes**，交付 PDF
- **對內** enablement：保留免責頁與 speaker notes
- **客製給特定客戶**：先換封面標題 / 講者 / 日期，再刪不相關功能頁

---

## Token / 成本最佳化

- **內容草稿與檔案生成分開**：先在對話確認所有頁的文字，再一次生成 .pptx
- 大型 deck（>20 頁）分多輪產出
- **Front-load 需求**：一開始就問清楚章節、要哪些功能頁、對內或對外、多長
- 模板型 deck 用標準 chat + `vcf-*` skill

---

## 參考檔

| 檔案 | 用途 |
|------|------|
| `references/donor-slides.md` | 預設底版 30 頁的 donor 對照 — 每頁的圖畫什麼、適合改成什麼、可填欄位 |
| `references/layout-map.md` | 兩份 Tech Tuesday 範本全部 268 個版型的「名稱 → 檔案 → master → 幾何」對照 |
| `scripts/clone-slide.py` | 複製整頁換字（`list` / `clone` / `settext` / `keep`）|
| `scripts/gen-layout-map.py` | 範本換版時重跑，重建 layout-map.md |
