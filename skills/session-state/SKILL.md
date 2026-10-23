---
name: session-state
description: 對抗 context 壓縮失憶的狀態持久化 workflow — 把任務目標、決策、進度寫進 dev-docs/ 檔案而不是留在對話裡。Use this skill whenever a task will span more than one sitting or is likely to hit auto-compaction。務必在下列情況觸發：(1) 開始任何多步驟 / 長時間任務（部署、升級、除錯、重構、寫交付文件）之前；(2) 使用者說「繼續」「接續上次」「我們做到哪了」「剛剛講到哪」「你是不是忘了」「重新確認一下」；(3) 對話被壓縮 / summarize 之後、或使用者提到 compact、壓縮、失憶、context window、上下文爆掉；(4) 使用者要求「存檔」「記錄一下決策」「handoff」「交接」「checkpoint」；(5) 完成一個里程碑、準備切換到不相關的任務之前。即使使用者沒有明講「skill」或「狀態檔」也要主動觸發 — 失憶的成本遠高於多寫一個檔案。
---

# Session State — 防壓縮失憶的狀態持久化

## 為什麼需要這個

Context 壓縮是必然的，不是意外。長 session 一定會被自動 compact，壓縮就是有損壓縮：決策理由、檔案路徑、踩過的坑會被摘要掉。使用者接著就會遇到「我們不是討論過了嗎」。

解法只有一個核心原則：

> **對話不是儲存媒介。檔案才是。**
> 任何需要跨壓縮存活的東西，當下就寫進檔案系統，不要指望對話歷史記得。

這個 skill 定義四個模式：**INIT / CHECKPOINT / RESUME / CLOSE**。判斷現在該進入哪一個，然後執行。

---

## 狀態檔位置

專案根目錄下的 `dev-docs/`（若使用者已有慣用位置，沿用他的）：

| 檔案 | 內容 | 更新頻率 |
|---|---|---|
| `dev-docs/plan.md` | 目標、範圍、**不做什麼**、完成標準、驗證指令 | 任務開始時寫，之後很少動 |
| `dev-docs/context.md` | 關鍵檔案路徑、**已做的決策 + 理由**、目前狀態、已知地雷 | 每有決策就追加 |
| `dev-docs/tasks.md` | checkbox 進度清單 | 每完成一步就勾 |

範本在 `assets/plan.md`、`assets/context.md`、`assets/tasks.md`，直接複製後填寫。

**安全邊界：狀態檔絕不寫入任何 credential**（密碼、API key、token、license key）。只寫「憑證來源」，例如 `vCenter 憑證：見 lab-info.md`。狀態檔會被 commit、會被貼到別的地方，當成公開檔案來寫。

---

## 模式一：INIT（任務開始）

在動手之前先建立契約。不要跳過 — 沒有明確的「不做什麼」，長任務一定會發散。

1. 檢查 `dev-docs/` 是否已存在。存在就走 RESUME，不要重建。
2. 執行 `bash scripts/init-state.sh <專案路徑>`（或手動從 `assets/` 複製範本）。
3. 和使用者確認 `plan.md` 的五個欄位後才開始執行：

```
- 目標（一句話，可驗證）
- In scope：
- Out of scope：      ← 最容易被跳過，也最重要
- Done when：
- 驗證指令：
```

4. 如果是 lab 環境的部署 / 組態任務，**先走 `lab-env` skill 的 READ 模式**：讀 `lab-info.md` 與 `dns-records.md`，把這次用到的主機 / IP / FQDN 抄進 `context.md` 的「關鍵資源」段落 — 這樣壓縮後不必重讀。**找不到那兩個檔案就停下來問使用者，絕不憑印象填 IP。**

---

## 模式二：CHECKPOINT（里程碑 / 壓縮前）

**時機**（任一成立就 checkpoint）：
- 完成一個里程碑（一個模組寫完、一個 bug 修掉、一份文件產出）
- `/context` 顯示使用率接近 60%（不要等自動壓縮）
- 準備切換到另一個子任務
- 使用者要離開、或明說「存個檔」

**動作：**

0. **先跑驗證，再存檔（gate，不可跳過）**

   執行 `plan.md` 的「驗證指令」。CHECKPOINT 是**閘門**，不是單純的存檔點 — 忠實存下一個壞掉的狀態，只會讓下次 RESUME 建立在錯誤基礎上繼續蓋，而且因為 `tasks.md` 已經勾了，沒有人會回頭懷疑它。

   | 結果 | 動作 |
   |---|---|
   | 通過 | 往下走步驟 1–4，正常勾 `tasks.md` |
   | 失敗 | **不要勾 `tasks.md`**，改走下面的失敗流程 |
   | 沒有驗證指令可跑 | 這是 `plan.md` 沒寫好 — 當場補上再繼續。無法驗證的「完成」不算完成 |

   **失敗流程**：狀態照樣要存，只是存的是「卡在這裡」而不是「做完了」。在 `context.md` 的「已知地雷」追加：

   ```
   ### 地雷 <日期> — <一句話症狀>
   - 驗證指令：<實際跑的那條>
   - 失敗輸出：<關鍵 3-5 行，不要貼整份 log>
   - 目前推測：<原因；沒把握就寫「未確認」>
   - 下次先試：<下一個具體動作>
   ```

   然後照樣執行步驟 1、3、4（跳過步驟 2 的勾選）。**「未確認」是合法且重要的值** — 假裝知道原因比承認不知道更貴。

