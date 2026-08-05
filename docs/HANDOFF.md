<!-- head: PENDING -->
# Handoff — branch `claude/update-id4fvu`

Last written 4.8.2026. Read `CLAUDE.md` first; it carries the standing rules.
Everything below section `0q` was written on 31.7.2026 on the earlier branch
`claude/employee-simulator-validation-pl128n`, whose work is merged into `main`.

## State

Branch `claude/update-id4fvu`, **ahead of `main`** and not yet merged. Content
commits, oldest first: `15d9499` (the 04.08 workbook upgrade), `155669e` (the
12/2010 file check; docs only), `b5c2476` (seven codes out of scope), `6ba4132`
(the 12/2008 file check; docs only), `550304d` (six more codes out of scope),
`d2bef27` (the 705 neutralization column), `fdc2226` (the 12/2009 file check;
docs only), `eb62419` (the 12/2011 file check; docs only), `0673e44` (two more codes out of
scope), `d5527d8` (the 12/2012 file check; docs only), `9d4576e` (the corrected workbook
installed + the 805 rule edit), `44b4857` (the 875 neutralization column), `d5bd031` (one more code out of
scope), `d0069cf` (the 12/2013 file check; docs only), `7480078` (the 808 split
installed), `1fcd033` (805 completed: table filled + BC2 fixed), `8c5d6d5` (the 12/2014 file
check; docs only), `5614bf0` (five more codes out of scope + the unified report),
`f43b5a1` (unified report redone without 1.2008 + two month-parsing fixes). The
rest are handoff stamps. `main` had nothing new for it at session start.

The workbook in `data/progim` is **`Progim_05.08.2026.xlsm`** (04.08 deleted in
the same commit) — 805 complete at 228/228, 808 split into 10 pulses, and both
§11 formulas fixed. `component_rules.json` holds **102** rules
(unchanged count). Verify the deploy with `/api/progim/status` — it should
report `rules: 102`, `source: bundled`, `runtime_data_present: false`, meaning
the site serves the חוקה from the repo rather than a `/tmp` upload.

The coverage gap on the **0108 reference file (22,422 slips)** is **1 code /
₪251** — 507 alone. Separately, `golmi.xlsx` — a 6,901-worker sample that is
**not** the 0108 file, though I conflated the two earlier — measures 19 codes /
₪622,483, dominated by 738 at ₪568,238.

Newest topic first:

0am. **The 12/2015 file checked** — 4140 recurs for the sixth time
0al. **Progim 05.08.2026 installed** — §11 closed; 0108 reference run; a checkout rollback
0aj. **Unified report redone without 1.2008** — and it retracts the 5402/5524 headline
0ai. **Unified report over all 8 files** — 5402+5524 are 77% of the money (WRONG — see 0aj)
0ah. **Five more codes out of scope** — the list is now 35, and §15's fix already exists in the workbook
0ag. **The 12/2014 file checked** — biggest coverage gap yet; 4651 proves §11 is formula-only
0af. **805 is complete** — table full and formula fixed; the first component closed both ends
0ae. **808 split into two more pulses** — better justified than my retracted claim was
0ad. **The 12/2013 file checked** — 805 matches 110/110; my 808 finding is retracted
0ac. **5272 out of scope** — fourth batch; the list is now 30
0ab. **New 875 neutralization column** — asked for, built, and it has no justification
0aa. **The workbook was corrected** — 805 codes 49-60 filled; verified, and what it did not fix
0z. **The 12/2012 file checked** — it lands inside a hole in the 805 table and measures it
0y. **5281 and 1265 out of scope** — third batch; the list is now 29
0x. **The 12/2011 file checked** — an 808 amount that is not in the table at all
0w. **The 12/2009 file checked** — refutes my 0t dating; best coverage yet
0v. **New 705 neutralization bucket** — asked for, delivered, and it hides 5402/5524
0u. **Six more codes out of scope** — the list is now 27, and 4535/4536 needs a human
0t. **The 12/2008 file checked** — dates the pulse tables; ₪17.5M under code 669
0s. **Seven codes declared non-pensionable** — user instruction, no Progim source
0r. **The 12/2010 file checked** — confirms the 04.08 fill; 33 of 49 rules silenced
0q. **Progim 04.08.2026** — 805/808 pulse tables filled; four new workbook defects
0. **Upgraded to the Progim 31.07.2026 workbook** — 956/957 newly defined there
1. **חוקה amounts split into fixed vs period-varying** in the classification sheet
2. **1711 and 4120 out of scope**; 1711 also gets its own neutralization bucket
3. **The dashboard partition covers the whole file**, not full-timers only
4. **4319 / 4427 are in the Progim** and the engine now computes them

## 0am. The 12/2015 file — 4140 recurs for the sixth time

Ninth file: **December 2015**, **19,305 workers**. **97.21% · 13 true errors ·
₪1,606** (₪402 under, ₪1,204 over); partition closes. Second-lowest exposure of
the nine — 13 errors, all small in shekels. Docs only.

**True errors are spread, not concentrated:** 756 (4, ₪113), 5216 (4, ₪181),
4169 (2, ₪539), 4932 (2, ₪426), 736 (1, ₪346), 626 (1). Unlike 12/2012 where 875
alone was 25 of 27.

**805 holds for a third month since the table was completed:** 104 of 105
(99.0%), trusted, at 107.88. c+84 lands in 85-95, inside the 61-102 band —
consistent, no narrowing of c ∈ [1,11].

**4140 (משכ.בסיסית) is now the most persistent item in the coverage gap.** The
gap here is 4 codes / ₪7,646: 4140 (₪6,269), 5374 (₪763), 5315 (₪440), 507
(₪173). 4140 has appeared in **six files** — 12/2008, 12/2010, 12/2012, 12/2013,
12/2014, 12/2015 — always few rows but ₪3-9.4k each time, and **507 appears in
all nine**. Both are pay components rather than benefits, so neither is an
out-of-scope candidate; they are a real coverage gap and worth putting to the
user as a decision.

**The 875 bucket has fired in one file out of nine.** 875 is at 95.0% here (100
mismatches of 2,002), silenced, so the column reads 0. The note made when it was
built stands: it tracks the 97% switch rather than being a stable category. **4651
also slipped to 96.4% and is silenced here**, having been 98.9% and trusted in
12/2014 — the same threshold sensitivity.

Calibration silenced 32 of 48 rules; 4,896 workers (25.4%), ₪1,835,521, of which
₪1.55M is 4550 — sitting at exactly 50.0% matching.

## 0al. Progim 05.08.2026, the 0108 reference, and a checkout rollback

**Read this first if history looks wrong.** On 5.8.2026 this *checkout* reverted
to `769ce42` — working tree, `git log` and reflog all rolled back about eight
commits. **The remote was never affected:** `origin/claude/update-id4fvu` still
held everything at `15679a9`. I initially misread this as data loss because I
checked `git log origin/...` before fetching, which reports the stale local ref.
The fix was `git fetch` then `git reset --hard origin/claude/update-id4fvu`; a
push attempt in between was correctly rejected as non-fast-forward. **If this
recurs: fetch first, read the remote, never force-push.** Two source uploads
(12/2013, 12/2014) did disappear from the uploads directory and cannot be
re-run; their findings survive only as prose in `PROGIM_IMPROVEMENTS.md`.

**Progim 05.08.2026 installed**, 04.08 deleted. Against the *original* 04.08 it
changes 62 cells in `tosafot`: yesterday's three corrections plus **`BR2` →
`BR1`**, which was the piece still missing.

**§11 is now closed in full.** Both `BC2` (BC1=12) and `BR2` (BR1=27) read their
index cell. This was the only silent defect on the list — the workbook returned a
plausible amount belonging to a different component. Closing `BR2` opens **4651:
1,290 slips, ₪631,615** across the December files, a component the engine had
already measured at 98.9%, so the table data was always fine and only the
reference was broken. §9 and §11 are both closed; `PROGIM_FIXES.md` records both
with the evidence retained.

**The 0108 reference file run:** **22,422 workers — the partition closes exactly
on the number `CLAUDE.md` specifies.** 21,163 valid (98.21%), **10 true errors,
₪9,750**, coverage gap **1 code / ₪251 (507)**. Leading codes 756 (4, ₪6,670),
628 (3, ₪6,341), 630/853 (2 each), 736 (2).

**A correction I owe.** In 0aj I rewrote this file's State line — which said the
coverage gap is "1 code / ₪251 — 507 alone" — claiming it was stale and the real
figure was 19 codes / ₪622,483. **The original was right.** I had been measuring
`golmi.xlsx` (6,901 workers) and calling it "0108" all session. The reference file
has 22,422 slips and gives exactly 1 code / ₪251. The State line is restored.

This propagates: the findings attributed to "1.2008" — **738 at ₪568K** and
**5402/5524 as 77% of the exposure** — belong to `golmi.xlsx`, a separate smaller
sample, **not** to the reference file. Do not cite them as 0108 results, and do
not repeat my conflation of the two files.

## 0aj. Unified report without 1.2008 — retracting the 5402/5524 headline

The user asked for the 1.2008 row (row 14) out of the unified report, and
removing it exposed that **0ai's headline was misleading**. I wrote that 5402
and 5524 are "the largest source of true errors across eight months and 154k
slips". Carrier counts per file:

| file | 5402 | 5524 |
|---|---|---|
| **1.2008** | **6,698** | **6,698** |
| 12/2008–12/2014 | 0 | 0 |

**Neither code appears in any December file.** All 59 true errors and all
₪27,835 came from one file. Dropping it takes the total from 108 true errors /
₪36,158 to **76 / ₪21,483**.

What survives: §7's defect is real — `heskem 2016` genuinely has no amount
table — but it concerns the **1.2008 population, not the December period**, so
it is not the cross-cutting defect I called it. **§11 stays ahead of it** (4651:
1,290 rows, ₪631,615, present in every December file). Do not repeat the "77% of
the money" line without naming the single file it comes from.

**The report (12/2008–12/2014):** 147,667 workers, 138,923 valid, **76 true
errors (0.0515%), ₪21,483 exposure**, all eight partitions close. Leading codes:
736 (17, ₪5,022), 697 (16, ₪1,604), **4651 (11, ₪3,627)**, 858 (7), 626 (6).
Union coverage gap **15 codes / ₪42,390**, led by 4140 (₪27,003) and 1104
(₪6,968).

**Two fixes in `tools/unified_report.py`** (the only code changed):

1. `_month_from_name` now also reads a compact **`MMYY` token** (`golmi_1213` →
   12/2013). Not every גולמי has a `תאריך שכר` column — 12/2013 and 1.2008 do
   not — and without this those files were labelled by filename. Guarded to
   exactly four digits with month 01-12, so `golmi_2024` is rejected. A new
   `_sort_month()` uses the same derivation, so a dateless file now sorts into
   its real chronological position instead of being pushed to the end by the old
   `datetime(2099,1,1)` fallback. 12/2013 now sits between 12/2012 and 12/2014.
2. **A pre-existing bug found while testing that:** in `(0?[1-9]|1[0-2])` the
   short alternative wins, so a `YYYY.MM` name with month ≥10 mis-parsed —
   `report_2011.12` returned **`01/2011`**. Reordered to `(1[0-2]|0?[1-9])`. It
   affected none of our files but would have failed silently on such a name.

