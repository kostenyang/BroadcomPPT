---
name: vcf-semiconductor
description: Create Broadcom VCF presentation decks for semiconductor / IC design / manufacturing customers (e.g. TSMC, MediaTek, ASE, UMC, Novatek). Trigger whenever the user wants a slide deck, proposal, or presentation targeting semiconductor fabs, IC design houses, OSAT companies, or manufacturing/MES environments. Also trigger for VSMC-type projects, OA/MES domain separation, factory automation, or any 半導體/晶圓廠 presentation request. Always use the official Broadcom template — never create from scratch.
---

# VCF Semiconductor Presentation Skill

Read `broadcom-ppt-base` SKILL.md first for template specs, colors, fonts, and editing workflow.
Location: `/home/claude/broadcom-ppt-skills/broadcom-ppt-base/SKILL.md`

> **⚡ 預設底版**：永遠使用 `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` (3.8MB)。  
> 只有使用者明確說「用 5.2 Master」時才改用大檔。

---

## Industry Context

Semiconductor customers have unique IT characteristics:
- **OT/IT convergence**: Fab floor (MES/OA) vs. enterprise IT are strictly separated
- **High-availability**: Tool uptime = wafer output; any downtime is extremely costly
- **Security**: IP protection is paramount — strict network segmentation
- **Scale**: Massive data volumes from process control, metrology, defect inspection

Key customer types in Taiwan:
- **Foundry/Fab**: TSMC, UMC, Powerchip, Nexchip
- **IC Design**: MediaTek, Realtek, Novatek, Aspeed
- **OSAT**: ASE, Amkor, SPIL
- **IDM**: Macronix, Winbond

---

## Recommended Deck Structure

### For OA/MES Domain Separation (VSMC-type)

1. **Title Slide** — `Title Slide – Leaf`
2. **Agenda** — 5 items
3. **Section: 客戶現況與挑戰** (Current State & Challenges)
   - OA vs. MES domain topology (Two-Content Balanced)
   - Pain points: VM sprawl, aging ESXi, no HA/DR (Comparison layout)
4. **Section: VCF 解決方案架構** (VCF Solution Architecture)
   - Management domain design (Diagram with Content on Right)
   - OA Workload Domain (Diagram with Content on Right)
   - MES Workload Domain with strict network segmentation
   - vSAN/FC storage decision (Comparison layout)
5. **Section: 升級路徑** (Upgrade Pathway) — use APJ 9.1 template section
   - Current → VCF 9.1 migration sequence
   - Offline migration strategy for DC move
6. **Section: 維運與監控** (Operations & Monitoring)
   - VCF Operations integration
   - Backup strategy (SFTP, Veeam)
   - AD/LDAP integration
7. **Big Statement** — Key business value
8. **Thank You / Closing**

### For General Semiconductor Pitch

1. Title Slide
2. Agenda
3. 半導體產業挑戰 (Industry challenges)
4. VCF 平台架構 (VCF platform)
5. 關鍵使用案例 (Key use cases): Private AI, GPU workloads, container workloads
6. 參考架構 (Reference architecture)
7. 升級路徑
8. 客戶成功案例 (Customer Success layout)
9. Closing

---

## Key Messages for Semiconductor

| Pain Point | VCF Answer |
|------------|-----------|
| OA/MES 域分離困難 | VCF Workload Domains — 完全隔離的管理邊界 |
| vSphere 版本老舊，升級風險高 | 標準化升級路徑，LCM 自動化 |
| GPU 工作負載 (EDA simulation) | vGPU + VKS，支援 NVIDIA AI Enterprise |
| 跨 DC 高可用 | vSAN Stretched Cluster + Live Recovery |
| 設備數據分析 AI 化 | VCF + Private AI Foundation |
| 嚴格的網路隔離 | NSX micro-segmentation + vDefend |

---

## Architecture Diagram Notes

When drawing OA/MES topology:
- **OA Domain**: Connected to fab floor equipment (SEMI E10/E30 standard tools)
- **MES Domain**: Connected to manufacturing execution system (SAP ME, WorkStream)
- **Management Domain**: Isolated, no direct fab floor access
- **DMZ Layer**: Controlled crossing between OA ↔ Enterprise
- Cross-VC vMotion: Only for planned maintenance, requires DMZ crossing approval

Storage recommendation:
- Management Domain: vSAN ESA (NVMe)
- OA Workload Domain: FC SAN (for Oracle DB, legacy tool integration)
- MES Workload Domain: vSAN OSA or FC depending on existing infrastructure

---

## Slide Color Recommendation

Use **Leaf (Teal/Green)** theme — conveys precision, technology, reliability.
- Primary: `#007A86` (Teal)
- Supporting: `#61A00A` (Green) for positive metrics
- Warning/callout: `#EDB516` (Gold)
- Dark slides: `#1B1E35` (Navy)

---

## Common Slides to Reuse from Template

From VCF 5.2 Master:
- Slide 8–20: VCF conceptual overview — adapt for semiconductor context
- Slides on NSX micro-segmentation
- vSAN ESA performance slides
- Lifecycle Management (LCM) slides

From APJ 9.1 Upgrade:
- Upgrade scenario tables (What's supported / not supported)
- VCF 5.2 → 9.1 upgrade flow diagrams
- IP/DNS requirements slides

---

## Speaker Notes Guidelines (中文)

- 強調 OT/IT 融合的重要性，以及 VCF Workload Domain 如何實現真正的邊界隔離
- 提及 VSMC 等台灣半導體客戶的實際案例（不點名具體細節）
- 升級章節：強調 zero-downtime 升級路徑與 LCM 自動化的商業價值
- 安全章節：強調 IP 保護、vDefend 東西向流量管控
