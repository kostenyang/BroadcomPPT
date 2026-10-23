# Man-day estimation notes (VCF / HCX / migration)

Seed material and sanity-check ranges for common VMware-by-Broadcom engagement work
packages. **These are rough planning ranges, not quotes** — always confirm with the
user and adjust for site count, scale, customer maturity, and change-control overhead.
Ranges assume one experienced engineer; split or scale for parallel teams.

## HCX / cloud migration (the CTBC/台銀 pattern)

| Phase | Typical tasks | Rough man-days |
|-------|---------------|----------------|
| 前置作業 | 架構設計；IP/網段/防火牆需求；資源/帳號申請；DNS;  Kick-off | 4 – 7 |
| 建置作業 | 地端 + 雲端 HCX 建置；L2 Network Extension；HCX 測試 (Cold/Hot/NE HA)；MoN 路徑最佳化 | 10 – 18 |
| 連線測試 | 遷移頻寬；DX/VPN 線路切換；遷移測試 VM；NE / MoN 延伸驗證 | 5 – 9 |
| Knowledge Transfer | KT Workshop；交付 KT decks | 1 – 3 |

> GPU-backed VMs and certain virtual-hardware levels have HCX migration constraints —
> add a separate task and extra man-days when present.

## VCF 5.2.1 → 9.1 upgrade

| Phase | Typical tasks | Rough man-days |
|-------|---------------|----------------|
| 規劃與盤點 | 現況盤點；相容性 / 升級路徑確認；備份回復方案；變更窗口 | 5 – 10 |
| 管理 Domain 升級 | 升級演練；元件升級 (VCF Ops→NSX→vCenter→ESXi→VCF Mgmt)；驗證；Aria/Automation 升級 | 8 – 15 |
| Workload Domain 升級 | 規劃 (vLCM Image 前置)；元件升級；驗證；Virtual Hardware 腳本開發/執行 | 8 – 15 |
| 驗證與移交 | 功能/效能驗證；穩定度觀察；文件；KT；結案 | 4 – 8 |

## Greenfield VCF 9.x deployment

| Phase | Typical tasks | Rough man-days |
|-------|---------------|----------------|
| 規劃與設計 | 需求訪談；HLD/LLD；IP/DNS/憑證；BOM | 6 – 12 |
| 基礎建置 | 機櫃/網路就緒；ESXi；vSAN ESA；NSX | 6 – 12 |
| VCF 組裝 | Cloud Builder；管理 Domain bring-up；Workload Domain | 5 – 10 |
| 平台服務 + 上線 | VCF Ops/Automation；AD/LDAP；備份；範本/藍圖；試移轉；上線 | 8 – 16 |
| 驗證與移交 | 驗證；文件；KT；結案 | 4 – 8 |

## Estimating tips

- Estimate at the **task** level, then let the phase subtotal roll up — it forces you to
  reason about each work item and is easier to defend than a single phase guess.
- Estimate in **whole days** (integers, no decimals); round up rather than carry
  fractions — finer precision is false precision for scoping.
- Put customer-dependency tasks (firewall/DNS/account approvals) as low engineer
  man-days but flag the dependency in 備註 — they drive schedule even at low effort.
- For a parent task whose children carry the effort, set parent `manday = 0` to avoid
  double-counting (the children sum into the same phase subtotal).
- Man-days here are **engineering effort**, not calendar duration. If the user then
  wants a dated schedule/Gantt, that is a separate deliverable (the wbs-gantt skill).
