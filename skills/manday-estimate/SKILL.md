---
name: manday-estimate
description: >-
  Create a man-day (人天) effort-estimate spreadsheet in Excel (.xlsx) — a WBS with
  per-task man-day estimates, a subtotal per phase, and a grand "Total Estimated
  man/day". Use this whenever the user wants to 估人天 / 估工時 / 人天估算 / effort
  estimate / sizing / scope a project's effort / build a WBS估算表, including pre-sales
  scoping for VCF / HCX / migration / deployment work. Trigger even on terse asks like
  "幫我估人天", "估一下這個案子要幾人天", "man-day estimate for ...", "做個工時估算表",
  or when the user uploads a task list / SOW / existing estimate to turn into a
  man-day sheet. This produces man-days only (no rates or cost). Do NOT use this for
  scheduling with calendar dates or progress tracking (that is the wbs-gantt skill),
  for slide decks (vcf-* skills), or Word/PDF deliverables.
license: Proprietary.
---

# Man-Day (人天) Effort Estimate (Excel)

Generate a single-sheet effort estimate with a two-level structure:

- **Per-task man-days** — each work item gets its own editable estimate (amber cells).
- **Phase subtotal** — `SUM` of the tasks in that phase (light-blue row).
- **Grand total** — `Total Estimated man/day` = sum of the phase subtotals
  (yellow row, red number), matching the CTBC/台銀 template convention.

Man-days only — no daily rate, no cost, no role split (kept deliberately simple, as a
scoping/quoting input). Produced by `scripts/build_manday_estimate.py` from a JSON spec.

## Workflow (in order)

1. **Read this file.** Skim `references/estimation_notes.md` for common VCF/HCX work
   packages and rough man-day ranges to sanity-check or seed an estimate.
2. **Language:** default to the language the user writes in (`--lang zh` / `en` / `bi`).
3. **Assemble the spec** (`spec.json`):
   - User gave a task list / SOW / uploaded estimate → use it. Read an uploaded `.xlsx`
     with `extract-text file.xlsx` (xlsx skill); note that source sheets often put one
     man-day number per *phase* (merged) — when expanding to per-task, split it so the
     task estimates sum to the original phase number, and confirm the split.
   - User gave only a project type → seed phases/tasks from
     `references/estimation_notes.md`, then **confirm the man-day numbers with the
     user** — never present invented effort figures as if they were agreed.
4. **Generate:**
   ```bash
   python scripts/build_manday_estimate.py spec.json -o "<專案名>_人天估算.xlsx" --lang zh
   ```
5. **Recalculate — MANDATORY** (openpyxl writes formulas, not values):
   ```bash
   python /mnt/skills/public/xlsx/scripts/recalc.py "<專案名>_人天估算.xlsx"
   ```
   Require `"total_errors": 0`. Then sanity-check that the phase subtotals and grand
   total match what you expect (read back with `data_only=True` or render to PDF).
6. **Present** the `.xlsx` with `present_files`. Tell the user the amber 人天 cells are
   the editable inputs; subtotals and the grand total recalculate automatically.

## Spec schema

```json
{
  "title": "CTBC EVS / HCX 雲端遷移",
  "sheet_name": "WBS估算",
  "phases": [
    {"wbs": "1", "name": "前置作業", "tasks": [
      {"wbs": "1.1", "task": "EVS 雲端及地端網路架構設計", "manday": 2, "notes": ""},
      {"wbs": "1.2", "task": "...", "manday": 1, "notes": "客戶側配合"}
    ]},
    {"wbs": "2", "name": "建置作業", "tasks": [ ... ]}
  ]
}
```

- `manday` is a **whole number of days (integers only — no decimal points)**. `notes`
  optional. `sheet_name` optional.
- Keep phases and tasks in display order. Sub-numbered items (`2.4.1`) are just tasks.

### Multi-sheet workbooks (one tab per scenario)

For a 公版 / template that needs several scenarios as separate tabs, use a `sheets`
array instead of a top-level `phases` (the single-sheet form still works unchanged):

```json
{
  "sheets": [
    {"sheet_name": "VCF→VCF 9.1",     "title": "...", "phases": [ ... ]},
    {"sheet_name": "vSphere8→VCF 9.1", "title": "...", "phases": [ ... ]}
  ]
}
```

Each entry becomes its own worksheet with its own phases, subtotals, and grand total.
- For a parent line that only groups sub-items (e.g. `2.4 HCX 測試` with `2.4.x`
  children carrying the effort), set the parent's `manday` to `0` and note "含 2.4.x
  子項" so it isn't double-counted.

## Structure produced

```
WBS 編號 | 工作項目 / 任務 | 人天 | 備註
── 1 前置作業 ────────────────────  (navy phase band)
1.1  ...                         2
...
                  前置作業 小計     7     (light-blue subtotal = SUM of tasks)
── 2 建置作業 ────────────────────
...
        Total Estimated man/day   32      (yellow row, red total = Σ subtotals)
```

## Customisation

Theme constants live at the top of `scripts/build_manday_estimate.py`: fonts
(`Microsoft JhengHei` / `Arial`), the navy phase band, light-blue subtotal, and the
yellow + red grand-total styling (matched to the CTBC template, consistent with the
user's white/blue + 藍綠紫 preference). Edit there for a different palette. If the user
later wants a rate/cost or role-split layer, add columns (e.g. `日費率`, `報價=人天×費率`
or `架構師人天` / `工程師人天`) and extend the subtotal/total formulas accordingly —
but the default and the CTBC convention is man-days only.
