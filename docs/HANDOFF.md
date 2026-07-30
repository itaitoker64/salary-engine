<!-- head: e7cc20f -->
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
ותק סטודנט → ותק קטוע → בסיס → גמול → תוספת 1999 → דריכות → גמול מנהל → בוררות מיסים → תוספת בית חולים → אמיתי
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

## Progim coverage check (added this session)

`progim_coverage()` splits pay codes into computable / referenced-only /
unknown. Every run reports the non-computable ones in sheet "חסר ב-Progim" plus
a dashboard banner — 53 codes and ₪5.4M on the 0108 file. This is a PRODUCT gap
list, not an engine bug list: the workbook has no formula for that money. Keep
it in the export; the user reads the Excel, not the docs.

## Progim 30.07 extraction (latest session)

Rules went 33 → 91. Rate resolution in extract_rules.py is now dynamic (tosafot
row 4 code labels, not cell addresses) — the old hardcoded addresses silently
broke on every workbook column shift and dropped 11 curated rules on
re-extraction. base_codes merges ADD-ONLY: the workbook no longer lists alias
pairs, so removal would regress alias-paid workers (728: 1,449 rows in 0108).

55 codes are declared type "reported" — the Progim takes their amount from the
מנהלת הגמלאות file rather than computing it. They are accepted as reported AND
summed into the bases of percent rules that reference them. The coverage report
now separates ₪4.84M reported-by-design (correct) from ₪742K real workbook gaps.

Fixed two bases against the workbook: 4374 (+647/667/897) and 4544
(+642/658/678). 0108 verdicts unchanged (21,217 / 332).

## Three-kind component taxonomy (current model)

Per the user: a component has a FORMULA, or its amount is a FIGURE IN THE חוקה,
or it is ENTERED BY HAND from the משרד האוצר file. `origin` on each rule records
which. Manual is exactly seven codes — 4120, 658, 678, 4173, 4643, 4935, 4318 —
and nothing else may claim `origin: manual`.

25 חוקה amounts are now validated as shekel rules against the workbook figure
(traced via tosafot!<L>3). Verified against 22,422 slips first: 97–100% match on
the twelve largest carriers. Unchecked ₪5.38M → ₪1.36M.

27 codes are חוקה amounts the extractor could NOT resolve (eligibility-gated
VLOOKUP chains) — labelled `type: reported, origin: hukka`. Do not relabel these
"manual": that would hide a coverage gap that is ours, not the workbook's.

Open: 16 workers pay exactly 96.77% of the חוקה figure across several codes — a
previous pulse the workbook keeps no history for. Reported to the user; do NOT
invent the historical amount to silence it.

## Scope: pensionable only

`NON_PENSIONABLE` in main.py (mirrored in engine.js) holds ten codes the Progim
deliberately does not cover — injury pay, הבראה, מילואים, ברוטו differences,
הפקעת שכר, ימי שביתה. They are filtered out of the coverage fix-list. The list
is explicit because the file's "ביט פנסיוני" column reads 'כן' on all 124,818
rows and cannot discriminate. Gap list: 25 codes/₪742K → 15 codes/₪294K.

## Report sheets

`collect()` returns `(summary, per_emp, code_gaps, recs, uncovered, codes_index)`
— update every caller when changing it. `codes_index` drives the "סיווג סמלי שכר"
sheet: every code ascending, classified as formula / חוקה amount / manual /
not-participating. Mirrored in both front-ends from `_bulkData.codesIndex`.

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