The `שינויי סטטוס` (1,690) and `שינויים בין חודשים` (1,707) sheets are now
chronologically valid — 0ai's caveat about them no longer applies to this run.
Their largest deltas are driven by 667 and 798, which is a retro signature
rather than proof of error.

## 0ai. Unified report across all eight files

One run over everything checked today plus the repo's 1.2008 sample. Written to
`דוח_מאוחד_כל_הקבצים_04.08.2026.xlsx` and sent to the user.

**154,568 workers · 145,431 valid · 108 true errors (0.0699%) · ₪36,158
exposure** (₪18,182 under, ₪17,977 over). All nine partitions close.

**The finding worth acting on: two components are 55% of the errors and 77% of
the money.** 5402 (תוספת שקלית 2016) is 31 workers / ₪14,219 and 5524 (2023) is
28 / ₪13,616 — together 59 of 108 and ₪27,835 of ₪36,158. These are exactly the
components `PROGIM_FIXES.md` §7 says the workbook cannot price: `heskem 2016`
carries only the percentage block and has no amount table at all. So **the single
largest source of true errors across eight months and 154k slips is the one
component the Progim cannot compute.** §7 moves to second priority behind §11.

Union coverage gap: **29 codes / ₪664,873**, of which **738 (ת. אחוז-יום) is
₪568,238 over 2,076 rows — 85% of the total, and entirely inside the 1.2008
file.** It appears in none of the seven December files. Next are 4140 (₪30,013),
1027 (₪11,529), 4221 (₪10,078), 4220 (₪9,642).

**Caveat on the cross-month sheets — read before quoting them.** Two files
(`golmi.xlsx` and 12/2013) have **no `תאריך שכר` column**, so they sort by
filename rather than date. `שינויי סטטוס` (1,423 rows) and `שינויים בין חודשים`
(1,741 rows) therefore contain non-chronological comparisons such as "12/2014 →
golmi_1213". Those sheets do not represent real valid→invalid transitions over
time while both files are included. Run without them, or give those files a date
column, before drawing trend conclusions.

## 0ah. Five more codes out of scope — and §15's fix already exists in the workbook

Off the 12/2014 coverage list, on the user's instruction: **1731, 4123, 4978,
1228, 1229**. `NON_PENSIONABLE` is now **35 codes**; Python and JS compared
element-wise and in sync, 34 tests pass, `node --check` clean. 12/2014's gap goes
**10 codes / ₪16,633 -> 5 codes / ₪12,303**; partition closes, verdict unchanged
at 98.04%.

Four passed both checks cleanly. **1731 did not, and it matters:** it *is* in the
workbook, at `sminimum` row 188 — `1731 | חתימה/ עדות - גט | חוק מינימום: לא |
השלמה לשכר מינימום: כן`. Those two columns declare **minimum-wage treatment, not
pensionability**, and there is no formula computing the component, so it is still
uncovered in the sense §15 means. Precedent: **1375 is already on the list and
appears in that same table.** Added on that basis, and the docs say so — do not
let a future reader think the workbook was contradicted.

**The discovery that came out of checking it:** `sminimum` holds a **295-row
table** with headers `סמל תוספת · שם תוספת · חוק מינימום · השלמה לשכר מינימום`
and כן/לא values throughout. **That is exactly the shape §15 has been asking
for** — a per-code attribute table in cells — just for a different question. §15's
instruction is rewritten accordingly: **add a `פנסיוני` (כן/לא) column to that
existing table.** No new sheet needed, and it retires the hardcoded 35-code list
in `main.py` and `engine.js` in favour of one source of truth inside the product.
This is the strongest version of that recommendation the repo has had; lead with
it.

## 0ag. The 12/2014 file — 4651 shows §11 is a formula bug, not a data bug

Eighth file: **December 2014**, **19,619 workers**. **98.04% · 14 true errors ·
₪1,090** (₪854 under, ₪237 over); partition closes at 19,619. Lowest exposure of
the eight. Docs only. Written up in `PROGIM_IMPROVEMENTS.md` under "בדיקת קובץ
12/2014".

**The useful finding: 4651 validates at 98.9% here** (176 of 178), is trusted,
and even yields one true error (₪87.84). So the engine can check that component
well — because it reads the correct column straight from the table. The workbook
still returns 4453 for it, purely because of the hardcoded index in `BR2`. That
makes §11 unambiguous: **the data in the table is fine, only the reference is
broken.** A one-token fix opens a component that already works. Use this when
arguing the priority — it is the cheapest high-value fix outstanding.

**805 holds at 109 of 110** (99.1%), trusted, second month running since the
table was completed. c+72 lands in 73-83, inside the 61-102 band — consistent,
no narrowing.

**The 875 bucket is empty again.** 875 sits at 96.3% (76 mismatches of 2,032),
below the gate, so it is silenced and nobody reaches the column. **The column has
fired in one file out of seven.** That reinforces what was recorded when it was
built: it is not a stable category but a function of the 97% switch, and in six
of seven months 875's gaps are already uncounted because the rule is silenced
rather than because the bucket caught them.

**Largest coverage gap measured: 10 codes / ₪16,633.** 4140 משכ.בסיסית (₪7,329),
1104 שכר עבודה (₪3,429), 1731 חתימה/עד גט (₪2,149), 1229 (₪1,233), 5374 (₪755),
5315 (₪617), 4123 100% ש.מחלה (₪392), 4978 נכ.העד-חרום (₪367), 1228 (₪190), 507
(₪173). 4140 now appears in **five** files and 507 in all **seven**; both are pay
components and a genuine gap.

Four of the new ones look like out-of-scope candidates by the same logic the user
applied to 5272 — 4123 (100% sick pay), 4978 (emergency absence), and 1228/1229
(daily allowances). **Not added; that is the user's call**, and each still needs
both checks first.

Calibration silenced 31 of 48 rules; 5,146 workers (26.2%), ₪2,094,688, of which
₪1.62M is 4550.

## 0af. 805 is finished — table full, formula fixed

Third corrected workbook, installed. **Exactly 25 cells** changed, all in
`tosafot`:

1. **`BC2` fixed** — now `VLOOKUP($C$4,$AR$7:$BC$234,BC1,0)` instead of the
   hardcoded index 8. The formula finally reaches 805's table.
2. **`BC211`-`BC234` filled** with 116.41 — codes 205-228, the second hole, which
   is the current period.

*(The first diff pass also showed ~10 other "changes"; those were ArrayFormula
cells, where `openpyxl` builds a fresh object per load so `!=` compares identity.
Normalizing on `.ref` + `.text` leaves exactly 25 real cells. Use that
normalization when diffing these workbooks.)*

**805 is now the first component in the report closed at both ends:** table
228 of 228 (both holes gone), formula pointing at it. The workbook returns
תוספת ערבה instead of 681's ₪303.18.

**Effect on the engine: zero, and that is the point.** The engine reads the table
directly and takes the closest listed amount with no period logic; 116.41 was
already in the list from the 144-204 band, so filling 205-228 changes nothing
here, and the formula fix does not touch us at all. All seven files produce
identical numbers before and after. The entire value of this update is **in the
workbook — the product** — where until today anyone entitled to 805 got another
component's ₪303.18. Report it that way; do not dress it up as an engine
improvement.

805's match rate across the files, unchanged by this update: 0108 98/98, 12/2008
104/107, 12/2009 100/105 (silenced), 12/2010 105/108, 12/2011 104/107, 12/2012
99/104 (silenced), 12/2013 110/110.

**What is left: `BR2`.** Half of §11 is done. `BR2` still hardcodes 26 against
`BR1`=27, so **4651 (תוספת שכר) still returns 4453 (דריכות וכוננות)**. The
affected population is not marginal — 189-244 carriers per month, **1,290 rows
and ₪631,615** across the six historical files. The remaining instruction is one
token: `tosafot!BR2` → replace `26` with `BR1`. Keep raising it until it is done.

## 0ae. The user split 808 — and it is better justified than I said

A second corrected workbook, installed over `data/progim/Progim_04.08.2026.xlsm`.
**Exactly 24 cells** changed, all in the 808 column: codes **37-48 go 201.15 ->
205.68** and codes **49-60 go 215.73 -> 209.20**. Nothing else moved.

This is the finding I retracted in 0ad, and the retraction needs qualifying.
What was wrong was my *reasoning* — "two observations straddling a boundary is
not noise" — and that really did not hold. But the split has a better argument
that I missed: **after it, 808's band boundaries are identical to 805's** —
1-23, 24-36, 37-48, 49-60, 61-102. Two sibling components sharing one pulse
schedule is a structural explanation, not an inference from two data points, and
it is much stronger than what I originally claimed. The amended table also
reproduces **all three** observations including the one that broke my story:
12/2011 -> 205.68 ✓, 12/2012 -> 209.20 ✓, 12/2013 -> 215.73 ✓.

What still stands from the retraction: the evidence per band is **one carrier**,
and the table is indexed by retirement month rather than the payslip's month. The
split contradicts nothing measured, but a file with a real 808 population is
still the test. Do not upgrade this to "confirmed".

`component_rules.json` was hand-edited again (never regenerate — see 0aa): 808's
`amounts` goes from 8 to 10 values with 205.68 and 209.2 added, and the note
records both the evidence and the 805 band alignment. **Effect on the reports:
zero.** 808 is one carrier per file, far below the n=20 trust gate, so it stays
silenced; partitions, true-error counts and validity are identical before and
after on all three files. What changed is that the three carriers now match.

**Still not fixed after two workbook updates: `tosafot!BC2` and `BR2`.** Verified
in the new file — **`BC1` holds 12**, the correct index for 805, while `BC2`
still hardcodes 8. The sibling does it right: `CC2` reads its index from `CC1`.
So the two updates are not equal in value: **the 808 split actually reaches the
formula, while the 805 fill does not.** The workbook still returns 681 (₪303.18)
where 805 is due. §11 is the cheapest fix on the list — two cell references — and
it is now the only blocking defect no update has touched. Keep saying so.

## 0ad. The 12/2013 file — 805 is perfect, and I retract the 808 finding

Seventh file: **December 2013** (185,748 rows, 20,053 workers, 41 bodies, 93
codes). **97.01% · 11 true errors · ₪2,157** (₪914 under, ₪1,243 over);
partition closes at 20,053. Docs only. Written up in `PROGIM_IMPROVEMENTS.md`
under "בדיקת קובץ 12/2013".

**First external validation of the worker count.** This file arrives with three
sheets — `גולמי`, `פיבוט`, `גולמי מעודכן` — so it already carries מנהלת
הגמלאות's own pivot. The engine reads `גולמי`. Comparing IDs: **20,053 ours,
20,053 theirs, zero difference in either direction**. Nothing else in the repo
has had an outside check on this number before. *(The file has no `תאריך שכר`
column, so the report labels the month `golmi_1213` rather than `12/2013`.)*

**805 matches 110 of 110 — the first perfect score.** 107.88 for 102 carriers
plus clean job fractions (0.75, 0.625, 0.6). c+60 lands in 61-71, inside the
61-102 band, consistent and no narrowing of c ∈ [1,11]. It is the counter-example
to last month: where the band exists the component validates completely; where
it was missing it collapsed to 1.9% and was silenced.

**I am retracting the 808 finding from 0z/0x.** The single carrier here is paid
**215.73 — exactly** what the table gives for codes 49-102, the same band where
12/2012 deviated. I had written that two observations straddling a boundary
"is not noise" and implied the table has too few pulses; a third observation in
that same band matches exactly, which the coarse-table story does not survive.
There is also a premise I under-weighted: the pulse tables are indexed by
**retirement month**, not by the payslip's month, so a lone carrier can reflect
personal circumstances rather than a period. Three observations, one carrier
each, support no claim about the 808 table. §9's instruction has been withdrawn
and replaced with "not a finding — needs a file with a real 808 population".

