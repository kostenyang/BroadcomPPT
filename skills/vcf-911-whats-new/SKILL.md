---
name: vcf-911-whats-new
description: Build Broadcom VCF 9.1 / 9.1.1 "What's New" sales-overview decks from the official 46-slide VCF_9.1_Whats_New_Sales_09.30.26 template (Sept 2026) — a 9.1.1 Updates section plus 9.1 GA features in four pillars, each feature slide with a Customer Benefits panel and English talk track. Trigger for VCF 9.1.1 新功能 / 9.1.1 What's New / 9.1.1 更新簡報, 業務版新功能簡報, sales overview, 客戶新版本介紹, release update briefing, or slides on 9.1.1 items (Multi-Tenant Model Sharing, AI Assistant for VCF, GitOps Service / Argo CD, EVPN enhancements, VKS 3.7 add-ons) or 9.1 features (NVMe memory tiering, vSAN global dedup, real-time observability, 500 VKS clusters, 5,000-host fleet, ZTP, Fast Deploy, S3 object storage, SQL DBaaS, vSAN for Recovery, QAT vMotion, cyber recovery, TPM live patching, vDefend, Avi, CrowdStrike, AMD MI350). L200–L300 Tech Tuesday deep-dives → vcf-whats-new; upgrade paths → vcf-upgrade. Always clone from the bundled template — never create from scratch.
---

# VCF 9.1 / 9.1.1 What's New — Sales Overview Skill

Read `vcf-base` SKILL.md first for colors, fonts, the clone-slide workflow and 對內/對外 rules.

> **⚡ 底版**：`VCF_9.1_Whats_New_Sales_09.30.26.pptx`（46 slides，16.9MB，Broadcom VCF Division，September 2026 · V 9.30.26）
> Download: `https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/VCF_9.1_Whats_New_Sales_09.30.26.pptx`
> 工具：`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/scripts/clone-slide.py`、`.../scripts/set-hant-font.py`
> 每頁可改欄位與 shape id：`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/skills/vcf-911-whats-new/references/slide-map.md`（或 `scripts/clone-slide.py list <deck> --slide N --shapes` 重產）

**Guardrail**：產出任何簡報前，先問「這次範圍是否包含 NSX Edge cluster（Edge nodes / T0-T1 gateway）」，確認後才動手。答案會影響 EVPN 兩頁的講法：slide 10（9.1.1 EVPN：Transit Gateway 直連 leaf switch）與 slide 42（9.1 EVPN Unified Fabric，原文寫 "reducing reliance on NSX Edge"）。客戶有 Edge cluster 時，42 的這句話要講成演進選項，不要講成取代；細節先查 TechDocs 再寫。

---

## 這份 deck 是什麼

**業務 / 客戶等級的版本差異簡報**（"Sales Overview"）。重點是「這版多了什麼、對客戶有什麼好處」，不是 L300 技術細節。

```
開場 1–4 → [A] 9.1.1 Updates 5–11 → [B] 9.1 GA 總覽 12–16
        → [C] 支柱1 Efficient Infrastructure 17–24
        → [D] 支柱2 High Velocity App Delivery 25–32
        → [E] 支柱3 Cyber Resilience & Data Security 33–40
        → [F] 支柱4 Open Ecosystem 41–44 → Advanced Services 45 → Thank You 46
```

**Feature 頁的固定版型**（7–11、18–24、26–32、34–40、42–44）：
標題 + 副標（placeholder）· 右上 badge 膠囊 · 左側示意圖或產品截圖 · 右側 "Customer Benefits" 面板（2–4 項「粗體開頭 + 內文」）· 英文講者備註（Challenges → What's new → Benefits）。

**支柱封面頁**（6、17、25、33、41）：左側大圖 + 支柱名，右側三項「標題 + 一段說明」。

---

## 頁面地圖（摘要；shape id 見 references/slide-map.md）

