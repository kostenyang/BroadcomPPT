<!-- 把以下內容貼進 project-root 的 CLAUDE.md（不要加 paths: frontmatter，
     否則壓縮後會被摘要掉）。這是 session-state 機制的啟動開關。 -->

## Session state（防壓縮失憶）

- 每個 session 開始時、以及每次 context 被壓縮 / summarize 之後，
  **先讀 `dev-docs/plan.md`、`dev-docs/context.md`、`dev-docs/tasks.md`**，
  再重述：目標 / 已完成 / 已改動檔案 / 剩餘任務 / 關鍵決策，等我確認後才動手。
- 若 `dev-docs/` 不存在而任務是多步驟的，先用 session-state skill 建立。
- 每完成一個里程碑，更新 `dev-docs/context.md`（決策 + 理由）與 `tasks.md`，
  然後提醒我做帶指示的 `/compact`。
- 狀態檔一律不得寫入 credential。
