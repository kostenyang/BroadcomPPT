# Donor-Slide Map — 預設底版 `TECH_TUESDAY_Whats_New_with_vSAN_in_VCF_9_1.pptx`

> **用途**：做 deck 時「要哪種頁就 clone 哪一頁」的對照表。
>
> `clone-slide.py` 只換 **placeholder 文字**，頁面上的圖與圖內文字方塊**不會被動到** ——
> 那正是要的（官方美術原封不動），但也代表**圖不會跟著你的新標題改**。
> 所以挑 donor 的唯一標準是：**這張圖畫的東西，跟我要講的事是不是同一類。**
>
> 欄位代號取自 `clone-slide.py list base.pptx --slide N` 的輸出。

---

## 版型分佈（30 頁）

| 版型 | 頁數 | 頁碼 |
|------|-----:|------|
| `Diagram with Content on Right` | 16 | 6–10, 12, 14, 16, 17, 19, 20, 23, 24, 25, 29, 30 |
| `Section Header – Plum` | 4 | 5, 11, 15, 22 |
| `Title, Subtitle and Content` | 3 | 13, 21, 26 |
| `Blank` | 2 | 3, 27 |
| `Title Slide – Plum with Circle` | 1 | 1 |
| `Actually Blank` | 1 | 2 |
| `Title Only` | 1 | 4 |
| `Diagram with Outcome, Benefit` | 1 | 18 |
| `Thank You / Closing - Plum` | 1 | 28 |

**主力是 `Diagram with Content on Right`（16/30）** — 這份範本是 **diagram-led**，
跟 vSphere Tech Tuesday（icon-led）不同。要 icon 列請改用那份備用範本。

---

## 骨架頁（每份 deck 都要）

| 頁 | 版型 | 圖裡有什麼 | 可填欄位 |
|---:|------|-----------|---------|
| **1** | `Title Slide – Plum with Circle` | Plum 圓形 hero 視覺 | `title` 主標<br>`subTitle:10` 一句話說明<br>`body:11` 講者姓名 (email)<br>`body:12` 部門<br>`body:14` 日期 |
| **2** | `Actually Blank` | 「用 PowerPoint 開，別用 Google Slides」警語 | 無（不要改）— **對外版刪掉** |
| **3** | `Blank` | About This Presentation / Do Not Distribute | 非 placeholder，要改需手動 — **對外版刪掉** |
| **4** | `Title Only` | **四象限總覽**：4 個 icon + 4 條垂直分隔線 + 4 組標題與清單 | `title`；四組標題與清單是文字方塊（`L0.4/3.6/6.8/10.0`，`T1.8` 標題、`T4.3` 清單）|
| **27** | `Blank` | 收尾大字：兩句反問 + vSAN HCI / storage clusters 併排圖 | 非 placeholder，要改需手動 |
| **28** | `Thank You / Closing - Plum` | Plum Thank You 頁 | 無 |

### 第 4 頁怎麼用

這是全 deck 最好用的一頁 —— **一頁交代整份簡報的四大主題**，跟後面四個 section 一一對應。
底版的四組是：Flexible & Efficient Storage Platform / Accelerated Modern App Development /
Secure and Cyber Resilient Storage / Simplified Operations。
換成你的四大主題即可，每組配 3–4 條 highlight（每條 ≤ 6 字最好看）。

---

## 章節分隔（4 張，可任選一張複製多次）

| 頁 | 章節名 | 副標 |
|---:|-------|------|
| 5 | Flexible & Efficient Storage Platform | Drive down hardware costs |
| 11 | Accelerated Modern Application Development | Delivering new capabilities and outcomes |
| 15 | Secure and Cyber Resilient Storage | Easily protect and secure your data |
| 22 | Simplified Operations | Making storage easier and more intuitive |

欄位：`title` / `subTitle:10`。四張視覺相同（全 Plum）。

