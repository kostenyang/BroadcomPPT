---
name: vcf-telecom
description: Create Broadcom VCF presentation decks for telecom / ISP / VCSP customers — telcos, mobile operators, and cloud service providers (e.g. 中華電信 CHT, 台灣大哥大 TWM, 遠傳 FET, 台灣之星). Trigger whenever the user wants a presentation for 電信業, VCSP, VCD (VMware Cloud Director), NFV, OpenStack migration, 5G core, or any telecom/ISP customer. Also trigger for CHT migration from OpenStack to VCF, VCSP multi-tenant cloud, or telecom cloud transformation topics. Always use official Broadcom template — never create from scratch.
---

# VCF Telecom Presentation Skill

Read `broadcom-ppt-base` SKILL.md first for template specs, colors, fonts, and editing workflow.
Location: `/home/claude/broadcom-ppt-skills/broadcom-ppt-base/SKILL.md`

> **⚡ 預設底版**：永遠使用 `APJ__Tech__Upgrade_Pathways_to_VCF_9_1-Slides.pptx` (3.8MB)。  
> 只有使用者明確說「用 5.2 Master」時才改用大檔。

---

## Industry Context

Taiwan telecom operators have distinct IT/network profiles:
- **VCSP (VMware Cloud Service Provider)**: Licensed to resell VCF-based cloud services
- **VCD (VMware Cloud Director)**: Multi-tenant cloud portal for enterprise customers
- **NFV (Network Function Virtualization)**: vRAN, vEPC, vIMS running on vSphere
- **OpenStack Legacy**: Many telcos built private cloud on OpenStack — now migrating to VCF
- **5G Core**: Cloud-native NFs require Kubernetes (VKS) + bare metal performance

Key customers in Taiwan:
- **Tier 1**: 中華電信 (CHT) — largest VCSP in Taiwan; OpenStack migration project
- **Tier 2**: 台灣大哥大 (TWM), 遠傳電信 (FET), 台灣之星 (TSTAR)
- **ISP/DC**: 數位聯合 (ISP), 是方電訊, iForte
- **Government Telco**: 中華電信研究院 (CHT Lab)

---

## Recommended Deck Structure

### For CHT / OpenStack → VCF Migration

1. **Title Slide** — `Title Slide – Aqua`
2. **Agenda**
3. **Section: OpenStack 現況痛點**
   - 運維複雜度高 (Neutron/Nova/Cinder 各自為政)
   - 版本升級困難，社群支援縮減
   - 多租戶效能隔離問題
   - 客戶自助服務體驗不佳
4. **Section: VCF + VCD 解決方案**
   - VCF 平台架構 (Management + Provider VDC)
   - VMware Cloud Director 多租戶入口
   - 與 OpenStack 功能對比表 (Comparison layout)
5. **Section: 遷移策略**
   - HCX bulk migration (VM cold/warm migration)
   - 網路切換策略 (VLAN → NSX Overlay)
   - 分階段遷移計劃 (Phased migration Gantt)
6. **Section: VCSP 商業模式**
   - 授權結構 (BSC VCSP program)
   - 計費/Chargeback 模型
   - 企業客戶 SLA 承諾
7. **Section: 升級路徑** (APJ 9.1 template)
8. **Closing**

### For 5G Core / NFV Modernization

1. Title Slide
2. 5G 核心網路虛擬化架構挑戰
3. VCF 平台支援 CNF/VNF 並存
4. VKS (Kubernetes) 支援 Cloud-Native NF
5. 效能保證：SR-IOV, DPDK, vRDMA
6. 網路切片 (Network Slicing) with NSX
7. 升級路徑
8. Closing

### For General VCSP Cloud Service Pitch

1. Title Slide
2. VCSP 商機與市場趨勢
3. VCF + VCD 架構圖
4. 多租戶隔離架構
5. 服務目錄 (Service Catalog)
6. 差異化競爭優勢 vs. AWS/Azure
7. 案例分享
8. Closing

---

## Key Messages for Telecom

| Customer Pain | VCF Answer |
|---------------|-----------|
| OpenStack 運維成本高 | VCF 整合架構，SDDC Manager 統一管理 |
| 多租戶隔離不足 | VCD Provider/Org VDC + NSX T1/T0 隔離 |
| 5G CNF 需要 K8s | VKS (原生 K8s) + GPU 支援 |
| NFV 效能不足 | SR-IOV, DPDK pass-through, NUMA pinning |
| 雲服務差異化困難 | VCD 自助服務入口 + API 自動化 |
| CapEx/OpEx 壓力 | BSC 授權簡化 + 超額訂閱最佳化 |
| DR 服務商機 | Live Recovery + SRM 作為增值服務 |

---

## OpenStack vs. VCF Comparison Slide

Use **Comparison** layout (Layout 18):

| 面向 | OpenStack | VMware VCF |
|------|-----------|-----------|
| 管理複雜度 | 高 (多個獨立元件) | 低 (SDDC Manager 統一) |
| 升級難度 | 極高，需停機 | LCM 滾動升級，不停機 |
| 多租戶隔離 | Neutron 租戶網路 | NSX T1/T0 + vDefend |
| K8s 支援 | 需自建 Magnum | VKS 原生整合 |
| 企業支援 | 社群 + 商業版本 | Broadcom 全球支援 |
| 生態系整合 | 有限 | vSphere/NSX/vSAN 深度整合 |

---

## Architecture Diagram Notes

For VCSP/VCD topology:
- **Provider Layer**: VCF Management Domain + Provider VDC
- **Tenant Layer**: Org VDC per enterprise customer
- **Network**: External network (BGP uplink) → T0 Router → T1 per tenant
- **Storage**: vSAN per cluster, or shared NFS for VCD catalog
- **Portal**: VCD portal (self-service) + API (automation)

For CHT OpenStack migration:
- Show parallel operation period (VCF + OpenStack coexist)
- HCX connector in OpenStack side, HCX cloud in VCF side
- VLAN-backed → NSX Overlay migration sequence

---

## Slide Color Recommendation

Use **Aqua** or **Leaf** theme:
- CHT: Aqua blue (`#005B84`) — matches CHT brand
- TWM: Plum (`#6C4B8F`) — differentiation
- Generic VCSP: Leaf green (`#007A86`) — innovation

---

## Speaker Notes Guidelines (中文)

- CHT 專案：強調從 OpenStack 遷移的 ROI，以運維人力節省為主軸
- VCSP 章節：強調 VCD 的自助服務能力是 CHT 與競品 (AWS/Azure) 差異化的關鍵
- 5G 章節：強調 VKS 支援 Cloud-Native NF，同時 vSphere 仍可運行傳統 VNF
- 升級章節：強調 LCM 的 Day 2 價值，不只是 Day 0 部署
- 結尾：建議 CHT 的 PoC 場景：選一個 OpenStack tenant 做平行遷移驗證
