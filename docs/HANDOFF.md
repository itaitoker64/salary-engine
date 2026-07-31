<!-- head: 573c435 -->
# Handoff — branch `claude/employee-simulator-validation-pl128n`

Written 31.7.2026. Read `CLAUDE.md` first; it carries the standing rules.

## State

Branch restarted from `origin/main` at `573c435` (the previous round merged as
PR #61). It now carries one topic: **4319 (פו"מ) and 4427 (תוספת שירות) are in
the Progim and the engine now computes them.**

## What changed, and why

The user asked which Progim version the engine reads, and pointed at
`tosafot!CX` / `tosafot!CY` in the 30.07.2026 workbook. He was right and the
previous report was wrong: those two codes were listed as "לא מוגדר בחוברת"
when the workbook defines them in full.

**Why the extractor missed them.** `extract_rules.py` resolves a rate from a
*scalar* in `tosafot` row 3. For these two the rate is not a number — it is
`VLOOKUP(דרגה, '<sheet>'!C6:E115, 2, 0)` into a dedicated per-grade sheet
(`פומ נתיב 4319`, `שרות נתיב 4427`). No scalar, no rule, and the code fell
through into the coverage-gap bucket. **That mislabel was ours, not the
workbook's** — exactly the failure mode `CLAUDE.md` warns about, a gap of ours
being reported as a defect in the product.

**What was added.** A new optional rule key `rate_by_grade` (grade label →
rate), read in `main.py` and mirrored in `engine.js` before the `grade_split`
branch. The two tables were copied straight out of the workbook, not fitted to
payroll data. Formulas, from `SACHAR`:

- 4319: `CP11 = (AA11+AC11+AD11) * CP7` → base = משולב + גמול א + גמול ב
- 4427: `CS11 = (AA11+AC11+AD11+CO11+CP11) * CS7` → the same **plus 4318 and
  4319 itself**

Careful reading needed on the key space: `'Netunei Gimlai'!B10` holds the grade
**index** (1..110), not the grade label — `DARGA!A` is the same index column.
The per-grade sheets mirror that layout, so the VLOOKUP is consistent; there is
no off-by-one. `rate_by_grade` is keyed by the *label* and resolved through
`normalize_grade_label`, which was verified against paid slips (below).

Also replaced `data/progim/Progim_18.07.2026.xlsm` with the 30.07 workbook —
the repo's declared source of truth was two versions behind the rules extracted
from it. And fixed the dashboard banner: it named a chain that no longer
matched the columns (1999 still last on the front-ends, תוספת בית חולים missing
everywhere). It is now one constant, `CHAIN_HE` in `tools/unified_report.py`,
with the same string in both front-ends.

## Verified

Before writing either rule, both formulas were computed by hand against the
0108 file for every worker who carries the codes — 10 each:

| | exact to the agora | deviating |
|---|---|---|
| 4319 | 8 / 10 | 2 |
| 4427 | 8 / 10 | 2 |

The deviants are one worker at grade 18 (4319: ₪757.81 paid vs ₪880.69;
4427: ₪3,252.10 vs ₪2,351.11) and one at 20+ (4427: ₪9.26). Nothing was fitted
to make them pass.

Full run, 0108 file, 22,422 slips:

```
עובדים 22422 · משרה חלקית 4667 · ללא בסיס 856 · שתי שורות 10
ותק סטודנט 0 · ותק קטוע 0 · בסיס 28 · גמול 95 · תוספת 1999 113
דריכות 30 · גמול מנהל 0 · בוררות מיסים 0 · תוספת בית חולים 1
שגויים אמיתיים 13 · תקין 16609      partition = 22422  OK
```

Verdicts unchanged (21,167 / 382) — see the trust note below. Coverage gap
13 codes / ₪248,503 (was 15 / ₪294K). Classification sheet: 35 formula,
55 חוקה, 7 manual, 10 out-of-scope, 13 undefined. 20/20 tests;
`node --check engine.js` clean; report regenerated and every column checked
against its header.

## Open

**1. The two new rules do not flag anyone yet, by design.** Self-calibration
needs `TRUST_MIN_N = 20` carriers of a code on a file before it trusts the
rule, and 0108 has 10. So the rules compute and display but cannot fail a slip
here. Do **not** mark them `stable` to force them through: that would flag 2
workers out of a 10-worker sample, which is the false-positive trade
`CLAUDE.md` forbids. Re-check on a file with ≥20 carriers.

**2. The workbook's rate tables cover 9 grades out of 110.** Column D of
`C6:E115` is filled for indexes 13–21 (grades 17–21) and empty everywhere else,
where the VLOOKUP silently returns 0 — a worker outside that band gets a
tosefet of zero with no error. `'פומ נתיב 4319'!Y5` carries the author's own
note: "התוספת חושבה לקצינים בלבד - להוסיף חישוב לנגדים". Written up as
`docs/PROGIM_FIXES.md` §6. The engine **skips** the check for an unlisted
grade rather than expecting 0, so the workbook's blank never flags a worker.

**3. Everything below this line is inherited from the merged round** and still
holds: the 1999 bucket tests gap-presence rather than causation and can hide a
larger error (worker 66392396, ₪347 behind an ₪85 gap); 27 codes are חוקה
amounts the extractor cannot resolve through eligibility-gated VLOOKUP chains
and are labelled `reported/hukka` on purpose; 16 workers pay exactly 96.77% of
the חוקה figure from a pulse the workbook keeps no history for — reported, not
silenced. `base_codes` merges are ADD-ONLY (the workbook stopped listing alias
pairs; 728 alone is 1,449 rows). `lookups.json` DARGA once had a factor-6 error
that survived an audit because the audit rebuilt its comparison dict with the
same last-wins bug — when auditing a lookup table, check for duplicate labels
first.
