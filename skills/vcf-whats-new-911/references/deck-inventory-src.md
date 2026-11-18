# SRC 精簡版底版逐頁清單（50 頁）

底版：`templates/VCF_9_1_1_Whats_New_Tech_Tuesday_SRC_v3.pptx`
來源：`VCF 9.1.1 - Whats New Deck - Tech Tuesday - Edited copy for SRC.pptx`（2026-11-18 匯入）
「原版頁」= 70 頁完整版 `VCF_9_1_1_Whats_New_Technical_Deck_v1.pptx` 的對應頁碼。

## 與完整版的差異

- **移除**：Kubernetes – VKS and Supervisor Services 整章（原版 9–17）；VCF Operations 總覽頁（原 19）、
  IPv6 License Server（原 29）、AI Assistant for VCF / BYO LLM / Tokenomics / Management Pack Builder（原 30–38）。
- **重排**：VCF Operations 章改為 Fleet Management 先（密碼 → 憑證 → 組態 → Identity），OTel / Grafana 放最後。
- **改字**：
  - 封面加「Tech Tuesday 10/5 & 10/6」— 做新場次要改日期。
  - Agenda 移除 Kubernetes，尾端加「*** Covered during Week of Enablement」。
  - Section Header（第 9 頁）副標「FLEET MANAGEMENT : x x Passwords Certificates Configuration Management Identity & Access」
    — 原檔用兩個 6pt 白字 `x` 撐行高；**v2 已改成不換行空白 (U+00A0)**，版面不變、文字擷取乾淨。
    `_v1` 保留未動的匯入原貌（僅清機密字樣）。
  - 第 17、18 頁（OTel / Grafana）加註：9.1.1 的 VCF Intelligent Assist 僅限特定客戶，需透過 account team 啟用。
  - 第 11 頁圖說、第 16 頁「OpenLDAP」小幅文字修正。
- speaker notes 45 頁（完整版 62 頁）。

## 逐頁

| 頁 | 原版頁 | Layout | 標題 |
|---|---|---|---|
| 1 | 1 | Title Slide – Leaf | VCF 9.1.1 What's New – Technical Deck（Tech Tuesday 10/5 & 10/6） |
| 2 | 2 | Agenda | Agenda |
| 3 | 3 | Section Header – Leaf | VCF Networking - NSX |
| 4 | 4 | Diagram with Outcome, Benefit | DHCP Relay on Virtual Network Appliances |
| 5 | 5 | 同上 | DTGW-EVPN: Support for Centralized Services |
| 6 | 6 | 同上 | DTGW-EVPN: Active/Active Route Controllers |
| 7 | 7 | 同上 | DTGW-EVPN: Direct Prefix Routing |
| 8 | 8 | 同上 | VLAN-backed VPCs for VCF Automation and VKS |
| 9 | 18 | Section Header – Leaf | VCF Operations（Fleet Management 副標） |
| 10 | 23 | 1_Diagram with Outcome, Benefit | Easy Password Management for OS and Application Accounts |
| 11 | 24 | 同上 | Password Policy Enforcement across the entire VCF Stack |
| 12 | 25 | 同上 | Centralized Certificate Management For All VCF Components |
| 13 | 26 | 同上 | Manage Components Configured with Non-TLS Certificates |
| 14 | 27 | 同上 | Component-managed Certificate Auto-renewal, Alerts and Guidance |
| 15 | 28 | 同上 | Real-world Configuration Management at Scale (VMware Salt) |
| 16 | 22 | 同上 | Enhanced Identity & Access (On-demand AD / OpenLDAP lookup) |
| 17 | 20 | 同上 | Faster Time to Resolution with OpenTelemetry based Observability |
| 18 | 21 | 同上 | Setup Monitoring in minutes – Import Grafana Dashboards |
| 19 | 39 | Section Header – Leaf | VCF Automation |
| 20 | 40 | 1_Diagram with Outcome, Benefit | Enabling Self-Service GitOps for App Deployments |
| 21–22 | 41–42 | 1_Title, Subtitle and Content | Centralized Argo CD management and access |
| 23 | 43 | 同上 | Easily Access Deployed ArgoCD Instances |
| 24 | 44 | 同上 | Authenticate Users for Self-Service |
| 25 | 45 | 同上 | Fine Tune and View ArgoCD Resources |
| 26 | 46 | 同上 | Self-service without privilege escalation |
| 27 | 47 | Section Header – Leaf | VMware Data Services Manager |
| 28 | 48 | Diagram with Outcome, Benefit | DSM 9.1.1 key pillars |
| 29 | 49 | 同上 | DSM now runs as a VCF Automation service |
| 30 | 50 | 同上 | DSM Health Validator |
| 31 | 51 | 同上 | PostgreSQL 18 / read replicas / extension preloading |
| 32 | 52 | 同上 | MySQL in-place 8.0 → 8.4 LTS upgrade |
| 33 | 53 | 同上 | SQL Server 2025 / gMSA / striped backups |
| 34 | 54 | Diagram with Content on Right | Better SQL Server visibility |
| 35 | 55 | Diagram with Outcome, Benefit | DSM 9.1.1 is the enterprise DBaaS for VCF |
| 36 | 56 | Section Header – Leaf | Private AI |
| 37 | 57 | 1_Four Icon | What's New in VCF Private AI Services 3.0 |
| 38–39 | 58–59 | 2_Diagram… / Generated | Hybrid Cloud LLM Support（+ 架構圖） |
| 40–41 | 60–61 | 3_Diagram… / Generated | Multi-tenant Model-as-a-Service（+ 架構圖） |
| 42–43 | 62–63 | 4_Diagram… / Generated | vSphere native plugin for Private AI Services（+ 架構圖） |
| 44–45 | 64–65 | 5_Diagram… / 2_Diagram with Content on Right | Multiple Authorization Providers |
| 46–47 | 66–67 | 6_Diagram… / Generated | Enhanced Observability: Metrics & Dashboards |
| 48 | 68 | Section Header – Leaf | Protection and Recovery |
| 49 | 69 | Diagram with Outcome, Benefit | Network Isolation Using "push button" Firewall Policies |
| 50 | 70 | Thank You / Closing - Leaf | — |

## 機密字樣

匯入時已用 `scripts/strip-confidential.sh` 清掉 14 處（全在 slideLayout 2/3/8/9/10/11/13/39/42/43；slides 與 master 0 處）。
來源檔（Downloads 裡那份）沒動，仍含這些字樣。

## 版本

- `_v1`：匯入原貌，只清 layout 層 14 處 "Proprietary and Confidential"。
- `_v2`：第 9 頁兩個白色 `x` 換成不換行空白。
- `_v3`（目前底版）：頁尾 `Broadcom Proprietary. Copyright © 2026 Broadcom.` 改為 `Copyright © 2026 Broadcom.`
  （slideMaster1 + slideLayout1 / 41，共 3 處；全 50 頁 PDF 文字擷取 0 處 Proprietary）。