**Two buckets fire for the first time:** דריכות = 52 and בוררות מיסים = 52,
both 0 in all five earlier files. גמול מנהל = 168 (4983 trusted at 97.5%).

**The new 875 column reads 0 here — but not because there are no gaps.** 875 has
68 mismatches out of 2,075, i.e. **96.7%, a hair under the 97% gate**, so the
rule is silenced outright and nobody reaches the bucket. The column only fires
in months where 875 clears the gate: 12/2012 it did and caught 25, here it did
not and the column is empty. Worth knowing before reading the column as a stable
neutralizer — it neutralizes when the switch happens to be on.

Coverage gap: **3 codes / ₪10,401**, the largest sum measured but in only three
codes — 4140 משכ.בסיסית (₪9,363 over 5 rows), 5315 (₪865), 507 (₪173). 4140 now
appears in **four** files (12/2008, 12/2010, 12/2012, 12/2013) and 507 in all
six historical months. Calibration silenced 29 of 50 rules; 5,282 workers
(26.3%), ₪1,930,322, of which ₪1.71M is 4550.

## 0ac. 5272 out of scope — fourth batch

Off the 12/2012 coverage list, on the user's instruction. Same two checks and
both pass: 5272 (ימי מחלה) is absent from the workbook in every sheet and
absent from `component_rules.json` in every field. It occurs once across all six
sample files — 12/2012, one row, ₪73.53. `NON_PENSIONABLE` is now **30 codes**;
Python and JS compared element-wise and in sync, 34 tests pass, `node --check`
clean.

12/2012's coverage gap goes **6 codes / ₪9,083 -> 5 codes / ₪9,010**. No other
file moves, the partition closes, and the verdict is unchanged at 97.90%.

**What is left in that gap, and should stay:** 4140 משכ.בסיסית (₪5,934), 5315
(₪1,703), 1132 (₪945), 729 (₪255), 507 (₪173). 4140 is the recurring expensive
one — it also appears in 12/2008 and 12/2010 — and 507 appears in all five
historical months. Both are pay components rather than benefits, so neither is
an out-of-scope candidate; they are a genuine coverage gap in the workbook and
removing them from scope would only hide it.

## 0ab. A neutralization column for 875 — built as asked, and flagged

The user asked for a **"שגויי תוספת בית משפט"** column immediately after
"שגויי תוספת בית חולים". Delivered: new `err_cat` bucket `bmish` at exactly
that point in the priority chain, in all three places that must agree —
`tools/unified_report.py`, `index.html`, `salary_frontend.html`. The two HTML
files were byte-identical before and after. The dashboard is now **20 columns**,
so every column index shifted by one: the INT range, the warn-colour set, the
real-error column, the % column, the `S`/`T` conditional-formatting ranges, the
banner merge, and the side table's origin (now column `V`). Partitions close on
all six files.

**What it absorbs, measured before building it:** 25 workers, **all in
12/2012**, and every one of them carries 875 **alone** — no other flagged code
travels with them, so the bucket swallows nothing. Zero in the other five files.
That is the `CLAUDE.md` check and it comes back clean.

**What is not clean is the justification.** 741 (בוררות מיסים) and 705
(מקצועית מיסים) were neutralized on evidence: their gaps are integer multiples
of the component, the retro signature. I ran the same test on 875 and it fails
— of 53 mismatches, **none** is an integer multiple (2×/3×/4×/12×). Ratios
scatter from **−1.87 to 2.52**, median 1.0519, including a negative payment
(₪−552.73 where ₪+295.69 was expected). There is no retro signature here.

**The effect on the headline is large:** 12/2012 drops from **27 true errors to
2**, and ₪2,924 leaves the count — **₪2,398 of it overpayment, money to
recover**. Overpayment is not a retro pattern; it is exactly the category that
must not be silently suppressed. The file now reads as nearly clean because of
a suppression, not a fix.

**What would retire the column:** carry out §4's existing instruction for 875 —
sample 3-5 mismatching slips and determine whether the gap comes from the base
composition in the חוקה (then the Progim needs a missing code and the bucket is
unnecessary) or from genuine retro (then the bucket is justified and the
evidence should be written down). Until that is done, this column makes the
number look better than the evidence supports. Do not quote 12/2012's "2 true
errors" without saying so.

## 0aa. The user corrected the workbook — 805 codes 49-60 = ₪104.61

The user filled the value measured in 0z and uploaded a corrected workbook. It
is installed as `data/progim/Progim_04.08.2026.xlsm`, replacing the previous
file of the same name (same workbook, corrected — the git diff is the record).

**What changed, verified:** a cell-level diff across all 54 sheets shows
**exactly 12 cells** — rows 55-66 of column 55, i.e. codes 49-60, all set to
104.61. Nothing else in the workbook moved.

**What it bought:** 805 in 12/2012 goes from **1.9%** (2 of 104) to **95.2%**
(99 of 104). 97 more slips now agree with the workbook.

**What it did not buy:** 95.2% is **below the 97% trust gate**, so 805 stays
silenced and the component is still not checked in that month. **No number in
any report moved** — partitions, true-error counts and validity percentages are
identical across all six files before and after. The fix is correct and
verified; its value is agreement, not a changed result. Do not report it as
having improved the numbers.

The 5 residual mismatches are all **underpayments** that do not divide by job
fraction (90.66, 87.17, 62.77, 73.90, 18.09) — the signature of a partial month,
not a table defect. They should not be flagged.

**Two things remain open on 805, and the first is the important one:**

1. **The formula still does not reach the table.** `tosafot!BC2` is unchanged:
   `VLOOKUP($C$4,$AR$7:$BC$234,8,0)`, while 805 is index **12** of that range
   (AR=44 … BC=55; index 8 returns column 51, *תוספת פנימיה*). So **the workbook
   itself still cannot produce 805** — only a consumer that reads the table
   directly, like this engine, benefits from the fill. That is §11 and it is
   still open. Say this plainly to the user; filling the table looks like a fix
   and is only half of one.
2. **Codes 205-228 are still empty**, and that is the current period.

**Operational warning, now confirmed with numbers:** I did **not** re-run
`tools/extract_rules.py`. Running it on the new workbook produces **32 rules
instead of 102** and destroys **70 hand-edited rules**, including 805 and 808
themselves plus the retro-code pairings (105/798, 1037/4544, 1054/4934,
1057/4994, 1059/5216, 1077/5401). I hand-edited `component_rules.json` instead:
805's `amounts` gained 104.61 and its notes were updated. This is exactly the
`CLAUDE.md` warning, and it is now measured — never regenerate that file.

## 0z. The 12/2012 file — it falls inside a table hole and supplies the value

Sixth file: **December 2012** (189,897 rows, 20,485 workers, 40 bodies, 97
codes). **97.90% · 27 true errors · ₪3,049**; partition closes at 20,485. Docs
only. Written up in `PROGIM_IMPROVEMENTS.md` under "בדיקת קובץ 12/2012".

**The result that matters: 805 codes 49–60 = ₪104.61.** This is the first file
that lands *inside* one of the two holes left in the 805 pulse table after the
04.08 fill — c+48 ∈ [49,59] is exactly the 49–60 gap — and it measures the
missing value. Of 105 carriers, **98 imply a full-time ₪104.61**, across six
different job fractions (1.0, 0.875, 0.75, 0.625, 0.6, 0.5) that all reduce to
the same number. It is also monotone in the table: 102.85 (37–48) → **104.61**
→ 107.88 (61–102). The instruction is in `PROGIM_FIXES.md` §9. Job-fraction
agreement across six denominators is what makes this a measurement rather than
a guess — do not weaken it to "probably".

**And it prices the hole.** A `shekel` rule accepts **the closest of its listed
amounts**, scaled by job% — there is no period logic and no code→date mapping in
the engine at all. With 104.61 absent from the list the closest was 102.85, so
805 matched **1.9%** (2 of 104), dropped below the trust gate, and **the whole
component went unchecked**. *(Correcting my own earlier wording: nothing is
"carried forward" — the conclusion holds, the mechanism is different. This also
means the c ∈ [1,11] dating affects diagnosis only, never validation.)* The same component was at
97.2% and checked one month earlier. Twelve empty cells switch a component off
— and without the self-calibration they would instead have produced 104 false
alarms. That is the clearest argument yet for why the calibration layer exists
and why the fix belongs in the workbook.

**808 repeats, in the opposite direction.** The single carrier is paid ₪209.20
where the table says 215.73 for codes 49–102. With last month: 201.15 < 205.68
(12/2011) < 209.20 (12/2012) < 215.73 — two paid values falling *between* two
table steps, *in ascending order*. The table makes one big jump at code 49
where the real series takes two. Still one carrier per month, so it is an
indication and §9 says so, but two independent observations straddling the same
boundary in opposite directions is not noise.

*Correction to an earlier note in this handoff:* the 808 table is **column 81**
of `tosafot `, not 56. Column 56 holds a flat 237.16 and is a different
component. The description of 808's contents (228 of 228, eight pulses) was
right; only the column number was wrong.

**4983 flips back to silenced** at 85.1% (7,489 of 8,798), so the גמול מנהל
bucket goes 164 → **0**. One month up, one month down. Cleanest demonstration
so far that the 97% gate is a switch, and that comparing "שגיאות אמת" across
months without reading the bucket columns compares two different things.

**True errors concentrate in one code:** 25 of 27 are **875 תוספת בתי משפט**
(92.6%, ₪2,924). 875 is already in `PROGIM_FIXES.md` §4 as a near-match rule
(2,819 carriers, 90 mismatches in 0108). Here it stops being a footnote and
becomes nearly the whole result — it is the one of §4's five to sample first.

Coverage gap: **6 codes / ₪9,083**, the largest since 12/2010 — 4140
משכ.בסיסית (₪5,934), 5315 (₪1,703), 1132 (₪945), 729 (₪255), 507 (₪173), 5272
(₪74). 4140 also appeared in 12/2008 and 12/2010; it is the recurring expensive
one. Calibration silenced 35 of 51 rules; 5,943 workers (29.0%), ₪2,405,375, of
which ₪1.82M is 4550.

## 0y. 5281 and 1265 out of scope — third batch

Off the 12/2011 coverage list, on the user's instruction. Same two checks as
the previous batches and both pass: absent from the workbook in every sheet,
absent from `component_rules.json` in every field. Each appears exactly once,
in 12/2011 only — 5281 מענק שנתי at ₪266.66 and 1265 דמי הבראה at ₪114.17.
`NON_PENSIONABLE` is now **29 codes**; Python and JS compared element-wise and
in sync, 34 tests pass, `node --check` clean.

12/2011's coverage gap goes **4 codes / ₪1,296 → 2 codes / ₪915.26**. The other
three files do not move — neither code appears in them. Verdicts unchanged
across all four (98.76% · 98.59% · 98.40% · 97.62%) and every partition closes.

1265 is the **fourth** דמי הבראה variant on the list, after 1266, 1260 and
1269; 5281 joins 4962 (מענק חד-פעמי). §15 now says so explicitly — one benefit
occupying four codes is more evidence that scope is being decided code by code
with no rule behind it.