| 區段 | 頁 | 功能（標 TP = Tech Preview、AS = Advanced Service 另購） |
|------|----|------|
| 開場 | 1 Disclaimer · 2 封面 · 3 VCF 9 平台全貌 · 4 VCF 9 成果數字 | |
| **A. 9.1.1 Updates** | 5 Section · 6 三主軸 | 7 Multi-Tenant Model Sharing · 8 AI Assistant for VCF（TP）· 9 GitOps Service / Argo CD（TP）· 10 EVPN Architectural Enhancements · 11 VKS 3.7 Add-on Framework |
| B. 9.1 GA 總覽 | 12 Section · 13 Messaging Themes · 14 Private AI 平台 · 15 Key Features 清單 · 16 Measurable Outcomes | |
| C. Efficient Infra | 17 封面 | 18 NVMe Memory Tiering · 19 vSAN Global Dedup + DaR Encryption · 20 Real-Time Observability · 21 VKS 500 clusters/Supervisor · 22 Fleet 5,000 hosts / 256 平行升級 · 23 ZTP（vSphere Elastic Provisioning）· 24 Topology Aware Scheduler |
| D. High Velocity App | 25 封面 | 26 Fast Deploy（VKS/VM）· 27 Container as a Service · 28 vSAN Native S3（TP）· 29 Tanzu Marketplace（AS）· 30 Private AI Model & GPU Metrics · 31 App Stack Formation · 32 SQL Server DBaaS（AS，DSM） |
| E. Cyber Resilience | 33 封面 | 34 vSAN for Recovery · 35 Encrypted vMotion w/ Intel QAT · 36 On-Prem Cyber Recovery（AS）· 37 ACC Continuous Compliance（AS）· 38 Live Patching for TPM Hosts · 39 vDefend Self-Service Lateral Security（AS）· 40 Avi Automated LB（AS） |
| F. Open Ecosystem | 41 封面 | 42 EVPN Unified Fabric（Cisco/Arista/SONiC）· 43 CrowdStrike EDR for RWR · 44 AMD MI350 DirectPath I/O |
| 結尾 | 45 Advanced Services 目錄 · 46 Thank You | |

---

## 常見組合

| 需求 | 保留頁（照順序） |
|------|------------------|
| **9.1.1 更新簡報**（客戶已了解 9.1） | 1, 2, 5, 6, 7, 8, 9, 10, 11, 46 |
| **完整 9.1 + 9.1.1 Sales Overview** | 全部 1–46 |
| **30 分鐘精簡版** | 1, 2, 3, 5, 6, 7, 10, 12, 15, 16, 18, 21, 26, 34, 38, 42, 45, 46 |
| **只講 9.1 GA** | 1, 2, 3, 12–45, 46 |
| **單一支柱 deep-dive** | 1, 2, 13（主題定位）, 該支柱封面 + feature 頁, 46 |
| **AI 主題** | 1, 2, 5, 6, 7, 8, 14, 21, 26, 30, 44, 46 |
| **維運 / 規模** | 1, 2, 8, 12, 17, 20, 22, 23, 24, 38, 46 |
| **資安 / 韌性** | 1, 2, 33, 34, 35, 36, 37, 38, 39, 43, 45, 46 |
| **網路** | 1, 2, 10, 42, 39, 40, 46（先過 Guardrail） |

產業切角（只挑頁，內容維持通用產業寫法；產業細節搭 `vcf-financial` / `vcf-telecom` / `vcf-semiconductor`，見 `vcf-router` 組合規則）：
- 金融：支柱 E（cyber recovery、ACC 對 PCI DSS、live patching）＋ 7（多租戶模型共用、資料隱私）
- 電信 / VCSP：10、42（EVPN）、21（VKS 規模）、22（fleet 規模）、23（ZTP）、11（add-on 生態）
- 半導體 / 製造：23（ZTP 大量站點）、24（拓撲感知排程）、18（NVMe tiering 降成本）、44（AMD GPU）

---

## 建置流程

