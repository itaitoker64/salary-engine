# -*- coding: utf-8 -*-
"""
classify_hukka_amounts.py — split the חוקה amounts into fixed vs period-varying.

A component whose amount is a figure in the חוקה is one of two things, and the
distinction matters to whoever reads the report: either the workbook holds ONE
figure that has applied for the whole period, or it holds a **חודש פרישה** table
whose figure has actually changed over time. The second kind cannot be checked
against a single number, and a file from another month needs the figure of that
month — so the report must say which is which.

The decision is read out of the workbook, never assumed:

1. `tosafot` row 4 gives each component its column. Rows 7..234 of that column
   are the amount per חודש פרישה (row 7 = 1.2008), and row 3 is the current
   figure. Two or more distinct non-zero amounts down that column ⇒ **varies**.
2. When the column is empty the amount lives on a dedicated sheet, named by the
   formula in row 2/3. `SOURCE_GRIDS` maps each such sheet to the month × tier
   grid the formula points at. A tier column that holds one amount for all 228
   months is **fixed** — the spread is across tiers, not across time; two or
   more amounts down a single tier column is **varies**.
3. Anything that resolves to neither is left **unknown** and says so. Guessing
   "fixed" here would put an unsourced claim in the deliverable.

Usage:
    python3 tools/classify_hukka_amounts.py [Progim.xlsm] [component_rules.json]
"""

import json
import re
import sys
from pathlib import Path

import openpyxl

TOSAFOT = "tosafot "
CODE_ROW = 4          # component code labels
CURRENT_ROW = 3       # the current figure (literal, or VLOOKUP into the block)
MONTH_ROW0, MONTH_ROW1 = 7, 234   # 1.2008 .. the last month the workbook carries

# Sheet -> (amount columns, first data row, last data row). Each entry is the
# grid the tosafot formula points at: rows are חודש פרישה, columns are the
# component's tiers (דירוג, תעריף, ותק-קבוצה...).
SOURCE_GRIDS = {
    "MANMASH 2022": (list("DEFG"), 5, 232),
    "5539 MEMUNE": (list("DEF"), 3, 230),
    "5268 LIVUI ORHIM": (list("DEF"), 3, 230),
    "tos reforma 4147": ([chr(c) for c in range(ord("H"), ord("S") + 1)], 7, 234),
    "heskem 2023": (list("GIKMO"), 4, 4),
    "heskem 2016": (list("GIKMO"), 4, 4),
}

SHEET_RE = re.compile(r"'([^']+)'!")


def _nums(values):
    return [round(float(x), 2) for x in values if isinstance(x, (int, float))]


def _column_of(tos_rows):
    """code -> 0-based column index, from the code labels in row 4."""
    out = {}
    for ci, label in enumerate(tos_rows[CODE_ROW - 1]):
        if label is None:
            continue
        for m in re.findall(r"\d{2,5}", str(label)):
            out.setdefault(int(m), ci)
    return out


def classify(wb_values, wb_formulas, code):
    """(period, evidence) for one pay code. period ∈ fixed | varies | unknown."""
    tos_v = list(wb_values[TOSAFOT].iter_rows(min_row=1, max_row=MONTH_ROW1,
                                              values_only=True))
    tos_f = wb_formulas[TOSAFOT]
    ci = _column_of(tos_v).get(code)
    if ci is None:
        return "unknown", "הסמל אינו מופיע בשורת הסמלים של tosafot"

    months = _nums(tos_v[r][ci] for r in range(MONTH_ROW0 - 1, MONTH_ROW1))
    distinct = sorted(set(x for x in months if x))
    if len(distinct) >= 2:
        return "varies", (f"טבלת חודש פרישה ב-tosafot: {len(distinct)} סכומים "
                          f"שונים על פני {len(months)} חודשים "
                          f"({min(distinct):g}–{max(distinct):g})")
    if len(distinct) == 1:
        return "fixed", (f"טבלת חודש פרישה ב-tosafot: סכום אחד, {distinct[0]:g} ₪, "
                         f"לכל {len(months)} החודשים")

    # Empty column — follow the formula to the sheet that holds the figure.
    from openpyxl.utils import get_column_letter
    col = get_column_letter(ci + 1)
    formula = " ".join(str(tos_f[f"{col}{r}"].value or "") for r in (2, CURRENT_ROW))
    sheet = next((s for s in SHEET_RE.findall(formula) if s in SOURCE_GRIDS), None)
    if sheet is None:
        lit = tos_f[f"{col}{CURRENT_ROW}"].value
        if isinstance(lit, (int, float)):
            return "fixed", f"סכום קבוע בתא tosafot!{col}{CURRENT_ROW}: {float(lit):g} ₪"
        if isinstance(lit, str) and lit.startswith("=") and "$C$4" not in lit:
            # An IF/VLOOKUP on a worker attribute (דרגה, רמה, גיל) — the choice
            # is per worker, but the figures themselves do not move with time.
            return "fixed", ("סכום נבחר לפי מאפיין עובד (דרגה/רמה/גיל), "
                             "לא לפי חודש — קבוע לאורך התקופה")
        return "unknown", "עמודת החודשים ריקה ולא אותר גיליון מקור לסכום"

    cols, r0, r1 = SOURCE_GRIDS[sheet]
    ws = wb_values[sheet]
    per_col = []
    for c in cols:
        s = _nums(ws[f"{c}{r}"].value for r in range(r0, r1 + 1))
        per_col.append(sorted(set(x for x in s if x)))
    widest = max((len(d) for d in per_col), default=0)
    if widest >= 2:
        allv = sorted({x for d in per_col for x in d})
        return "varies", (f"גיליון '{sheet}' — טבלת חודש פרישה: עד {widest} סכומים "
                          f"שונים בתוך מדרג יחיד ({min(allv):g}–{max(allv):g})")
    if widest == 1:
        allv = sorted({x for d in per_col for x in d})
        return "fixed", (f"גיליון '{sheet}': סכום אחד לכל חודש בכל מדרג "
                         f"({', '.join(f'{x:g}' for x in allv)} ₪ — ההבדל בין "
                         "המדרגים, לא בין החודשים)")
    return "unknown", f"גיליון '{sheet}' נמצא אך טבלת הסכומים ריקה"


def main():
    xlsm = Path(sys.argv[1] if len(sys.argv) > 1
                else "data/progim/Progim_30.07.2026.xlsm")
    rules_path = Path(sys.argv[2] if len(sys.argv) > 2 else "component_rules.json")
    wb_v = openpyxl.load_workbook(xlsm, data_only=True, keep_vba=True)
    wb_f = openpyxl.load_workbook(xlsm, data_only=False, keep_vba=True)
    rules = json.loads(rules_path.read_text(encoding="utf-8"))

    tally = {"fixed": 0, "varies": 0, "unknown": 0}
    for key, rule in rules.items():
        if rule.get("origin") != "hukka":
            rule.pop("amount_period", None)
            rule.pop("amount_period_note", None)
            continue
        code = int(rule["codes"][0])
        period, why = classify(wb_v, wb_f, code)
        rule["amount_period"] = period
        rule["amount_period_note"] = why
        tally[period] += 1
        print(f"{code:>6}  {period:<8} {why}")

    rules_path.write_text(json.dumps(rules, ensure_ascii=False, indent=2),
                          encoding="utf-8")
    print(f"\n{tally}  → {rules_path}")


if __name__ == "__main__":
    main()
