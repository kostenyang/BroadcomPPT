---
name: vcf-delivery-docs
description: 產出 VCF 安裝/升級專案的正式交付文件 — 前置檢查表 (Prerequisite Checklist)、設計文件 (HLD/LLD/Design Decisions)、安裝組態手冊 (Installation & Configuration Procedures)、測試驗收 (Verification Workbook/RTM/UAT)、維運 SOP、竣工文件 (As-Built)、升級計畫 (Upgrade Implementation Plan/Gap Analysis)。一律以使用者持有的 Broadcom PSO 官方交付套件 (Pro Cloud Service delivery kit) 為底、絕不從零建立。只要使用者要做 VCF/VMware 安裝案或升級案的任何交付文件 — 包括「前置檢查」「需求檢核」「設計書」「LLD」「HLD」「安裝手冊」「組態文件」「驗收計畫」「測試報告」「SOP」「維運手冊」「竣工文件」「as-built」「upgrade plan」「gap analysis」 — 就使用本 skill。輸出語言（中文/英文）依客戶而定，文件結構允許依客戶實際狀況增刪。
---

# VCF 交付文件 Skill（官方 PSO Delivery Kit 客製）

哲學與使用者的 PPT skills 相同：**永遠從官方檔案出發，絕不從零建立**。
官方 kit 提供結構正確、版本對齊 9.1 的骨架；本 skill 的工作是把它變成**特定客戶的交付版**。

---

## 官方 Kit 位置

使用者資料夾：`PSO Project-OneDrive/tsmc/design/`（掛載後 bash 路徑通常是 `.../mnt/tsmc/design/`）。
若目前 session 沒有掛載此資料夾，先請使用者連結它（資料夾選擇器），不要自己重建內容。
注意：kit 是**通用官方文件**，不含客戶專屬內容 — 放在 tsmc 資料夾只是存放位置，任何客戶案都用同一套。

```
design/
├── Build a Private Cloud/   ← 全新安裝案
│   ├── VCF-High-Level-Design/            HLD + Design Library + Planning & Prep Workbook
│   ├── VCF Environment Instantiation/    環境建置
│   ├── VCF Automation/                   ─┐
│   ├── VCF Operations (Consumption)/      │ 每個模組都有同一組八件套
│   ├── VCF Operations for logs/           │ （見下方「模組八件套」）
│   ├── VCF Operations for Networks/       │
│   ├── VCF Operations Orchestrator/       │
│   ├── VCF vSphere Kubernetes Service Add-on/ ─┘
│   ├── VCF NIST Hardening/               資安：Security Config/Verification Workbook + STIG
│   ├── VCF Requirements Traceability Matrix/  RTM
│   └── Automation-Terraform/             IaC 參考
└── Upgrade/                 ← 升級案
    ├── VCF Upgrades/        UPG 四件套（Checklist / ImplementationPlan / Verification / GapAnalysis）
    ├── VCF Import/          IMP 四件套（vSphere 環境 import 進 VCF）
    └── VCF Requirements Traceability Matrix/
```

### 模組八件套（每個產品模組資料夾內，前綴如 VCFA_ / VCFOL_ / VCFON_ / VCFVKS_）

| 檔案 | 用途 | 交付階段 |
|---|---|---|
| `*_PrerequisiteChecklist.xlsx` | 前置需求檢核（Design + Deploy 兩張表） | 開案/建置前 |
| `*_DesignDecisionsWorkbook.xlsx` | 設計決策清單（決策點/選項/理由） | 設計 |
| `*_LowLevelDesign.docx` | LLD：Conceptual → Logical → Detailed Design | 設計 |
| `*_ConfigurationWorkbook.xlsx` | 組態參數（實際填值） | 建置 |
| `*_InstallationAndConfigurationProcedures.docx` | 安裝組態步驟手冊 | 建置 |
| `*_VerificationWorkbook.xlsx` | 驗證測項（測試驗收基礎） | 測試 |
| `*_StandardOperatingProcedures.docx` | 維運 SOP | 知識轉移 |
| `*_EngagementWBS.xlsx` | 該模組工作分解 | 專案管理 |

---

## 交付物 → 來源檔對照