```bash
# 0. 取範本與工具（scripts/ 在同一個 repo）
curl -LO https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/VCF_9.1_Whats_New_Sales_09.30.26.pptx
# 1. 依上表挑頁，順序照給的順序（頁碼 = 範本原始頁碼）
python3 scripts/clone-slide.py keep VCF_9.1_Whats_New_Sales_09.30.26.pptx --slides 1,2,5,6,7,8,9,10,11,46 --out deck.pptx
# 2. 看某頁有哪些欄位（keep 之後用新頁碼；shape id 不變）
python3 scripts/clone-slide.py list deck.pptx --slide 5 --shapes
# 3. 封面
python3 scripts/clone-slide.py settext deck.pptx --slide 2 --out deck.pptx \
    --title "What's New in VMware Cloud Foundation 9.1.1" --subtitle "<客戶> 新版本功能說明" \
    --set "body:4=2026 年 10 月"
# 4. Feature 頁：標題 / 副標 / badge / Customer Benefits
python3 scripts/clone-slide.py settext deck.pptx --slide 5 --out deck.pptx \
    --title "Share AI Models Securely Across Teams" \
    --subtitle "跨事業單位安全共用 AI 模型，兼顧資料隱私與 GPU 成本" \
    --shape "6251=降低基礎架構成本::多個事業單位共用同一套模型堆疊，不必每個租戶各建一套。|自助式存取::單一管理平面統一控管存取與政策。|資料隱私內建::租戶隔離的存取控制，不暴露敏感訓練資料。"
# 5. 支柱封面頁的三項：每項 "標題|內文"
python3 scripts/clone-slide.py settext deck.pptx --slide 4 --out deck.pptx \
    --shape "6232=加速 AI 導入與維運|跨團隊安全共用 AI 模型，並以 AI 診斷縮短 MTTR。"
# 6. 繁中字型（這份 theme 的 Hant 是新細明體）→ 微軟正黑體
python3 scripts/set-hant-font.py deck.pptx deck.pptx
# 7. QA
soffice --headless --convert-to pdf deck.pptx && pdftoppm -r 50 -png deck.pdf qa
```

### 改字規則

- **選圖已經對的頁再改字**。左側示意圖 / 截圖不會跟著改，不要拿 EVPN 的頁去講 S3。
- **`--shape` 格式**：`id=項目1|項目2|…`；`粗體開頭::內文` 會沿用原框的粗體/一般字樣式、原框的段落間距（空白段或 spcBef）與「粗體換行接內文」格式。第 N 項套原框第 N 段的樣式，項目多於原框時沿用最後一段。
- **Customer Benefits**：維持 2–4 項，每項粗體開頭 ≤ 15 字、內文 ≤ 45 字（中文）；超過會擠出面板。
- **Badge**：≤ 30 個英文字元或 ≤ 12 個中文字，通常保留英文功能名。
- **中英雙語**（依 vcf-base）：標題保留英文功能名；副標、Customer Benefits 可改中文；英文技術名詞（VKS、Supervisor、EVPN、vSAN、Argo CD、MTTR）不翻。
- 封面版號（body:4 的 "V 9.30.26"）是 Broadcom 版控，對外版改成日期即可。
- 不支援 markdown；`**粗體**` 會原樣印出。局部粗體用 `::`。

### 講者備註

每張 feature 頁都有英文 talk track（結構：Customer Challenges → 功能 → Benefits）。
- 對內 enablement：保留，可補中文 conclusion-first 摘要在前面。
- 客製給客戶講：改成中文 talk track，保留原結構，數字與原文一致。
- 對外交付（PDF / 寄給客戶）：依 vcf-base 移除講者備註；**slide 1 Disclaimer 保留**（含 TP 與產品方向內容）。

---

## 內容事實（範本原文；客製時照用，不要自己改數字）

**9.1 與 9.1.1 不要混講**：7–11 是 **9.1.1** 新增；12–45 是 **9.1 GA**。EVPN 與 Cisco/Arista/SONiC 互通是 9.1（slide 42），9.1.1 是在其上的架構強化（slide 10）。

**9.1.1（7–11）**
- Multi-Tenant Model Sharing：跨租戶 / 事業單位安全共用 AI 模型，共用模型堆疊（fewer GPUs, fewer stacks），租戶隔離存取控制。
- AI Assistant for VCF **[Tech Preview]**：Conversational Diagnostics（白話英文查問題、降 MTTR）、Intelligent Health Visibility（跨 vSphere 與 VCF 管理服務做主動告警關聯）、Management Packs Builder（AI 產生 management pack，不需 API 專業）。
- GitOps Service **[Tech Preview]**：Argo CD 成為 VCF Automation 內建服務，自助部署 Argo CD instance；OIDC 認證整合 VCF Automation。
- EVPN 強化：Transit Gateway 與 leaf switch 直接 datapath（East-West 最佳化）；EVPN 支援 NAT、NSX 與 Avi LB、DHCP Relay；可經 VCF Automation 自助部署與消費。
- VKS 3.7 Add-on 管理框架，四層支援：Product（Broadcom 管 lifecycle + runtime）、Partner（TAP 認證，Broadcom 管 lifecycle、ISV 管 runtime）、Community（Broadcom 管 lifecycle、runtime 由社群）、Bring Your Own（客戶自理）。範例：Antrea / Velero、Cilium / Headlamp。