> **多章 deck 要換色**：底版全 Plum，做 4 章時建議改配
> `Section Header – Plum` → `– Aqua` → `– Leaf` → 或主題式 `Section - Storage` / `Section - Networking` /
> `Section - AI` / `Section - Availability`（見 `layout-map.md`），並讓該章內容頁的細色條跟著走。

---

## 圖文頁 donor（`Diagram with Content on Right`）

欄位一律是：`title`（benefit headline）/ `subTitle:10`（feature name）/ `body:17`（右欄 3–5 條 bullets）。
幾何：title `L0.6 T0.5 W12.0 H0.4`、subtitle `L0.6 T0.9 W12.0 H0.3`、body `L9.2 T1.8 W4.2 H5.0`，
左側 `0.6–9.0 in` 是圖。

### 依「圖畫什麼」分類挑 donor

| 圖的類型 | donor 頁 | 圖裡實際畫的 | 適合改成什麼題目 |
|---------|--------:|-------------|----------------|
| **資料路徑 / 分層堆疊** | **6** | 3 台 ESX 主機 + upper/lower vSAN layer + LFS + 壓縮資料流 | 任何「資料在堆疊中如何流動」：壓縮、加密、快取、寫入路徑、I/O 分層 |
| **硬體 BOM / 規格分級** | **7** | CyberRecovery-SM / MED / LRG 三個伺服器規格卡 | ReadyNode 分級、硬體選型、T-shirt sizing、方案分級 |
| **三層階梯 / 分級比較** | **8** | 三條橫帶（ReadyNodes for HCI / storage clusters / Cyber Recovery），每帶再分 SM / MED / LRG，帶與帶之間有 "Better Performance" 箭頭 | 三種架構選項、三種部署模式、方案分級、由低到高的階梯式比較 |
| **跨叢集掛載拓撲** | **9** | vSAN OSA / ESA / compute cluster 交叉掛載箭頭 | 跨叢集、跨站點、跨 vCenter 的資源共享或遷移 |
| **VM 層級操作** | **10** | Oracle RAC / WSFC 共用磁碟 + Extend 箭頭 | 叢集應用、共用磁碟、線上擴充、VM 層級 Day-2 操作 |
| **多租戶自助服務** | **12** | Provider Admin (VCF Automation) → Tenant #1 / #2 物件儲存 | 多租戶、自助服務、VCF Automation 消費層、Namespace |
| **服務層 / 協定層** | **14** | vSAN Datastore + protocol services + NFS/SMB | 檔案服務、協定閘道、服務層效能 |
| **跨叢集加密傳輸** | **16** | compute cluster ↔ storage cluster，標示加密段落 | 傳輸加密、網路安全邊界、disaggregated 拓撲 |
| **inline vs post-process 流程** | **17** | 寫入資料 → 去重 metadata → 資料物件，含節流標示 | 資料縮減、後處理流程、非同步作業 |
| **多來源複寫** | **19** | VMFS / NFS / vSAN 三種來源 → vSAN ESA 目標 + Site Recovery | 異質來源整併、資料遷移、備援複寫 |
| **隔離環境 / clean room** | **20** | 正式站台 → 隔離復原環境（Cyber Recovery） | 勒索軟體復原、隔離網段、DR 站台、air-gapped |
| **策略自動套用** | **23** | 4-host / 12-host stretched cluster + Auto-RAID 套用 | 策略自動化、依規模自動調整、系統自我管理 |
| **UI 容量儀表** | **24** | vCenter「Effective Capacity 600.00 TB」畫面示意 | 容量報表、UI 新畫面、可觀測性數字 |
| **雙站點 site-aware** | **25** | Site - Milan / 另一站，site aware storage + vSphere clusters | 延伸叢集、雙活站點、跨 workload domain |
| **記憶體分層** | **29** | 主機內 NVMe 裝置分成 memory tiering / vSAN 兩群 | NVMe Memory Tiering、資源分層、硬體資源切分 |
| **編號步驟流程** | **30** | 1. 檢查資格 → 2. 加裝置 → 3. 啟用 vSAN → 4. 完成 | 任何 3–5 步驟的流程、導入步驟、遷移程序 |

