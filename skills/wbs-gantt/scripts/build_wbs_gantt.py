#!/usr/bin/env python3
"""Build a WBS + auto-updating progress Gantt workbook from a JSON spec.

Usage:
    python build_wbs_gantt.py spec.json -o output.xlsx [--today-line] [--lang zh|en|bi]

The output has two sheets:
  WBS   - the editable data table (dates, % complete) + a KPI summary block.
          Duration / 已完成 / 剩餘 / Offset / 狀態 are all FORMULAS, so editing a
          date or % recalculates the chart automatically.
  Gantt - a stacked horizontal bar chart (the classic Gantt trick): an invisible
          Offset spacer + a green "done" segment + a blue "remaining" segment.

Spec JSON schema:
{
  "title": "專案名稱",
  "project_start": "2026-01-20",        # YYYY-MM-DD
  "tasks": [
    {"wbs":"1.1","task":"...","phase":"1 啟動","owner":"動安 + Broadcom CXS",
     "start":"2026-01-20","end":"2026-02-15","percent":0.6,"notes":"KB 389276"}
  ]
}
percent is 0..1 (0.6 = 60%). notes is optional.
"""
import argparse, datetime as dt, json, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import FormulaRule
from openpyxl.chart import BarChart, ScatterChart, Reference, Series
from openpyxl.chart.axis import ChartLines
from openpyxl.chart.legend import LegendEntry
from openpyxl.chart.marker import Marker
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties
from openpyxl.worksheet.properties import PageSetupProperties

# ---- Theme (white / blue-green-purple, aligned to Broadcom 2F5597) ----
FONT        = "Calibri"
C_HEADER    = "1F3864"   # deep navy header band
C_DONE      = "70AD47"   # completed segment (green)
C_REMAIN    = "2F5597"   # remaining segment (Broadcom blue)
C_TODAY     = "C00000"   # today line (red)
C_INPUT     = "0000FF"   # editable input cells (blue text)
C_INPUT_BG  = "FFF2CC"   # editable input cells (light amber fill)
C_TITLE     = "1F3864"
PHASE_BANDS = ["FFFFFF", "EAF1FB"]  # alternating phase row bands
F_OVERDUE   = "FFC7CE"   # conditional: overdue
F_PROGRESS  = "BDD7EE"   # conditional: in progress
F_DONE      = "C6EFCE"   # conditional: complete

THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

LABELS = {
    "zh": dict(wbs="WBS 編號", task="任務", phase="階段", owner="負責單位",
               start="開始日", end="結束日", dur="工期(天)", pct="% 完成",
               done="已完成(天)", remain="剩餘(天)", offset="Offset(天)",
               status="狀態", notes="備註 / 連結",
               title_suffix="— WBS 進度甘特圖", pstart="專案起始日",
               note="說明：修改開始/結束日、% 完成 或專案起始日，甘特圖會自動更新。",
               ov="專案進度總覽", today="今天", span="專案區間", oa="整體完成",
               should="時程應完成", lag="進度落差", late="落後任務數",
               chart="進度甘特圖", s_done="已完成", s_remain="剩餘",
               st_done="完成", st_prog="進行中", st_todo="未開始", st_late="落後"),
    "en": dict(wbs="WBS", task="Task", phase="Phase", owner="Owner",
               start="Start", end="End", dur="Duration(d)", pct="% Done",
               done="Done(d)", remain="Remain(d)", offset="Offset(d)",
               status="Status", notes="Notes / Links",
               title_suffix="— WBS Progress Gantt", pstart="Project Start",
               note="Edit Start/End, % Done or Project Start and the chart updates automatically.",
               ov="Project Overview", today="Today", span="Project Span", oa="Overall % Done",
               should="Schedule % Expected", lag="Variance", late="Tasks Behind",
               chart="Progress Gantt", s_done="Done", s_remain="Remaining",
               st_done="Done", st_prog="In Progress", st_todo="Not Started", st_late="Behind"),
}