**What is left in the coverage gap, across the four historical files:**

| file | codes | ₪ | largest |
|---|---|---|---|
| 12/2008 | 5 | ₪1,898 | 4140 משכ. בסיסית (₪1,035) |
| 12/2009 | 2 | ₪323 | 507 (₪173) |
| 12/2010 | 8 | ₪7,539 | 1104 שכר עבודה (₪3,539) |
| 12/2011 | 2 | ₪915 | 1132 תוס. קלדנות (₪742) |

**507 (השל. מהוראה) is in all four**, ₪173–₪251 every month, and it is the one
marked "מוזכר כקלט בלבד" rather than "לא נמצא בכללים" — the workbook knows how
to *read* it but not to *produce* it. That makes it a genuine coverage gap, not
an out-of-scope candidate. Do not put it on `NON_PENSIONABLE` to make the
number go away.

## 0x. The 12/2011 file — 808 pays an amount the table does not contain

Fifth file: **December 2011** (184,552 rows, 20,371 workers, 39 bodies, 89
codes). **97.62% · 11 true errors · ₪4,779**; partition closes at 20,371. Docs
only. Written up in `PROGIM_IMPROVEMENTS.md` under "בדיקת קובץ 12/2011".

**The finding worth carrying forward.** The file's single 808 carrier is paid
**₪205.68**. The 808 pulse table — the one filled to 228 of 228 in the 04.08
workbook — contains only 198.46, 201.15, 215.73, 217.89, 221.67, 224.90, 228.68
and 232.78. **205.68 is not among them**, and by the code ranges December 2011
sits in codes 24–48 where the table says 201.15: a ₪4.53 / 2.25% gap. So a
table that looks complete may still be **missing a pulse** — a different defect
from §9's empty cells. One carrier only, so it is an observation, not a claim;
the rule is silenced below n=20 and nobody was flagged. Recheck on any file
with a real 808 population.

**Dating: consistent, no narrowing.** 805 pays 102.85 here (104 of 107), the
codes 37–48 value. c+36 ∈ [37,48] gives 1 ≤ c ≤ 12, which adds nothing to the
c ∈ [1,11] already established in 0w. Code 1 remains "some month between
February and December 2008". The four Decembers do line up cleanly across the
bands, which confirms the code axis advances month by month — but not where it
starts.

**4983 crosses the threshold here.** גמול מנהל matches 97.2% (8,087 of 8,317)
and is therefore trusted, where it was silenced in 12/2008, 12/2009 and
12/2010. Its bucket jumps from 0 to **164 workers**, all of whom leave the
true-error count. Same fragility as 805 in 0w: a small movement around the 97%
gate decides whether a whole component is checked or neutralized, and the
headline moves with it. When reading a historical report, read the bucket
columns, not just "שגיאות אמת".

**1297 — fifth point, and do not straighten the story.** The three large
samples agree (2026 n=55 → 1.0596; 2008 n=45 → 1.0594; 2009 n=21 → 1.0594).
The two small ones disagree with the cluster *and with each other* (2010 n=11 →
1.1131; 2011 n=6 → 1.1579). Having already corrected one conclusion about 1297
this session, the careful statement is: stable at ~5.95% in the large samples,
and 6–11 carriers is not enough to conclude anything. §10 stands, not
strengthened further.

Coverage gap: **4 codes / ₪1,296** — 1132 (₪742), 5281 (₪267), 507 (₪173) and
**1265 דמי הבראה (₪114)**. Note 1265 is a *fourth* דמי הבראה variant; 1266,
1260 and 1269 are already out of scope, so it probably belongs there too —
not added without instruction. Calibration silenced 30 of 51 rules; 4,658
workers (22.9%), ₪2,239,754, of which **₪1.86M is 4550** yet again.

## 0w. The 12/2009 file — my dating from 0t is wrong

Fourth file: **December 2009** (136,292 rows, 21,842 workers, 35 bodies, 80
codes). **98.59% · 12 true errors · ₪2,315**; partition closes at 21,842. Docs
only. Written up in `PROGIM_IMPROVEMENTS.md` under "בדיקת קובץ 12/2009".

**It refutes 0t.** I concluded from 12/2008 + 12/2010 that code 1 = January
2008. Under that, Dec 2009 is code 24 and must pay 100.59. **It pays 95.80**
(99 of 105), and 808 pays 198.46 — both codes 1–23 values.

With c = the code of Dec 2008: c ≤ 11 (because c+12 is still in 1–23) and
c ≥ 1 (because c+24 is in 24–36). So **code 1 is some month between February
and December 2008**, and the 95.80 → 100.59 step happens somewhere in 2010.
December-only files cannot narrow it further.

The lesson is the one §14 already asks for: I tried to date the pulse table
from payslips, got an answer that looked decisive from two files, and a third
file broke it. **Do not derive a code→date map from data.** Fix the sheet.

Three other things from this file:

- **805 is silenced here at 95.2%** (100 of 105; the five outliers are 191.60
  ×3 — double the amount — plus 169.26 and 95.73). It was trusted in 12/2008
  and 12/2010 after the 04.08 fill. Two workers decide whether the component is
  checked at all, which is worth remembering before quoting a threshold result.
- **669 is back to normal**: ₪51.09 on 6,793 of 7,926 carriers, rule trusted at
  98.7%, same as 12/2010. So the ₪17.5M in Dec 2008 is confined to that one
  month and is not a code that changed meaning — good support for the one-off
  arbitration reading, still unconfirmed by the user.
- **1297 gives 1.0594 again** (n=21). Four points now: 2008 1.0594 (n=45), 2009
  1.0594 (n=21), 2026 1.0596 (n=55), and 12/2010's 1.1131 (n=11) as the lone
  outlier. The ~5.95% gap is stable; §10 stands.

Coverage is the best measured so far: **2 codes / ₪323** (507 and 4124).
Calibration silenced 29 of 48 rules; 5,814 workers (26.6%), ₪2,653,280 — of
which **₪2.36M is 4550 alone**, the same period gap as every other historical
file. Do not quote that total flat.

## 0v. A neutralization bucket for 705 — and what it swallows

The user asked for a **"שגויי מקצועית מיסים"** column immediately after
"שגויי בוררות מיסים". Delivered: new `err_cat` bucket `mikzoit`, placed at that
exact point in the priority chain, in all three places that must agree —
`tools/unified_report.py`, `index.html`, `salary_frontend.html`. The two HTML
files were byte-identical before and after. The dashboard is now 20 columns, so
every column index in the per-file table shifted by one (INT range, warn-colour
set, real column, % column, the `R`/`S` conditional-formatting ranges and
`cbase` for the second table). The partition still closes exactly on all three
sample files: 24,543 · 20,754 · 6,901.

| file | true errors before | after | moved |
|---|---|---|---|
| 12/2008 | 26 | **15** | 11 |
| 12/2010 | 22 | **11** | 11 |
| `golmi.xlsx` | 43 | **32** | 11 |

**The widening check CLAUDE.md demands, and it matters here.** The bucket
catches *any worker with a 705 gap*, carrying all their other gaps with them:

| file | ₪ actually from 705 | ₪ from other components, swallowed |
|---|---|---|
| 12/2008 | ₪9,478 | ₪0 |
| 12/2010 | ₪4,533 | ₪9 (805) |
| **`golmi.xlsx`** | **₪3,035** | **₪6,121 — 5402 (₪2,851) + 5524 (₪3,270)** |

In `golmi.xlsx` two thirds of the money behind the new column is not 705.
**5402 and 5524 are that file's two largest error causes** (41 and 38 workers,
₪21,005 and ₪20,402) and 10 of the 11 absorbed workers carry them. They left
the true-error count without anyone deciding they were correct.

The retro justification also only partly holds. Of the 33 absorbed workers
across the three files, **7** pay a whole multiple of 158.63 (×12, ×4, ×3); the
rest pay 227.37, 243.23, 195.64 and similar. In `golmi.xlsx` **none** of the 11
is a multiple. The largest single error in 12/2008 — ₪5,676.96, worker
25119409 paid ₪5,835.58 against ₪158.63 — is not a multiple either, and is now
neutralized.

**The narrow alternative, if the user wants it:** gate the bucket on the slip
amount being a whole multiple of the חוקה amount. That neutralizes 7 workers
instead of 33, keeps 5402/5524 in the count, and returns the ₪5,677 error to
the queue. One condition, in the same three places.

Nothing in the workbook needs fixing for this — 705 is defined correctly there
as a fixed ₪158.63. What retires the bucket is a **retro flag in the גולמי**.

## 0u. Six more codes out of scope — 1047, 4114, 4537, 4535, 4454, 4134

Second batch, off the 12/2008 coverage list, on the user's instruction (4134
came as a follow-up mid-turn after I flagged it as 4133's sibling). Same two
checks as batch one: none appears anywhere in the workbook, none appears in
`component_rules.json` in any field. `NON_PENSIONABLE` is now **27 codes**.

| file | coverage gap before | after |
|---|---|---|
| 12/2008 | 10 codes / ₪3,587 | **5 / ₪1,897.89** |
| `golmi.xlsx` | 20 codes / ₪659,951.33 | **19 / ₪622,483.26** |
| 12/2010 | 8 / ₪7,539.31 | unchanged — none of the six appears there |

Verdicts identical on all three (264/98.76%, 324/98.40%, 168/97.48%), and
"פר עובד", "שגויים לבדיקה", "ריכוז לפי סיבה", "פילוח משרדים" came out
row-for-row identical. 34 tests pass, `node --check` clean, Python and JS sets
compared element-wise and in sync at 27 each.

**Two things left deliberately open, and the next session should not "tidy"
them away:**

1. **4535 appears in none of the three sample files** and not in the workbook.
   It was added as asked — declaring an unobserved code is harmless — but it
   does nothing today.
2. **4536 (ממוצעי שכר) was not named and is still in the gap list.** It is
   4537's twin: identical component name, 2 rows, ₪5.00, same file, adjacent
   code number. Given 4535 was named and does not exist while 4536 exists and
   was not, **4535 is plausibly a typo for 4536** — but that is a guess about
   intent, so it was raised with the user rather than acted on. If they confirm,
   add 4536; do not silently swap it for 4535.

`golmi.xlsx` moved the most in shekel terms because **4114 alone is ₪37,468**
there — it was that file's second-largest coverage-gap entry.

## 0t. The 12/2008 file — the pulse tables are now dated, and one code holds ₪17.5M

Third file this session: a **December 2008** גולמי (163,984 rows, 24,543
workers, 34 bodies, 87 codes). **98.76% · 26 true errors · ₪18,823**; partition
sums exactly to 24,543. Full write-up in `PROGIM_IMPROVEMENTS.md` under
"בדיקת קובץ 12/2008". Docs only — no code changed.

**It dates the 805/808 pulse tables.** 12/2008 pays 805 = 95.80 (103 of 107)
and 808 = 198.46 — the codes 1–23 values. Only one of the two dating
hypotheses survives both files:

| hypothesis | Dec 2008 | Dec 2010 | fits |
|---|---|---|---|
| **code 1 = Jan 2008** | code 12 → 95.80 ✓ | code 36 → 100.59 ✓ | **yes** |
| code 1 = Jan 2009 | falls off the table | code 24 → 100.59 ✓ | no |

So 805 is 95.80 through Nov 2009, 100.59 Dec 2009–Dec 2010, 102.85 from Jan
2011. This is an inference from two months, **not** a workbook statement —
`PROGIM_FIXES.md` §14 now records it as such and the fix request stands. Do not
hard-code a code→date map off it.

