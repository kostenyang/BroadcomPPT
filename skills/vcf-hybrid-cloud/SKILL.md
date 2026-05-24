---
name: vcf-hybrid-cloud
description: Create Broadcom VCF hybrid/multi-cloud presentation decks covering on-premises VCF with public cloud extensions (GCVE, AVS, VMC on AWS), HCX migration, cross-site DR, and multi-site topologies. Trigger whenever the user wants a presentation on 混合雲, 多雲, hybrid cloud, GCVE, HCX, cloud bursting, 內雲/外雲/公雲, multi-site VCF, or any architecture spanning on-prem + public cloud. Also trigger for GBP全行平台擴充案 or any project combining VCF with GCP/Azure/AWS. Always use official Broadcom template — never create from scratch.
---

# VCF Hybrid/Multi-Cloud Presentation Skill

Read `broadcom-ppt-base` SKILL.md first for template specs, colors, fonts, and editing workflow.
Location: `/home/claude/broadcom-ppt-skills/broadcom-ppt-base/SKILL.md`

---

## Industry Context

Hybrid cloud is the dominant architecture pattern in Taiwan enterprises:
- **內雲 (Private Cloud)**: On-premises VCF — primary compute, sensitive data
- **外雲 (Managed/Co-location)**: VCF at co-lo DC (CHT IDC, 數位聯合, iForte)
- **公雲 (Public Cloud)**: GCVE, AVS, VMC on AWS — burst, DR, global reach

Key use cases driving hybrid cloud adoption:
- **DR to Public Cloud**: Replace secondary DC with GCVE for cost reduction
- **Cloud Bursting**: Overflow non-sensitive workloads to GCVE during peak
- **Global Expansion**: Tokyo/Singapore GCVE for Japan/SEA market reach
- **Migration**: HCX as migration highway (on-prem → cloud)

---

## Multi-Site Topology Patterns

### Pattern A: 台北 + DR (GCVE Tokyo)
- Primary: On-prem VCF (台北)
- DR: GCVE Tokyo (日本)
- Connectivity: CHT/TWM cloud exchange + Google Cloud Interconnect
- Use case: Financial services (離岸備援), Manufacturing

### Pattern B: 台北 + 台南 + Singapore (GCVE)
- Primary: VCF 台北
- Secondary: VCF 台南 (active-active)
- Public: GCVE Singapore (burst + global)
- Use case: Large enterprise, global operations

### Pattern C: 頭份 + 七賢 (雙機房 active-standby)
- Both sites on-prem VCF
- Stretched cluster or SRM replication
- Use case: Manufacturing, conservative compliance

### Pattern D: 台北 + 東京 GCVE (Hybrid)
- On-prem VCF + GCVE Japan Region
- HCX connects both
- Use case: Japanese subsidiaries, global enterprise

---

## Recommended Deck Structure

### For Hybrid Cloud Architecture Proposal

1. **Title Slide** — `Title Slide – Plum` (multi-cloud = innovation)
2. **Agenda**
3. **Section: 混合雲趨勢與挑戰**
   - Why hybrid (regulatory + agility)
   - Pain: Data gravity, latency, cost unpredictability
   - Taiwan market: FSC allows GCVE as DR target since 2022
4. **Section: Broadcom 混合雲架構**
   - 內雲/外雲/公雲 三層架構圖 (Diagram with Content)
   - VCF on-prem + GCVE topology
   - HCX connectivity (WAN Opt, Network Extension, Mobility)
5. **Section: HCX 遷移與延伸**
   - HCX deployment components (HCX-IX, HCX-NE, HCX-WO, HCX-MON)
   - Migration modes: bulk / cold / vMotion / RAV
   - Network extension: stretch VLAN to GCVE
   - OSAM constraints (GPU VMs, RDM, large memory)
6. **Section: DR 與 Business Continuity**
   - Live Recovery (VCDA) RPO/RTO SLA
   - SRM orchestration
   - vSAN Stretched Cluster (zero RPO)
   - Runbook automation
7. **Section: 升級路徑** (from APJ 9.1 template)
   - Current VCF version → 9.1
   - GCVE compatibility matrix
8. **Big Statement** — TCO comparison (on-prem DR DC vs. GCVE DR)
9. **Closing**

### For GBP 全行平台擴充案

1. Title: GBP 平台架構擴充提案
2. 現有架構回顧 + 擴充需求
3. VCF 擴充設計 (新增 Workload Domain / ESXi hosts)
4. 網路設計更新 (NSX segment / T1 addition)
5. 儲存擴充 (vSAN capacity / FC zoning)
6. 遷移與上線計劃
7. Closing

---

## Key Messages for Hybrid Cloud

| Customer Pain | VCF Answer |
|---------------|-----------|
| DR 機房 CapEx 昂貴 | GCVE 按需付費，替代第二機房 |
| 工作負載遷移困難 | HCX 零停機遷移，保留 IP/MAC |
| 公私雲管理工具不統一 | VCF Operations 統一監控 on-prem + GCVE |
| 公雲成本不可控 | HCX + VCF 混合，敏感資料留地端 |
| 網路延伸複雜 | HCX NE (Network Extension) 自動延伸 VLAN |
| 合規：資料不出境 | GCVE 台灣 region (彰化) 已開放 |

---

## Architecture Diagram Conventions

For multi-site diagrams, always show:
```
[Site A: 台北 VCF]          [Site B: 台南/東京 GCVE]
  Management Domain    ←→     GCVE SDDC
  Workload Domain      HCX    Workload VMs
  NSX T0/T1           ←→     NSX T0/T1
  vSAN               WAN     vSAN
       ↕                          ↕
  [Underlay Network: CHT MPLS / Google Interconnect]
```

HCX component placement:
- HCX Manager: Management Domain vCenter
- HCX-IX (Interconnect): Each site (pair)
- HCX-NE (Network Extension): Source site
- HCX-WO (WAN Opt): Optional for bandwidth optimization
- HCX-MON (Mobility Optimized Networking): For stretched IP

OSAM limitations to call out:
- ❌ GPU passthrough VMs cannot be vMotion migrated
- ❌ RDM (Raw Device Mapping) not supported
- ❌ VMs > 100GB RAM: use bulk/cold migration instead
- ✅ Regular vSphere VMs: full support

---

## Slide Color Recommendation

Use **Plum** theme for innovation/multi-cloud feel:
- Primary: `#6C4B8F` (Plum)
- Supporting: `#007A86` (Teal) for on-prem elements
- Public cloud: `#0193C2` (Sky Blue) for GCVE/cloud elements
- Critical path: `#EDB516` (Gold) for HCX migration path

Or use gradient section approach:
- On-prem sections: Leaf (green)
- Cloud sections: Aqua (blue)

---

## Speaker Notes Guidelines (中文)

- 開場：以「大型企業的現實：沒有純公雲，也沒有純私雲」作為破題
- GCVE 章節：強調 GCVE 是 VMware 原生，不是 re-platform，管理工具完全一致
- HCX 章節：強調網路延伸 (Network Extension) 是 HCX 最大差異化，競品無法做到零停機切換
- DR 章節：以 GCVE 替代第二機房的 TCO 試算作為 hook (5年 CapEx vs. OpEx 對比)
- 升級章節：強調 GCVE 的版本由 Google/Broadcom 管理，客戶不需要自行升級
- 結尾：建議 HCX 試用 + GCVE 免費試用 (Google Cloud trial) 作為下一步
