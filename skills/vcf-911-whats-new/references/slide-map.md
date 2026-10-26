# VCF 9.1 / 9.1.1 What's New — Sales Overview：完整頁碼對照

底版：`VCF_9.1_Whats_New_Sales_09.30.26.pptx`（46 頁，16:9，Broadcom VCF Division，September 2026 · V 9.30.26）

- 頁碼 = 範本原始頁碼。`keep` 之後頁碼會變，但 **shape id 跟著投影片走、不會變**。
- `title` / `subTitle:1` 是 placeholder（用 `--title` / `--subtitle`）。
- `shape:<id>` 不是 placeholder，要用 `--shape '<id>=…'`。重產：`clone-slide.py list <deck> --slide N --shapes`
- Feature 頁的 "Customer Benefits" 標籤本身也是 shape，**不用改**。
- TP = Tech Preview；AS = Advanced Service（另購授權）。這兩種標註在原頁有註腳，客製時保留。

---

## 開場（1–4）

| # | 版型 | 內容 | 可改欄位 | 備註 |
|---|------|------|----------|------|
| 1 | 1_Title, Subtitle and Content | Disclaimer（產品方向免責聲明） | title, body:2 | 有 roadmap / TP 內容時對外也要留 |
| 2 | Title Slide – Leaf | 封面 What's New in VMware Cloud Foundation 9.1 / Sales Overview | title, subTitle:1, body:3（單位）, body:4（日期/版號） | 客製先改這頁 |
| 3 | 1_Title and Subtitle | VCF 9 平台全貌（Advanced Services / Modern Cloud Interface / Automation & Operations / Compute-Storage-Network；On-Prem / Public / Sovereign / Edge / Telco） | title | 圖內文字非 placeholder，不改 |
| 4 | Blank | VCF 9 成果數字：40% Server TCO、39% Storage TCO、5x Containers Density、Zero Downtime vMotion for AI、40% Risk Reduction (vDefend) | — | 註腳：Broadcom 內部估算 2026/4、Principled Technologies 2026/3、Forrester TEI 2025/3 |

## A. VCF 9.1.1 Updates（5–11）

| # | 版型 | 標題 / 副標 | badge | benefits | 註記 |
|---|------|-------------|-------|----------|------|
| 5 | Blank | Section：VMware Cloud Foundation 9.1.1 Updates | — | — | 標題 shape:6188（兩段，不建議改） |
| 6 | Blank | 9.1.1 三主軸總覽 | — | — | 標題 shape:6231；三項 shape:6232 / 6233 / 6234（`標題\|內文`） |
| 7 | Title and Subtitle | Share AI Models Securely Across Teams / Secure model sharing… | 6252 Multi-Tenant Model Sharing | 6251 | 左圖 Before/After（Org1/Org2 共用 Model Runtime） |
| 8 | Title and Subtitle | AI Diagnostics, Proactive Health, and AI-Built Management Packs [TP] | 6266 AI Assistant for VCF [Tech Preview] | 6265 | **TP** |
| 9 | Title and Subtitle | New GitOps Service [TP] / Argo CD self-service | 6289 New GitOps Service [Tech Preview] | 6278 | **TP** |
| 10 | Title and Subtitle | EVPN Architectural Enhancements | 6298 EVPN in VCF 9.1.1 | 6297 | 與 NSX Edge 問題相關（見 SKILL.md Guardrail） |
| 11 | Title and Subtitle | VKS 3.7 Add-on management Framework / Speeding up ecosystem adoption | 6312 VKS Ecosystem Adoption | 6311 | 左圖四象限（Product / Partner / Community / BYO Add-on） |

## B. VCF 9.1 GA 總覽（12–16）

| # | 版型 | 內容 | 可改欄位 | 備註 |
|---|------|------|----------|------|
| 12 | Blank | Section：VMware Cloud Foundation 9.1 · Generally Available | shape:6401（標題）, 6402（GA 膠囊） | |
| 13 | Title Only | 9.1 Messaging Themes（4 支柱） | title；6497 / 6489 / 6467 / 6460 | |
| 14 | Blank | Most Cost-Effective, Secure Platform for Private AI（三支柱 + Open Platform 橫條） | — | 圖內文字多，建議不改 |
| 15 | Title Only | Key VMware Cloud Foundation 9.1 Features（三欄 × 兩組功能清單） | title；6568 / 6570 / 6571 / 6572 / 6575 / 6576 | 註腳 6577：1=TP in 9.1.x、2=AS、3=GPU 虛擬化/vMotion 未來版本 |
| 16 | 1_Title and Subtitle | VCF 9.1 — Measurable Outcomes（6 個數字） | title | 數字是官方宣稱，**不改**；註腳 6680 |

## C. 支柱 1：Efficient Infrastructure at Scale（17–24）

