# 單頁專案狀態報告 — 欄位定義與填寫範例

供 `vcf-project-status` skill 產生 1 頁 PPTX 時參考。所有數字 / 日期 / owner 一律向使用者取得，
缺資料就問，**不要編造或留 placeholder (xxx / TBD 以外)**。

## 8 區塊欄位定義

### 1. 抬頭 Header
- `project_name`：專案名稱（例：VCF 9.1 升級專案）
- `customer` / `org`：客戶或單位
- `pm` / `owner`：專案經理 / 負責人
- `report_date`：報告日期
- `period`：報告期間（例：2026/06/01–06/07，第 12 週）

### 2. 整體健康度 Overall RAG
- `overall_rag`：Green / Amber / Red
- `headline`：一句話總評（例：「整體 On Track，NSX 設定有風險但已有對策」）

### 3. 進度 Progress
- `percent_complete`：整體完成 %（0–100）
- `planned_percent`：依計畫應達 %（用來顯示落後 / 超前）
- `current_phase`：目前階段（例：Phase 2 — 部署）

### 4. 里程碑 Milestones（3–6 個）
每筆：`name` | `date` | `status`（done ✅ / in-progress ⏳ / not-started ⬜ / delayed ⚠️）
- 範例：環境準備 | 06/03 | ✅；管理域部署 | 06/14 | ⏳；工作負載域 | 06/28 | ⬜

### 5. 本期完成 Accomplishments（3–5 條）
本報告期間實際完成的事項，動詞開頭、可量化。
- 範例：完成 4 台 ESXi 主機 imaging；完成 vSAN 叢集驗證；通過 upgrade precheck。

### 6. 下期計畫 Next Steps（3–5 條）
下個期間預計工作。
- 範例：部署 NSX Edge；設定 FWaaS 規則；安排 workload 域 cutover 演練。

### 7. 風險與議題 Risks / Issues
- 風險 (Risk，尚未發生)：`desc` | `severity`(高/中/低) | `owner` | `mitigation`
- 議題 (Issue，已發生)：`desc` | `impact` | `owner` | `action`
- 範例風險：第三方憑證到期 | 中 | 王 | 6/10 前更新
- 範例議題：vCenter precheck 失敗 | 阻擋升級 | 李 | 已開 SR，預計 6/9 解

### 8. 範圍 / 資源 / 預算 Scope / Budget（選填）
- `scope_change`：本期範圍變更（無 → 「無變更」）
- `resourcing`：人力 / 人天狀態
- `budget`：預算燒錄 %（選填，對外版常省略）

## 填寫範例 (JSON 形式，方便餵給 pptx 產生)

```json
{
  "project_name": "VCF 9.1 升級專案",
  "customer": "範例客戶",
  "pm": "陳大文",
  "report_date": "2026-06-08",
  "period": "2026/06/01–06/07 (W12)",
  "overall_rag": "Amber",
  "headline": "整體進度大致 On Track，NSX 設定有風險但已有對策",
  "percent_complete": 55,
  "planned_percent": 60,
  "current_phase": "Phase 2 — 部署",
  "milestones": [
    {"name": "環境準備", "date": "06/03", "status": "done"},
    {"name": "管理域部署", "date": "06/14", "status": "in-progress"},
    {"name": "工作負載域", "date": "06/28", "status": "not-started"}
  ],
  "accomplishments": ["完成 4 台 ESXi imaging", "vSAN 叢集驗證通過", "通過 upgrade precheck"],
  "next_steps": ["部署 NSX Edge", "設定 FWaaS 規則", "排 cutover 演練"],
  "risks": [{"desc": "第三方憑證到期", "severity": "中", "owner": "王", "mitigation": "6/10 前更新"}],
  "issues": [{"desc": "vCenter precheck 失敗", "impact": "阻擋升級", "owner": "李", "action": "已開 SR，預計 6/9 解"}],
  "scope_change": "無變更",
  "resourcing": "2 名工程師 + 1 PM，依計畫",
  "budget": "—"
}
```

## 視覺要點
- 大 RAG 燈號放右上最醒目位置；燈號色用 broadcom-ppt-base 的紅黃綠。
- 進度用水平進度條 + 百分比，旁標「計畫 NN%」便於對比落後 / 超前。
- 里程碑用小狀態圖示 (✅⏳⬜⚠️)，日期靠右對齊。
- 風險 / 議題分兩塊，嚴重度用色塊或標籤，勿只靠文字。
- 全頁維持單張 16:9，左量化 / 右時間軸，留 ≥0.5" 邊距，勿塞滿。
