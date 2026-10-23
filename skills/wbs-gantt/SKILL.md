---
name: wbs-gantt
description: >-
  Create a project WBS schedule with an auto-updating progress Gantt chart in Excel
  (.xlsx). Use this whenever the user wants a 專案進度表 / WBS / 甘特圖 / project plan /
  project schedule / Gantt chart / timeline / 工作分解 / 任務排程 / 里程碑表 as a
  spreadsheet — including upgrade/migration project plans, deployment schedules, and
  any task list with start/end dates and owners. Trigger even if the user only says
  "幫我做專案進度", "排個甘特圖", "WBS Excel", "build a project timeline", or uploads a
  task list / existing Gantt to rebuild or extend. The output tracks progress
  (% complete, on-track / behind status, overall vs scheduled completion). Defaults
  lean toward VCF / Broadcom upgrade-migration projects but work for any project.
  Do NOT use this for slide decks (use the vcf-* presentation skills) or for
  Word/PDF deliverables.
license: Proprietary.
---

# WBS Progress Gantt (Excel)

Generate a two-sheet Excel workbook:

- **WBS** — the editable data table. Dates and `% 完成` are inputs (blue/amber cells);
  `工期 / 已完成 / 剩餘 / Offset / 狀態` are **formulas**, plus a `專案進度總覽` KPI block.
  Editing any date or % recalculates the chart automatically.
- **Gantt** — a stacked horizontal bar chart (the classic Gantt trick): an invisible
  `Offset` spacer positions each bar, a **green** segment shows the completed portion
  and a **blue** segment the remaining portion, so progress reads straight off the bars.

The whole thing is produced by `scripts/build_wbs_gantt.py` from a small JSON spec.
Do not hand-roll the openpyxl chart code — the script encodes the stacked-bar trick,
the reversed category axis, the no-fill spacer, the status logic, and the conditional
formatting, all of which are fiddly to get right.

## Workflow (follow in order)

1. **Read this file first** (you're here). Skim `references/technique.md` for the chart
   mechanics and `references/vcf_defaults.md` for default phases/owners.
2. **Decide the language.** Default to the language the user is writing in. If they
   write Traditional Chinese, use `--lang zh`; English, `--lang en`; if they ask for
   both, `--lang bi`. Don't ask unless it's genuinely unclear.
3. **Assemble the spec** (`spec.json`). Three sources, in priority order:
   - The user gave tasks / dates / an uploaded list or existing Gantt → use those.
     To read an uploaded `.xlsx`, dump it with `extract-text file.xlsx` (xlsx skill).
   - The user gave only a project type (e.g. "VCF 5.2.1 → 9.1 升級") → seed the WBS
     from `references/vcf_defaults.md`, then confirm scope/dates with the user.
   - Always confirm `project_start` and rough dates if the user hasn't given them —
     don't silently invent a schedule and present it as fact.
4. **Run the generator:**
   ```bash
   python scripts/build_wbs_gantt.py spec.json -o "<專案名>_甘特圖.xlsx" --lang zh
   ```
   Add `--today-line` only if the user explicitly wants the in-chart vertical Today
   line AND will open the file in Microsoft Excel (see caveat below).
5. **Recalculate — MANDATORY.** openpyxl writes formulas but not their values:
   ```bash
   python /path/to/xlsx/scripts/recalc.py "<專案名>_甘特圖.xlsx"
   ```
   The xlsx skill's `recalc.py` lives at `/mnt/skills/public/xlsx/scripts/recalc.py`.
   Require `"total_errors": 0`. If errors appear, fix the spec/script and rerun. Never
   deliver a workbook with `#REF!`, `#DIV/0!`, `#VALUE!`, etc.
6. **(Recommended) Eyeball it.** Render to image to confirm the chart looks right:
   ```bash
   soffice --headless --convert-to pdf --outdir . out.xlsx
   pdftoppm -png -r 100 out.pdf page
   ```
   Then `view` the Gantt page. This catches collapsed bars or mis-scaled axes.
7. **Present** the `.xlsx` with `present_files` and a 2–3 line summary. Tell the user
   which cells are editable (dates + % 完成, the amber/blue cells) and that the chart
   updates on its own.

## Spec schema

```json
{
  "title": "玉山 VCF9 升級轉移專案",
  "project_start": "2026-01-20",
  "tasks": [
    {"wbs": "2.2", "task": "相容性與升級路徑確認", "phase": "2 現況盤點與前置作業",
     "owner": "動安 + Broadcom CXS", "start": "2026-02-16", "end": "2026-03-31",
     "percent": 0.5, "notes": "KB 389276"}
  ]
}
```

- Dates are `YYYY-MM-DD`. `percent` is `0..1` (`0.5` = 50%). `notes` is optional.
- Keep tasks in display order (top → bottom of the chart). Group by `phase` so rows
  of the same phase sit together — the generator colour-bands them and the Gantt reads
  cleanly. The chart maps row-for-row to the table, so don't insert phase header rows.
- `工期(天)` is inclusive: `end - start + 1`. A same-day task is 1 day.

## Progress tracking (what the user gets)

- **狀態 column** (formula, with conditional formatting): `完成` (green) / `進行中`
  (blue) / `未開始` / `落後` (red — past its end date but `% < 100`).
- **專案進度總覽 KPI block**: 今天, 專案區間, 整體完成 % (duration-weighted),
  時程應完成 % (time elapsed), 進度落差 (actual − scheduled), 落後任務數.
- These render in **any** viewer (Excel, LibreOffice, Google Sheets) and are the
  dependable way to see "are we on track today?".

## The Today line (`--today-line`) — read before using

A true vertical "today" line on a horizontal Gantt requires an XY-scatter series on a
secondary axis combined with the bar chart. **Microsoft Excel renders this correctly,
but LibreOffice and Google Sheets often render the combo chart badly (bars collapse,
line misplaced).** So:

- Default is **OFF**. The KPI block + `落後` status already convey "where is today".
- Turn it **ON** only when the user will open in real Excel and explicitly wants the
  line. Tell them the LibreOffice/Sheets caveat.
- If you enable it, still verify by rendering — and if it looks broken in your
  LibreOffice preview, that's expected; note it'll be fine in Excel, or fall back to OFF.

## Customisation

Colours, fonts, and the status thresholds are constants at the top of
`scripts/build_wbs_gantt.py` (theme defaults to white + Broadcom blue `2F5597`,
green `70AD47`, with red `C00000` for the today line / 落後). Edit there if the user
wants a different palette (e.g. 藍綠紫). See `references/technique.md` for how the
stacked-bar Gantt and the formulas fit together before changing the chart logic.