| # | 版型 | 標題 / 副標 | badge | benefits | 註記 |
|---|------|-------------|-------|----------|------|
| 17 | Blank | 支柱封面 | — | — | 標題 6689（`Efficient Infrastructure \|at Scale\|副標` 三段）；三項 6690 / 6691 / 6692 |
| 18 | Title and Subtitle | Improving Performance and Efficiency / with NVMe Memory Tiering | 6707 Enhanced NVMe Memory Tiering | 6710 | 4 項 |
| 19 | Title and Subtitle | Enhanced vSAN Data Reduction in VCF 9.1 | 6726 Enhanced vSAN Dedup, Compression | 6725 | 粗體開頭換行接內文 |
| 20 | Title and Subtitle | Accelerating Troubleshooting / with Real-Time VCF Observability | 6735 Real-Time VCF Observability | 6741 | |
| 21 | Title and Subtitle | Deliver large-scale Kubernetes / With higher efficiency | 6751 Enhanced VKS Scalability & Efficiency | 6750 | |
| 22 | Title and Subtitle | Increased Fleet Size / and Accelerated Parallel Upgrade Scale | 6764 Increased Fleet Size, Upgrade Scale | 6763 | 2 項 |
| 23 | Title Only | Zero Touch Provisioning for Edge Deployments at Scale | 6782 Zero Touch Provisioning | 6778（3 行短句） | 說明框 6777（`標題\|內文`）；版型與其他 feature 頁不同 |
| 24 | Title and Subtitle | Maximize Performance / with Topology Aware Scheduling enhancements for ESX | 6792 Topology Aware Scheduler | 6791 | |

## D. 支柱 2：High Velocity Application Delivery（25–32）

| # | 版型 | 標題 / 副標 | badge | benefits | 註記 |
|---|------|-------------|-------|----------|------|
| 25 | 1_Title and Subtitle | 支柱封面 | — | — | 標題 6802；三項 6805 / 6806 / 6807 |
| 26 | Title and Subtitle | Accelerating Cluster Deployment / with Fast Deploy for VKS and VMs | 6873 Fast Deploy (VKS and VMs) | 6876 | 左圖長條圖（建立/升級時間） |
| 27 | Title and Subtitle | Containers as a Service | 6893 Container as a Service | 6888 | |
| 28 | Title and Subtitle | Delivering Object Storage / as a Native VCF Service | 6902 vSAN Native S3 Object Storage* | 6901 | **TP**（註腳 6903） |
| 29 | Title and Subtitle | Developer Provisioned Services for VKS with Tanzu Marketplace Integration | 6915 Tanzu Marketplace Integration | 7019 | **AS**：Tanzu Platform（註腳 6916）；4 項 |
| 30 | Title and Subtitle | Actionable AI Insights / into AI Models and Agents | 7028 Private AI Model and GPU Metrics | 7031 | 2 項 |
| 31 | Title and Subtitle | Accelerate Service Delivery / with App Stack Formation | 7042 Live Application Stack Blueprints | 7041 | |
| 32 | Title and Subtitle | MS SQL Server Database-as-a-Service | 7056 SQL Server DBaaS | 7054 | **AS**：Data Services Manager（註腳 7060） |

## E. 支柱 3：Cyber Resilience and Data Security（33–40）

| # | 版型 | 標題 / 副標 | badge | benefits | 註記 |
|---|------|-------------|-------|----------|------|
| 33 | Blank | 支柱封面 | — | — | 標題 7068；三項 7070 / 7071 / 7072 |
| 34 | Title and Subtitle | Extending Cyber Resilience with vSAN for Recovery | 7096 vSAN for Recovery | 7094 | |
| 35 | Title and Subtitle | Encrypted vMotion offloading with Intel QAT to reclaim CPU cores | 7110 Encrypted vMotion with Intel QAT | 7108 | |
| 36 | Title and Subtitle | On-Premises Cyber Recovery | 7121 On-Premises Cyber Recovery | 7120 | **AS**（註腳 7122）；4 項 |
| 37 | Title and Subtitle | Continuous Compliance Enforcement（ACC） | 7135 ACC - Continuous Compliance Enforcement | 7134 | **AS**（註腳 7137）；內含 "Key Benefits" 子清單，改寫時整框重寫 |
| 38 | Title and Subtitle | Extending Zero-Downtime Patching to TPM-Enabled Hosts | 7151 Live Patching for TPM Enabled Hosts | 7149 | |
| 39 | Title and Subtitle | VMware vDefend: Self-Service Lateral Security with Automation | 7167 Self-Service Lateral Security | 7166 | **AS**；firewall conversion tool 為 **TP**（註腳 7203）；4 項 |
| 40 | Title and Subtitle | VMware Avi: Automated Load Balancing | 7212 Automated Load Balancing | 7211 | **AS**；4 項 |

## F. 支柱 4：Open Ecosystem（41–44）

| # | 版型 | 標題 / 副標 | badge | benefits | 註記 |
|---|------|-------------|-------|----------|------|
| 41 | Blank | 支柱封面 | — | — | 標題 7274；三項 7275 / 7279 / 7283 |
| 42 | Title and Subtitle | Simplifying Network Operations / with a Unified Fabric | 7325 EVPN-based Unified Network Fabric | 7323 | 左圖含 Cisco / Arista / SONiC；與 NSX Edge 問題相關 |
| 43 | Title and Subtitle | Crowdstrike EDR Integration for RWR | 7394 Crowdstrike EDR Integration for RWR | 7393 | |
| 44 | Title and Subtitle | Advancing AI with AMD / Virtualization enabled | 7565 Enhanced DirectPath I/O for Latest AMD GPUs | 7558 | 註腳 7566：GPU 虛擬化與 vMotion 在未來版本 |

## 結尾（45–46）

| # | 版型 | 內容 | 備註 |
|---|------|------|------|
| 45 | Title Only | A Robust Catalog of Advanced Services（8 類：Cyber Compliance / Advanced Security / Load Balancing / Application Services / Identity Security / Business Operations / Network Observability / Data Services） | 全部是另購 Advanced Services |
| 46 | Thank You / Closing - Leaf | Thank You | |