1. 更新 `context.md` — 追加這次的**決策 + 理由**，不是流水帳。壞例子：「改了 nsx.yaml」。好例子：「Edge 走 active/standby 而非 active/active，因為 Route Server 只學到 standby 的 BGP peer；改動 `nsx/edge-cluster.yaml:42`」。理由才是壓縮後真正救命的東西。
2. 更新 `tasks.md` 的 checkbox。
3. 告訴使用者可以主動壓縮，並**給出帶指示的 compact 指令**，不要讓自動壓縮亂猜：

```
/compact 保留：目標、已做的決策與理由、改動的檔案路徑、剩餘 TODO、驗證指令、上次驗證結果（含失敗症狀）。丟掉：探索過程、繞路的嘗試、大段檔案內容。
```

4. 若接下來要做的是**不相關**的任務，建議 `/clear` 而不是 `/compact` — 舊 context 只會排擠掉真正需要的檔案。`/clear` 是硬清除、不可回復，所以務必先完成步驟 1–2。

---

## 模式三：RESUME（壓縮後 / 新 session）

觸發訊號：使用者說「繼續」、對話最上面出現摘要、或你發現自己在重問已經回答過的問題。

1. **先讀完三個檔案**：`dev-docs/plan.md` → `context.md` → `tasks.md`。
2. 讀 `git diff --stat` 和 `git log --oneline -5`，對照 `tasks.md` 確認實際進度（檔案可能沒更新到最新）。
3. **主動重述**，讓使用者在 5 秒內抓到偏差：

```
目標：<plan.md 的一句話目標>
已完成：<tasks.md 已勾選>
已改動檔案：<git diff --stat>
剩餘任務：<未勾選>
驗證指令：<plan.md>
上次驗證：通過 / 失敗（<症狀 + context.md 地雷編號>）   ← 失敗就從這裡接手，不要往下開新工
關鍵決策（不要推翻）：<context.md 摘要 2-3 條>
```

4. 得到使用者確認後才繼續動手。壓縮後最危險的行為是「憑印象接續」— 那正是造成不一致的原因。

---

## 模式四：CLOSE（任務結束）

1. 在 `context.md` 底部寫 handoff receipt：

```
## Handoff <日期>
- 改動檔案：
- 執行過的指令：
- 結果：
- 剩餘風險：
- 下一步最佳動作：
```

2. 把跨任務、長期有效的結論（環境慣例、踩過的雷、團隊規約）**上升到 project-root 的 `CLAUDE.md`** — 因為只有從 disk 啟動載入的東西壓縮後會回來。
3. 建議 `git commit` 一起帶上 `dev-docs/`，狀態檔要進版控。

---

## 壓縮後什麼會回來、什麼不會（關鍵機制）

這決定了指令該放哪裡：

| 內容 | 壓縮後 |
|---|---|
| project-root `CLAUDE.md` | ✅ 從 disk 重新注入 |
| unscoped rules、auto memory | ✅ 重新注入 |
| 用 `paths:` frontmatter scope 的 rule | ❌ 被摘要掉，要等再次讀到符合的檔案才回來 |
| 子目錄的 nested `CLAUDE.md` | ❌ 同上 |
| Skill body | ⚠️ 會重新注入，但大 skill 會被截斷，**保留檔案開頭** |
| 對話裡講過的所有話 | ❌ 有損摘要 |

推論：
- **必須跨壓縮存活的規則（credential boundary、部署 routing、絕對不能做的事）→ 放 project-root `CLAUDE.md`，不要加 path scope。**
- 寫 SKILL.md 時把最關鍵的指令放最前面，因為截斷是從後面砍。
- 想讓這個 skill 在壓縮後自動被想起來，把 `assets/claude-md-snippet.md` 的內容貼進 project-root `CLAUDE.md`。這是整套機制的啟動開關 — 沒有它，壓縮後不會有人叫你去讀狀態檔。

---

## 反模式（不要做）

- **等自動壓縮才想到要存檔** — 那時細節已經在被丟棄的路上了。
- **把大量 log / 檔案內容貼進對話** — 導向檔案，用 `rg` 精準搜尋，或交給 subagent 讀，讓大段內容留在它的 context 而不是主 session。
- **把 `context.md` 寫成流水帳** — 它是決策紀錄，不是操作日誌。「為什麼」比「做了什麼」重要。
- **把 CHECKPOINT 當存檔點而不是閘門** — 沒跑驗證就勾 `tasks.md`，等於把「我以為做完了」寫成「已完成」。狀態檔一旦說謊，整套機制就失效了。
- **壓縮後憑印象繼續** — 一定先 RESUME 重述。