**9.1 GA 數字**（官方註腳：Broadcom 內部估算或測試，2026/4，可能變動；5x 來自 Principled Technologies 2026/3）
- NVMe Memory Tiering：server 成本最多降 **40%**；NVMe 軟體 mirroring、裝置健康與耗損可視化。
- vSAN：Global Dedup 可與 Data-at-Rest Encryption 同時啟用、不影響 dedup ratio；TCO 最多降 **39%**（vs 外接儲存陣列）。
- VKS：每個 Supervisor 最多 **500** 個 VKS cluster（原 190，**2.6x**）；Fast Deploy（linked clone）新建 cluster 最多快 **70%**、升級快 **75%**；Containers 密度 / scaling **5x**（vs 競品）。
- Fleet：每個 instance **5,000** ESX hosts（9.0 為 2,500）；平行升級 **256** clusters（9.0 為 64，**4x**）。
- Real-time observability：秒級 telemetry 取代分鐘級 polling，涵蓋 vCenter、ESXi、vSAN、NSX。
- ZTP（vSphere Elastic Provisioning）：裸機以 UEFI HTTP/S 網路開機自動部署 ESX，數百站點平行、免派工到現場。
- Topology Aware Scheduler：針對高核心數 CPU 的 NUMA / cache / memory 排程（DRS-like 模型）。
- vSAN Native S3 Object Storage **[Tech Preview in 9.1.x]**：多租戶自助 S3；TCO 最多降 **34%**（vs 專用物件儲存）。
- Private AI Model & GPU Metrics：VCF Operations 與 PAIS UI 顯示 agents running、MCP servers 數、tokens/sec、KV cache usage。
- Encrypted vMotion + Intel QAT：vMotion 時 CPU 最多省 **70%**。
- Live Patching for TPM-enabled hosts：免 evacuate 修補，最多涵蓋 **80%** 安全修補情境。
- vDefend：VKS 可受 distributed IDS/IPS 保護；"Turbo mode" IDPS 最高 **9 Tbps**；firewall conversion tool 為 **Tech Preview**。
- AMD Instinct MI350：Enhanced DirectPath I/O（支援 Snapshot、vSphere HA、Live Patch、Storage vMotion、hot add/remove）；**GPU 虛擬化與 vMotion 在未來版本**，不要講成已支援。

**另購 Advanced Services**（slide 15 註腳 2 與各頁註腳）：Tanzu Platform / Marketplace（29）、Data Services Manager / SQL DBaaS（32）、Advanced Cyber Compliance / On-Prem Cyber Recovery / Continuous Compliance（36、37）、vDefend（39）、Avi（40）、slide 45 整頁目錄。報價或提案時明講需另購，不要包進 VCF 授權。

範本以外的數字、版本支援矩陣、GA 時程，先查 Broadcom TechDocs / KB / Release Notes 再寫，並在備註標示來源。

---

## 與其他 skill 的分工

| 需求 | 用哪個 |
|------|--------|
| 這版多了什麼、業務 / 客戶等級（9.1 GA + 9.1.1） | **本 skill** |
| vSphere / vSAN 功能的 L200–L300 技術 deep-dive（Tech Tuesday） | `vcf-whats-new` |
| 怎麼升級到 9.1、升級路徑 | `vcf-upgrade` |
| VCF 9 平台價值（非版本差異）、高階主管 | `vcf-ebc` / `vcf-summary` |
| VCF Automation 9.1 deep-dive | `vcf-automation` |
| 官方 150 頁總覽挑章節 | `vcf-tech-deck:vcf-tech-deck` |
