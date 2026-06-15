---
name: vcf-ebc
description: VMware Cloud Foundation 9 EBC (Executive Briefing Center) / 客戶高階簡報製作 skill。完整 52-slide EBC 範本，涵蓋 The Value of Private Cloud、VCF 平台介紹、Modern Applications、Cost Control (52% lower TCO / 34% lower infra cost / 61% faster deploy)、PCMO (Private Cloud Modernization Program：Assess/Accelerate/Achieve + Cloud Maturity Model)、Customer Success Stories、VCF 9 核心創新 (NVMe Memory Tiering、vSAN ESA Global Dedupe、Native VPC multi-tenancy、Fleet Management、VCF Import)、Advanced Services (Private AI Foundation with NVIDIA、Live Recovery、vDefend、AVI Load Balancer、Data Services Manager)，並含 Click-Through Demo 與 Whiteboard 章節。當使用者要做 VCF 9 高階主管/CIO-level 簡報、EBC、客戶價值論述、私有雲價值 pitch、whiteboard session 時觸發。
---

# VCF 9 EBC / Customer Deck Skill

先讀 `vcf-base` SKILL.md (template specs、顏色、字體、編輯流程)。

> **⚡ 底版**：本 skill 以原始來源檔 `VCF9 - EBC and Customer Deck.pptx` (52 slides) 為基礎範本。
> 下載：`https://raw.githubusercontent.com/kostenyang/BroadcomPPT/main/VCF9%20-%20EBC%20and%20Customer%20Deck.pptx`
> 注意原檔標示 **LIMITED USE / Work in Progress** — 對外簡報前移除 disclaimer 並更新 revision date。

---

## 簡報定位

VCF 9 的 **Executive Briefing Center (EBC)** 主力簡報，聽眾為 **CIO / V-level / CIO-1**。
依場景挑選章節 (原檔 slide 1 "How to Use This Presentation" 有建議組合)：

- **Section 1 (多數 EBC 推薦)**：Value of Private Cloud → VCF 介紹 → Modern Apps → Cost Control → PCMO → Customer Stories
- **Deep Dive**：VCF 9 核心創新 + Advanced Services
- **Interactive**：Click-Through Demo + Whiteboard Session

---

## 推薦簡報結構 (對應原檔 52 slides)

### 開場 (1–3)
1. How to Use This Presentation (內部導引，對外刪除)
2. Disclaimer (對外場景移除或保留 Legal 版本)
3. VCF 9 封面

### Section 1 — Value of Private Cloud (4–17)
4. Today's Reality — Data Center Silos Slow Innovation (42% higher ops cost / 40% more server footprint / 34% higher infra cost)
5. Public Cloud Unified the Silos (Automation / Agility / Self-Service)
6. …but Higher Cost (39% migration expensive / 51% privacy concern / data sovereignty)
7. The Best of Both Worlds — Cost-Control + Flexible + Sovereign = True Private Cloud
8. **VCF 平台架構** — Compute / Storage / Networking / Automation & Operations + Containers/K8s/VMs；Customer Managed (on-prem/edge) + Provider Managed (public/partner)
9. A Story of Continuous Innovation (2000s vSphere → 2010s SDDC → 2020s Private Cloud + Private AI)
10. What VCF Delivers — Cloud Operating Model / Modern Infra / Self-Service
11. Business Value — 61% Faster deploy / 34% Lower cost / 66% Quicker data-loss recovery (IDC)
12. 52% Lower TCO running VMs + Containers；1.5x VM density；native K8s runtime
13. Operate Cost-Efficiently — Cost Visibility / Predictive Modelling / Resource Reclamation / Chargeback
14. **PCMO — Private Cloud Modernization Program**：①Assess ②Accelerate (Jumpstart Workshops) ③Achieve (Free Learning + VCF Certification)
15. Cloud Maturity Model — Step 1 Assessment
16. **Customer Success at Scale** — Banking / Private AI / Modern apps / Factory Automation / Sovereign cloud / Edge
17. Let's Talk — Whiteboard Session (Goals / Challenges / Blockers)

### VCF 9.0 Platform Deep Dive (18–28)
18–19. VCF 9.0 統一平台架構 (Automation & Operations / NSX / vSphere / vSAN / Modern Cloud Interface / Tenant Management)
20. The Fundamental Shift — One interface for ops；One interface for consumption；Run K8s+VMs+traditional natively；Sovereign & secure
21. New Build & Operate Experience — Quick Start App / Governance / SecOps / Proactive Diagnostics
22. Tenant Management — Resource allocation / Identity / Cloud Governance
23. Run Containers, VMs & Traditional Apps Natively
24. Sovereign, Secure & Compliant as a Platform — Zero Trust / Guardrails
25. Infrastructure Cost Visibility — track / breakdown / optimize
26. Modernize, Consume & Protect
27. Modernize Your Infrastructure — Fleet Management / VCF Installer / VCF Import / Chargeback / VCF Operations Console
28. VCF 9.0 Core Innovation — 40% more consolidation (Memory Tiering NVMe) / 34% lower TCO (vSAN ESA Global Dedupe) / 3x switching (NSX Enhanced Data Path)

### Section — Advanced Services (29–36)
29. Advanced Services for VCF (總覽)
30. 服務地圖 — Advanced Security / Data Services / Load Balancing / App Services / DR & Ransomware / Private AI / Network Observability / Secure Access
31. **VMware Private AI Foundation with NVIDIA** — Resource Sharing / Policy & Control / Lower TCO / Centralized Ops
32. **VMware Live Recovery** — Cyber + DR，含 Isolated Clean Room (75% faster recovery)
33. **VMware vDefend** — NDR / Distributed Firewall / IPS / Malware prevention
34. **VMware AVI Load Balancer** — 10x fewer devices / 90% faster deploy
35. **VMware Data Services Manager** — PostgreSQL+pgvector / MySQL / RabbitMQ / Valkey
36. VCF — The Future of Private Cloud (Start on the Path Today)

### Demo & Backup (38–52)
- 38–50：VCF 9 Click-Through Demo (Build & Operate: VCF Import / Fleet Mgmt / Config Drift / Certificates / SecOps；Consume: Tenants / VPCs / Self-Service Catalog / Kubernetes / Cost Control)
- 51. One Platform for Operations & Automation 總結

---

## Key Messages

| 主題 | 關鍵訊息 / 數字 |
|------|----------------|
| Private Cloud Value | Best of both worlds：Cost-Control + Flexible + Sovereign |
| TCO | 52% lower TCO (VM+container)、34% lower infra cost |
| 速度 | 61% faster deploy、66% quicker data-loss recovery |
| 整併 | 40% more server consolidation (NVMe Memory Tiering) |
| 儲存 | 34% lower TCO with vSAN ESA Global Dedupe |
| 網路 | 3x switching performance (NSX Enhanced Data Path) |
| Modernization | PCMO：Assess → Accelerate → Achieve |
| Advanced | Private AI / Live Recovery / vDefend / AVI / DSM |

---

## 簡報語氣 (給高階主管)
- 開場用 IDC/Forrester 數字點出「silo 成本高 + 公雲不夠主權」雙痛點
- 主軸落在 business outcome (TCO / agility / sovereignty)，技術細節留 deep dive
- Customer Success 章節務必客製成在地案例 (可搭配 `vcf-cxs`)
- 收尾導向 PCMO 與 Whiteboard Session 作為下一步