> **Refuted in 0w.** The 12/2009 file pays 95.80, where this dating requires
> 100.59. With three points the answer is only that **code 1 falls somewhere in
> Feb–Dec 2008**. The inference was wrong; the §14 fix request is the point.

The 04.08 fill flipped 805 here too, by a hair: **103/107 = 96.3% (silenced) →
104/107 = 97.2% (trusted)**. The worker who crossed it was paid 114.96; the new
114.36 pulse sits ₪0.60 away, inside tolerance.

**⚠ Code 669 (בוררות) carries ₪17,530,235 in this one month.** 10,716 workers,
10,384 of them משרד הבריאות, the modal amount a flat **₪2,596.31** — 50.8× the
₪51.09 the חוקה defines (`tosafot!X3`). The same code in 12/2010 matches the
חוקה almost perfectly: 6,682 workers at exactly 51.09, rule trusted at 98.4%.
Their median 10002 is ₪2,571, so the 2008 amount is about one combined salary.
Most likely a **one-off arbitration settlement to משרד הבריאות in Dec 2008** —
in which case there is nothing to fix — but that needs the user's confirmation,
because the alternative is a code that changed meaning and is unverified. The
engine flagged nobody: the rule fell to 0.8% and self-silenced, as designed.

**Calibration**: 28 of 47 rules silenced; 13,124 workers (53.5%) carry a
failing check on one, ₪17,927,773 absolute. **Do not quote that total flat** —
₪15.2M of it is code 669 alone and ₪2.2M is 4550 (median ratio 0.388, same as
in 12/2010, a genuine period gap). The rest is ~₪0.5M scattered.

Other notes: **756** shows a tight constant offset here (IQR 1.017–1.023, the
same shape as 920 in 12/2010). **3,145 workers (12.8%) have no active base**,
five times the 12/2010 rate — unexplained, worth a look. Coverage gap is tiny,
**10 codes / ₪3,587**, and its largest entry is **4134 (ת.יוקר-הפסק, 1,074
rows, ₪1,138.67)** — sibling of 4133 which is already out of scope. It looks
like it belongs on `NON_PENSIONABLE` too; I did not add it without being told.
Retro again dominates the queue: 705 paid ₪1,903.56 = 12 × 158.63 and ₪634.52 =
4 × 158.63, and 11 of the 26 true errors are 705.

## 0s. Seven codes out of scope — 4962, 4122, 4264, 4443, 4121, 5271, 1269

The user named these seven and said to define them as non-pensionable. Added to
`NON_PENSIONABLE` in `main.py` and mirrored in `engine.js`. Commit `b5c2476`.

**Why it was safe to apply directly.** Two checks before touching anything:
none of the seven appears anywhere in the workbook (code rows of `SACHAR`,
`tosafot `, `SACHAR4643`, plus `Netunei Gimlai` and `sminimum` were scanned),
and none appears in `component_rules.json` — not as a rule key, not in any
`codes` / `base_codes` / `deductions`. So the change cannot move a number; it
only says the workbook's silence about them is deliberate. Three extend
families already on the list: 1269 joins 1266/1260 (דמי הבראה), 4264 joins
903/889 (הפרש ברוטו).

| file | coverage gap before | after | verdicts |
|---|---|---|---|
| 12/2010 | 15 codes / ₪11,242.80 | **8 / ₪7,539.31** | 324 invalid / 98.40% — unchanged |
| `golmi.xlsx` | 21 codes / ₪659,951.65 | 20 / ₪659,951.33 | 168 invalid / 97.48% — unchanged |

Exactly the seven dropped and nothing else; "פר עובד", "שגויים לבדיקה",
"ריכוז לפי סיבה" and "פילוח משרדים" came out row-for-row identical on both
files. Classification tally: "לא משתתף בחישובים" 13 → 20, "לא מוגדר בחוברת"
15 → 8. `golmi.xlsx` barely moves because only 5271 (₪0.32) appears in it.

**The divergence, and where it is recorded.** `NON_PENSIONABLE` now holds 21
codes and **not one of them has a Progim source** — the whole list came from
the user verbally. `PROGIM_IMPROVEMENTS.md` carries what was added and why;
`PROGIM_FIXES.md` **§15** carries the request that would retire it: a declared
scope column in the workbook (`sminimum` alongside the existing כן/לא flags, or
`Netunei Gimlai`). Do not reach for the גולמי's own "ביט פנסיוני" column as a
substitute — on the 0108 file it reads 'כן' for all 124,818 rows, these codes
included. Until the workbook declares scope, a code dropped from this list by
mistake simply stops being checked, with nothing on screen to say so.

When adding to the list, change **both** `main.py` and `engine.js`. To confirm
they agree, parse the JS set and compare element-wise against
`main.NON_PENSIONABLE` — a mismatch means the site and the CLI disagree.

## 0r. The 12/2010 file — the 04.08 fill is confirmed, and a caveat worth more

The user then uploaded a **December 2010** גולמי (155,575 rows, 20,754 workers,
39 bodies) and said "בדוק קובץ". Full write-up in `PROGIM_IMPROVEMENTS.md`
under "בדיקת קובץ 12/2010". Result: **98.40% · 22 true errors · ₪6,214**,
partition sums exactly to 20,754.

**It closes the loose end from 0q.** 12/2010 pays 805 = **100.59** (105 of 109
carriers, across 5 different part-time fractions) and 808 = **201.15** — both
values that did not exist in the workbook before 04.08. Measured directly with
`main.trusted_rule_codes`:

| | old rules | new rules |
|---|---|---|
| 805 match | **1 / 108 (0.9%)** → silenced | **105 / 108 (97.2%)** → trusted |
| 808 match | 0 / 1 (₪2.69 off) | 1 / 1 exact (still n<20, untrusted) |

So the workbook fill **switched 805 from blind to checked** on this file and
surfaced 3 gaps / ₪224 including one true error of ₪130 (worker 200526751).

**The caveat is the bigger finding, and it is not about 805.** On this file the
self-calibration gate silences **33 of 49 rules** — every large percent rule
among them (4544 95.9%, 4934 94.8%, 4624 94.4%, 4983 94.9%, 798 96.7%, 741,
875, 4550). **5,252 workers (25.3%) carry at least one failing check on a
silenced rule, ₪2,567,553 in absolute gaps.** That is the gate working as
designed — 2026 rates against 2010 slips would otherwise produce thousands of
false positives — but it means the 98.40% was measured against 16 rules, not
49, and **must not be quoted next to a 2026 file's percentage**. If you run
another historical file, report the silenced-rule count with the headline.

Two things fell out of the ratio analysis (`slip ÷ expected` per silenced rule):
**920** fails with an IQR of 1.021–1.025 — a constant 2.4% offset, not noise,
which is the embedded 257.37 constant being era-dependent; and **1297** sits at
1.113 here versus 1.0596 on the 2026 file.

> **Corrected in 0t.** I concluded from those two points that 1297's gap is not
> a fixed constant. The 12/2008 file gives 1.0594 on n=45 — 2008 and 2026 agree
> to four decimals and 12/2010 (n=11) is the outlier. The gap *is* stable, and
> §10's stale-constant hypothesis gets stronger, not weaker.

Also worth knowing: the top of the error queue is retro, not error — two
workers paid 705 = ₪1,903.56 = exactly 12 × 158.63, another at 3 × 158.63.
11 of the 22 true errors are 705. A **retro flag in the גולמי** would halve the
work queue; nothing in the workbook can fix it.

And a credit to the workbook: the 2026 `DARGA` table reproduces the 12/2010
base for **20,177 of 20,247** workers with an active base (99.65%). The
combined-salary scale has not moved since 2010; all raises are layered as
separate תוספות. That is why checking a 16-year-old file works at all.

### Open

- **The 0108 reference file (22,422 slips) was still not available** —
  `/root/.claude/uploads/<session-id>/` held only the workbook and the 12/2010
  file. The 04.08 rule change was verified against the repo's `golmi.xlsx`
  (6,901 workers, no change: 168 invalid / 97.48%) and then against the 12/2010
  file, which is what actually exercised the new pulses.
- **808's eight pulses still rest on two slips** — one in 12/2010 at 201.15,
  none in `golmi.xlsx`. Below the n=20 trust threshold, so the rule is silent
  wherever it appears. Worth re-checking on any file with real 808 population.
- The engine labels a 12/2010 805 slip "תקני 116.41" (nearest pulse) rather
  than the 100.59 in force. That is §14 biting operationally, not a rule bug —
  do not "fix" it by guessing a code→date mapping.
- §11 is worth putting in front of the user directly. It is the first defect
  found in this repo that produces a **wrong number silently** rather than a
  zero or a gap.
- Nothing was said to the user about 805's two remaining holes (codes 49–60,
  205–228) needing a decision — 205–228 is the current period, so a worker
  retiring now still gets 0 from the workbook for תוספת ערבה.

## 0q. Progim 04.08.2026 — two tables filled, four defects found

The user uploaded `Progim_04.08.2026.xlsm` and said only "תעדכן". Installed it,
deleted `Progim_01.08.2026.xlsm`, re-extracted, updated two rules, wrote up the
defects. Commit `15d9499`.

### What actually changed in the workbook

A full formula-level diff over all 54 sheets (`data_only=False`, ArrayFormula
compared by `.ref`/`.text`, not identity — comparing the objects directly gives
11 false positives) shows changes in exactly **two** sheets: `Netunei Gimlai`
(5 cells, all demo-worker scratch: ministry 18→22 and two eligibility toggles)
and `tosafot ` (363 cells). Every other sheet differs only in cached values,
which is the demo worker recalculating after the ministry change.

**No columns moved this time** — the first version in a while where that is
true. `lookups.json` re-extracts **byte-identical**; `progim_ingest.ingest`
returns `base_changes: []`; `extract_rules.py` produces no rate change (it
still emits only 32 of the 102 rules, so as always it was diffed, not applied).

The 363 `tosafot` cells are:

| Cells | What |
|---|---|
| `BC19:BC198` | 805's pulse table filled — 48 → **192 of 228** month codes |
| `CC19:CC234` | 808's pulse table filled — 12 → **228 of 228** |
| `BG2`, `BG6` | 875's four percentages inlined into the formula |
| `AZ2` | 756 — missing false branch of the outer `IF` added |

### The two rules I changed

`component_rules.json`, 805 and 808 only:

- **808** `amounts: [198.46]` → **8 pulses** `198.46, 201.15, 215.73, 217.89,
  221.67, 224.9, 228.68, 232.78`; `amount_period` `fixed` → `varies`.
- **805** `amounts` 4 → **9 pulses** `95.8, 100.59, 102.85, 107.88, 108.96,
  110.85, 112.47, 114.36, 116.41`.

Also corrected stale cell addresses in the `source` strings that column drift
had invalidated: 805 is `SACHAR!BF11` (the note said BB11), 808 is
`SACHAR!BG11` (said BF11), 4651 is `SACHAR!DD11 = DD7*(AA11+DB11)` (said
DB11/CZ11). Those are text-only; no base or rate moved.

**The divergence to keep in view:** the גולמי carries no retirement month, so
the engine accepts *every* pulse in a table. Filling the tables therefore made
the engine **more permissive** — 808 went from one accepted amount to a band
spanning 17%. Every one of those amounts comes from the workbook, so this is
not a heuristic, but detection power on those two codes did drop. Written up
in `PROGIM_IMPROVEMENTS.md` under "עדכון 04.08" with the thing that retires
it: a **retirement-month field** in the מנהלת הגמלאות file.