---

## 雙成果對照頁（`Diagram with Outcome, Benefit`）

| 頁 | 圖裡有什麼 | 欄位 |
|---:|-----------|------|
| **18** | 延伸叢集雙站點（Milan / Turin），左組 = Maintenance、右組 = Permanent Failure + Takeover | `title` / `subTitle:10`<br>左組：`body:17` 小標 + `body:20` 說明<br>右組：`body:19` 小標 + `body:21` 說明 |

適合：**兩種情境並排對照**（正常 vs 故障、before vs after、選項 A vs 選項 B）。

---

## 純文字頁（`Title, Subtitle and Content`，無架構圖）

| 頁 | 圖裡有什麼 | 欄位 |
|---:|-----------|------|
| **13** | 3 個橫向區塊：每塊一個粗體小標 + 一句效益 | `title` / `subTitle:10`（三塊內容是文字方塊）|
| **21** | 3 個橫向區塊：能力敘述 + 對應效益 | 同上 |
| **26** | 3 欄：Storage Performance Insights / Enhanced vSAN Diagnostics / Protection and Recovery，每欄 3 條 bullets | 同上 |

適合：**沒有好圖可畫、但要講 3 件事**的頁。26 是最完整的三欄版，優先拿它。

---

## 挑 donor 的決策順序

```
要做一頁 → 這頁有沒有架構圖？
            ├─ 有 → 上面「依圖畫什麼分類」找最接近的一頁 → clone → 換 title/subtitle/bullets
            │        └─ 都不像 → 挑最接近的，然後在 PowerPoint 手動改圖內標籤
            ├─ 兩種情境對照 → clone 18
            ├─ 三件事、無圖 → clone 26（或 13 / 21）
            └─ 一句話結論 → clone 27，或用 `Big Statement - Plum` 版型
```

---

## 常用組裝流程

> ⚠️ **順序很重要：先 clone、後 keep。**
> `clone` 是在**同一個檔案內**複製第 N 頁到最後，所以一旦先 `keep` 砍掉了 donor 頁，就再也 clone 不到它。
> 正確做法是**先在完整的 30 頁底版上把要的 donor 都 clone 出來（會依序接在 31、32、33…）**，
> 最後再用 `keep` 一次指定最終順序。

```bash
cp base.pptx deck.pptx          # 永遠不要改原始範本

# 1) 在完整底版上 clone donor 頁（新頁接在最後：31, 32, ...）
python3 scripts/clone-slide.py clone deck.pptx --slide 8 --out deck.pptx \
    --title "三種部署型態，一套平台" \
    --subtitle "VCF 9.1 deployment options" \
    --bullets "HCI 叢集|儲存叢集|Cyber Recovery 叢集"      # → 第 31 頁

python3 scripts/clone-slide.py clone deck.pptx --slide 30 --out deck.pptx \
    --title "四步驟導入" --subtitle "Deployment steps"      # → 第 32 頁

# 2) 一次指定最終順序（骨架 + 剛做好的新頁）
python3 scripts/clone-slide.py keep deck.pptx \
    --slides 1,4,5,31,32,28 --out final.pptx

# 3) 換封面
python3 scripts/clone-slide.py settext final.pptx --slide 1 --out final.pptx \
    --title "VCF 9.1 技術簡報" \
    --set 'body:11=Kosten Yang' --set 'body:14=2026 年 8 月'

# 4) QA
soffice --headless --convert-to pdf --outdir qa final.pptx
pdftoppm -png -r 70 qa/final.pdf qa/slide
```

每 clone 一頁，指令都會印出「新頁在第 N 頁」—— **把這些 N 記下來**，最後 `keep` 就照這串 N 排順序。