| 使用者要的 | 從這裡出發 |
|---|---|
| 前置檢查表（整案） | `VCF-High-Level-Design/vcf-9.1-planning-and-preparation-workbook.xlsx`（含 Prerequisite Checklist、Sizing、Deploy 各階段參數表） |
| 前置檢查表（單一模組） | 該模組 `*_PrerequisiteChecklist.xlsx` |
| HLD / 概念與邏輯設計書 | `VCF - High Level Design.docx`（章節：Overview → Conceptual Design(需求/SLO/限制/假設/風險/Use Case) → Logical Design(各 Architectural Options)），設計選項素材查 `VCF - Design Library*.docx/xlsx` |
| LLD / 實體設計書（模組） | 該模組 `*_LowLevelDesign.docx` + `*_DesignDecisionsWorkbook.xlsx` |
| 安裝手冊 | 該模組 `*_InstallationAndConfigurationProcedures.docx` |
| 測試驗收計畫 / UAT | 該模組 `*_VerificationWorkbook.xlsx`；跨模組驗收用 RTM（`VCF - Requirements Traceability Matrix v3.0.xlsx`）彙整需求→測項對應 |
| 維運手冊 / SOP | 該模組 `*_StandardOperatingProcedures.docx` |
| **竣工文件 (As-Built)** | 官方無此檔。做法：以 LLD 為骨架 + 把 `*_ConfigurationWorkbook.xlsx` 的實際填值織入，標題改為 As-Built，加入「與設計差異」一節 |
| 升級計畫書 | `Upgrade/VCF Upgrades/VCF_UPG_ImplementationPlanContent_9.1.x.docx`（Purpose→Success Criteria→Current State→Future State→Upgrade Steps） |
| 升級前檢查 / Gap 分析 | `VCF_UPG_ChecklistContent_9.1.x.xlsx` / `VCF_UPG_TechnicalGapAnalysis_9.1.x.xlsx` |
| vSphere 匯入 VCF (Import/Converge) | `Upgrade/VCF Import/VCF_IMP_*` 四件套 |
| 資安遵循 / NIST / STIG | `VCF NIST Hardening/` 內 Security Configuration/Verification Workbook |

---

## 實戰範例（必讀）

官方 kit 之外，`references/real-world-examples.md` 收錄真實客戶案的交付模式：
檔名慣例、依安全域分區（DMZ/MES/OA）的 Configuration Workbook 實戰結構、
以及官方沒有的「設計文件 PPT 變體」（design review/workshop 用，101 頁實例章節流）。
做 Configuration Workbook 或設計文件前先讀它。真實範例檔的取得順序：
1. 使用者資料夾 `claude-output/vcf-delivery-examples/`（若有掛載）
2. 從 GitHub 拉：`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/vcf-delivery-examples/<檔名>`
   （檔名見 references/real-world-examples.md）

---

## 客製流程

1. **確認四件事**：交付物類型、產品模組範圍、客戶（產業即可，未提供名稱就用通用產業寫法）、**語言（中文或英文）**。
   語言不明時問一次 — 官方 kit 是英文，交付語言完全看客戶。
2. **複製官方檔為工作檔**（xlsx 直接複製；docx 大檔可先抽取結構再重建），保留官方章節/表頭結構。
3. **客製**：
   - 封面/標題：客戶名（或產業）、專案名、版本、日期；移除 "Pro Cloud Service" 字樣改為實際服務名（依使用者慣例，通常對應 CXS 交付方法）。
   - **中文交付**：翻譯標題、表頭、說明文字；技術名詞保留英文原文（SDDC Manager、vCenter、NSX、Supervisor⋯⋯不翻）；步驟指令與 UI 路徑保留英文。
   - 依客戶環境填入/刪除不適用的模組、架構選項、決策項 — **官方結構是起點不是鐵律**，實際交付會因客戶而變化，主動依訪談/需求資訊裁剪。
   - xlsx 中的 `Architecture_Models` / `MenuVersionsSummary` / `Product_Selected` / `microsoft.com:*` 為官方下拉選單與公式支援表，保留勿刪，交付時可隱藏。
4. **文件機制**：docx 產出讀 `docx` skill；xlsx 產出讀 `xlsx` skill。
5. **配套**：估人天 → `manday-estimate`；排時程 → `wbs-gantt`（可拿 `*_EngagementWBS.xlsx` 當任務來源）；簡報 → 走 `vcf-router`。

---

## 章節骨架速查（不必開原檔即可回答結構問題）

**HLD**：Version History → Overview (Executive Summary / Document Focus) → Conceptual Design (Diagram / Business & Technical Requirements / SLO / Constraints / Assumptions / Risks / Use Cases) → Logical Design (Architectural Options：Fleet Deployment/Sizing、Automation、Supervisor、Network Consumption、Workload Connectivity、Load Balancing、Management Services/Network、Operations、Log Management⋯)

**模組 LLD**（以 VCFA 為例）：Version History → Document Overview (Executive Summary / Conceptual / Logical Overview) → Conceptual Design (Constraints / Assumptions / Risks / Use Cases / Verification 對應) → Low Level Design (Detailed Design / Deployment Patterns / Tenancy Models / Network Design)

**升級計畫**：Purpose → Overview → Success Criteria → Assumptions / Constraints / Risk → Target Environments (Current State：SDDC Manager/NSX/vCenter/ESX) → Future State Specifications → Upgrade Preparation → Upgrade Steps (依 5.x 起點與管理元件有無分場景)

**Planning & Prep Workbook 分頁**：Prerequisite Checklist → VCF & VVF Planning → Management Domain Sizing → Deploy/Configure Management Domain → Deploy Fleet Management Day-N → Deploy/Configure Workload Domain → Deploy Cluster → Change Control