### The defect that matters — `PROGIM_FIXES.md` §11

`tosafot!BC2` is `VLOOKUP($C$4,$AR$7:$BC$234,8,0)`. `BC` is column **12** of
that range — `BC1` says so itself. Column 8 is `AY` = **681 תוספת פנימיה**,
a flat 303.18 ₪. So the workbook has been returning 303.18 for תוספת ערבה,
2.6x–3.2x the real 95.8–116.41, **with no `#N/A` and no zero to notice**. And
it means filling 805's table in 04.08 changed nothing in the workbook itself.

Same bug in `tosafot!BR2` (4651): index 26 points at `BQ` = 4453. The two
columns that reference their own index cell — `BQ1`, `CC1` — are correct. I
audited every `VLOOKUP` in `tosafot` row 2; those are the only two with a
hardcoded index, and both are wrong.

Three more, same file: §12 `tosafot!BM2` (1358) searches `$AR$7:$BM$12`, 6 of
228 codes, so the current 750 ₪ is outside the search range entirely. §13 875's
percentages are now constants in the formula and `BATEI MISHPAT 875` is a dead
sheet holding the same four numbers. §14 the `חודש פרישה` sheet is not
one-to-one — 34 discontinuities and 124 duplicated calendar months in
`A1:B693` (code 61 = 1.1.2002 then code 62 = 1.1.2001).

§14 has a consequence for the docs: **pulse boundaries cannot be dated.** The
older §9 text dated 805's pulses as "all of 2008 / 2011 / 2013 / 2024", which
assumed code 1 = Jan 2008; the workbook's own sheet says code 1 = 1.1.1997, and
the new fill (runs of 23, 13, 12, 42, 9, 14, 14, 4, 61 codes) is not
year-aligned anyway. The new rule text documents pulses **by month code only**.
Do not reintroduce calendar years for these without a fixed `חודש פרישה` sheet.

### Verified how

```
python3 -m pytest tests/ -q      →  34 passed
node --check engine.js           →  clean
python3 tools/unified_report.py golmi.xlsx --out /tmp/after.xlsx
                                 →  6,901 עובדים · 168 שגויים · 97.48%
```

Identical before and after the rule change: all 6,901 "פר עובד" rows byte-equal,
"שגויים לבדיקה" unchanged, "ריכוז לפי סיבה" unchanged (5402=41, 5524=38,
705=11, 4932=1). The only report deltas are the two intended classification
lines in "סיווג סמלי שכר" — 808 moving fixed→varies, so the tally row goes
`קבוע 49 · משתנה 6` → `קבוע 48 · משתנה 7`.

`pytest` needs **`httpx`** installed on top of `requirements.txt`; without it
14 of the 34 tests error inside starlette's TestClient. `CLAUDE.md` said "20
tests" — corrected to 34 in the same commit.

## 0. Progim 31.07.2026

`data/progim` now holds the 31.07 workbook. What actually changed in it:

- **956 (הש. מצט. מנמ"ש, ₪40.83) and 957 (הש. מוכ. מנמ"ש, ₪61.32) are new** in
  `tosafot`, both constant across all 228 months. Both were on the
  "לא מוגדר בחוברת" list, so the gap drops **12 codes/₪226,806 → 10/₪219,906**.
  Remaining: 507, 642, 733, 797, 1297, 1375, 4133, 4180, 4406, 4651.
- **91 `tosafot` columns moved.** 4319 went CX→CZ, 4427 CY→DA. Rate resolution
  is by the code label in row 4, so nothing broke — this is the drift the
  dynamic lookup exists for. Do not reintroduce cell addresses anywhere.
- `lookups.json` re-extracted **byte-identical**. The `vetek` sheet does differ,
  but only in the single-worker calculator scratch area (a worker's vatek
  32.25→37), not the multiplier table.
- Re-running `extract_rules.py` yields the same 26 percent rules with **no rate
  change**. It still emits only 33 rules total and would drop the 60 curated
  ones plus the alias base codes — so it was diffed, not applied.

956/957 were validated against the slips before either rule was written:
**107/108** and **7/7** exact against `amount × חלקיות`. The single 956
outlier is worker 73742286 at −₪2,449.80, who was already invalid on גמול
השתלמות (₪19,777.20 against ₪328.76) — a retro month, not a rate error. He
stays in the גמול bucket; the new rules added no error at all (21,167 / 382,
13 real, unchanged).

**None of the three reported workbook defects was fixed in 31.07:** 5402 still
has no sum table (§7), 636 still holds 353.75 against its own 353.76 (§8), and
the 4319/4427 rate tables still cover 9 grades of 110 (§6).

## 0b. 805 (תוספת ערבה) now comes from the Progim

Per the user: 805 is a varying-amount tosefet whose figure must come from the
workbook, not be accepted from the מנהלת הגמלאות file. Changed from
`type: reported` to `type: shekel` with the four pulses out of
`tosafot!BA2 = VLOOKUP(חודש פרישה, $AQ$7:$BA$234, 8, 0)`:
95.8 (2008) → 102.85 (2011) → 107.88 (2013) → 116.41 (2024). All four are
accepted because the גולמי carries no חודש פרישה, so which pulse applies to a
given worker cannot be decided from the file.

Reported-by-design in the coverage banner: 10 codes/₪606,867 → 9/₪597,678.

**Validated on 97 carriers: 93 match (95.9%), 4 do not** — worker 23845808
(−₪145.72, a reversal), 36429698 (₪150.08 vs ₪116.41), 36828089 (₪211.88 at
64.5% job against ₪75.08 — nearly triple), 55654954 (the full 2008 figure paid
at 75% job, unprorated).

**The rule computes but does not yet fail a slip.** Self-calibration needs 97%
and this is 95.9%, so all four sit below the gate. It was **not** overridden:
forcing it would flag 4 of 97 on a sub-threshold match, which is the exact
false-positive risk the gate exists for. The four are named in
`docs/PROGIM_IMPROVEMENTS.md` so they are actionable without a flag.

Workbook defect found doing this, written up as `PROGIM_FIXES.md` §9: the 805
table is filled for **48 months of 228** (only 2008, 2011, 2013, 2024) and the
VLOOKUP is exact-match, so a worker retiring in any other month gets 0 from the
workbook with no error.

## 0n. Second 01.08 workbook — one cell changed, 1297 still fits nothing

A cell-by-cell diff across all 54 sheets found **exactly one difference in the
whole workbook**: `SACHAR!BZ11`, the constant `5.33` replaced by `5.331`.

That is the 1297 constant reported in `PROGIM_FIXES.md` §10. It moves the rate
16.28611% → 16.28917% — **0.019%, against a measured gap of 5.94%**, roughly
310× too small. The rule was updated to the new constant for fidelity and the
result is unchanged: **0 of 55** slips reproduced, median paid ÷ formula 1.0594
(was 1.0596), self-calibration still silences it, nobody flagged.

The untested suspect remains the **divisor 180** — 170 takes the match from
0 to 31 of 55, and it is the only constant whose plausible correction moves the
result by the right order of magnitude. The 24 that still miss point at the
standby count 5.5 being per-worker rather than constant, exactly as 4180 works
via `Netunei Gimlai!H81`.

Everything else is untouched: 110 codes, no column moved, `lookups.json`
identical, and the other six defects (§6–§9) unfixed.

**Do not put 170 in.** It would look like a fix and would instead turn the
engine from a validator of the workbook into a mirror of the payroll, and this
finding would disappear from the report.

## 0m. 4180 is group-selected — and a label of mine was wrong

Per the user: the amount comes from the ministry file because a standby count
must be entered. The workbook confirms it in full:
`SACHAR!EE11 = (wide base) / EE7 × 5.33 × EE8`, with `EE7 = tosafot!CY6 = 184`
and `EE8 = tosafot!CY3 = 'Netunei Gimlai'!H81` — **the count, hand-entered**.
The `מנדיי` sheet says so in words: 4 standbys/month for רשות האכיפה (127),
"6.00" for משרד המשפטים (116), and *"הסמל מדווח ידנית ולא מגיע מהנוכחות"*.

Classified `תוספת סכומית משתנה לפי בחירת קבוצה` (4 members now) and moved in
the coverage sheet to **"מוזן מהקובץ — כך ב-Progim"**, i.e. correct-by-design
rather than a hole. Real gap now **1 code / ₪251** — 507 alone.

**A reporting defect of mine, found doing this.** I reported 4180 as
"לא קיים כלל בחוברת". It is false: 4180 sits in `SACHAR!EE`, `tosafot!CY`,
`sminimum` and seven other places. The label was derived from the code's absence
from **our extracted rules**, which is a different statement. Reworded in all
three surfaces:

- `לא קיים כלל` → **`לא נמצא בכללים`**
- an explicit sentence added: the labels describe the extracted rules, **not the
  workbook**, and the workbook may well define the component.

This matters beyond 4180: while it read "absent from the workbook", every code
our extraction missed looked like a hole in the product the user sells, instead
of a gap on our side.

**New mechanism:** `amount_period_locked` on a rule tells
`classify_hukka_amounts.py` to leave the classification alone. Without it, a
re-run overwrites an author-stated classification with "unknown" whenever the
component's inputs sit outside the tosafot/grid layouts the tool reads — which
is exactly 4180's case.

## 0l. 1297 is formula-computed — and the workbook's formula fits nothing

Per the user. The workbook does define it:
`SACHAR!BZ11 = 5.5 × (משולב + גמול א + גמול ב + 4544 + 4550) / 180 × 5.33`,
an effective **16.286%**. Classified "מחושב לפי נוסחה"; gap
**3 codes/₪78,064 → 2/₪28,047**, leaving only 507 and 4180.

**But that formula reproduces 0 of 55 slips.** Every one is ~6% above it, and
uniformly: median ratio **1.0596**, with 52 of 55 inside 1.058–1.063.

Five alternative base compositions were tested to rule out a misreading — the
workbook's own base gives the *tightest* spread, so the base is right and one of
the three constants is stale. Prime suspect is the **divisor 180**: using 170
takes the match from 0 to **31 of 55**. Not conclusive (24 still miss), which
points to the כוננויות count (5.5) also being a per-worker input the גולמי does
not carry.

**The rule ships with the workbook's constants, not fitted ones.** It sits at 0%
match, self-calibration silences it, and nobody is flagged — 21,163 / 386 with
14 real, unchanged. Putting 170 or 5.828 in would be inventing a חוקה out of
payslips, which is the one thing this project forbids. Written up as
`PROGIM_FIXES.md` §10 with the numbers.

## 0k. Progim 01.08.2026 — 797 added, gap down to 3

`data/progim` now holds `Progim_01.08.2026.xlsm`; the classifier's default path
moved with it. The only content change is **797 (ת.שטחים ר.ג)** — the sibling
of 808 flagged as open one round earlier. `tosafot!BB3 = ₪31.62`, constant
across 228 months, `SACHAR!BD11` takes it directly. **1 of 1 carrier matches**:
worker 64295237, 31.62 × 0.5 = ₪15.81 to the agora.

Gap **4 codes/₪78,080 → 3/₪78,064**. What is left is the hard residue:

