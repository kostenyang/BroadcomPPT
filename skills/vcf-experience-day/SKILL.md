---
name: vcf-experience-day
description: Build Broadcom VCF 9.1 Experience Day (VXD) workshop decks from the official 144-slide "Master - VXD-VCF-910-PPT v1.2 Taiwan Version" template — storyline-driven (Sarah / OmniCorp) hands-on workshop with modules, labs, quiz slides and leave-behind links. Trigger whenever the user wants a VCF Experience Day, VXD, VCF 9.1 workshop, 體驗日, 動手實作工作坊, hands-on lab session deck, 客戶實作課程簡報, enablement day, lab-led training deck, or a module subset of it (VCF Installer / converge / VCF Import / VPC & Transit Gateway / VKS & Supervisor / VCF Automation / VCF Operations / Private AI Services / Key Providers & vSAN encryption) delivered as a workshop with labs and comprehension checks. Always clone slides from the bundled template — never create from scratch.
---

# VCF 9.1 Experience Day (VXD) Workshop Skill

Read `vcf-base` SKILL.md first for colors, fonts and the clone-slide workflow.

> **⚡ 底版**：`VXD-VCF-910-PPT-v1_2-Taiwan.pptx`（144 slides，Leaf/Plum 主題，白底內容頁，**每頁都有講者備註，大多已有中文**）。
> Download: `https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/VXD-VCF-910-PPT-v1_2-Taiwan.pptx`
> 完整頁碼 → 版型對照：`references/slide-map.md`

**Guardrail**：產出任何簡報前，先問「這次範圍是否包含 NSX Edge cluster（Edge nodes / T0-T1 gateway）」；確認後才動手。（VPC 模組的 Centralized Transit Gateway 那頁就靠 Edge，答案會決定 slide 61 保留或改講 DTGW-only。）

---

## 這份 deck 是什麼

不是 pitch deck，是**半天到一天的動手工作坊**。整份以一條故事線串起來：
**Sarah — OmniCorp（虛構跨國企業）的 VP of Platform Engineering**，一年內帶團隊完成三大目標：
Infrastructure Modernization · Application Modernization · Security Modernization（slide 5）。

每個模組的固定節奏（做客製版也維持這個節奏）：

```
Section Header (Leaf) → Storyline (Challenge / Solution) → 技術內容頁 → Comprehension Check (Quiz) → Leave Behind Links → Lab 頁 (Big Statement 2 - Leaf)
```

---

## 模組地圖（頁碼 = 範本原始頁碼）

| # | 模組 | Section | Storyline 主題 | 內容頁 | Quiz | Links | Lab |
|---|------|---------|----------------|--------|------|-------|-----|
| 0 | 開場 | 1 Title · 2 Speakers · 3 Agenda | 4 Meet Sarah · 5 三大目標 | — | — | — | — |
| 1 | VCF Overview | 6 | 7 Infrastructure chaos | 8–13（Fleet/Instance/WLD 架構、集中 LCM、儲存選項、HCI 演進、網路虛擬化） | 14 | 15 | — |
| 2 | Deploying VCF 9.1 | 16 | 17 Greenfield Anxiety | 18–28（VCF Installer、Depot online/offline、Simple vs HA 模式、Mgmt Domain sizing、Converge 需求與儲存需求） | 29 | 30 | 31 Lab 01 Deploy & Converge（iSim 15m） |
| 3 | Expanding w/ Existing Infra | 32 | 33 Technical Debt | 34–37（擴充 Fleet、VCF Import、Import 需求/限制、支援的 inventory） | 38 | 39 | 40 Lab 02（20m） |
| 4 | Private Cloud Networking | 41 | 42 Network Bottleneck | 43–62（What is VPC 動畫序列 44–55、Why VPC 57–58、Transit Gateway 60–62：Centralized TGW on Edge vs **Distributed TGW**） | 63 | 64 | 65 Lab 03 VPC Creation（25m） |
| 5 | Kubernetes Overview | 66 | 67 Dev vs Ops | 68–82（Supervisor、9.1 新功能、VKS 3.6/3.7、Add-ons、Container Service、VM Service、Supervisor Services、Argo CD、網路選項） | 83 | 84 | 85 Lab 04（10m） |
| 6 | VCF Automation | 86 | 87 Wanting Everything Now | 88–98（組織痛點、統一消費、Modern Cloud Interface、Private Cloud Services、Blueprint/IaC、App Stack Formation、Governance、Tenant、Content Hub） | 100 | — | 99 Lab 05 |
| 7 | VCF Operations | 101 | 102 Fragmented tools | 103–119（Manage：Fleet Mgmt/Capacity/FinOps；Operate：Health/Troubleshooting/Storage/Network/App/K8s 監控；Protect：Security Posture/Forensics） | 121–122 | — | 120 Lab 06-13（50m） |
| 8 | Private AI Services | 123 | 124 Agentic chatbot | 125–128（PAIS 全貌、Model Gallery/Runtime/Agent Builder/MCP、端到端流程） | 130 | 131 | 129 Lab 19（15m） |
| 9 | Security & Compliance | 132 Security XD 廣告 | — | 133–141（Key Provider 三選一、KEK/DEK/Wrapping Key、NKP、vTPM、vSAN DaR/DiT 加密） | — | — | 142 Lab 20/21（20m） |
| 10 | 結尾 | — | 143 The End | — | — | — | 144 Thank You |

