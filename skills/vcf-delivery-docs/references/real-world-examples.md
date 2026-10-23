# 實戰交付範例（真實案例模式）

真實案例檔（半導體客戶新加坡站點案）兩處可取得：
- 使用者資料夾 `claude-output/vcf-delivery-examples/`
- GitHub：`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/vcf-delivery-examples/` + 檔名
  - `VSMC_SG-VCF-Region_Configuration-Workbook-v2.6.3_VKS.xlsx`
  - `VCF_LowLevelDesign.docx`
  - `VSMC_VCF_Design_DOC_20260312.pptx`

官方 kit 給結構，這裡給「實際交付長什麼樣」。做同類文件時先讀對應範例再動工。

## 1. 檔名慣例

實例：`VSMC_SG-VCF-Region_Configuration-Workbook-v2.6.3_VKS.xlsx`

格式：`<客戶>_<站點/區域>-<範圍>_<文件類型>-v<主.次.修>_<模組>.ext`
設計簡報則用日期版本：`<客戶>_VCF_Design_DOC_<YYYYMMDD>.pptx`
沿用客戶案的既有慣例優先；新案用上述格式起頭。

## 2. Configuration Workbook 實戰版（vs 官方版）

官方 `*_ConfigurationWorkbook.xlsx` 是通用參數表；實戰版重構為**依安全域分區**的完整組態手冊。
半導體案的三域隔離：**DMZ / MES（廠務生產）/ OA（辦公）**，每個域各自一組分頁。

實例分頁結構（28 sheets）：

- 治理：`Version Control`、`name_rules`（命名規則獨立成頁）
- 資源規劃：`Share Components`、`VCF Resource`、`OA VCF Resource`、各類 VM 清單（`IN House VMs` / `FDC VMs` / `MES VMs` / `OA VM`）、`Overcommit Ratio`
- 網路：每域一張 CIDR 表（`DMZ CIDR` / `MES CIDR` / `OA CIDR`）、每域一張 VCF Components config（IP 配置）、`MGMT_Network_*`、`Host_Network`
- 儲存：`MES_Storage` / `OA_Storage`（依域分開）
- 安全：`Firewall List`（跨域防火牆規則清單 — 半導體案必備）
- 實體：`Phyical Server`、每 DC 的 `RackProfile`、Resource Pool 配置
- 帳密：`VCF Deploy Roles & Credentials`

要點：域隔離客戶（半導體 OT/IT、金融 DMZ/內網）的組態文件**以域為軸**組織，不是以產品為軸。

## 3. LLD Word 版

實例 `VCF_LowLevelDesign.docx` 幾乎完全沿用官方 Pro Cloud Service LLD 結構
（Document Overview → VCF Detailed Design：External Services / Physical Network / vSphere / ESXi / vSAN / vCenter / Cluster⋯⋯每小節配 Logical Design + Sizing + Requirements & Recommendations 表）。
結論：**Word LLD 直接用官方檔客製即可**，變化不大；把客戶環境值填入 Requirements/Recommendations 決策表。

## 4. 設計文件的 PPT 變體（官方 kit 沒有的交付型態）

實戰中設計文件常以 **PowerPoint** 交付（給客戶 review / workshop 用），實例
`VSMC_VCF_Design_DOC_20260312.pptx`（101 頁）章節流：

1. Naming Rule → 2. Hardware → 3. VCF Component 清單 → 4. IP Addressing 原則 →
5. VCF High-Level Design → 6. 域隔離設計（Isolating Different Types ×N 域）→
7. 管理元件架構 → 8. 各域 Cluster / vSAN 設計 → 9. Network LLD（邏輯架構 / 實體接線圖 per 域 per DC）→ 10. Rack Design

路由判斷：使用者說「設計**簡報**」或「design review / workshop 用」→ 做 PPT 變體（結構照上面，
版型走 Broadcom 範本，參考 `vcf-base`）；說「設計**書**/文件」→ Word 官方 LLD。不確定就問一句。