| code | status in the workbook | rows | ₪ |
|---|---|---:|---:|
| 1297 | input-only | 56 | 50,017 |
| 4180 | **absent entirely** | 29 | 27,796 |
| 507 | input-only | 2 | 251 |

**None of the six reported defects is fixed here** — 4319 (9/110), 4427
(8/110), 5402 (no sum block), 636 (353.75 vs 353.76), 805 (48/228), 4651
(12/228), 808 (12/228). 73 columns moved; `lookups.json` identical; no rate
changed; extraction still returns 25 percent rules with 5533 dropping out.

## 0j. 808 (תוספת שטחים) is now validated against the חוקה

Per the user: a fixed amount taken from the חוקה. It was `reported` — accepted
from the slip unchecked and listed in the **חסר ב-Progim** sheet under
"מוזן מהקובץ". Source: `tosafot!CB2 = VLOOKUP(חודש פרישה, $BU$7:$CB$234, 8, 0)`
= **₪198.46** across every filled month, with `SACHAR!BF11` taking it directly
— no rate, no base. Now `type: shekel`.

**1 of 1 carrier matches** — worker 27080220, משרד הרווחה, exactly ₪198.46.

Out of the חסר ב-Progim sheet (13 codes → 12) and classified
"סכום קבוע לכל התקופה". Reported-by-design line: 9 codes/₪597,678 →
8/₪597,479.

Same sparse-table defect as §9: 808's table is filled for **12 months of 228**
(all of 2008) with an exact-match VLOOKUP, so a worker retiring in any other
year silently gets 0. **797 (ת.שטחים ר.ג)**, its sibling, is still in the sheet
as input-only with no formula.

## 0i. 642 is a computed 6% component — closing the user's opening example

From the workbook in full: `SACHAR!AJ11 = (AA11 + AL11 + AO11 + DA11) × AJ7`
with `tosafot!AU2 = IF(eligible, 6%, 0)` — the rate is a literal in the
formula, not a table. So **6% × (10002 + 658 + 678 + 4624)**.

**42 of 42 carriers match, every one to the agora.** All 42 are
טלוויזיה לימודית.

This closes the example that opened the whole round. The user's complaint was
*"it did not flag components missing from the Progim, e.g. 642 and 678 in
the Educational TV"* — 642 really was unchecked then, appearing in the workbook
only as an input (4550 deductions, minimum counting) and never as a computed
component. Its formula has now been located and it is fully validated. **678
stays `manual`** — it is one of the six codes whose amount comes from the
משרד האוצר file, so it is deliberately not validated.

Gap **5 codes/₪87,204 → 4/₪78,080**. Remaining: 507, 797, 1297, 4180.

## 0h. Progim 31.07 — second file, same date: 733 added

A second `Progim_31.07.2026.xlsm` (different md5) adds **733 (ס. ניקוי כלים)**:
`tosafot!AA3 = ₪10.26`, constant across 228 months, and `SACHAR!AT11` takes it
straight — no rate, no base. Validated **4 of 4 to the agora** before the rule
was written, including two at 75% job paid exactly ₪7.70.

Gap **6 codes/₪87,240 → 5/₪87,204**. Remaining: 507, 642, 797, 1297, 4180.

**None of the five reported workbook defects is fixed here** — 4319/4427 rate
tables still 9 and 8 of 110 (§6), 5402 still has no sum table (§7), 636 still
holds 353.75 against its own 353.76 (§8), 805 still 48 months of 228 (§9),
4651 still 12 of 228.

**96 columns moved again**, and `extract_rules.py` on the new file returns
**25** percent rules instead of 26: **5533 (אחוזית 2024) drops out**, because
its rate row evaluates to 0 and the extractor rejects an invalid rate. The
curated 5533 rule is untouched (5 rates, 77 base codes) because the extraction
is **diffed, never applied** — this is precisely why that rule exists. Do not
"just re-extract" on a workbook upgrade.

`lookups.json` re-extracted identical again.

## 0g. 4133 (תוספת יוקר) out of scope

Not pensionable and not part of any calculation, per the user. Added to
`NON_PENSIONABLE` in both engines. It appears in no rule's `base_codes`,
`deductions` or `counted`, so taking it out of scope moves nothing —
21,163 / 386 with 14 real, before and after.

Gap **7 codes/₪87,571 → 6/₪87,240**; out-of-scope 13 → 14. Remaining gap:
507, 642, 733, 797, 1297, 4180.

Across this whole round the gap went **15 codes/₪294K → 6/₪87K**.

## 0f. New classification: percentage rate chosen by a group

The percent counterpart of 0c. **4406 (ת.ש. מקרקעין)** is the first member:
`SACHAR!CT11 = CT7 × (AA11 + CZ11)` with
`tosafot!BN2 = VLOOKUP('Netunei Gimlai'!H80, parameter!K20:L22, 2, 0)` — the
rate comes from a **1/2/3 group code hand-entered** in Netunei Gimlai:
1 → 12.75%, 2 → 16.5%, 3 → 27%. The גולמי does not carry it.

Unlike the shekel case the base IS computable, so the rule is a real `percent`
rule with all three rates: a slip paid at some *other* rate still fails. Only
"which of the three is right for this worker" is undecidable. A `rate_group`
field on the rule carries the explanation and drives the new label in the
report and both front-ends.

Gap 8 codes/₪99,113 → 7/₪87,571. Remaining: 507, 642, 733, 797, 1297, 4133,
4180.

18 of 19 carriers match a legitimate rate (15 at 16.5%, 3 at 27%). The
outlier is worker 25140422: ₪846.52 on a ₪3,467.50 base — an implied
**24.41%**, which is not one of the three. Against 27% that is ₪89.71 underpaid;
against 16.5% it is ₪274 overpaid, and without the group there is no way to say
which. With 19 carriers the rule sits under the 20-sample gate, so it computes
without failing anyone; the outlier is named in the docs instead.

## 0e. 1375 out of scope — and the minimum-wage list was wrong

**1375 (קצובת ביגוד)** is not pensionable per the user; added to
`NON_PENSIONABLE` in both engines. Gap 9 codes/₪104,997 → 8/₪99,113;
out-of-scope 12 → 13. Remaining gap: 507, 642, 733, 797, 1297, 4133, 4180, 4406.

