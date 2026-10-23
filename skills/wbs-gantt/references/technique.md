# How the WBS Progress Gantt works

Read this before changing the chart logic or the formulas in `build_wbs_gantt.py`.

## The stacked-bar Gantt trick

A Gantt chart in Excel is a **horizontal stacked bar chart** with the visible bars
pushed rightward by an invisible spacer:

1. **Series 1 — `Offset`** = `start_date − project_start` (days). Filled with
   **no fill** (`GraphicalProperties.noFill = True`). It's an invisible spacer that
   positions where each task's bar begins.
2. **Series 2 — `已完成`** = `工期 × % 完成` (days). Green (`70AD47`). The completed
   portion of the task.
3. **Series 3 — `剩餘`** = `工期 × (1 − % 完成)` (days). Blue (`2F5597`). The
   not-yet-done portion.

`grouping = "stacked"`, `overlap = 100` so the three segments butt together into one
continuous bar per task. Because Offset is invisible, you only see green→blue starting
at the task's real start date.

## Why the category axis is reversed

`bar.x_axis.scaling.orientation = "maxMin"` flips the category (task) axis so the first
task sits at the **top** and time reads top-to-bottom — the conventional Gantt layout.
(For a `type="bar"` chart, openpyxl still calls the category axis `x_axis` and the value
axis `y_axis`, regardless of the visual orientation.)

## Why the value axis max is pinned

`bar.y_axis.scaling.max = total` (project length in days + a margin) keeps the time
axis stable so bars don't rescale oddly and so an optional Today line aligns. `min = 0`
anchors day 0 at the project start.

## The formulas (all live in the WBS sheet)

| Column | Meaning        | Formula                          |
|--------|----------------|----------------------------------|
| G      | 工期(天)        | `=F-E+1` (inclusive)             |
| H      | % 完成 (input)  | hardcoded 0..1                   |
| I      | 已完成(天)      | `=G*H`                           |
| J      | 剩餘(天)        | `=G*(1-H)`                       |
| K      | Offset(天)      | `=E-$B$2` (start − project start)|
| L      | 狀態            | nested IF on TODAY(), E, F, H    |

The Gantt sheet only holds cross-sheet links (`=WBS!B<row>` etc.) feeding the chart, so
the chart is a pure view of the table — edit the table, the chart follows.

### Status logic (column L)
```
=IF(H>=1,"完成",
   IF(TODAY()<E,"未開始",
      IF(AND(TODAY()>F,H<1),"落後","進行中")))
```

### KPI block formulas
- 整體完成 % (duration-weighted): `=SUMPRODUCT(G_rng,H_rng)/SUM(G_rng)`
- 時程應完成 % (time elapsed): `=MIN(1,MAX(0,(TODAY()-$B$2)/(MAX(F_rng)-$B$2)))`
- 進度落差: 整體完成 − 時程應完成 (negative = behind schedule)
- 落後任務數: `=SUMPRODUCT((TODAY()>F_rng)*(H_rng<1))`

## The Today line (optional, Excel-only)

A vertical line at `x = TODAY() − project_start` is drawn as a 2-point XY-scatter series
`(today, 0) → (today, n_tasks)` on a **secondary** axis pair whose min/max are locked to
the bar chart's, then hidden (`delete = True`), and combined via `bar += scatter`.

This is the correct technique and works in Microsoft Excel. **LibreOffice and Google
Sheets frequently render the bar+scatter combo incorrectly** (the bar categories
collapse, the line lands at x≈0). That is why `--today-line` is opt-in and the
dependable "where is today" signal is the KPI block + `落後` status colouring instead.

## Recalc is mandatory

openpyxl saves formula *strings* with no cached values, so a fresh file shows blanks
until recalculated. Always run the xlsx skill's `recalc.py` after generating, and
require `total_errors: 0`.