def L(lang):
    if lang == "en":
        return LABELS["en"]
    if lang == "bi":
        z, e = LABELS["zh"], LABELS["en"]
        return {k: (z[k] if k in ("note",) else f"{z[k]} / {e[k]}") for k in z}
    return LABELS["zh"]


def parse_date(s):
    return dt.datetime.strptime(s, "%Y-%m-%d")


def build(spec, out_path, today_line=False, lang="zh"):
    lab = L(lang)
    ps = parse_date(spec["project_start"])
    tasks = spec["tasks"]
    n = len(tasks)
    if n == 0:
        sys.exit("spec has no tasks")

    wb = Workbook()
    ws = wb.active
    ws.title = "WBS"

    # ---------- Title + project start + KPI overview ----------
    ws["A1"] = f'{spec.get("title","專案")} {lab["title_suffix"]}'
    ws["A1"].font = Font(name=FONT, bold=True, size=15, color=C_TITLE)
    ws.merge_cells("A1:M1")

    ws["A2"] = lab["pstart"]
    ws["A2"].font = Font(name=FONT, bold=True)
    pcell = ws["B2"]; pcell.value = ps; pcell.number_format = "yyyy-mm-dd"
    pcell.font = Font(name=FONT, bold=True, color=C_INPUT)
    pcell.fill = PatternFill("solid", start_color=C_INPUT_BG); pcell.border = BORDER

    ws["A3"] = lab["note"]
    ws["A3"].font = Font(name=FONT, italic=True, size=9, color="808080")
    ws.merge_cells("A3:M3")

    HR = 9                      # header row of the task table
    r0 = HR + 1                 # first data row
    rN = r0 + n - 1            # last data row
    dur_rng    = f"G{r0}:G{rN}"
    pct_rng    = f"H{r0}:H{rN}"
    start_rng  = f"E{r0}:E{rN}"
    end_rng    = f"F{r0}:F{rN}"
    status_rng = f"L{r0}:L{rN}"

    # KPI block (rows 5-7), formulas so it tracks edits
    kpi = [
        (lab["today"],  "=TODAY()",                                   "yyyy-mm-dd"),
        (lab["span"],   f'=TEXT($B$2,"yyyy-mm-dd")&" ~ "&TEXT(MAX({end_rng}),"yyyy-mm-dd")', "@"),
        (lab["oa"],     f"=SUMPRODUCT({dur_rng},{pct_rng})/SUM({dur_rng})", "0.0%"),
        (lab["should"], f"=MIN(1,MAX(0,(TODAY()-$B$2)/(MAX({end_rng})-$B$2)))", "0.0%"),
        (lab["lag"],    f"=SUMPRODUCT({dur_rng},{pct_rng})/SUM({dur_rng})-MIN(1,MAX(0,(TODAY()-$B$2)/(MAX({end_rng})-$B$2)))", "0.0%"),
        (lab["late"],   f'=SUMPRODUCT((TODAY()>{end_rng})*({pct_rng}<1))', "0"),
    ]
    ws["A5"] = lab["ov"]; ws["A5"].font = Font(name=FONT, bold=True, size=12, color=C_TITLE)
    for i, (k, f, fmt) in enumerate(kpi):
        rr = 6 + i // 3
        cc = 1 + (i % 3) * 3            # A / D / G
        kc = ws.cell(rr, cc, k); kc.font = Font(name=FONT, bold=True, size=9, color="595959")
        vc = ws.cell(rr, cc + 1, f); vc.number_format = fmt
        vc.font = Font(name=FONT, bold=True, color=C_TITLE)

    # ---------- Task table header ----------
    headers = [lab["wbs"], lab["task"], lab["phase"], lab["owner"], lab["start"],
               lab["end"], lab["dur"], lab["pct"], lab["done"], lab["remain"],
               lab["offset"], lab["status"], lab["notes"]]
    for j, h in enumerate(headers, 1):
        c = ws.cell(HR, j, h)
        c.font = Font(name=FONT, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", start_color=C_HEADER)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDER

    # ---------- Task rows ----------
    phases, band_of = [], {}
    for t in tasks:
        p = t.get("phase", "")
        if p not in band_of:
            band_of[p] = PHASE_BANDS[len(phases) % len(PHASE_BANDS)]
            phases.append(p)

    for i, t in enumerate(tasks):
        r = r0 + i
        band = PatternFill("solid", start_color=band_of[t.get("phase", "")])
        vals = [t.get("wbs", ""), t.get("task", ""), t.get("phase", ""), t.get("owner", "")]
        for j, v in enumerate(vals, 1):
            c = ws.cell(r, j, v); c.font = Font(name=FONT); c.fill = band; c.border = BORDER
        cs = ws.cell(r, 5, parse_date(t["start"])); cs.number_format = "yyyy-mm-dd"
        cs.font = Font(name=FONT, color=C_INPUT); cs.fill = PatternFill("solid", start_color=C_INPUT_BG); cs.border = BORDER
        ce = ws.cell(r, 6, parse_date(t["end"]));   ce.number_format = "yyyy-mm-dd"
        ce.font = Font(name=FONT, color=C_INPUT); ce.fill = PatternFill("solid", start_color=C_INPUT_BG); ce.border = BORDER
        cd = ws.cell(r, 7, f"=F{r}-E{r}+1"); cd.font = Font(name=FONT); cd.fill = band; cd.border = BORDER
        cp = ws.cell(r, 8, float(t.get("percent", 0))); cp.number_format = "0%"
        cp.font = Font(name=FONT, color=C_INPUT); cp.fill = PatternFill("solid", start_color=C_INPUT_BG); cp.border = BORDER
        ci = ws.cell(r, 9, f"=G{r}*H{r}"); ci.number_format = "0.0"; ci.font = Font(name=FONT); ci.fill = band; ci.border = BORDER
        cj = ws.cell(r, 10, f"=G{r}*(1-H{r})"); cj.number_format = "0.0"; cj.font = Font(name=FONT); cj.fill = band; cj.border = BORDER
        ck = ws.cell(r, 11, f"=E{r}-$B$2"); ck.font = Font(name=FONT); ck.fill = band; ck.border = BORDER
        # status formula
        cl = ws.cell(r, 12,
            f'=IF(H{r}>=1,"{lab["st_done"]}",'
            f'IF(TODAY()<E{r},"{lab["st_todo"]}",'
            f'IF(AND(TODAY()>F{r},H{r}<1),"{lab["st_late"]}","{lab["st_prog"]}")))')
        cl.font = Font(name=FONT, bold=True); cl.alignment = Alignment(horizontal="center"); cl.border = BORDER
        cn = ws.cell(r, 13, t.get("notes", "")); cn.font = Font(name=FONT); cn.fill = band
        cn.alignment = Alignment(wrap_text=True); cn.border = BORDER

    # ---------- Conditional formatting on status column ----------
    ws.conditional_formatting.add(status_rng,
        FormulaRule(formula=[f'$L{r0}="{lab["st_late"]}"'], fill=PatternFill("solid", start_color=F_OVERDUE)))
    ws.conditional_formatting.add(status_rng,
        FormulaRule(formula=[f'$L{r0}="{lab["st_prog"]}"'], fill=PatternFill("solid", start_color=F_PROGRESS)))
    ws.conditional_formatting.add(status_rng,
        FormulaRule(formula=[f'$L{r0}="{lab["st_done"]}"'], fill=PatternFill("solid", start_color=F_DONE)))

    # ---------- Column widths ----------
    widths = dict(A=10, B=30, C=22, D=24, E=12, F=12, G=10, H=8, I=11, J=11, K=10, L=11, M=32)
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    ws.freeze_panes = f"A{r0}"

    # helper cells for chart today line (off-screen, right side)
    ws["P1"] = "today_offset"; ws["Q1"] = "=TODAY()-$B$2"
    ws["P2"] = "task_count";   ws["Q2"] = n

    # ============ Gantt sheet ============
    g = wb.create_sheet("Gantt")
    g["A1"] = f'{spec.get("title","專案")} — {lab["chart"]}'
    g["A1"].font = Font(name=FONT, bold=True, size=14, color=C_TITLE)
    g.merge_cells("A1:N1")
    g["A4"] = lab["task"]; g["B4"] = lab["offset"]; g["C4"] = lab["s_done"]; g["D4"] = lab["s_remain"]
    for col in "ABCD":
        g[f"{col}4"].font = Font(name=FONT, bold=True)
    gr0 = 5
    for i in range(n):
        wr = r0 + i; grow = gr0 + i
        g.cell(grow, 1, f"=WBS!B{wr}")
        g.cell(grow, 2, f"=WBS!K{wr}")
        g.cell(grow, 3, f"=WBS!I{wr}")
        g.cell(grow, 4, f"=WBS!J{wr}")
    grN = gr0 + n - 1
    g.column_dimensions["A"].width = 30

    end_max = max(parse_date(t["end"]) for t in tasks)
    total = (end_max - ps).days + 2

    bar = BarChart()
    bar.type = "bar"; bar.grouping = "stacked"; bar.overlap = 100; bar.gapWidth = 50
    bar.title = lab["chart"]
    cats = Reference(g, min_col=1, min_row=gr0, max_row=grN)
    for col, color in [(2, None), (3, C_DONE), (4, C_REMAIN)]:
        ref = Reference(g, min_col=col, min_row=4, max_row=grN)
        s = Series(ref, title_from_data=True)
        gp = GraphicalProperties()
        if color is None:
            gp.noFill = True
        else:
            gp.solidFill = color
        gp.line = LineProperties(noFill=True)
        s.graphicalProperties = gp
        bar.series.append(s)
    bar.set_categories(cats)
    bar.x_axis.scaling.orientation = "maxMin"          # first task on top
    bar.y_axis.scaling.min = 0
    bar.y_axis.scaling.max = total
    bar.y_axis.majorGridlines = ChartLines()
    bar.height = max(8, 0.55 * n + 4)
    bar.width = 24
    # hide the invisible "Offset" series from the legend
    if bar.legend is not None:
        bar.legend.legendEntry = [LegendEntry(idx=0, delete=True)]

    if today_line:
        g["F4"] = "tx"; g["G4"] = "ty"
        g["F5"] = "=TODAY()-WBS!B2"; g["G5"] = 0
        g["F6"] = "=TODAY()-WBS!B2"; g["G6"] = n
        sc = ScatterChart()
        xref = Reference(g, min_col=6, min_row=gr0, max_row=gr0 + 1)
        yref = Reference(g, min_col=7, min_row=gr0, max_row=gr0 + 1)
        ser = Series(yref, xref, title="Today")
        ser.marker = Marker(symbol="none")
        ser.graphicalProperties = GraphicalProperties()
        ser.graphicalProperties.line = LineProperties(solidFill=C_TODAY, w=25000)
        sc.series.append(ser)
        sc.x_axis.axId = 300; sc.y_axis.axId = 301
        sc.x_axis.scaling.min = 0; sc.x_axis.scaling.max = total
        sc.y_axis.scaling.min = 0; sc.y_axis.scaling.max = n
        sc.y_axis.crosses = "max"; sc.x_axis.delete = True; sc.y_axis.delete = True
        bar += sc

    g.add_chart(bar, "A" + str(grN + 3))
    g.page_setup.orientation = "landscape"
    g.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    g.page_setup.fitToWidth = 1; g.page_setup.fitToHeight = 1

    wb.save(out_path)
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", help="path to spec JSON")
    ap.add_argument("-o", "--out", default="wbs_gantt.xlsx")
    ap.add_argument("--today-line", action="store_true",
                    help="add native in-chart vertical Today line (renders in Excel; "
                         "may not render in LibreOffice/Google Sheets)")
    ap.add_argument("--lang", default="zh", choices=["zh", "en", "bi"])
    a = ap.parse_args()
    spec = json.load(open(a.spec, encoding="utf-8"))
    p = build(spec, a.out, today_line=a.today_line, lang=a.lang)
    print(f"saved {p}")


if __name__ == "__main__":
    main()