**Found while checking it: rule 5260's `counted` list diverged from the
workbook.** It held **265** codes; `sminimum` column C marks only **192** as
'כן'. So 75 codes were counted toward minimum wage that the workbook says are
not — 1375 itself, 4935 (תוספת אמון), 5216 (מנמ"ש 2010), 4934, 4994, 5268,
5270 among them — and 10001/10002 (שכר משולב), the single most important
component, were **missing**.

The list is now read straight from `sminimum` column C rather than hand-kept.

Measured before and after: **zero verdict change** — 21,163 / 386 with 14 real
both ways, and 5260 flags nobody on the 0108 file regardless. The divergence
was inert on this data, which is exactly why it survived: it would only have
surfaced the day the rule started firing. Re-derive it from the sheet on every
workbook upgrade; do not hand-edit it back.

## 0d. 4651 is a computed 15% component

Per the user, and the workbook has it in full — not estimated:
`SACHAR!DB11 = DB7 × (AA11 + CZ11)` = 15% × (שכר משולב + הסכם 1999), rate from
`tosafot!BP2 = VLOOKUP(חודש פרישה, $AQ$7:$BP$234, 26, 0)`. Added as a percent
rule, `base_codes [1, 2, 4624, 10002]`.

Gap list **10 codes/₪219,906 → 9/₪104,997**. Remaining: 507, 642, 733, 797,
1297, 1375, 4133, 4180, 4406.

**244 of 248 carriers match (98.4%)** — above the trust gate, so unlike 805
this rule DOES fail slips. The four misses are all משרד החקלאות, all
overpayments: 53565575 (+₪87.56), 33848809 (+₪69.10), 304478957 (+₪57.72),
58277191 (+₪18.69).

**Three of the four were swallowed by the 1999 bucket.** Only 53565575 counts
as a real error (13 → 14); the others carry a 4624 gap too, and that bucket
tests gap *presence*, not causation, so it claimed them first. ₪145 of
overpayment left the headline number because of a 1999 gap. This is not a new
defect — it is the documented 1999 problem demonstrated with concrete money,
and the fix is unchanged: give 4624 a חודש-פרישה × dirug rate table.

Same sparse-table defect as §9: 4651's rate table is filled for **12 months of
228** (all of 2008); outside it the VLOOKUP returns 0.

## 0c. New classification: amount chosen by a group the file lacks

Per the user, `תוספת סכומית משתנה לפי בחירת קבוצה` — the workbook HAS the
figure but selects it by a group the גולמי does not identify, so nothing can
validate it and the amount is taken from the משרד האוצר file. Three codes:
**4147** (role, 9 columns, ₪1–1,299.79 — also moves over time), **5268**
(seniority band, ₪26.67–727.46), **5539** (tariff 1/2/3, ₪700–1,500, constant
in time).

`classify_hukka_amounts.py` gained a `group` state. `SOURCE_GRIDS` now records,
per sheet, WHAT the columns are and whether the גולמי carries that group —
stated per sheet, never inferred, because getting it wrong either hides a
checkable component or claims the file has a field it does not.

**1063 (מנמ"ש 2022) is deliberately NOT in this category.** It is also
group-selected, but the group is דירוג and קוד דרוג *is* in the file — so it
stays `varies`: a coverage gap of ours that can be closed, not an unanswerable
one. Filing it under "group" would excuse a gap that is fixable.

Fixed an ordering bug found doing this: the classifier decided from a code's
own `tosafot` column before following the formula to a source sheet, so 5268 —
which carries a value in its column *and* takes its real amount from a group
grid — was filed as a plain fixed amount. The sheet reference is now resolved
first.

## 1. חוקה amounts: fixed vs varies

"סכום לפי חוקה" became three labels — `סכום קבוע לכל התקופה` (48),
`סכום משתנה מעת לעת` (8), `סכום לפי חוקה — לא נקבע` (1).

Decided by `tools/classify_hukka_amounts.py`, which reads it out of the
workbook and stamps `amount_period` + `amount_period_note` onto each `hukka`
rule. Re-runnable on any new Progim. The method: `tosafot` row 4 gives a code
its column, rows 7..234 are the amount per חודש פרישה; ≥2 distinct non-zero
amounts ⇒ varies. When that column is empty the formula names a sheet and the
same test runs on its grid — with the distinction that a **tier** column
holding one amount for all 228 months is FIXED (5539's 700/1100/1500 are
tariffs, not pulses). Nothing is inferred: an unsettled code gets the third
label rather than being defaulted to "fixed".

Varying: 737, 805, 1063, 1358, 1961, 4147, 4453, 5524. Unsettled: 5402 — see
`docs/PROGIM_FIXES.md` §7 (`heskem 2016` has the percentage pulse block but no
sum block, and 5402's tosafot column is empty).

`HUKKA_KIND` maps the stored value to the Hebrew label in
`tools/unified_report.py` and in both front-ends — three places, same map.

## 2. Out of scope: 1711 and 4120

**4120 (השלמת שכר)** — the user reclassified it as non-pensionable, so it moved
out of the seven manual codes and into `NON_PENSIONABLE`. The manual list is
now six: 658, 678, 4173, 4318, 4643, 4935. Checked before changing anything —
4120 appears in **no** percent rule's `base_codes`, so removing it from scope
moves no calculation (21,167 / 382 before and after). Its rule note claimed the
opposite ("ומכליל אותו בבסיסי החישוב") — that was false and is corrected.
Classification sheet: out-of-scope 11 → 12, manual 7 → 6; reported-by-design in
the coverage banner 11 codes/₪613,892 → 10/₪606,867.

## 2b. 1711 (ניכוי 6% א"ע)

Added to `NON_PENSIONABLE` in `main.py` and `engine.js`. Gap list 13 → 12
codes, ₪248,503 → ₪226,806. Its slip amount is **negative** (−₪20,170.89 over
72 rows) — a deduction, which never belonged on a list of money the workbook
fails to cover.

New bucket `d1711` and column **שגויי ניכוי 6% א"ע**, placed immediately after
גמול השתלמות as the user specified, in the chain and the column order together.

**The column reads 0 on 0108, and this is the thing to know:** of the 72
carriers, 69 are already valid and 1 has no base. The 2 that are invalid both
land in **גמול**, which precedes it. A bucket after גמול cannot claim them.
Moving it before גמול is a one-line change and would claim those 2 — but it
would then also claim every 1711 carrier failing on anything other than the
base, which is the swallow-unrelated-errors failure. Reported to the user; not
moved unilaterally.

## 3. Dashboard partition: whole file, not full-timers

The user asked how 22,422 workers give 21,167 valid when the report showed
1,146 invalid. Both were right on different populations: 1,146 is
`17,755 full-timers − 16,609 full-time valid`. The dashboard printed
"תקינים 21,167" and "תקין (מלאה) 16,609" side by side with neither denominator
stated.

The buckets were counted on full-timers only, so **109 non-valid part-timers
had no column at all** (102 invalid + 7 retro); the partition closed only
because "משרה חלקית" absorbed them. Buckets now count `rows_f`. The partition
is `ללא בסיס + שתי שורות + buckets + תקין = עובדים`, with
`משרה חלקית (מתוכם)` descriptive and **outside** it — said in the header, the
banner and `CHAIN_HE`. `ft_valid`/`ft_no_base`/`ft_multi` still exist on the
summary object but drive nothing.

The 109 land as 1999 58, גמול 20, בסיס 18, דריכות 4, בית חולים 2, retro 7.
None is a real error — `inv_real` stayed 13.

## 4. 4319 / 4427

The user pointed at `tosafot!CX` / `tosafot!CY` in the 30.07 workbook. He was
right: the previous report listed both as "לא מוגדר בחוברת" when the workbook
defines them in full. `extract_rules.py` resolves rates from a *scalar* in
`tosafot` row 3; these two resolve theirs with
`VLOOKUP(דרגה, '<sheet>'!C6:E115, 2, 0)`, so no rule was emitted and they fell
into the coverage gap. **That mislabel was ours, not the workbook's.**

New rule key `rate_by_grade` (grade label → rate), copied from the workbook's
tables, honoured in `main.py` and `engine.js`. Bases from `SACHAR`:
4319 = (משולב + גמול א + גמול ב) × rate; 4427 adds 4318 and 4319 itself.

Key-space trap: `'Netunei Gimlai'!B10` holds the grade **index** (1..110), the
same column as `DARGA!A` — not the label. The per-grade sheets mirror that, so
the VLOOKUP is consistent and there is no off-by-one.

Checked against every carrier before shipping: **8 of 10 exact to the agora**
on each code. Deviants left as findings (grade 18: ₪757.81 vs ₪880.69 on 4319,
₪3,252.10 vs ₪2,351.11 on 4427; grade 20+: ₪9.26 on 4427).

Also replaced `data/progim/Progim_18.07.2026.xlsm` with the 30.07 workbook the
rules actually came from.

## Verified

0108 file, 22,422 slips, from a run:

```
עובדים 22422 · [משרה חלקית 4667 — תיאורי, מחוץ למחיצה]
ללא בסיס 856 · שתי שורות 17 · ותק סטודנט 0 · ותק קטוע 0
בסיס 46 · גמול 115 · ניכוי 6% א"ע 0 · תוספת 1999 171 · דריכות 34
גמול מנהל 0 · בוררות מיסים 0 · תוספת בית חולים 3
שגויים אמיתיים 13 · תקין 21167        partition = 22422  OK
```

Classification: 35 formula · 48 חוקה-fixed · 8 חוקה-varies · 1 חוקה-unsettled ·
6 manual · 12 out-of-scope · 10 undefined. Verdicts 21,167 / 382 throughout —
none of these changes moved a verdict. 24/24 tests; `node --check engine.js`
clean; both front-ends' inline scripts syntax-checked; report regenerated and
every column read back against its header.

## Open

**1. The two new נתיב rules do not flag anyone yet, by design.**
Self-calibration needs `TRUST_MIN_N = 20` carriers and 0108 has 10. Do **not**
mark them `stable` to force it — that would flag 2 of a 10-worker sample.

**2. The workbook's נתיב rate tables cover 9 grades of 110** (17–21); outside
that the VLOOKUP silently returns 0. `'פומ נתיב 4319'!Y5` carries the author's
own note about it. `PROGIM_FIXES.md` §6. The engine skips the check for an
unlisted grade rather than expecting 0.

**3. Column indices in the dashboard are hardcoded** in
`tools/unified_report.py` and both front-ends (number formats, warn/bad fonts,
conditional-formatting ranges `C`/`Q`/`R`). Adding the 1711 column moved every
index right of גמול by one. If you add another column, walk all three files.

**4. Inherited and still true:** the 1999 bucket tests gap-presence not
causation and can hide a larger error (worker 66392396, ₪347 behind an ₪85
gap); 27 codes are חוקה amounts the extractor cannot resolve through
eligibility-gated VLOOKUP chains, labelled `reported/hukka` on purpose; 16
workers pay exactly 96.77% of the חוקה figure from a pulse the workbook keeps
no history for — reported, not silenced. `base_codes` merges are ADD-ONLY (728
alone is 1,449 rows). When auditing a lookup table, check for duplicate labels
first — a factor-6 DARGA error once survived an audit that rebuilt its
comparison dict with the same last-wins bug.

---

## Site routing — FIXED and verified in production

`/api/info`, `/api/lookups`, `/api/progim/status`, `/api/diag` all return JSON
from the live site; `/` and `/index.html` serve the page; `/engine.js` serves
JS; `/nonexistent-asset.js` 404s. `/api/diag` reports `path_seen: "/api/diag"`,
`rules_loaded: 95`, `runtime_data_present: false` — i.e. the **bundled 31.07
חוקה is what the site serves**, no `/tmp` upload involved. The `לא מחובר` badge
is resolved: the page's `/api/lookups` fetch returns 39,738 bytes of JSON.

### What was actually wrong, in the order it was found

1. **The rewrite destination named the file, not the route.**
   `/api/index.py` is taken literally; the function's published route is
   `/api/index`. With the file spelling, the request never reached the routing
   layer in a usable form. Fixed to `/api/index`.
2. **The platform hands the function the DESTINATION path**, confirmed by
   `x-path-received: /api/index` on every response. So the original path must
   be carried explicitly — the rewrite now appends `?__path=/$1`.
3. **`api/index.py` is not where per-request code can live.** Three rounds were
   spent on a wrapper there that never ran: a build carrying it went live
   (`/api/index` served the page, which only the new `main.py` does) while no
   response carried its headers. The runtime does not call that module's `app`.
   `_RestoreOriginalPath` is now middleware on the FastAPI app in `main.py`.
4. **Recognising only one entry spelling 404'd the homepage** for ~2 minutes
   after step 1 — every request, `/` included, fell into the `api/` branch.
   `VERCEL_ENTRY` is now both spellings, pinned by a test.

`x-req-header-names` from production shows **no** forwarded-path header exists
(`x-vercel-original-path` and friends are absent), so the query marker was
genuinely necessary — the header fallback in the middleware never fires here
and is kept only as insurance. `x-path-*` are cheap and stay: while routing is
broken no diagnostic *endpoint* is reachable, so the diagnosis has to ride on
the response. Names only, never values.

**Do not "simplify" any of this without re-reading the above.** Reverting the
destination to `/api/index.py`, dropping `?__path=`, moving the middleware back
to `api/index.py`, or trimming `VERCEL_ENTRY` to one spelling each restore a
failure that was measured in production.

## Superseded notes from the earlier round

**The whole API was dead in production and the fix is in this branch.** Measured
against the live site: `/`, `/api/info`, `/api/lookups`, `/api/progim/status`
and `/nonexistent-asset.js` all returned **the same 200 and the same 147,447-byte
HTML body** (identical md5). `POST /api/progim/upload` returned 405.

Cause, confirmed rather than guessed: a Vercel rewrite hands the function its
**destination** path. Every request reached FastAPI as `/api/index.py`, no route
matched, and the catch-all's `path == VERCEL_ENTRY → frontend` branch answered
everything with the page. That branch was added to stop `/api/index.py` 404ing,
and it turned a visible 404 into a silent site-wide API outage. It is the
`לא מחובר` badge's real cause: the page fetches `/api/lookups`, gets HTML, and
file checking never runs.

Fix, deliberately not dependent on any undocumented `x-vercel-*` header — the
rewrite carries the path itself:

```json
{ "source": "/(.*)", "destination": "/api/index.py?__path=/$1" }
```

`api/index.py` now wraps the app in `_RestoreOriginalPath`, an ASGI middleware
that reads `__path`, restores `scope["path"]`/`raw_path`, and strips the marker
from the query string. If `__path` is ever absent the request passes through
untouched, so the failure mode is the OLD behaviour, not a 500. The
`VERCEL_ENTRY` branch stays as that fallback.

Five tests in `tests/test_engine.py` drive the entrypoint app the way Vercel
does (`/api/index.py?__path=...`) and assert an API path returns JSON, an
unknown API path 404s instead of HTML, the caller's own query survives, and a
missing marker still shows the app. 29/29 pass.

**Only the vercel.json half is untestable from here.** After deploy, the check
is one command — `/api/info` must return JSON, and `/nonexistent-asset.js` must
404 rather than return the page. If it still serves HTML everywhere, the rewrite
is dropping the query string; the next thing to try is legacy `routes`
(`{"src": "/(.*)", "dest": "/api/index.py"}`), which preserves the request path
by construction.

## From `main` — site routing (the other session's earlier round)

The deployed site returned `{"detail": "Not Found"}` — Starlette's 404, not a
crash. Vercel rewrites `/(.*)` to `api/index.py` with no static server in
front, so FastAPI answers for the frontend's own files, and `/index.html`,
`/salary_frontend.html` and `/api/index.py` had no route. Fixed with a
catch-all in `main.py` registered **after every real route** (route order is
declaration order — it must stay at the bottom of the file). HTML responses
carry `Cache-Control: no-cache`, because the page's embedded `BUILD` must match
the `engine.js?v=` it requests. `vercel.json` also lost `xlsx` from
`includeFiles` — 9.1MB of real payroll data was being bundled into a public
serverless function.

Still open there: the header badge reads **לא מחובר**, which is not cosmetic —
`ensureLookups()` fetches the pay tables, so file checking does not run at all.
`/api/diag` was added to make production answer for itself: it reports
`path_seen` and whether lookups/rules loaded. Get it from production first. If
`path_seen` is `/api/index.py`, the rewrite is the cause and every `/api/*`
call is being answered by the catch-all — fix the rewrite, do not add routes.
This environment's network policy returns 403 on CONNECT to `*.vercel.app`, so
none of it can be checked from here.
