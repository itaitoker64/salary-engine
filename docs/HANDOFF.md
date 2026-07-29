<!-- head: 0ae17f7 -->
# Handoff — branch `claude/employee-simulator-validation-pl128n`

Written 29.7.2026. Read `CLAUDE.md` first; it carries the standing rules.

## State

**Not merged.** One substantive commit (`bff6c3e`, the chain reorder below) plus
the session-tooling commits. `main` is ahead from the other session, and both
sides touched `index.html`, `salary_frontend.html` and
`tools/unified_report.py` — a merge will conflict in the neutralization chain.
The SessionStart brief prints the live counts; trust it over this paragraph.

## What this branch changed, and why

The dashboard said 9 שגויי תוספת 1999 while the work queue showed a 1999 gap on
110 rows. Both were right: the dashboard counts **bucket assignment** (one
worker, one bucket) and the column counts **any worker carrying that gap**.
1999 sat last in the priority chain, so 101 of the 110 had already been claimed
by an earlier bucket (89 דריכות, 6 גמול, 6 בסיס).

The user decided 1999 should be attributed to the root rather than the symptom:
4624 sits inside the base of 798 (דריכות) and the other percent tosafot, so a
retro difference on 1999 propagates into them. The chain is now

```
ותק סטודנט → ותק קטוע → בסיס → גמול → תוספת 1999 → דריכות → גמול מנהל → בוררות מיסים → אמיתי
```

in `tools/unified_report.py`, `index.html` and `salary_frontend.html`, with the
dashboard column moved to match.

Also fixed: the CLI report's totals row listed 16 values against 17 header
columns (`inv_h1999` was omitted), shifting every total after שגויי גמול one
column left. Browser-generated reports were unaffected.

## Verified

Re-ran the 0108 file (22,422 slips) through `unified_report.collect`:

| bucket | before | after |
|---|---|---|
| שגויי תוספת 1999 | 9 | **98** |
| שגויי דריכות | 119 | **30** |
| שגויים אמיתיים | 5 | 5 |

Partition still exact: 4,667 + 856 + 10 + 16,633 + 28 + 95 + 98 + 30 + 5 =
22,422. Generated the workbook and confirmed header/data/totals alignment.
20/20 tests pass; `node --check engine.js` clean.

## Non-Progim additions on this branch (report these to the user)

The chain reorder is **not** a Progim rule — the workbook has no buckets, and a
1999 gap there is simply a gap. Declared in `docs/PROGIM_IMPROVEMENTS.md` →
"שכבת הנטרול בלוח הבקרה", with what the workbook needs to retire it: a
month-of-retirement × dirug rate table for 4624, like `heskem 2016` has for
5401. Until then the bucket hides real errors — see item 2 below.

## Open — read before touching the chain

**1. `main` moved the column but not the priority.** Commit `4e3ce1b` says it
moved שגויי תוספת 1999 after שגויי גמול "so display order and priority order
still agree" — but on `main` the `err_cat` chain still assigns `h1999` last, in
both `tools/unified_report.py` and `index.html`. On `main` the column therefore
sits in the new place showing the old number (9), with דריכות still at 119.
This branch moved the priority. Resolve the conflict by keeping **this
branch's** chain order and `main`'s other dashboard work (the רטרו rename, תקין
moved last, % over all workers).

**2. The 1999 bucket still swallows real errors.** Its condition is
`gap_4624 is not None` — the presence of a 1999 gap, not 1999 being the cause.
4624 sits below the self-calibration trust threshold, so a 1999 gap alone never
marks a worker invalid; every worker reaching that branch is invalid for some
other reason. On the 0108 file the 9 original members were flagged on 756 (5),
697 (4) and 4169 (1) — including worker 66392396, paid ₪736.08 on תוספת ענ"א
against an expected ₪388.88, a ₪347 gap hidden by an ₪85 gap on 1999. The user
has been shown this and chose the move anyway; the narrow fix, if wanted later,
is to require 4624 to be the only flagged component. The בוררות מיסים (741)
bucket does not have this problem — it tests `741 in flags`.

**3. Superseded work parked at `1f69692`.** An earlier version of this branch
carried Progim-fidelity fixes that never merged: population calibration for
5402/5524 (the amount tracks retirement month, which the file does not carry —
a fixed 2-value set falsely flagged 48 workers sharing ₪698.70), a separate
bucket for השלמת מינימום (441 of 1,125 flagged workers on the 18.07 run), and
`base_minus` for 5401/5533 (SACHAR subtracts 4935 at 12.25%; the rules added it
at full weight). A patch is in the session scratchpad. Do **not** re-apply the
4550 floor change from it: `docs/PROGIM_FIXES.md` shows no 4550 formula variant
reproduces the slips (38.9% are frozen personal amounts).

**4. `lookups.json` DARGA had a factor-6 error** for grades 10/11/12/12+, fixed
on `main` in `1cc105b`. It survived an earlier audit here because the audit
script rebuilt its comparison dict the same last-wins way the extractor did, so
it validated the bug against itself. When auditing a lookup table against the
workbook, check for duplicate labels first.
