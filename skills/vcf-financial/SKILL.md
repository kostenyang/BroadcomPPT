---
name: vcf-financial
description: Create Broadcom VCF presentation decks for financial services customers — banks, securities firms, insurance companies, and fintech (e.g. CTBC 中信銀行, 國泰世華, 富邦, 玉山, 兆豐). Trigger whenever the user wants a presentation, proposal, or slide deck for 金融業, 銀行, 證券, 保險, or any FSI customer. Also trigger for topics like 金融雲, core banking modernization, regulatory compliance (FSC/金管會), DR/BC requirements, or VCF multi-tenancy for banks. Always use the official Broadcom template — never create from scratch.
---

# VCF Financial Services Presentation Skill

Read `broadcom-ppt-base` SKILL.md first for template specs, colors, fonts, and editing workflow.
Location: `/home/claude/broadcom-ppt-skills/broadcom-ppt-base/SKILL.md`

---

## Industry Context

Taiwan financial institutions operate under strict regulatory frameworks:
- **金管會 (FSC)**: Financial Supervisory Commission — mandates DR, data residency, audit trails
- **中央銀行**: Core banking system availability requirements
- **Basel III / BCBS 239**: Data aggregation and risk reporting
- **個資法 (PDPA)**: Personal Data Protection Act — data classification and encryption
- **雙機房 DR**: Regulators require active-standby or active-active DC pairs

Key customers in Taiwan:
- **Commercial Banks**: CTBC (中信銀行), 國泰世華, 富邦, 玉山, 台新, 永豐, 兆豐, 合庫
- **Public Banks**: 台灣銀行, 土地銀行, 第一銀行, 彰化銀行, 華南銀行
- **Securities**: 元大證券, 富邦證券, 凱基證券
- **Insurance**: 國泰人壽, 富邦人壽, 南山人壽
- **Payment/Fintech**: 財金公司 (FISC), 聯合信用卡中心

---

## Recommended Deck Structure

### For Core Banking Modernization / VCF Adoption

1. **Title Slide** — `Title Slide – Aqua` (blue = trust, finance)
2. **Agenda**
3. **Section: 金融業 IT 挑戰**
   - Legacy infrastructure risk (aging vSphere, end-of-support)
   - Regulatory pressure (FSC circular requirements)
   - Hybrid cloud demand vs. data sovereignty
4. **Section: VCF 平台架構**
   - Management + Workload Domain design
   - Network segmentation (Core Banking / DMZ / Internet Banking)
   - Multi-tenancy: VCF VPC for business unit separation
5. **Section: 法規遵循與資安** (Compliance & Security)
   - vDefend for east-west micro-segmentation
   - Encryption at rest (vSAN encryption) and in transit
   - Audit trail via VCF Operations
   - FSC compliance mapping table
6. **Section: DR / BC 架構**
   - Live Recovery (formerly VCDA) for RPO/RTO SLA
   - vSAN Stretched Cluster for zero-RPO
   - SRM orchestration
7. **Section: 升級路徑** (from APJ 9.1 template)
   - VCF 5.2 → 9.1 upgrade path
   - Minimal downtime strategy
8. **Customer Success** slide (Layout 24)
9. **Big Statement** — ROI / TCO reduction message
10. **Thank You / Closing**

### For VCF VPC Multi-tenancy Proposal

1. Title Slide
2. 銀行雲架構挑戰 — 各業務單位資源爭搶與隔離需求
3. VCF VPC vs. 傳統分區設計對比 (Comparison layout)
4. VPC 架構圖 — Central IT + BU tenants
5. 網路權責分離 — 中央網路團隊 vs. 租戶自助
6. 權限模型 (Permission Model) — Org → VPC → vApp hierarchy
7. 成本回收 / Chargeback 機制
8. Closing

---

## Key Messages for Financial Services

| Customer Pain | VCF Answer |
|---------------|-----------|
| 老舊 vSphere 升級風險 | 標準化升級路徑，LCM 一鍵升級 |
| 金管會 DR 要求 (RPO<15min) | Live Recovery + vSAN Stretched Cluster |
| 核心系統零停機要求 | vMotion + HA + DRS 自動化 |
| 業務單位資源隔離 | VCF VPC multi-tenancy |
| 資安合規 (個資法/Basel) | vDefend micro-segmentation + 加密 |
| 私有雲成本居高 | VCF 整合授權 (BSC) + 資源超額訂閱最佳化 |
| 混合雲需求 (GCP/Azure) | HCX + GCVE 混合雲延伸 |

---

## Regulatory Compliance Slide

Include a compliance mapping table:

| FSC/法規要求 | VCF 對應功能 |
|-------------|-------------|
| 機房異地備援 | Live Recovery / SRM |
| 資料加密 | vSAN Data-at-Rest Encryption |
| 網路隔離 | NSX Segments + vDefend |
| 稽核紀錄 | VCF Operations audit log |
| 存取控制 | vCenter RBAC + AD/LDAP |
| 漏洞管理 | VCF Operations vulnerability assessment |

---

## Architecture Diagram Notes

For Taiwan bank topology, always show:
- **Primary DC** (台北/信義 or 內湖) ← → **DR DC** (桃園/台中)
- Zones: Core Banking | Internet Banking | DMZ | Management
- Connectivity: MPLS/SD-WAN between DCs, Internet Gateway at DMZ
- For hybrid: GCVE Tokyo + CHT/TWM cross-connect

Network authority model:
- **中央/實體網路團隊**: Manages underlay, uplinks, BGP
- **雲端/租戶團隊**: Manages NSX overlay, VPC segments

---

## Slide Color Recommendation

Use **Aqua (Blue)** theme — conveys trust, stability, financial credibility.
- Primary: `#005B84` (Ocean Blue)
- Accent: `#0193C2` (Sky Blue)
- Success metrics: `#61A00A` (Green)
- Alert/compliance gap: `#EDB516` (Gold) or red callout

---

## Speaker Notes Guidelines (中文)

- 開場：以金管會最新法規公文或 FSC 指引作為切入點
- 強調 VCF 是業界唯一整合 Compute/Storage/Network/Security 的私有雲平台
- DR 章節：強調 RPO/RTO 數字，對比競品 (Pure Storage, NetApp, HPE)
- 安全章節：強調 vDefend 是 NSX 原生整合，非第三方外掛
- 多租戶章節：強調 VPC 是真正的網路邊界隔離，不是 vApp/Folder 的假隔離
- 結尾：建議 PoC 或 Workshop 作為下一步行動