Agenda（slide 3）講者分工：01–06 Sean Chung；07–10 Gina Wang。Speakers 頁（slide 2）：Sean Chung、Gina Wang（Solutions Architect）；TA：Benson Tseng、Alan Wang（TAM）、Kosten Yang（Professional Services Architect）。

---

## 常見組合

| 需求 | 保留頁 |
|------|--------|
| **完整一天 VXD** | 全部 1–144（只改封面日期/講者/Agenda） |
| **半天：基礎架構場**（建置 + 擴充 + 網路） | 1–5, 6–15, 16–31, 32–40, 41–65, 143, 144 |
| **半天：應用現代化場**（K8s + Automation + AI） | 1–5, 66–85, 86–100, 123–131, 143, 144 |
| **維運場**（Operations + Security） | 1–5, 101–122, 132–142, 143, 144 |
| **無 Lab 的講解版** | 任一組合，去掉 Lab 頁（31, 40, 65, 85, 99, 120, 129, 142）與 Quiz 頁 |
| **單一模組 deep-dive** | 1, 3（改 agenda）, 4, 該模組全部頁, 143, 144 |

刪減後 slide 3 的 Agenda 必須同步改號、改講者；slide 5 三大目標保持不動（故事主軸）。

---

## 建置流程

```bash
# 0. 取範本
curl -LO https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/VXD-VCF-910-PPT-v1_2-Taiwan.pptx
# 1. 看頁 / 欄位（便宜）
python3 scripts/clone-slide.py list VXD-VCF-910-PPT-v1_2-Taiwan.pptx --slide 18
# 2. 依上表挑頁，順序照給的順序
python3 scripts/clone-slide.py keep VXD-VCF-910-PPT-v1_2-Taiwan.pptx --slides 1,2,3,4,5,16,17,18,...,144 --out vxd.pptx
# 3. 改封面 / 文字
python3 scripts/clone-slide.py settext vxd.pptx --slide 1 --out vxd.pptx --title "VCF 9.1 Experience Day — <客戶>"
# 4. QA
soffice --headless --convert-to pdf vxd.pptx && pdftoppm -r 50 -png vxd.pdf qa
```

- **一律複製官方頁再換字**，不要從空白頁畫。VPC 44–55、Transit Gateway 60–62 是逐頁動畫式序列，要整串保留或整串刪，不要只拿其中一頁。
- Slide 1 的 "Speaker" 與日期（原為 20th August 2026）、slide 2 講者名單、slide 3 agenda 不是 title placeholder，要改 XML 文字（unpack → 搜字串 → 改 → pack）。
- 講者備註已是中文 talk track（Storyline 頁是逐句中文翻譯，技術頁是 Key Message / Talk Track）——保留，客製時同步改備註。
- 新增客戶專屬頁時（例如客戶現況、客戶 Lab 環境），複製 Storyline（7）或 Two-Content（18）版型套內容，維持 Leaf 綠/Plum 紫配色。

