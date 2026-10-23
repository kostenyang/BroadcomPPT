# VCF / Broadcom default WBS templates

Seed material for when the user names a project type but hasn't given a task list.
**Always confirm dates and scope with the user** — these are starting skeletons, not
fixed schedules. Phase numbering keeps same-phase tasks contiguous so the Gantt bands
cleanly.

## Owner shorthand (typical Taiwan VCF engagements)

- `動安 + Broadcom CXS` — joint delivery (SI partner + Broadcom Customer Success)
- `Broadcom CXS` — Broadcom-led (e.g. script development, deep upgrade ops)
- `<客戶>專案窗口` — customer PM / governance
- `<客戶>應用團隊` — customer app team (validation, UAT)
- `網路團隊` — network/firewall changes

## Template A — VCF 5.2.1 → 9.1 upgrade / migration

Mandatory component upgrade sequence inside the management domain:
**VCF Operations → NSX → vCenter → ESXi → VCF Management Services**. vLCM **Image mode**
is a prerequisite for workload-domain upgrades. Fleet Management Appliance is retired in
9.x; plan the new Services Cluster IPs.

| Phase | Representative tasks |
|-------|----------------------|
| 1 專案啟動與規劃 | 啟動會議；範疇與時程規劃；角色與權責確認 |
| 2 現況盤點與前置作業 | VCF5 現況盤點；相容性與升級路徑確認；備份與回復方案；測試環境與變更窗口確認 |
| 3 管理 Domain 升級 | 升級模擬與演練；管理 Domain 元件升級（依序）；升級驗證；Aria/VCF Automation 升級規劃→執行→驗證 |
| 4 Workload Domain 升級 | 規劃（vLCM Image 前置）；元件升級；驗證；Virtual Hardware 升級腳本開發→執行 |
| 5 HCX 部署與搬遷 | HCX 架構設計；安裝設定；網路與防火牆調整；測試遷移(PoC)；正式遷移至 VCF9；轉移腳本開發測試 |
| 6 功能驗證與穩定度觀察 | 系統功能驗證；效能與穩定度觀察；問題收斂與調整改進 |
| 7 文件更新與移交 | 文件與配置更新；移交與教育訓練；專案結案 |

## Template B — Greenfield VCF 9.x deployment

| Phase | Representative tasks |
|-------|----------------------|
| 1 規劃與設計 | 需求訪談；HLD/LLD；IP/DNS/憑證規劃；BOM 確認 |
| 2 基礎建置 | 機櫃/網路就緒；ESXi 安裝；vSAN ESA 組態；NSX 部署 |
| 3 VCF 組裝 | Cloud Builder；管理 Domain Bring-up；Workload Domain 建立 |
| 4 平台服務 | VCF Operations / Automation；身分(AD/LDAP)；備份 |
| 5 工作負載上線 | 範本/藍圖；測試移轉；正式上線 |
| 6 驗證與移交 | 功能/效能驗證；文件；教育訓練；結案 |

## Template C — HCX migration (workload move to VCF)

| Phase | Representative tasks |
|-------|----------------------|
| 1 規劃 | 來源/目標盤點；遷移波次規劃；網路延伸設計 |
| 2 HCX 建置 | 安裝與配對；Network Extension；防火牆調整 |
| 3 試遷移 | PoC / 試搬；回退演練 |
| 4 正式遷移 | 分波 vMotion / Bulk Migration；切換與驗證 |
| 5 收尾 | 來源退役；文件；移交 |

> GPU-backed VMs and certain virtual-hardware levels have HCX migration constraints —
> flag these as separate tasks (often `Broadcom CXS`-led) if relevant.