---

## 內容事實（範本內已載明，做客製時直接引用，勿自行改數字）

**Deploy（模組 2）**
- VCF Installer 取代 Cloud Builder；屬 SDDC Manager OVA；Installer mode（部署在 Mgmt Domain 外，可部署多個 Fleet/Instance）vs SDDC Manager mode。
- Depot：Online（直連或 proxy）/ Offline（暗站，需本地 web server + VCF Download Tool）。
- Simple 模式：vSAN 最少 3 台 / 外部儲存 2 台，給 test/dev/POC；HA 模式：最少 4 台，給 production。
- Mgmt Domain 9.1：Simple = 10 必要 + 4 選配 appliance；HA = 16 必要 + 6 選配。9.1 起 Fleet Management 與 Logs 移入 VCF Services Platform；VIDM → VIDB（部署後再裝）。
- Mgmt Domain 主要儲存：vSAN、NFS v3/4.1、VMFS-FC/FCoE、NVMe-oF、iSCSI；vSAN 建議但非必要；stretched 每 AZ 最少 4 台。

**Import（模組 3）**
- 需 vSphere 8.0 U3a+、NSX 4.2+（三節點）、VDS、VMkernel 靜態 IP；不可用 vLCM baseline（VUM）、不可 ELM、不可 VxRail。
- NSX 若不存在會自動部署（Quiz：Import 前不需先裝 NSX = False）；inventory 可含 standalone host、單 host cluster、VSS、LACP VDS。

**Networking（模組 4）**
- VPC 子網三種範圍：Public（global）/ Private TGW（tenant 內）/ Private（VPC 內）。
- 對外：傳統 Centralized TGW on Edge（BGP 宣告）vs **VCF 9 新 Distributed TGW（每台 ESX）**——後者不需 Edge。進階跨 VPC 控制靠 vDefend Firewall（add-on）。

**Kubernetes（模組 5）**：Supervisor = VM / K8s / Container 統一控制平面；VKS 3.6（K8s 1.35、BYO CNI、Multi-NIC、RHEL BYOI）、VKS 3.7（K8s 1.36、Helm add-on、Gatekeeper/Multus/Headlamp）；Supervisor 規模 25,000 VMs / 500 VKS clusters。

**Automation（模組 6）**：Org for VM Apps vs Org for All Apps 功能不同（頁腳已註明）；production 偏好 Self-Service Catalog。

**Operations（模組 7）**：Security Posture Management 需 add-on 授權（slide 118 已註明）。

**Private AI（模組 8）**：Model Gallery（Harbor OCI）、Model Runtime、Data Indexing & Retrieval、Agent Builder、MCP。

**Security（模組 9）**：Standard / Wrapped / Native Key Provider；NKP 只服務 VCF/vSphere cluster，可 shallow rekey 互轉；vSAN DaR 加密不犧牲 dedupe/compression。

任何超出範本的數字或新版功能，先查 Broadcom TechDocs / KB 再寫，並在備註標示來源。

---

## 台灣客製提示

- 金融客戶：模組 9 加強（金管會資料加密/金鑰管理要求），模組 7 強調 Compliance benchmark 與稽核 forensics。
- 電信 / VCSP：模組 6 Tenant Management（Service Provider model）與模組 4 multi-tenant VPC 優先。
- 半導體 / 製造：模組 3 Import（既有 vSphere 不搬遷）是最有感的切入點。
- Lab 時間（iSim 15m、Lab 02 20m、Lab 03 25m、Lab 04 10m、Lab 06-13 50m、Lab 19 15m、Lab 20/21 20m）用於排議程；確認客戶當天 lab pod 數量後再寫進 Agenda。
