<!-- head: 558906b -->
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

The workbook in `data/progim` is **`Progim_06.08.2026.xlsm`** (05.08 deleted in
the same commit; 04.08 before it) — 805 complete at 228/228, 808 split into 10 pulses, and both
§11 formulas fixed. `component_rules.json` holds **102** rules
(unchanged count). Verify the deploy with `/api/progim/status` — it should
report `rules: 102`, `source: bundled`, `runtime_data_present: false`, meaning
the site serves the חוקה from the repo rather than a `/tmp` upload.

The coverage gap on the **0108 reference file (22,422 slips)** is **1 code /
₪251** — 507 alone. Separately, `golmi.xlsx` — a 6,901-worker sample that is
**not** the 0108 file, though I conflated the two earlier — measures 19 codes /
₪622,483, dominated by 738 at ₪568,238.

Newest topic first:

0di. **§10 SOLVED by one cell** — 1297 median 1.0594 → 1.0000; plus the 657 and 669 columns
0dh. **§30 closed — 907.66 → 907.76** — 6/6 bands match; reports unchanged because ₪0.10 was inside tolerance
0dg. **657 rebuilt — new MEONOT sheet** — tariff-2 band added, §11 closed, one 10-agora gap left
0df. **4544 neutralization column** — 14,975 on מנהלי; 2,739 of them came from other defined buckets
0de. **Progim 07.08.2026 installed** — workbook filled 5402 for מהנדסים/הנדסאים; engineers check-all 35.8% → 10.7%
0dd. **‼‼ 5402 was OUR bug** — 143,644 false positives; מנהלי check-all 52.63% → 13.01%
0dc. **✅ Every neutralization column verified firing** — but 5402/4550/669 are 86% of what is left, and have none
0db. **‼‼ `--check-all` mode added** — 0.205% → 52.6% on מנהלי; one code (5402) is 91% of it
0da. **מח"ר complete — 20 files to 02/2026** — 1699 starts working in 12/2024; the 12/2024 base step appears on a second track
0cz. **‼‼ The report does NOT check every code** — 24 of 132 on מח"ר, and 1699 never runs there
0cy. **Third track opened — דירוג מח"ר (11)** — 11 files, 48 true errors, but two thirds of the חוקה never runs
0cx. **New workbook installed** — 3 tables filled; it exposed a silent extractor bug (5401 lost)
0cw. **Six more codes out of scope** — coverage gap ₪636,303 → ₪142,036
0cv. **מנהלי extended to 02/2026** — 19 files; base mismatches jump 6× in 12/2024
0cu. **‼‼ 633/634 out of scope** — 633 alone is 80.1% of the מנהלי coverage gap
0ct. **1027, 1044, 1904, 0 out of scope** — 60 codes; code 0 is a nameless ₪0 junk row
0cs2. **633/634 traced + the missing 2024-2026 explained** — both codes start in 12/2020; no מנהלי files past 12/2023
0cs. **Engineers series extended to 12/2025** — 19 files; 12/2025 is the first file with zero true errors
0cr. **4651 neutralization column** — 14 workers; the rate table is filled for 2008 only (§29)
0cq. **‼ 5253 neutralization column** — 42 true errors and ₪20,914 leave the headline
0cp. **‼ 5253 — three workbook bands nobody is paid** — and the first measured proof of the §14 month-agnostic gap
0co. **"שגויי דירוג" column + 5527/4536 out of scope** — 5 slips / ₪927; true errors unchanged at 743
0cn. **✅ New מנהלי unified report** — 175 → 743 true errors, 1699 is 80% of them
0cm. **‼‼ 1699 minimum-wage check was broken — our bug, not the workbook's** — 4.6% → 96.7%
0cl. **‼ 12/2020–12/2022 engineers — TWO of my findings were wrong** — 4453's completion broke, 602 is not flat
0ck. **12/2019 engineers** — 602 confirmed at ₪557.24 for a third year, and it is growing
0cj. **12/2018 engineers + 602 traced** — the biggest engineers hole, and it is nowhere in the workbook
0ci. **‼ 12/2016 + 12/2017 — the gate caught in the act** — 4544 crosses 97% for one file and the headline x15
0ch. **12/2015 engineers** — §25's completion passes its first test; no-base "trend" retracted
0cg. **4453 converted + 1168 declared file-fed** — 105 rules; the 4453 table is 3 cells of 228
0cf. **12/2014 engineers** — 607's table end confirmed correct; no-base is climbing
0ce. **✅ 954, 1170, 4540 out of scope** — 54 codes; two of them were fake holes §24 predicted
0cd. **‼ The workbook already declares pensionability for 841 codes** — and §17 undercounts the contradictions
0cc. **Progim 06.08.2026 installed** — 607 extended to 12/2013; extractor un-pinned from a stale filename
0cb. **✅ 5274 out of scope — a new kind of declaration** — 51 codes; "ימי X" is now eight
0ca. **‼ Framing correction: the 16 December files are דירוג מנהלי** — not "the full population"
0bz. **✅ 1623 out of scope + engineers unified** — 50 codes; the elections family is complete
0by. **12/2012 engineers + correction** — the pay-agreement stall is retro, not a 4550-style bug
0bx. **607 extended to 12/2012 + 12/2011 engineers** — the pay-agreement family stalls at 94-97%
0bw. **✅ 1631 out of scope — workbook-backed** — 49 codes; the elections family is now two
0bv. **607 extended to 12/2010 + 12/2010 engineers** — 607 is engineers-only, measured
0bu. **607 added to the workbook + 12/2009 engineers** — first file with a zero coverage gap
0bt. **12/2008 engineers checked + 669 traced** — the anomaly is one month, not the track
0bs. **✅ 1622 out of scope — backed by the workbook** — 48 codes; clears the biggest 12/2023 hole
0br. **🔧 Engineers track opened + 4550 corrected** — the gate hides 14 of 22 rules on a small file
0bq. **✅ 5270 fixed by the user** — five-tier pulse table; gaps collapse, two defects left
0bp. **5270 ותק פעילות is defined and unchecked** — the seventh such component; report in progress
0bo. **Seventh neutralization column: 697** — the most effective bucket yet, and the most consequential
0bn. **Sixth neutralization column: 1063** — built as asked, and it reads 0 everywhere
0bm. **‼✅ The pulse dating is SOLVED** — it was in the workbook all along; §14 reversed
0bl. **✅ 1063 was never checked — ₪10.1M** — the biggest one yet, now at 98.6%
0bk. **Fifth neutralization column: 5524** — justified, and it swallows 1096 whole
0bj. **The 12/2023 file checked** — the trust gate silences 805 and 738; 80% of "true errors" are day-proration
0bi. **4438 out of scope** — 47 codes; the "ימי X" family is now six of them
0bh. **657 filled and now checked** — 90%, and one missing tier explains the rest; 12/2022 run
0bg. **4538 out of scope (2nd contradiction) + 657 reclassified** — 657's table is empty
0bf. **Four more codes out of scope** — 45 now, and three are backed by the workbook
0be. **Fourth neutralization column: 738** — clean, swallows nothing
0bd. **The 12/2021 file checked** — both new buckets fire together; 738 is 52% of errors
0bc. **New 14-file unified report** — 288,640 slips, 212 true errors, all fixes in
0bb. **New 5340 neutralization column** — asked for, built, and it swallows 626/728/959
0ba. **⚠ 4140 out of scope against the workbook** — the one entry that contradicts the Progim
0az. **5340 was never checked** — fixed amount, now validated; a fifth misclassified component
0ay. **The 12/2020 file checked** — the converted rules already find errors; two costly new gaps
0ax. **737, 5251, 5253 converted to pulse tables** — two were never checked at all
0aw. **‼ 738 correction** — the workbook was right, our extractor was wrong; rule added
0av. **738 analysed** — the workbook has everything but the formula; two conflicting rates
0au. **The full 13-file unified report** — the series is complete; 12/2013+12/2014 recovered
0at. **Unified report over 11 files** — 229,426 slips; 94% of the coverage gap is 4 codes
0as. **The 12/2019 file checked** — my dating model is refuted outright; fourth 5402 anchor
0ar. **New 4140 neutralization column** — asked for, justified, and it moves no headline
0aq. **Four more codes out of scope** — the list is now 39; whole benefit families spread across it
0ap. **The 12/2018 file checked** — coverage gap explodes to ₪1.06M; third 5402 anchor
0ao. **The 12/2017 file checked** — a second 5402 anchor; the component ramps
0an. **The 12/2016 file checked** — 5402 measured on 18,578 slips; the dating narrows
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

## 0di. Two more columns (657, 669) + §10 solved by a one-cell workbook change

### §10 solved — 1297 כוננות מיוחדת

Fourth 07.08 revision, **one cell**: `SACHAR!CB11` gained four codes in its
base — **756, 4934, 4983, 4994**.

§10 had been open since 30.07: *"the formula reproduces none of the 55 slips;
median paid÷formula 1.0594"*. Swapping the 5.33 constant for 5.331 had not
helped (0.019% against a 5.94% gap). **The rate was never the problem — the
base was.**

| | before | **after** |
|---|---|---|
| **median paid ÷ formula** | **1.0594** | **1.0000** |
| מנהלי 12/2008 | 0 of 45 | **38/45 (84%)** |
| מנהלי 12/2010 | — | **10/11 (91%)** |
| מנהלי 12/2012 | — | **5/5 (100%)** |
| total | 0% | **53/62 (85.5%)** |

A median of exactly 1.0000 — the formula now reproduces the median slip to the
agora, and the 5.94% gap was precisely the weight of the four missing codes.
**§10 closed** (new §31). Nine stragglers remain out of 62, including the one
מח"ר 12/2012 case at ratio 1.60.

Note for the next session: 1297 is **not** produced by `extract_rules.py` — it
is hand-maintained in `component_rules.json` — so a workbook change to CB11
has to be applied by hand. Also caught here: the 657/MEONOT revision had
silently changed the *extracted* 738 rule, but the stored 738 is richer (3
rates against 1), so it was **left alone** rather than overwritten.

### Two neutralization columns

657 immediately after הסכם 2001, and 669 immediately after בית חולים מאוחדת,
per instruction. **Both take only from "real" — no other bucket moved.**

| track · mode | 657 | 669 | true errors |
|---|---|---|---|
| מנהלי · gated | 32 | 2 | 833 → **803** |
| מנהלי · check-all | 14 | **7,334** | 34,651 → **27,317** (9.56% → 7.53%) |
| מח"ר · gated | 22 | 0 | **352** |
| מח"ר · check-all | 10 | 429 | 11,102 → **10,673** |
| engineers · gated | 0 | 0 | **57** |
| engineers · check-all | 0 | 59 | 1,766 → **1,707** |

657 is small — 59 flagged slips in total. It takes 32 in gated mode but only
14 under check-all, because there 18 of them are already claimed by the 4544
bucket upstream.

**669 is the second of the three "big" leftovers.** 7,334 slips on מנהלי, 21%
of the true errors that remained. Of the three codes measured at 86% of the
residue (5402, 4550, 669), the first turned out to be our own bug and the
third now has a column — **only 4550 is left**.

The neutralization is documented rather than assumed: §23 records 669's
workbook value as correct in 15 of 16 files and wrong in 12/2008, and on
מח"ר 12/2008 it scores **1 of 556**. The rule is wrong for whole eras and
tracks, not for individual workers — which is what makes it a bucket rather
than an error. Retiring it means fixing 669's value per era and track.

Partition closes on every row in all six reports.

## 0dh. §30 closed — 907.66 → 907.76, and the report does not move

Third 07.08 revision: **12 cells, `MEONOT!D185:D196` (codes 181-192), 907.66 →
907.76.** Exactly the §30 instruction, nothing else touched.

657's table now matches payroll on **6 of 6 bands**:

| month | code | workbook | paid | rule match |
|---|---|---|---|---|
| 12/2018 | 132 | ₪833.33 | ₪833.33 × 396 | 98.3% |
| 12/2019 | 144 | ₪839.66 | ₪839.66 × 401 | **99.3%** |
| 12/2020 | 156 | ₪844.70 | ₪844.70 × 359 | 97.1% |
| 12/2022 | 180 | ₪862.40 | ₪862.40 × 380 | 97.9% |
| **12/2023** | **192** | **₪907.76** | **₪907.76 × 389** | 97.1% |
| 12/2024 | 204 | ₪934.63 | ₪934.63 × 398 | 98.0% |

### ‼ The reports are byte-identical before and after — and that is correct

מנהלי 19 files, both modes: valid 339,320 / 286,139, true errors 833 / 34,747,
exposure unchanged, **no bucket moved at all**.

`MATCH_THRESHOLD = 1.0`, so a ₪0.10 gap was **already inside tolerance** — the
389 workers were passing on the old value too. The correction buys fidelity to
the חוקה, not new flags. Worth saying plainly rather than implying the fix
"improved" anything measurable: it removed a discrepancy that the tolerance had
been absorbing, which is exactly the kind of thing that hides until the
tolerance is tightened.

**§30 is closed.** 657 is now among the best-specified components in the
workbook: a dedicated sheet, two tariff bands, 84 cells each, a correct column
index, and agreement with payroll on every band.

## 0dg. 657 rebuilt in the workbook — new MEONOT sheet, and §11's last instance closed

Second 07.08 revision, **15 cells plus one new sheet**. 657 got its own sheet,
`MEONOT`, and two long-standing items closed at once.

```
tosafot!AW2 = IF(MISRAD!AZ2=1, IF('Netunei Gimlai'!G59=TRUE, MEONOT!E1, 0), 0)
MEONOT!E1   = INDEX(MEONOT!D5:E232, month-code, tariff)
              tariff = 'Netunei Gimlai'!H59 ∈ {1, 2}
```

**The tariff-2 band now exists.** Our own note on 657 said in as many words
that the second band was measured in the files (₪500 / ₪504 / ₪507.02, ~32-35
carriers a month) and **was not in the workbook**, so those workers failed.
It is now column E, filled for codes 121-204.

**§11's last open instance is fixed.** `AW3` was
`VLOOKUP(C4, AR7:AW234, 5, 0)` — index 5 points at AV, not AW — and is now
`VLOOKUP(C4, AR7:AW234, AW1, 0)` with `AW1 = 6`, and AR..AW is exactly 6
columns.

### Verified — five bands exact, one off by 10 agorot

| month | code | workbook (tariff 1) | paid | |
|---|---|---|---|---|
| 12/2018 | 132 | ₪833.33 | ₪833.33 × 396 | ✔ |
| 12/2019 | 144 | ₪839.66 | ₪839.66 × 401 | ✔ |
| 12/2020 | 156 | ₪844.70 | ₪844.70 × 359 | ✔ |
| 12/2022 | 180 | ₪862.40 | ₪862.40 × 380 | ✔ |
| **12/2023** | **192** | **₪907.66** | **₪907.76 × 389** | **✘ −₪0.10** |
| 12/2024 | 204 | ₪934.63 | ₪934.63 × 398 | ✔ |

`MEONOT!D` for codes 181-192 is 10 agorot below what 389 workers were paid.
The tariff-2 value for the same period (₪544.83) *does* match, so the gap is
in column D alone. New **§30** carries the instruction: 907.66 → 907.76.

Our rule had 907.76 — the value the payroll actually uses — but recorded it as
coming from the workbook while the workbook said otherwise. Both are now
documented.

### Engine and reports

Rule rebuilt to 12 amounts (both tariffs) with `amounts_by_code` and separate
`tariff_tables`. The tariff selector is a per-worker input **the גולמי does not
carry**, so the check accepts either band — that is why 657 stays a plain
`shekel` rule instead of becoming tariff-aware.

657 match: **98.3%** (12/2018), **97.1%** (12/2020), **97.1%** (12/2023),
**98.0%** (12/2024).

| מנהלי, 19 files | before | after |
|---|---|---|
| check-all true errors | 34,942 | **34,747** (−195) |
| check-all underpaid | ₪3,293,470 | ₪3,229,909 |
| gated true errors | 818 | **833** (+15) |

Same pattern as every other fix of this kind: check-all falls because real
carriers now pass, gated rises because the rule clears the trust gate and its
genuine outliers surface. Partition closes on every row in both.

## 0df. 4544 neutralization column — the largest yet, and it drains other buckets

User instruction: a column for 4544 immediately after שגויי תוספת 1999, with
those workers coming off the true-error count. That position is **early** in
the chain, so the bucket pulls from every bucket defined *after* it, not only
from "real". Measured both ways before and after.

| track (check-all) | true errors before | **after** | 4544 column | underpaid |
|---|---|---|---|---|
| מנהלי | 47,178 (13.01%) | **34,942 (9.64%)** | **14,975** | ₪4,027,545 → ₪3,293,470 |
| מח"ר | 24,510 (17.49%) | **11,303 (8.06%)** | **14,961** | ₪2,216,253 → ₪1,242,208 |
| engineers | 2,035 (10.75%) | **1,766 (9.33%)** | 381 | ₪160,595 → ₪116,310 |

Gated mode barely moves: מנהלי 826 → 818, column = 12, because 4544 clears the
trust gate in only some files.

### Where the 14,975 came from on מנהלי

**12,236 from "real"** — and **2,739 from buckets the user had already
defined**: דריכות 961, בוררות מיסים 654, תוספת בית משפט 608, תוספת מיוחדת
222, גמול מנהל 149, שקלית 2023 41, 4651 41, and 63 across five more. Two
columns emptied completely (5524 and 4651 → 0) and תוספת בית משפט fell from
622 to 14.

Partition closes on every row in all six reports — nobody double-counted,
nobody lost — but the by-column picture changed materially, and that is worth
the user seeing before this becomes the standing report.

**The argument for the position:** 4544 is a base component of the
pay-agreement family (4550/4934/4994 sit on it), so a retro difference in it
rolls into everything above — the same reasoning that placed 4624 early.
**The alternative** (last in the chain, just before "real") would leave every
other column untouched and take only the 12,236. Offered to the user.

## 0de. Progim 07.08.2026 installed — the workbook answered §7 the same day

**303 cells, no structural change** — nothing moved, so no column letters
shifted and no citation went stale.

| sheet | cells | what |
|---|---|---|
| **`heskem 2016`** | **252** | **columns O (מהנדסים) and P (הנדסאים) filled** in the 5402 grid |
| `Netunei Gimlai` | 43 | simulation scratch area cleared + input cells changed — not חוקה data |
| `tos reforma 4147` | 8 | value updates (845→850, 964→970, 1084→1091, …) |

**This is a direct answer to the §7 instruction written hours earlier.** The
5402 grid now covers **four rating groups** (1 מינהלי, 11 מח"ר, 12 מהנדסים,
13 הנדסאים) at 126 cells each, up from two.

Verified against payroll before touching the rule: מהנדסים 12/2016 ₪108.27
×963, 12/2020 ₪448.80 ×786, 12/2023 ₪482.33 ×565 — match, and the 5402 check
on those files goes to **99.1% / 98.1% / 97.8%**.

`component_rules.json`: 5402 goes 26 → **50 amounts**, 2 → **4 rating groups**.
Extracted rules are otherwise **unchanged** (25 percent rules, 32 total); the
only extractor delta was 4544 leaving 1699's `counted`, which the stored list
never contained, so nothing was applied.

### Engineers is where it lands

| | before | **after** |
|---|---|---|
| check-all true errors | 6,702 (35.81%) | **2,035 (10.75%)** |
| check-all underpaid | ₪558,885 | **₪160,595** |

מנהלי and מח"ר are **byte-identical to the pre-0708 runs** (10,950 / 64,341
and 4,678 / 36,011 invalid) — correct, since columns O and P do not touch
ratings 1 and 11.

### Engineers extended to 02/2026 — 20 files

A 02/2026 engineers file arrived in the same turn. 20 files · **18,932
slips** · partition closes. Gated: **81 true errors / 0.428%**. The last two
files are clean — 12/2025 and 02/2026 both return **0 true errors**.

Gated counts rose on this track (53 → 81) for the same reason as on מנהלי
after the 5402 fix: the rule now clears the trust gate, so its genuine
outliers surface instead of being suppressed wholesale.

## 0dd. ‼‼ 5402 — the user was right again, and it was the biggest bug yet

**User: "the amounts in the PROGIM are correct for מנהלי and מח"ר." They were
right, and they named exactly the two ratings the workbook fills.**

§7 said 5402 has no amounts table. **False in the current workbook.** The real
chain, read out of the file:

```
SACHAR!DX11      = +U11
SACHAR!U11       = 'heskem 2016'!B6
'heskem 2016'!B6 = INDEX(D12:P239, B2, B3)
                   B2 = month code (row)
                   B3 = SACHAR!K11 = חילן rating code (column, D..P = 1..13)
```

A **month × RATING grid**. Column D = מינהלי, N = מח"ר, O = מהנדסים, P =
הנדסאים. **Only D and N are filled** — 126 cells each — which is exactly the
pair the user named.

**Verified against payroll before changing anything, and it matches to the
agora on all five checks:** מנהלי 12/2016 ₪66.88 ×15,537 · 12/2017 ₪102.72
×16,218 · 12/2023 ₪326.34 ×14,397 · מח"ר 12/2016 ₪84.84 ×6,786 · 12/2023
₪400.73 ×7,768.

**Our bug:** the rule held `amounts: [336, 437.21]` — two numbers that appear
in **no cell of the table** — with no month and no rating awareness. 0.0% of
carriers matched.

**Fix:** 26 amounts read from the workbook, plus `amounts_by_droog_code` so
the check narrows to the worker's own rating (a מח"ר amount must not pass on a
מנהלי slip). Both engines; an unlisted rating falls back to the union rather
than failing the worker.

| file | before | **after** |
|---|---|---|
| מנהלי 12/2016 | 0.0% | **98.4%** |
| מנהלי 12/2023 | 0.0% | **98.4%** |
| מח"ר 12/2016 | 0.0% | **97.5%** |
| מח"ר 12/2023 | 0.0% | **96.7%** |

### What it did to the reports

| | check-all before | **after** |
|---|---|---|
| מנהלי true errors | 190,822 (52.63%) | **47,178 (13.01%)** |
| מנהלי underpaid | ₪17,756,938 | **₪4,027,545** |
| מח"ר true errors | 69,280 (49.42%) | **24,510 (17.49%)** |
| מח"ר underpaid | ₪6,066,339 | **₪2,216,253** |

**143,644 of the 190,822 were our own false positives**, and ₪13.7M of
"underpaid" exposure was never real.

In gated mode the fix *adds* flags rather than removing them — מנהלי 742 → 826,
מח"ר 168 → 374 — because 5402 now clears the trust gate and its genuine
outliers surface. Partition closes on every row in all four reports.

### ‼ What is still a real workbook defect

**Column O (מהנדסים) and everything past N is empty.** An engineers slip
carrying 5402 gets `INDEX` → 0, so it is not computable. Instruction added to
§7: fill `heskem 2016!D12:P239` for the remaining ratings, starting with O.

### The lesson, written into §7

The original §7 instruction — "add a shekel block to `heskem 2016`" — **had
already been carried out in the workbook, and we never re-checked.** A fix
list entry is not closed by writing it; it has to be re-measured after every
workbook update. §7 now carries the correction at the top and keeps the old
text below it, marked superseded.

## 0dc. Verified: every neutralization column the user defined does fire

Asked directly whether the codes defined for neutralization are in fact
neutralized. Measured on the 19 מנהלי files, gated vs `--check-all`.

**Yes — all of them exist and fire**, and most absorbed *more* under
check-all: 4624 3,210→5,705, 4983 1,089→2,875, 798 431→1,538, 1711 20→652,
875 103→622, 741 297→762, 697 70→227, 738 26→82, 4140 16→62, 4651 14→41.
Four shrank — 705 181→130, 5340 129→32, 5524 60→41, 5253 42→34 — **not
because they stopped working** but because a higher-priority bucket claimed
those workers first. Partition closes on every row, so nobody is
double-counted and nobody vanishes.

### But they cover different codes than the ones flooding the report

Decomposed the 190,822 slips still landing in "real":

| code | on a real-error slip | **sole failing code** | has a column? |
|---|---|---|---|
| **5402 תוספת שקלית 2016** | 164,295 | **143,645** | **no** |
| **4550 הסכם 2001 אישי** | 24,678 | **12,823** | **no** |
| **669 בוררות** | 7,337 | **7,326** | **no** |
| 4544 | 12,236 | 147 | no |
| 4934 | 12,042 | 133 | no |
| 4994 | 11,627 | — | no |
| 5401 | 3,331 | 220 | no |
| 1699 | 762 | 79 | no |

**5402, 4550 and 669 are 163,794 of the 190,822 as sole cause — 86%.** None
has a neutralization column and none is among the codes the user nominated.

**No columns opened on my own initiative.** A 5402 bucket would drop the
headline from 190,822 to roughly 47,000 in one move, and it would swallow
every unrelated error sharing those slips — exactly the decision `CLAUDE.md`
forbids taking without an instruction. Left as the user's call.

Note on 1699: it is the sole cause on only 79 slips, not because it is clean
but because most of its carriers are already claimed earlier in the chain.

## 0db. ‼‼ `--check-all` mode — every code, no gate, and what it costs

User instruction, recorded as a standing rule in `CLAUDE.md`: **"תכניס בחוקה
שלך שיש לבדוק את כל הסמלים בכל הדוחות כולל סמל 1699."**

Implemented as `--check-all` in `tools/unified_report.py`, `check_all=` in
`main.run_engine_full`, and `checkAll` in `engine.js` — every rule applied
with no trust gate, and `check_minimum_population(..., gated=False)` so
1699/5260 fire wherever a target can be inferred. Both engines, same shape.

| track | slips | valid (gated) | **valid (all)** | errors (gated) | **errors (all)** |
|---|---|---|---|---|---|
| מנהלי | 362,567 | 339,476 | **141,684** | 742 (0.205%) | **190,822 (52.6%)** |
| מח"ר | 140,176 | 130,109 | **46,763** | 168 (0.120%) | **69,280 (49.4%)** |
| engineers | 18,715 | 17,688 | **9,668** | 53 (0.283%) | **6,702 (35.8%)** |

מנהלי exposure goes ₪156,935/₪130,849 → **₪17,756,938 / ₪16,053,921**.
Partition closes on every row and total in all three.

### One code is 91% of it

| code | gaps (מנהלי) | ₪ | what it is |
|---|---|---|---|
| **5402 תוספת שקלית 2016** | **172,917** | **₪15,458,240** | **§7: the workbook has no amounts table for it at all** |
| 4550 | 28,250 | ₪5,737,728 | personal amounts — §2 |
| 4544/4934/4994/5401 | 69,179 | ₪2,561,024 | pay-agreement family, known retro |
| 669 | 8,513 | ₪15,243,139 | §23 — wrong value in some eras |
| **1699** | **7,283** | **₪4,236,558** | the point of the instruction |

**5402 alone is 91% of the new gaps** and is not computable from the workbook
in the first place, so every carrier fails. That is a measurement of a hole
already documented in §7, not a discovery about pay.

### The honest framing, and it is in CLAUDE.md now

52.6% of מנהלי slips carry at least one gap the חוקה cannot reproduce. That
is a real and useful number **about the workbook**. It is **not** a list of
mispaid workers. So both reports ship together from now on: gated answers
"who do we believe is wrong", ungated answers "what can the חוקה not
reproduce". `CLAUDE.md` now requires reporting both numbers whenever
`--check-all` runs — never the ungated count alone.

**What the instruction actually bought:** 1699 now produces 7,283 gaps /
₪4,236,558 on מנהלי, 2,525 / ₪1,585,475 on מח"ר and 218 / ₪98,951 on the
engineers — **10,026 slips and ₪5.92M that were previously not examined at
all** in the files where the gate had silenced the rule.

## 0da. מח"ר complete — 20 files to 02/2026, and 1699 starts working in 2024

The whole track landed: **01/2008 and 12/2008–12/2025 plus 02/2026, all
דירוג 11. 20 files · 140,176 slips · partition closes everywhere.**
**168 true errors / 0.120%**, ₪49,356 underpaid against ₪113,496 overpaid.

### ‼ The 1699 silence is an ERA problem, not a track problem

Instrumented the real gate on the three newest files. It changes the
diagnosis recorded in 0cz:

| file | carriers | inferred target | match | outcome |
|---|---|---|---|---|
| מח"ר 12/2009 | 1,027 | 3,850.20 | 88.2% | silenced |
| מח"ר 12/2017 | 2,704 | 4,532.90 | 96.0% | silenced |
| מח"ר 12/2023 | 4,514 | 5,571.80 | 95.9% | silenced |
| **מח"ר 12/2024** | 4,704 | 5,880.00 | **97.3%** | **runs — 232 flagged** |
| **מח"ר 12/2025** | 2,007 | 6,247.70 | **99.7%** | **runs — 97 flagged** |

**99.7% on 12/2025.** The model is right for this track; what fails is the
older periods. 0cz said "the base term is wrong for this track
specifically" — **that reading was too narrow.** It is wrong for מח"ר *in
the older era*, and it converges to near-perfect as the files approach the
present. Same shape as the era-dependent gaps already recorded for מנהלי
(0cn: silenced in 12/2008–12/2010, 12/2012, 12/2018, 12/2022).

The corrected statement: **1699 is checked on מח"ר only in 12/2024, 12/2025
and 02/2026 — 3 of 20 files.** In the other 17, its carriers are unchecked.

### Where the errors concentrate — the last three files

| file | workers | true errors | שגויי בסיס |
|---|---|---|---|
| 12/2022 | 9,292 | 4 | 52 |
| 12/2023 | 9,049 | 2 | 68 |
| **12/2024** | 8,530 | **24** | **153** |
| **12/2025** | 2,576 | **22** | **140** |
| **02/2026** | 2,646 | **33** | **116** |

**79 of the track's 168 true errors sit in the last three files**, on 9.8%
of the population — and שגויי בסיס jumps the same way. This is the **third
independent sighting of the 12/2024 step**: מנהלי showed 0.5% → 3.1% base
mismatches at exactly the same boundary (0cv), and now מח"ר does too. Two
tracks, same month. **A 2024 pay agreement the חוקה does not carry is now
the leading hypothesis, and it is still not traced.**

Note the population collapses 9,049 → 2,576 between 12/2023 and 12/2025, so
the per-file rates are on a much smaller base.

### Coverage gap grew with the later files — 47 codes / ₪726,541

Still led by **1616 פיצ אבדן מש**, and 4221 תוספת שעמ is now second. Also 20
codes / ₪20,287,303 declared file-fed and therefore correct.

## 0cz. ‼‼ Answering "does the report check every code, including minimum wage?" — NO

Asked directly. Measured on the 11-file מח"ר report rather than reasoned about.

### The census: 24 of 132 codes are actually validated

| | codes |
|---|---|
| distinct codes appearing on a מח"ר slip | **132** |
| of them, have a rule in the חוקה | 76 |
| of them, declared `reported` — fed from the file, **never validated by design** | 9 |
| of them, declared non-pensionable — **out of scope by design** | 32 |
| of them, no rule and no declaration — **the coverage gap** | 25 |
| **of them, actually checked in at least one file** | **24** |

Per file it is starker — codes present against rules that clear the trust gate:

| file | codes on slips | **rules that ran** |
|---|---|---|
| 01/2008 | 63 | **8** |
| 12/2008 | 72 | **7** |
| 12/2013 | 101 | 14 |
| 12/2017 | 106 | 13 |

### ‼ Minimum wage (1699) is not checked on this track at all

**18,209 carriers across the 11 files. Zero checked. Zero flagged.**

| file | carriers | inferred target | match | gate |
|---|---|---|---|---|
| מח"ר 01/2008 | 775 | 3,710.20 | 91.8% | silenced |
| מח"ר 12/2009 | 1,027 | 3,850.20 | **88.2%** | silenced |
| מח"ר 12/2013 | 1,672 | 4,300.00 | 96.2% | silenced |
| מח"ר 12/2017 | 2,704 | 4,532.90 | 96.0% | silenced |
| **מנהלי 12/2017** | 12,171 | 4,532.90 | **97.5%** | **runs — 352 flagged** |
| **מנהלי 12/2023** | 14,671 | 5,571.80 | **97.5%** | **runs — 441 flagged** |

Every מח"ר file lands between 88.2% and 96.2%, under the 97% gate, so the
check never fires. **The inferred targets are exactly the statutory minimum
wages** and match מנהלי for the same month — so target inference is fine and
the **base term is wrong for this track specifically**. That is the same shape
as the bug fixed in 0cm, one track over, and it is **not yet diagnosed**.

5260 is silenced too (only 123 carriers, all in 12/2017).

### ‼ A measurement of mine was wrong and I caught it by cross-checking

My first attempt replicated the gate in a standalone script and reported
מח"ר 12/2013 at 97.1% and 12/2017 at 97.0% — i.e. **passing**. That
contradicted the flag counts (0 everywhere), which is what made me re-check.

The bug: `check_minimum_population` runs **before** flags flip slips to
invalid, so it scores its match on the pre-flag VALID population. My script
ran after `run_engine_full` had already flipped them, so it scored a cleaner
subset and inflated every rate by ~1 point — enough to cross the gate on two
files. Re-measured by instrumenting the real function; the numbers above are
from the real call. **Lesson for the next session: never replicate a gate,
instrument it.**

## 0cy. Third track opened — דירוג מח"ר (11), 11 files, and a caveat that outweighs the headline

Files arrived for a rating never checked before: **דירוג 11 (מח"ר)**,
01/2008 and 12/2008–12/2017, delivered in three batches and folded into one
report each time. Data sits on `Sheet1`, not `גולמי`; `load_golmi` falls back
to the first sheet, so they read correctly.

**11 files · 72,804 slips · partition closes on every row and the total.**

| file | workers | true errors | valid | ללא בסיס |
|---|---|---|---|---|
| 01/2008 | 5,495 | 1 | 5,211 | 169 |
| 12/2008 | 5,719 | 9 | 5,300 | 291 |
| 12/2009 | 5,890 | **0** | 5,605 | 149 |
| 12/2010 | 6,154 | 6 | 5,803 | 179 |
| 12/2011 | 6,277 | 3 | 5,943 | 176 |
| 12/2012 | 6,472 | 8 | 6,139 | 167 |
| 12/2013 | 6,697 | 3 | 6,269 | 225 |
| 12/2014 | 6,852 | 4 | 6,441 | 222 |
| 12/2015 | 7,448 | 4 | 6,958 | 244 |
| 12/2016 | 7,680 | 6 | 7,186 | 272 |
| 12/2017 | 8,120 | 4 | 7,483 | **380** |
| **total** | **72,804** | **48** | **68,338** | **2,474** |

**48 true errors / 0.066%** — on paper the cleanest track by a wide margin
(מנהלי 0.205%, engineers 0.283%). ₪4,025 underpaid against **₪75,940
overpaid** — the only track that skews this hard toward overpayment, and the
ratio holds as files are added (18:1 at five files, 18:1 at seven, **19:1 at
eleven**).

The population **grows** across the series, 5,495 → 8,120, unlike the other
two tracks which shrink. ללא בסיס grows faster still — 169 → 380, i.e. 3.1%
→ 4.7% of the file. **Not investigated.**

### ‼ Do not report 0.064% as "מח"ר is cleaner". It is mostly the gate.

Counted how many rules with ≥20 carriers actually clear `TRUST_MIN_MATCH`:

| file | candidate rules | **actually checked** | silenced |
|---|---|---|---|
| מח"ר 12/2008 | 25 | **6** | **19** |
| מח"ר 12/2011 | 30 | **10** | 20 |
| מח"ר 12/2014 | 31 | **11** | 20 |
| מח"ר 12/2017 | 33 | **12** | 21 |
| מנהלי 12/2011 | 39 | **21** | 18 |

**Roughly two thirds of the חוקה never runs on this track, in every file.**
The silenced rules cluster just under the gate — 741 at 94–96%, 875 at 95%,
798 at 95%, 858 at 92–93% — the same retro signature as the engineers track
(0bx, 0ci), not a formula defect.

But the later files are worse than a near-miss in places: on 12/2017
**4550 scores 77%, 4544 79%, 920 80%, 630 and 853 81%**. Those are not
rounding tails. 4550 and 4544 are the pay-agreement family already flagged on
the engineers track; **on מח"ר they are further off, and unexamined.** This is the third measured instance of the
rule recorded in 0ci — **true-error counts are not comparable across files or
tracks** — and here it is the difference between "cleanest track we have" and
"a track where two thirds of the חוקה never ran."

The one real exception worth a look: **669 בוררות scores 1/556 = 0%** on
מח"ר 12/2008. Not a near-miss — the rule is simply wrong for this track in
that month. §23 already records 669 being wrong for 12/2008 on another track;
this is a second, much larger instance. **Not investigated.**

### Coverage gap is genuinely small — 21 codes / ₪206,521

Much smaller than either other track, and no single item dominates it. The
bulk of מח"ר pay the workbook does not compute is **declared file-fed and
therefore correct**: 15 codes / ₪10,182,580, led by 4147 תוס. רפורמה. The
real holes are led by **1616 פיצ אבדן מש at ₪136,748 over 30 rows — 66% of
the gap on its own**, and it grew from ₪24,457 at seven files, so it is
concentrated in 12/2014–12/2017. Then 1104 ₪16,815, **5365 שכר יסוד ₪10,648
on a single row** (a base code with no rule — worth a look), 4447 ₪6,315,
1132 ₪6,114, 1605 ₪6,015, and fourteen more.

### Neutralization profile differs from the other tracks

**גמול השתלמות is 1,039 of the 4,466 non-valid slips** — by far the largest
bucket, where on מנהלי the leaders are תוספת 1999 and בסיס. ללא בסיס is 2,474
(3.4%). Worth knowing before anyone compares bucket columns across tracks.

The later files exercise columns the first seven did not: **5253 reaches 14**,
**4651 reaches 2**, and 4140 and 1711 register 1 each — the first time either
appears outside מנהלי.

Note: **752 הופעה 20%** — one of the five שגויי דירוג codes — appears here on
2 rows (₪1,432), on slips that are **valid**, so the דירוג column reads 0.
The earlier statement that those five codes appear on four slips in total was
scoped to the 35 files then loaded; מח"ר adds carriers.

## 0cx. New workbook installed — three tables filled, and an extractor bug it exposed

A later 06.08 revision arrived (same date, **7,614 cells different**). This is
a **structural** change, not a values update, and it moves column letters.

| sheet | cells | what happened |
|---|---|---|
| `tosafot` | 5,813 | **columns inserted** — 30 labels from `CW` on shifted |
| `sminimum` | 672 | row inserted (`$A$7:$D$304` → `$D$305`) |
| `simlei sachar` | 402 | row inserted for **1168 תוספת מבצעית** |
| `SACHAR` | 298 | **column inserted for 5268 ליווי אח"מים** — 5401 moved `DV` → `DW` |
| `Netunei Gimlai` | 292 | rows shifted |
| others | 137 | references that followed |

### ‼ The bug it exposed in our extractor

`tools/extract_rules.py` pinned the end of the חוקה block to a **letter**:
`BLOCK_LAST = "DV"`. The 5268 insertion pushed 5401 to `DW`, so the extractor
**silently dropped the 5401 rule** — 25 percent-rules became 24, no error, no
warning. Exactly the failure mode recorded in `0cc` for a pinned *filename*,
now for a pinned *column*. Fixed: the block end is resolved at run time from
the **code** 5401, scanning 24 columns past the old literal, with a stderr
warning if the code is ever absent. Both workbooks now extract 25/25.

### Three pulse tables filled — two of them answer our own findings

- **4453 דריכות וכוננות** (`BR`): 14 → **218 of 228**. This retires the
  hand-built completion of §25 — including the guessed 533/933 boundary that
  turned out to be wrong. Now read from the workbook, no guessing.
- **4651 תוספת שכר חקלאות** (`BS`): 12 → **192**. §29 fixed for codes 1–192
  (1.2008–12.2023); **codes 193–228 (2024–2026) are still empty.**
- **5254 תוספת שכר מיסים** (`DN`): a **new column**, 177 cells, 14 bands over
  codes 52–228. Converted from `reported` (never validated) to a checkable
  `shekel` rule — and **it passes on every row**: it left the "fed from the
  file" list without entering the gap list.

`sminimum` changed the minimum-wage base: **5539 out, 1168 in**, in both 1699
and 5260.

### ‼ A mistake I made and caught before it shipped

My first merge refreshed the whole `counted` list for 1699 and 5260 from the
new extraction. That was wrong: the stored lists carry **independent prior
hand edits** (1699: +105/1040/1072/99998, −733/4544; 5260 is a curated 192
against the extractor's 257). A wholesale refresh would have added 69 codes to
the 5260 base and silently changed the 1699 check — **80% of all true errors**
— as a side effect of a workbook install. Reverted from git and re-applied
**only the workbook's own delta** (−5539 +1168). `counted_note` on both rules
records this, and the stored-vs-extracted divergence is now an open question
for the user, not something to resolve quietly.

### Measured

| | מנהלי (19 files) | engineers (19 files) |
|---|---|---|
| slips | 362,567 | 18,715 |
| true errors | 742 → **742** | 53 → **53** |
| valid | 339,476 → **339,476** | 17,688 → **17,688** |
| partition | closes | closes |

The workbook change is **headline-neutral on both tracks** — the only movement
is ₪156,077 → ₪156,935 underpaid on מנהלי (+₪858). That is the right outcome:
the filled tables replaced our guesses with the workbook's own numbers and
agreed with them.

## 0cw. Six more codes out of scope — 77.7% of the מנהלי coverage gap

User instruction: 712, 1524, 1903, 4441, 6920, 7902. `NON_PENSIONABLE`
62 → **68**, py/js element-wise equal.

| code | name | ₪ in the 19-file gap | declared in the workbook? |
|---|---|---|---|
| **1524** | העדרות | **₪217,260** | no |
| **6920** | הפרשי פנסיוני וקה"ש | **₪160,435** | no |
| **7902** | הפרשי פנסיוני וקה"ש | **₪102,961** | no |
| 712 | דרגת קידום | ₪10,289 | no |
| **1903** | תגמ. מלואים | ₪3,292 | **yes — `לא` in every column** |
| 4441 | חובת שעות שישי | ₪30 | no |

**Coverage gap: 38 codes / ₪636,303 → 32 / ₪142,036.** True errors 742 → 742,
valid unchanged, every bucket unchanged.

Only **1903** is workbook-backed. The other five rest on silence — though
6920/7902 are employer **pension and study-fund differentials**, not pay, so
they are outside the Progim's scope by construction, and 1524 is the same
absence family as 1027/1044.

**Running total of what has been declared out of scope rather than fixed in
the workbook:** across today's batches the מנהלי coverage gap went ₪636,303 →
₪142,036 and, before that, ₪603,269 → ₪119,800 via 633. **Almost none of it
was closed by the workbook computing more; nearly all of it was closed by
declaring codes out of scope.** That is the honest reading of the number, and
§24 remains the fix: the workbook should declare these itself.

## 0cv. מנהלי series extended to 02/2026 — 19 files, and the base breaks in 2024

The missing מנהלי files arrived: **12/2024, 12/2025 and 02/2026**, all
דירוג 1, on the `גולמי` sheet (each file also carries a `גולמי מעודכן`
sheet — that one is a **pivot**, one row per worker with codes across
columns; `load_golmi` picks `גולמי` by exact name, so the right sheet is
read in all three, including 0226 where the pivot sits first).

**19 files · 362,567 slips · partition closes on every row and the total.**
742 true errors / 0.205%; ₪156,077 underpaid, ₪130,849 overpaid.

| file | workers | שגויי בסיס | % | true errors |
|---|---|---|---|---|
| 12/2023 | 18,289 | 90 | 0.5% | 50 |
| **12/2024** | 17,389 | **543** | **3.1%** | 37 |
| **12/2025** | 11,311 | **481** | **4.3%** | 6 |
| **02/2026** | 11,537 | **385** | **3.3%** | 12 |

### ‼ The base-mismatch rate jumps 6× in 12/2024 and stays there

0.5% → 3.1% → 4.3% → 3.3%. That is not drift; it is a step. The likely
cause is a pay agreement effective in 2024 whose base tables the חוקה does
not carry — but **this is not yet traced.** It is the first thing to look
at next: pick a handful of 12/2024 slips with a base gap and diff the
recomputed base against DARGA.

**שגויי דריכות also appears for the first time** in these files — 50 / 49 /
59, against 0 in every earlier מנהלי file.

### 15 new coverage-gap codes, ₪499,210

The three files bring codes never seen in 12/2008–12/2023:

| code | name | rows | ₪ |
|---|---|---|---|
| **1524** | העדרות | 410 | **₪217,260** |
| **6920** | הפרשי פנסיוני וקה"ש | 74 | **₪160,435** |
| **7902** | הפרשי פנסיוני וקה"ש | 57 | **₪102,961** |
| 712 | דרגת קידום | 2 | ₪10,289 |
| 5283 | תוספת שקלית | 2 | ₪4,061 |
| 1903 | תגמ. מלואים | 1 | ₪3,292 |
| (9 more) | | | ₪912 |

**6920 / 7902 / 6902 are a new numbering family** (pension and study-fund
differentials) that appears in no earlier file. **1524 העדרות is the same
absence family as 1027 and 1044**, both of which the user has just put out
of scope — so 1524 is very likely the same call, but it has not been
instructed and I have not made it.

Total coverage gap for the series: **38 codes / ₪636,303**.

## 0cu. ‼‼ 633 and 634 out of scope — one code erases 80% of the coverage gap

User instruction. `NON_PENSIONABLE` 60 -> **62**, py/js element-wise equal.
**By impact this is by far the largest batch so far.**

| | before | **after** |
|---|---|---|
| **coverage gap — מנהלי (16 files)** | **25 codes / ₪603,269** | **24 / ₪119,800** |
| coverage gap — engineers | 9 / ₪143,935 | 8 / ₪141,324 |
| true errors | 687 | 687 |
| valid | 302,625 | 302,625 |

**633 alone is ₪483,469 — 80.1% of the entire מנהלי coverage gap.** One
declaration cut the product's own scorecard by a factor of five, **without
the workbook changing by one character.**

That cuts both ways and must stay on the record: if 633 really is out of
scope, the old number was inflated and this is a correction. If it is not,
we have just hidden the largest hole we ever found.

| | 633 ת.מפ. בזק ב | 634 ת.מפ. בזק ג |
|---|---|---|
| declared in `מאפייני רכיבי שכר` | **no** | **no** |
| rule in the חוקה | none | none |
| rows | 269 | 13 |
| ₪ | ₪454,896 (₪483,469 absolute) | **−₪6,564** |
| first file | **12/2020** | **12/2020** |
| concentration | **98.4% in 12/2020 alone**, then 14 → 1 → 1 | 12/2020 and 12/2021 only |

**Both rest on the workbook's silence, not on a workbook statement** — like
1170, 4536 and 1904, but at a completely different scale. §24 established
that the workbook declares 841 codes; **633 and 634 are not among them**,
so there is no way to verify the call from the product itself. The fix is
to add both to `מאפייני רכיבי שכר` with `משכורת קובעת = לא`.

**633's shape supports the decision:** 98.4% in one month, a decaying tail,
and a sudden start in 12/2020 — the signature of a one-off retro settlement,
not a recurring supplement the חוקה is meant to compute.

After removing it the gap is far more evenly spread: the largest remaining
item (4221, ₪19,639 over 16 files) is 16% of it, not 80%.

## 0ct. 1027, 1044, 1904, 0 out of scope — 60 codes, and code 0 is a junk row

User instruction. `NON_PENSIONABLE` 56 -> **60**, py/js element-wise equal.

| code | name | workbook declaration | where it appears |
|---|---|---|---|
| **1027** | ימי היעדרות | **משכורת קובעת = לא, ברוטו = כן** | engineers 12/2024, 12/2025 |
| **1044** | שעות היעדרות | **משכורת קובעת = לא, ברוטו = כן** | engineers 12/2024, 12/2025 |
| 1904 | השלמ.למשתלם | not declared | engineers 12/2020 (3 rows, ₪19,369) |
| **0** | — | not declared | **engineers 12/2025 — one row** |

1027/1044 are the 5274/5527 shape — in the gross, outside משכורת קובעת — so
workbook-backed. Both are absence components whose amounts are mostly
negative (−₪10,256 and −₪4,889). 1904 rests on silence.

**Code 0 is not a pay code.** Scanned all 35 files: it appears exactly once
— engineers 12/2025, one row, **no name, ₪0**, on a slip already flagged
`no_base`. It was reaching the coverage-gap list as a nameless zero-value
code. Suppressing it is cleanup, not a scope decision.

Caveat recorded in the code: `המרת סמלי שכר` row 2 maps סמל מלמ 0 to
'יסוד\משולב' — the base. This list only suppresses coverage-gap reporting
and feeds no rule or base computation (base is 1 / 10002), so it cannot
corrupt a calculation — but if a future file carries code 0 as a real base
row, this entry would silence a hole that should be loud.

**Measured on the 19 engineers files:** coverage gap **13 codes / ₪181,725
-> 9 / ₪143,935** (−₪37,790). True errors 53 -> 53, valid 17,688 -> 17,688 —
nothing on the dashboard moved. No effect at all on the מנהלי files; none of
the four appears there.

## 0cs2. Two questions answered — 633/634, and the missing 2024-2026

**Where 633 and 634 appear** (scanned all 35 files; the earlier 631 scan was
the wrong code and is superseded):

| code | name | files | rows | ₪ |
|---|---|---|---|---|
| **633** ת.מפ. בזק ב | מנהלי 12/2020 | 249 rows / 249 workers | | **₪447,500** |
| | מנהלי 12/2021 | 14 | | ₪4,769 |
| | מנהלי 12/2022 | 1 | | ₪2.37 |
| | מנהלי 12/2023 | 1 | | ₪12.70 |
| | מהנדסים 12/2020 | 4 | | ₪2,611 |
| **634** ת.מפ. בזק ג | מנהלי 12/2020 | 4 | | ₪110.75 |
| | מנהלי 12/2021 | 9 | | **−₪6,674.61** |

**Both codes start in 12/2020 and appear in no earlier file.** 633 totals
269 rows / ₪454,896, of which **98.4% is 12/2020 alone** — the shape of a
one-off retro settlement, then a tail of 14 → 1 → 1. 634 is 13 rows and
**net negative**, i.e. mostly reversals. Top ministries for 633: רשות
האוכלוסין וההגירה ₪176,934, רשות האכיפה והגבייה ₪55,503, מכס ומע"מ ₪55,044.
Neither code is declared in `מאפייני רכיבי שכר`, neither has a rule, and
both carry ביט פנסיוני = כן on every row.

Note on the scan: `golmi_1208e.xlsx` keeps its data on a third sheet named
`גולמי` (sheets 1-2 are pivot leftovers), so a header-indexed scan skips it
unless the sheet is named explicitly. Re-checked that file directly —
**none of 633, 634, 0, 1027, 1044, 1904 appears in it.**

**Why the מנהלי report has no 2024/2025/2026:** because those files do not
exist here. Listed every staged file and read its pay date — the דירוג 1
series runs **12/2008 through 12/2023 and stops**. 12/2024 and 12/2025 exist
for **דירוג 12 only** (they arrived in the last upload). Nothing for 2026 in
either track. Send the מנהלי files for 12/2024 and 12/2025 and they go
straight in.

## 0cs. Engineers series extended to 12/2025 — 19 files, and the first zero

Three new דירוג 12 files arrived (12/2023, 12/2024, 12/2025) and were run
with the 16 existing engineers files. **19 files · 18,715 slips ·
partition closes on every row and the total.**

| | workers | true errors | valid |
|---|---|---|---|
| 12/2022 (previous last) | 721 | 3 | 676 |
| 12/2023 | 655 | 2 | 617 |
| 12/2024 | 449 | 1 | 417 |
| **12/2025** | **204** | **0** | **184** |

**12/2025 is the first file in the whole project with zero true errors.**
Read it with the population in mind: the cohort is shrinking fast (1,275
in 01/2008 → 204), so "0" here is 0 out of 204, not 0 out of 20,000.

Series totals: **53 true errors / 0.283%**, ₪3,094 underpaid + ₪9,747
overpaid. Coverage gap 13 codes / ₪181,725 — still dominated by **602
(₪113,860)**, the §26 hole.

Watch item: **12/2025's שגויי בסיס is 7 of 204 (3.4%)**, against 11 of 449
(2.4%) in 12/2024 and 2 of 721 (0.3%) in 12/2022. On 204 workers that is
five slips of movement, so it may be noise — **not investigated.**

Note on identifying the files: they arrived unlabelled and their column
order differs from the מנהלי files (`רכיב שכר` before `קוד רכיב שכר`).
Confirmed as דירוג 12 by reading the rating column: 7,274 / 5,727 / 2,825
rows, all rating 12. Staged as `golmi_1223e/1224e/1225e.xlsx` — note the
uploaded 1223 is the **engineers** 12/2023, not a new version of the
22,000-row מנהלי file of the same name.

## 0cr. 4651 neutralization column — 14 workers, placed last on purpose

User asked for a "שגויי תוספת 4651" column with no position given.
**Measured first, and the measurement decided the position.** 23 slips in
the 16 מנהלי files carry a 4651 flag, but they are not all true errors
today: **14 sit in "real", 8 in תוספת 1999, 1 in גמול**.

So the column went **last in the chain**, immediately before שגיאות אמת.
Anywhere earlier would have pulled in the 9 already neutralized by a
better-understood cause, replacing a good explanation with a worse one.

| | before | **after** |
|---|---|---|
| **true errors** | 701 | **687** |
| שגויי 4651 | — | **14** |
| all 21 other buckets | — | **unchanged** |

Exactly the 14 predicted. By month: 12/2008 5 · 12/2011 3 · 12/2009 2 ·
12/2017 2 · 12/2014 1 · 12/2020 1. Composition of all 23 flagged: 17 on
4651 alone, 3 also 1699, 2 also 628, 1 also 628+667+4983; ₪11,105 total,
14 material. The engineers series picks up 7 more.

### Why it is a bucket and not an error (new §29)

`tosafot!BS` — 4651's rate table — is filled for **12 of 228 codes**:
1–12 (all of 2008) at 0.15, and **13–228 (1.2009–12.2026) empty**. The key
column AR *is* complete, so `VLOOKUP` finds the row and **returns 0** — no
`#N/A`, no error indicator. **The workbook computes 4651 = 0 for every
month from 2009 on, silently.** The engine holds a flat 15% and keeps
checking, which is why slips fail. Fix: fill BS for codes 13–228.

**Correction to our own note:** `component_rules.json` claimed BS2 suffered
the §11 hard-coded-index defect (index 26 → BQ instead of BR). **No longer
true** — the 06.08 workbook has `$AR$7:$BS$234` with `BS1=28`, which is
correct. Citation fixed; `source_correction` records it.

## 0cq. ‼ 5253 neutralization column — it cost 42 true errors and ₪20,914

User asked for a column for 5253 right after שגויי מקצועית מיסים. Built in
all four places; dashboard is now **29 columns**, partition closes 16/16
and on the total (322,330).

**Unlike the דירוג column, this one moves the headline:**

| | before | **after** |
|---|---|---|
| **true errors** | 743 | **701** |
| % true errors | 0.2305% | 0.2175% |
| שגויי 5253 | — | **42** |
| every other bucket | — | **unchanged** |

**All 42 came from "real".** The column does not re-attribute existing
neutralizations — it takes 42 workers out of the count, carrying
**₪20,914** of exposure with them, 20 of it material (≥₪100). Direction:
27 underpaid / 15 overpaid.

Composition of the 42: **35 flagged on 5253 alone**; 5 also carry 737 *and
1699*; 1 also 737; 1 also 5251. **The five 1699 gaps are neutralized along
with them** — small, but 1699 is 80% of all true errors, so this is the
exact "bucket swallows unrelated errors" risk `CLAUDE.md` warns about. If
it grows, narrow the bucket to slips whose *only* gap is 5253.

By month: 12/2012 13 · 12/2014 12 · 12/2015 7 · 12/2020 4 · 12/2022 4 ·
12/2016 1 · 12/2019 1 · **0 in the other nine.** A 0 is not evidence of
correctness — 12/2013 is 0 because all 2,625 carriers pay ₪475, which is
*not* the workbook's amount (§28), and 12/2023 is 0 because the rule is
silenced there at 94.6%.

**Naming, flagged to the user:** they wrote "שגויי בוררות מיסים 5253", but
בוררות מיסים is **741** and already has its own column; 5253's workbook
name is **תוספת שכר מיסים**. Built for the code they gave (5253), labelled
"שגויי תוספת שכר מיסים (5253)" to avoid two identically-named columns.
Rename on request.

**Verified:** pytest 34 passed · `node --check` clean on engine.js and the
extracted front-end script · front-ends byte-identical · full 16-file run.

## 0cp. 5253 — the user's question was right, and it exposed three bad bands

**User asked:** "5253 is ₪492 in 2014 in both the file and the PROGIM — why
does it come out as an error?" **It doesn't.** Measured on 12/2014: 2,554
carriers, **2,456 pay exactly ₪492, and 0 of them are flagged.** The 52
flagged slips pay something else entirely (₪501, ₪738, ₪510, ₪623.20,
₪88.88…), and only 12 of the 52 are flagged on 5253 alone. The 411 in the
dashboard's gap table is all 16 files, not 2014.

### What the check found instead (new `docs/PROGIM_FIXES.md` §28)

Swept all 16 files and compared the modal full-time amount against the
workbook's pulse table. **8 bands match exactly; 3 do not:**

| file | code | workbook | paid | carriers |
|---|---|---|---|---|
| 12/2013 | 72 | **483** | **475** | 2,625 |
| 12/2020 | 156 | **493.74** | **490.8** | 2,047 |
| 12/2021 | 168 | **493.74** | **490.8** | 2,007 |

The years on both sides of each gap match to the agora, so the code→month
mapping is right and the **bands** are wrong. Two workbook bands (₪483 for
2013, ₪493.74 for 2020–2021) are paid by **zero** slips anywhere. Either
they should be deleted (the previous band extends), or 2,625 workers were
underpaid ₪8 and 4,054 underpaid ₪2.94.

**Why the engine stayed quiet: `shekel` rules are month-agnostic** — they
accept the closest of all 14 amounts, so ₪475 in 2013 passes because it is
a valid amount *for another year*. First measured demonstration of the §14
gap on a real code. Checked whether it hides anything else: in 12/2014,
**0** full-time slips pay a valid-other-year amount.

Also: **in 12/2023 the rule is silenced entirely** — 1,776/1,877 = 94.6%,
under the 97% gate. 0 flagged there means unchecked, not clean.

### Two corrections to `component_rules.json`

1. **The source citation was wrong.** It said `tosafot!CM3` / range
   `$CE$7:$CN$234`. Actual: **`CN3` = `VLOOKUP($C$4,$CF$7:$CO$234,9,0)`**.
   `CM` is 5251 (ת.מבקר חשב') — a different component; `CE` holds 424 in
   every row and is not the key column, `CF` (קוד חודש) is. The extracted
   amounts were right (14/14 against column CN); only the reference was
   wrong. `source_correction` records it.
2. **Added the full `amounts_by_code`** — 14 bands, codes 52–228. The
   engine does not use it yet; the moment month-aware checking lands, the
   three rows above fire on their own.

Rules still 105. `pytest` 34 passed.

## 0co. "שגויי דירוג" column + 5527/4536 out of scope — and the headline did not move

Two user instructions, both landed, both measured on the full 16-file
מנהלי series (322,330 slips). **Neither changed the true-error count.**

### The דירוג bucket — measure first, build second

Asked for a "שגויי דירוג" column covering 981, 839, 1565, 4640, 752. **I
scanned all 32 files before building it.** The five codes appear **five
times, on four slips, ₪927** — 0.0012% of the population:

| code | ₪ | file | slip status |
|---|---|---|---|
| 981 תגבור 94 | 74.10 | מנהלי 12/2010 | invalid |
| 839 תמריץ משפטנים | 31.06 | מנהלי 12/2021 | invalid — **same worker as 1565** |
| 1565 תוס.משפטנים | 9.53 | מנהלי 12/2021 | invalid — **same worker as 839** |
| 4640 הסכם אח 97 | **−150.48** | מנהלי 12/2008 | invalid (17% job, negative retro row) |
| 752 הופעה 20% | 661.57 | מנהלי 12/2020 | **valid** |

Run result: **bucket = 3.** It took 2 from שגויי בסיס (1,334→1,332) and 1
from שגויי תוספת 1999 (3,116→3,115). **True errors 743 → 743. תקין
302,625 → 302,625.** Partition closes 16/16 and on the total.

The bucket is keyed on **carrying** the code (the 4140 shape), not on
failing a rule — none of the five has a rule to fail. So it neutralizes a
slip whose error may be somewhere else entirely. At 3 slips that is
noise; if a דירוג 21 (legal service) or nursing file ever arrives, this
becomes a wide bucket that swallows unrelated errors and must be narrowed
to a per-component gap. **Flagged to the user in the same turn.**

**Why they have no rule (new `docs/PROGIM_FIXES.md` §27):** all five are
declared `משכורת קובעת = כן` in `מאפייני רכיבי שכר`, four of them
`בסיס למינימום רובד 1 = כן` — and **none has a formula anywhere.** 1565's
only substantive mention is a cell reading **"מחכה לאישור"**
(`רכיבים דלוייט!L55`); 981 appears only as an *input* to another
component's base; 839 is absent entirely; 4640 appears in four sheets as a
name with no value. Same shape as §26 (602), five times over.

### 5527 + 4536 non-pensionable — 56 codes

`NON_PENSIONABLE` 54 → **56**, py/js element-wise equal (56/56, no
symmetric difference). 5527 is workbook-backed (`משכורת קובעת = לא`,
`ברוטו = כן` — the 5274 shape); 4536 is not declared at all and rests on
the workbook's silence.

**Trap checked before shipping:** 5527 also keys the "ותק סטודנט"
neutralization bucket. That bucket reads `cp.code == 5527` off the slip
directly and does **not** go through `NON_PENSIONABLE`, so the list change
leaves it alone — verified, bucket stayed 0.

Coverage gap **27 codes / ₪607,938 → 25 / ₪603,269** (−₪4,669). No bucket
and no headline number moved.

### Front-end bugs found and fixed while wiring this

The earlier front-end edit had shipped `DERUG_CODES` **referenced but never
declared** — a ReferenceError that would have broken every bulk run in the
browser. Declared it above `runBulk` in both files. The Excel-export column
indices in `downloadUnified` were also still on the 27-column layout
(number formats, the warn-colour list, אמיתיים/%/תקין, and the `Z`/`Y`
conditional-formatting ranges); all shifted to 28. `index.html` and
`salary_frontend.html` verified byte-identical in their script block.

**Verified:** `python3 -m pytest tests/ -q` → 34 passed · `node --check`
clean on `engine.js` and on the extracted front-end script · full 16-file
run, partition 322,330 = 322,330.

## 0cn. New מנהלי unified report — the 1699 fix lands

**16 files · 322,330 slips.** Partition closes on all 16 rows and the total.

| | before | **after** |
|---|---|---|
| valid | 304,110 | 302,625 |
| **true errors** | 175 | **743** |
| exposure | ₪62,385 | **₪273,103** |
| under / over | — | ₪138,867 / ₪134,235 |

**568 new true errors and ₪210,762 of new exposure, all of it 1699.**

**1699 is now 80% of all true errors** — 596 workers, ₪210,098 — ahead of 736
(42), 5253 (42) and 756 (15). Of those 596, **388 underpaid and 208 overpaid**.
That two-sided split matters: a residual engine bug would skew one way, so this
reads as real gaps rather than another modelling error.

**The rule still does not clear the gate everywhere.** It fires in 12/2011,
12/2013–12/2017, 12/2019–12/2021 and 12/2023, and remains silenced in 12/2008–
12/2010, 12/2012, 12/2018 and 12/2022. Those four still sit under 97% after the
fix, so **a further model gap remains there** — the next open item on 1699.

Coverage gap essentially unchanged: 27 codes / ₪607,938 against 28 / ₪608,076.
The fix touched checking, not coverage.

## 0cm. ‼‼ The 1699 minimum-wage check was broken — and the bug was ours

**The user said their own checks show the Progim is accurate on 1699. They were
right, and here is why.**

The rule is `completion = MAX(0, target × job% − Σ counted)`. The engine summed
the **paid base** as its base term — which carries the seniority multiplier.
**The counted base must be the grade base at seniority zero**
(`grade_base × job%`), exactly as the comment directly above that code had said
all along. The implementation contradicted its own comment.

Because the paid base exceeds the seniority-zero base, the counted sum came out
inflated, the expected completion came out too small, and essentially every slip
looked overpaid.

| file | 1699 carriers | paid base (bug) | **seniority-zero (fixed)** |
|---|---|---|---|
| מנהלי 12/2008 | 7,924 | 7.1% | **96.4%** |
| מנהלי 12/2014 | 10,358 | 4.6% | **96.7%** |
| מנהלי 12/2018 | 12,784 | 7.7% | **95.8%** |
| מנהלי 12/2023 | 14,671 | 4.5% | **97.0%** |

**The inferred target was correct all along** — ₪3,850.20 (2008), ₪4,300 (2014),
₪4,656 (2018), ₪5,571.80 (2023), i.e. the statutory minimum wage of each era. I
had told the user the target was the prime suspect; it was not, and that guess
is retracted.

**Consequence.** The gate had silenced 1699 in *every* file, so 8,000–14,700
slips a month were never checked for minimum-wage completion at all. With the
fix the rule passes and fires: **342 workers flagged in 12/2014, 441 in
12/2023.** These are genuine new findings and they will move headline numbers in
every report — correctly.

Fixed in `main.py` and `engine.js` together; 34 tests pass, `node --check`
clean.

**Standing lesson:** a 5% match rate is not "a difficult component", it is an
error message. The comment described the right rule and the code did something
else, and the trust gate hid the discrepancy instead of surfacing it.

## 0cl. 12/2020, 12/2021, 12/2022 — and two of my own claims refuted

| | 12/2020 | 12/2021 | 12/2022 |
|---|---|---|---|
| workers | 966 | 838 | 721 |
| valid | 833 | 775 | 676 |
| true errors | 1 | 1 | 3 |
| exposure | ₪292 | ₪15 | ₪135 |
| checked / components | 10/31 | 7/30 | 7/32 |
| no-base | **111** | 53 | 30 |

### ‼‼ 1. §25's completion was wrong — 4453 steps to ₪933 before code 193

I filled codes 13–192 with 533 off measurements ending at code 84, and it then
passed at codes 96, 108, 120, 132 and 144. **12/2022 (code 180) pays ₪933 to 9
full-timers.** The full 16-file series: 383 at code 1, **533 continuously at
codes 12–168** (12.2008–12.2021), **933 already at code 180.**

So the step happens **between codes 169 and 180 — not at 193**, which is where
the workbook's own 933 band starts. `amounts_by_code` corrected to 533≤168,
933≥180, with 169–179 marked explicitly unknown.

**The completion survived seven consecutive confirmations and then broke. Seven
confirmations are not proof.**

### ‼ 2. §26 was wrong — 602 is not flat, it pulses

I wrote that a flat column "is a faithful description of what was measured".
It was measured only to 12/2019. The three new files say otherwise:

| codes | dates | amount | carriers |
|---|---|---|---|
| 1–108 | to 12.2016 | **0 carriers** | — |
| 109–144 | 1.2017–12.2019 | **₪557.24** | 21, 18, 26 |
| 145–180 | 1.2020–12.2022 | **₪567.35** | 24, 22, 28 |

602 needs a pulse table, not a single value. §26 corrected.

**602 remains the dominant hole** in all three files — ₪14,241, ₪12,482
(the *entire* gap that month), ₪15,886.

### New: 1904 השלמ.למשתלם — ₪19,369 in 12/2020

Absent from tosafot, SACHAR and SACHAR4643. Unlike 602 its amounts vary widely
(₪7,379, ₪6,219, ₪5,771 among full-timers), so it looks computed or
individually set rather than a tariff — **not** a candidate for a flat column.
Undiagnosed.

**no-base spikes to 111 of 966 (11.5%) in 12/2020**, then falls to 53 and 30.
Given 0ch's retraction, this is recorded as an observation, not a trend.

## 0ck. 12/2019 engineers — 602 firms up, 4453's range reaches 12/2019

**Run:** 945 workers, all דירוג 12 · 897 valid · **5 true errors** (0.53%) ·
₪1,221 exposure. Partition closes. Gate checks 11 of 32. Pay-agreement family
silenced for an **eleventh** consecutive file (4544 95.5%, 4550 93.8%, 4934
95.3%, 4994 93.0%).

**602 gets its third and cleanest data point.** 26 carriers, and **all 26 pay
exactly ₪557.24** — no outlier at all, where 12/2017 and 12/2018 each had one.
The value is now confirmed at codes 120, 132 and 144. §26 updated: a flat
`=+$<col>$3` from code 109 is a faithful description of what was measured, while
codes 1–108 should stay empty (12/2016 has 0 carriers) and anything past code 144
is the user's call rather than our measurement.

**It is also the file's whole coverage gap and it is growing:** ₪12,222 →
₪10,480 → **₪14,488**. The gap is down to 3 codes / ₪15,762, of which 602 is
₪14,488 — 4623 and 1653 dropped out entirely this month, leaving only 1169 and
4447 beside it.

**✅ 4453 completion holds again:** ₪533 at code 144. Confirmed range is now
code 12 → **code 144** (12.2008–12.2019) continuous. Codes 145–192 remain ours.

## 0cj. 12/2018 engineers, and 602 chased down

**Run:** 982 workers, all דירוג 12 · 919 valid · **1 true error** (0.10%) · ₪131
exposure. Partition closes. Gate checks 9 of 34. Pay-agreement family silenced
for the **tenth consecutive file** (4544 back to 95.1%, 4550 93.5%, 4934 94.9%,
4994 93.1%) — 12/2016's crossing really was a one-file blip.

**✅ 4453 completion holds again:** ₪533 at code 132. Confirmed range now runs
code 12 → **code 132** (12.2008–12.2018) continuously. Codes 133–192 remain ours.

**602 ע"ח פריון — written up as `PROGIM_FIXES` §26.** It is the largest hole on
this track (₪12,222 in 12/2017, ₪10,480 in 12/2018) and it **appears nowhere in
the workbook** — not in tosafot, SACHAR, SACHAR4643 or sminimum, and no rule
references it. Yet `מאפייני רכיבי שכר` declares it `משכורת קובעת = כן`, so it
belongs in the pensionable base. A real coverage hole, not a misclassification.

Measured: **0 carriers in 12/2016**, then 22 carriers paying a flat **₪557.24**
(21 of 22) in 12/2017 and 19 paying the same (18 of 19) in 12/2018. It starts in
2017 and looks like a flat shekel tariff — one `tosafot` column would cover it.
§26 carries the column template and an explicit warning **not** to fill all 228
codes from two data points, which is the mistake 805 needed correcting for.

## 0ci. 12/2016 and 12/2017 — the trust gate caught in the act

| | 12/2016 | 12/2017 |
|---|---|---|
| workers | 1,035 | 1,016 |
| valid | 971 | 973 |
| **true errors** | **15 (1.45%)** | **4 (0.39%)** |
| exposure | ₪3,166 | ₪1,490 |
| components checked | 7 of 30 | 7 of 31 |

**The cleanest demonstration yet that the gate is a switch.** True errors go 1
(12/2015) → **15** (12/2016) → 4 (12/2017), and the cause is not the payroll:

| file | 4544 match | checked? | true errors |
|---|---|---|---|
| 12/2015 | 95.6% | ❌ silenced | 1 |
| **12/2016** | **97.1%** | **✅ checked** | **15** |
| 12/2017 | 95.8% | ❌ silenced | 4 |

**A 1.5-point move flipped a component carried by 1,006 of 1,035 workers from
invisible to active, and multiplied the file's headline by fifteen.** Same
component, same population, adjacent years. 12/2016's largest gap is indeed 4544
— 29 gaps, ₪1,688.

**Consequence for reading the series: true-error counts are not comparable
across files**, because the number of components being checked changes from file
to file. 12/2016 is not a bad year; it is the year one more rule was awake.

**✅ 4453 completion holds at two more points:** ₪533 at code 108 (9 carriers)
and code 120 (7). Confirmed range extends from code 96 to **code 120**; codes
121–192 still unverified.

**Two new coverage holes, both declared `כן`:** **602 ע"ח פריון at ₪12,222** in
12/2017 — the largest hole on this track so far — and 978 תפקיד-מחקר at ₪395 in
12/2016. **1653 counted as a hole for the fourth and fifth time** while declared
`לא`.

## 0ch. 12/2015 engineers — our 4453 completion survives its first test

**Run:** 1,102 workers, all דירוג 12 · 1,048 valid · **1 true error** (0.09%) ·
₪5 exposure. Partition closes.

**✅ First independent test of §25's completion.** We filled codes 13–192 with
533 on measurements that stopped at code 84, and flagged that codes 85–192 had
no support at all. **12/2015 is code 96 — the first point inside the guessed
range** — and it pays **₪533 to 11 full-timers.** The completion holds there.

Confirmed range extends from code 84 to **code 96**. **Codes 97–192 remain
unverified**, so it is still our number and §25's instruction to fill
`BR19:BR192` stands.

**Pay-agreement family, ninth consecutive file:** 4544 95.6%, 4550 93.4%, 4934
94.6%, 4994 94.5%, each on 913–1,067 of 1,102 workers. **The gate checks 5 of
29** — a new low for the series, and another reminder that "1 true error" here
measures what was checked, not how the payroll behaved.

**Coverage gap unchanged:** the same 4 codes / ₪4,838 as 12/2014 — 4623
(₪3,117), 1169 (₪637), 4447 (₪637), 1653 (₪448). Third file running where 1653
is a hole while the workbook declares it `לא`.

**‼ Retraction from 0cf.** I flagged the no-base bucket as climbing (24 → 39 →
46). **12/2015 comes in at 33.** That is fluctuation, not a trend — the
observation is withdrawn.

## 0cg. 4453 converted, 1168 marked file-fed — and one completion is ours, not the workbook's

Both on the user's instruction. `component_rules.json` is now **105** rules.

**1168 תוס. מבצעית → `reported`.** The user says it is taken from the file. The
workbook declares it משכורת קובעת = כן, so it is pensionable but not computed;
`reported` takes it off the coverage-hole list without claiming it is checked.

**4453 דריכות וכוננות → `shekel`.** The workbook *does* define it —
`tosafot!BR2 = IF('Netunei Gimlai'!G86=TRUE, VLOOKUP($C$4,$AR$7:$BR$234,BR1,0), 0)`
— but **its table holds 3 filled cells out of 228**: code 1 = 383, code 12 =
533, codes 193–204 = 933. Everything else is blank.

Measured on eight engineers files (full-timers): 383 at code 1 and **533 at
codes 12, 24, 36, 48, 60, 72 and 84** — 01/2008 through 12/2014. Both workbook
values are exactly right; the rest of the table simply is not there.

**‼ So we filled codes 13–192 with 533 in the rule's `amounts_by_code`. That
is our completion, not the workbook's.** It rests on six consecutive
measurements (codes 24–84) and has **no coverage at all from code 85 to 192** —
there is no engineers file from 2015 onward. 4453 now reads 100% on both files
checked, but that 100% leans on a number we supplied. `PROGIM_FIXES` §25 carries
the instruction to fill `BR19:BR192`, locate where the 933 pulse begins, and
delete `amounts_by_code` once the workbook is complete.

**Effect on 12/2014's coverage gap:** 5 codes / ₪8,392 → **4 codes / ₪4,838**
(4623 ₪3,117, 1169 ₪637, 4447 ₪637, 1653 ₪448). 4453 left the list entirely by
becoming a validated rule; 1168 moved to the "fed from the file, as the Progim
defines" line.

## 0cf. 12/2014 engineers — and 607's table end is confirmed

**Run:** 1,147 workers, all דירוג 12 · 1,088 valid · **3 true errors** (0.26%) ·
₪728 exposure, all underpayment. Partition closes.

**✅ 607 closed.** Its table stops at code 72 (12.2013) and 0bv recorded that we
could not tell whether the component continued. **It did not: 0 carriers in
12/2014.** The table ends in exactly the right place — no further extension
needed.

**669 disappears from engineers too** — 0 carriers after 99 in 12/2013. That
matches the מנהלי track, where the population collapsed from 5,630 to 199 in the
same year. Both tracks lost it together in 2014, which is one more argument that
669 is period-driven rather than track-driven (§23).

**Pay-agreement family, eighth consecutive file:** 4544 95.4% (1,101 carriers),
4550 94.0% (954), 4934 94.2% (1,101), 4994 94.3% (1,100). The gate checks
**7 of 29** components — the lowest ratio in the series.

**‼ 1653 counted as a hole again.** The coverage gap is 5 codes / ₪8,392: 1168
(₪3,554, declared `כן` — real), 4623 (₪3,117, undeclared), 4447 (₪637, declared
`כן` — real), 1169 (₪637, undeclared), and **1653 (₪448, declared `לא`)**. Second
file running where 1653 is a hole only because the engine does not read the
declaration. Still not removed — no instruction covers it.

**Trend worth watching:** the no-base bucket climbs 24 (12/2010) → 39 (12/2013)
→ **46** (12/2014) while the population shrinks (1,225 → 1,147). Undiagnosed.

## 0ce. 954, 1170, 4540 out of scope — §24's prediction, paid out

On the user's instruction, taken straight off 12/2013's coverage list. All three
pass the three checks. `NON_PENSIONABLE` = **54**, py/js equal.

| code | name | workbook declaration |
|---|---|---|
| **954** | תוספת שעות גלובלית | row 150: `משכורת קובעת = לא`, **gross = כן** |
| **4540** | ש. נ. 521% | row 546: `לא` in every column |
| 1170 | תוספת שעות | **not declared at all** — rests on silence |

**954 and 4540 are two of the three §24 measured** as counted in the coverage
gap while the workbook already placed them out of scope. Re-running the same
file: **8 codes / ₪11,138 → 5 codes / ₪6,955**. Of the ₪4,183 removed, **₪1,747
should never have been there** had the engine read `משכורת קובעת`.

**‼ One of that kind is left, and I did not remove it.** **1653 (תוס. כוננות,
₪448) is declared `משכורת קובעת = לא`** and still counts as a hole. No
instruction was given for it, and codes do not leave scope on my initiative. It
waits, along with §24's other 464.

This is the sharpest illustration of §24 yet: three codes were excluded by hand
and two of them were already written in the workbook. Until the engine reads the
sheet, each one costs a full round-trip of report → instruction → code → report.

## 0cd. 12/2013 engineers — and the sheet that makes §15 free

**Run:** 1,193 workers, all דירוג 12 · 1,133 valid · **3 true errors** (0.25%) ·
₪211 exposure, all overpayment. Partition closes. 669 reads 99.0% (sixth §23
confirmation). The pay-agreement family stalls again for the seventh straight
file: 4544 95.2%, 4550 94.3%, 4934 93.9%, 4994 93.9%. Trust gate: 10 of 31.

**Coverage gap returns: 8 codes / ₪11,138**, after four consecutive clean files.
Chasing what was in it produced the real finding.

### `מאפייני רכיבי שכר` already contains what §15 asks for

It declares **841 codes** — **486 with `משכורת קובעת = לא`**, 218 with `כן`.
Our hand-grown `NON_PENSIONABLE` has 51.

| | count |
|---|---|
| ours matching a `לא` declaration | 22 |
| **ours that the workbook declares `כן`** | **12** |
| ours not declared at all | 17 |
| **declared `לא`, absent from ours** | **464** |

**‼ §17 undercounts.** It records 4140 and 4538 as "the only entries that
contradict the workbook". The real list is twelve: **1260, 1269, 1731, 4122,
4123, 4140, 4437, 4457, 4538, 5272, 5374, 5438** — all added on the user's
instruction. That does not make the user wrong; the declaration may be stale.
It does mean twelve places where code and workbook say opposite things, only
two of them documented. Each needs an explicit call.

**Concrete cost, from this file's own gap list:** of the 8 codes, 1168 (₪2,713)
and 4447 (₪637) are declared `כן` — genuine holes. But **4540 (₪1,216), 954
(₪531) and 1653 (₪448) are declared `לא`** and should never have been counted.
Three of eight are holes only because we do not read the sheet. The remaining
three (4623, 1170, 1169) are not declared at all.

**Scale of the 464:** small in money — 5 appear in 12/2023 (₪5,431), 3 in this
file (₪2,195). But two of them, **739 (תוספת סיכון) and 883 (תוספת אבטחה), are
actively validated by our rules** while the workbook says they are not part of
the pensionable salary. That needs a decision.

**The instruction, and it is free this time:** §15 asks for a declared
`פנסיוני` column. It already exists — it is `משכורת קובעת`, populated for 841
codes. The engine should read it instead of maintaining a 51-code list that
grows one batch at a time. Doing so retires all sixteen batches, closes three of
the eight gaps above, and forces the twelve contradictions into the open.
**Not done — it changes behaviour on every file, so it is the user's call.**
`PROGIM_FIXES` §24.

## 0cc. Progim 06.08.2026 installed, and a quietly broken tool fixed

A clean 12-cell diff: `tosafot!AS67:AS78`, codes 61-72 (1.2013-12.2013), all
₪1,943.23. 607's table now covers **codes 1-72**, empty from code 73. Fourth
extension: 1-24 → 1-36 → 1-60 → 1-72. Installed under the new name
`Progim_06.08.2026.xlsm` with `Progim_05.08.2026.xlsm` deleted in the same
commit, the same way 04.08 gave way to 05.08.

**Found while installing:** `tools/classify_hukka_amounts.py` hard-coded
`data/progim/Progim_04.08.2026.xlsm` as its default workbook — a file deleted
two days ago. The tool has been **silently broken** since. It now picks the
newest `Progim_*.xlsm` in the directory (verified: resolves to
`Progim_06.08.2026.xlsm`).

**General lesson worth acting on:** the workbook is re-issued under a new
filename on almost every edit — eleven versions today alone. **Any code that
pins a workbook filename goes stale within hours.** If there are other such
pins, they are worth hunting down now rather than discovering broken later.

## 0cb. 5274 out of scope — and the first declaration that distinguishes gross from pensionable

On the user's instruction. Clean on all three checks, and declared in
`מאפייני רכיבי שכר` row 648. `NON_PENSIONABLE` = **51**, py/js equal.

**The declaration differs from every previous one, and it is the better shape:**

| code | name | tier 1 | tier 2 | משכורת קובעת | ברוטו תקציבית | ברוטו צוברת |
|---|---|---|---|---|---|---|
| 1622 | מנהל בחירות | לא | לא | **לא** | לא | לא |
| 1631 | הכנה לבחירות | לא | לא | **לא** | לא | לא |
| 1623 | סגן מנהל בחירות | לא | לא | **לא** | לא | לא |
| **5274** | **ימי השתלמות בשכר** | לא | לא | **לא** | **כן** | **כן** |

The elections codes are לא everywhere — outside every computation. 5274 is the
first to say something sharper: **it does count in gross, and is excluded only
from the pensionable base.** That is exactly what `NON_PENSIONABLE` encodes, and
it is the cleanest evidence yet that **`משכורת קובעת` is the right field to lean
on** rather than the workbook's silence — silence cannot distinguish "not
present" from "present but not pensionable".

**The "ימי X" family is now eight codes** — 5271, 5272, 4123, 5273, 4436, 4437,
4438, 5274 — added one at a time across sixteen batches. 5274 appears in **none**
of the files checked (0 rows in 12/2023 and in the engineers files), so it was
declared ahead of a gap rather than in response to one, which is the better
order.

§15 again: there is no way to know the family has ended. A `פנסיוני` column over
the 295 codes in `sminimum`, populated from `משכורת קובעת`, retires all sixteen
batches at once.

## 0ca. ‼ The 16 December files are the מנהלי track, not "the full population"

Checked when the user asked for a מנהלי unified report. **All sixteen December
files — and the 22,422-slip 0108 file — are 100% דירוג 1 (מינהלי — עובדי
מדינה).** Sampled 12/2008, 12/2015, 12/2020, 12/2023 and 0108: single track in
every one.

**I called them "the full population" all session, in chat and in the docs.
That is wrong.** They are one track out of the 30+ in `DERUG`. Every number
measured on them — coverage gaps, match rates, neutralization buckets, the 175
true errors — **describes דירוג מנהלי**, not state employees at large.

**What survived re-checking:**

- **§23 (669) — the conclusion holds, the argument I gave for it did not.** I
  wrote there that 669 "is not דירוג-dependent" on the strength of comparing the
  engineers files against the December files — which is *precisely* a
  cross-track comparison, so that reasoning was wrong. But the measurement
  stands: מנהלי pays ₪2,596.31 in 12/2008 and ₪51.09 after; engineers pay
  ₪2,596.31 in 12/2008 and 51.09 after (98.9%). **Both tracks move together**,
  so 669 really is period-dependent and 12/2008 really is the sole anomaly.
- **1063, 5524, 5270, 5340, 737, 5251, 5253 — measurements valid, scope
  narrower than stated.** All were measured on מנהלי files. 1063's ₪10.1M is
  ₪10.1M *in the מנהלי track*; whether other tracks add to it is **unmeasured**.

**And it turns a stray fact into a finding:** the מנהלי coverage gap is 28
codes / ₪608,076 while the engineers' is **0 / ₪0**. Those are two tracks, not a
before and after. The workbook covers engineers completely and מנהלי not — which
is invisible if you call one of them "the full file".

**Deliverable:** the unified report produced under 0bz *is* the מנהלי report;
it was re-delivered under a correctly named file rather than re-run, since it
already includes every change through 1623.

## 0bz. 1623 out of scope, and the engineers series consolidated

On the user's instruction. Clean on all three checks, and the workbook states it
outright: `מאפייני רכיבי שכר` row 376 declares **סגן מנהל בחירות** with
משכורת קובעת = לא. `NON_PENSIONABLE` = **50**, py/js element-wise equal.

**The elections family is complete** — 1622 (row 375), 1631 (row 380), 1623 (row
376). These are **the only three of fifteen batches with an explicit declaration
in the workbook**, and they are all one family; the other 47 codes rest on the
workbook's silence. The workbook clearly *can* declare pensionability — it just
does so for 3 of the 50 codes we have had to place out of scope. When
`sminimum` carries a filled `פנסיוני` column for all 295 codes, all fifteen
batches collapse into one lookup. That is §15's whole argument, now with a
concrete ratio behind it.

### Engineers unified — 6 files, 7,462 slips

**7,462 slips · 7,158 valid · 20 true errors (0.27%) · ₪5,659 exposure** (₪506
under, ₪5,154 over). Partition closes on every row and in the total.

| month | workers | true errors | valid |
|---|---|---|---|
| 01/2008 | 1,275 | 0 | 1,230 |
| 12/2008 | 1,260 | 14 | 1,181 |
| 12/2009 | 1,243 | 1 | 1,203 |
| 12/2010 | 1,225 | 0 | 1,182 |
| 12/2011 | 1,226 | 4 | 1,176 |
| 12/2012 | 1,233 | 1 | 1,186 |

**Coverage gap across the whole series: 0 codes / ₪0** (plus 3 codes / ₪75,422
fed from the file as the workbook intends). First track where the workbook
covers 100% of the pensionable components.

**The caveat still governs:** 20 errors over 7,462 slips reads well, but in all
six files the gate mutes the pay-agreement family (4544, 4550, 4934, 4994) —
the components carried by nearly every worker. The number describes what was
checked, not the files.

The user asked for "a unified control report" without naming a series; both were
produced, since the phrase had meant the 16 December files up to now but the
recent work is all engineers.

## 0by. 12/2012 engineers — and a correction to my own read of the stall

**Run:** 1,233 workers, all דירוג 12 · 1,186 valid · **1 true error** (0.08%) ·
₪136 exposure, all overpayment. Partition closes. **Coverage gap 0 / ₪0 —
fourth consecutive file.** 669 reads 97.9%, a fifth §23 confirmation. Trust gate:
**10 of 29 checked**, the lowest ratio yet.

### ‼ Correction to 0bx

In 0bx I wrote that digging into 4544/4934/4994 would likely turn up a formula
bug like 4550's. **Measured, and that is probably wrong.** The failure signatures
are opposite:

| | direction | slip/expected spread |
|---|---|---|
| **4550 before §22** | **628 of 628 the same way** (slip < expected) | tight, 0.39-0.61 |
| 4544 (12/2012) | 18 under vs 26 over | wide: 0.92, 1.18, 1.23, 1.26, 1.59 |
| 4934 | 14 under vs 46 over | 0.98, 1.04, 1.21, 1.25 |
| 4994 | 23 under vs 38 over | 0.93-1.23 |

One-directional failure in a tight ratio band is the signature of a wrong
formula — that is exactly what led to the 4550 fix. **Bidirectional failure with
a wide spread is the signature of retro adjustments folded into the component.**

**So the recommendation changes:** do not hunt a formula bug in these three. Find
out whether the גולמי carries a **retro flag** that would let those rows be
identified and neutralized deliberately, instead of dragging the match rate to
95% and silencing the component outright — the same remedy §7 already records
for 705.

**What stands from 0bx:** the four components really do sit under the gate in
every one of the six engineers files, really are carried by almost the whole
file, and really are never checked. Only the suspected cause has changed.

## 0bx. 607 extended through 12/2012, 12/2011 checked, and a pattern worth chasing

A 24-cell diff fills `tosafot!AS43:AS66` — codes 37-60 (1.2011-12.2012) — with
₪1,943.23. The table now covers **codes 1-60**, empty from code 61. Third
extension of the day: 1-24 → 1-36 → 1-60.

**12/2011 engineers:** 1,226 workers, all דירוג 12 · 1,176 valid · **4 true
errors** (0.33%) · ₪314 exposure. Partition closes. **Coverage gap 0 / ₪0 —
third consecutive file.** 669 reads 98.9% (fourth §23 confirmation); 607 has one
carrier left, matching.

### ‼ The pattern across all five engineers files

The same components sit under the 97% gate every single time, so they are never
checked:

| code | name | 01/2008 | 12/2008 | 12/2009 | 12/2010 | 12/2011 |
|---|---|---|---|---|---|---|
| 4544 | הסכם 2001 / תוספת 3.6 | 96.8% | — | 95.4% | 96.8% | 95.9% |
| 4550 | הסכם 2001 אישי | 94.2%* | 95.2% | 93.4% | 94.9% | 94.2% |
| 4934 | הסכם 2009 | — | — | — | 95.7% | 94.5% |
| 4994 | הסכם 2011 | — | — | — | — | 94.5% |

<sub>* after §22's fix; 42.1% before it.</sub>

All four are the **pay-agreement family** (2001 / 2009 / 2011), each carried by
1,000-1,250 of the ~1,225 workers — essentially the whole file — and all four
stall in a narrow 94-97% band. Four related components, five files, always the
same range: that does not read as noise.

**Practical meaning:** in these files the components covering almost every
worker are precisely the ones not being checked. Every "0 true errors" on this
track must be read next to this table.

**Next step, not yet done:** find out why the pay-agreement family stalls at ~95%
for engineers, exactly as §22 did for 4550 and found a wrong formula. This is
now the largest open item on the track.

## 0bw. 1631 out of scope — the second batch the workbook backs

On the user's instruction. Passes all three checks cleanly — no column in
tosafot/SACHAR/SACHAR4643, no rule of its own, referenced by no other rule — and
the workbook states it outright: `מאפייני רכיבי שכר` row 380 declares
**הכנה לבחירות** with משכורת קובעת = לא, and לא for both minimum tiers and both
gross columns. `NON_PENSIONABLE` reaches **49**, py/js element-wise equal.

**The elections family is now two codes**, 1622 (מנהל בחירות) and 1631
(הכנה לבחירות) — and they are **the only two of fourteen batches with an
explicit pensionability declaration in the workbook**. Every other batch rests
on the workbook's silence. That sharpens §15: the fix is a declared `פנסיוני`
column over all 295 codes, not a list that grows one file at a time.

**Footprint, measured across all sixteen files:** 1631 appears in **exactly one
— 12/2018, 46 rows, ₪207,244** — and has zero rows in the other fifteen. 2018
was a municipal-election year in Israel, which is consistent with a
"preparation for elections" component paid once and gone, but that is an
observed coincidence, not a verified explanation.

After the change, 12/2018's coverage gap reads **4 codes / ₪87,136** and 1631 is
no longer in it.

**Verified how:** `pytest tests/ -q` → 34 passed; `node --check engine.js` →
clean; NON_PENSIONABLE 49/49 with no symmetric difference.

## 0bv. 607 extended through 12/2010, and that file checked

A clean 12-cell diff: `tosafot!AS31:AS42`, codes 25-36 (1.2010-12.2010), all
₪1,943.23. The table now covers **codes 1-36** and is empty from code 37 on.

**607 is an engineers-only component — measured, not assumed.** Exactly 2
carriers at ₪1,943.23 in each of the four engineers files (01/2008, 12/2008,
12/2009, 12/2010) and **zero carriers in all sixteen full-population December
files**. The same two workers pay the identical amount across three years, so
607 is flat rather than pulsing and the table describes it correctly.

**What cannot be settled yet:** where the table should end. There is no
engineers file from 2011 or later, so whether 607 continued past 12/2010 is
unanswerable from the data in hand. The next file answers it.

**12/2010 engineers run:** 1,225 workers, all דירוג 12 - 1,182 valid - **0 true
errors** - ₪0 exposure. Partition closes (24 no-base + 2 ותק קטוע + 2 base + 13
gmul + 1 תוספת 1999 + 1 דריכות + 1,182 valid). **Coverage gap 0 codes / ₪0** —
two consecutive files with none.

**Third confirmation of §23:** 669 reads **100%** here (84 of 84). 12/2008
remains the only anomaly in the whole series.

**4550 after §22's fix:** 94.9% on 1,043 carriers — improving on every file
checked (42.1% -> 95.2% -> 93.4% -> 94.9%).

**Trust gate: 11 of 26 checked.** Silenced above n=20 again include the three
most-carried components in the file — 4544 (1,201 carriers, 96.8%), 4934 (1,201,
95.7%) and 4550 (94.9%). The 0 is not a clean bill of health.

## 0bu. 607 gets a workbook column, and the 12/2009 engineers file

The user added a `tosafot!AS` column for **607 טיסה פעילה** —
`AS3 = VLOOKUP(C4,AR7:AT234,2,0)` over a pulse table. Until now 607 existed only
as a *deduction* inside 4550 and had no rule of its own. Added as `shekel`;
`component_rules.json` is now **104** rules. **The table covers ₪1,943.23 for
codes 1–24 (1.2008–12.2009) and is empty from code 25 on**, so slips from 2010
onward cannot be checked against it — continue the table if 607 is still paid,
declare it discontinued if not.

**12/2009 engineers run:** 1,243 workers, all דירוג 12 · 1,203 valid · **1 true
error** (0.08%) · ₪1,802 exposure, all overpayment. Partition closes (21 no-base
+ 1 ותק קטוע + 4 base + 13 gmul + 1 real + 1,203 valid).

**Coverage gap: 0 codes / ₪0 — the first file in the entire series with none.**

**Independent corroboration for §23:** 669 reads **98.9%** here (86 of 87),
exactly as the sweep concluded — ₪51.09 is right from 12/2009 on and 12/2008 is
the sole anomaly. This is a second, track-scoped confirmation.

**4550 after §22's fix:** 93.4% on 1,058 carriers, still under the gate.

**Trust gate: 9 of 26 checked.** Silenced above n=20: 4544 (1,221 carriers,
95.4%), 4550 93.4%, 4651 96.7%, 756 93.4%, 798 92.2%, 697 95.3%, 4624 86.8%.
The file's two most-carried components are muted again, so "1 true error" is not
a clean bill of health — same caveat as 0br.

**Maintenance:** the new column moved 74 components in `tosafot`. A sweep
compared every `tosafot!<col>` citation in the rules' prose against the
workbook's actual column and repointed **44 fields**; several had been stale
since earlier versions (681 pointed at `AV` where the column is `AZ`). These
citations are documentation only and do not affect computation, but they are
what a human uses to verify a rule against the workbook.

**Verified how:** `pytest tests/ -q` → 34 passed; `node --check engine.js` →
clean.

## 0bt. The 12/2008 engineers file — and a 669 finding I had to narrow twice

**Run:** 1,260 workers, all דירוג 12 · 1,181 valid · **14 true errors** (1.11%) ·
exposure ₪3,407. Partition closes (37 no-base + 5 two-משולב + 9 ותק קטוע + 1
base + 7 gmul + 6 תוספת 1999 + 14 real + 1,181 valid). Largest gaps: 4544 (31
gaps / ₪2,727) and 897 (10 / ₪3,919). Coverage gap 1 code / ₪3,886.

**4550 after §22's fix reads 95.2% here** on 1,055 carriers — against the 42.1%
measured pre-fix on the 01/2008 engineers file. Still under the gate, but the
correction is holding.

**Trust gate:** 11 of 25 components checked; 9 silenced for n < 20 and 5 for
match — 669 (1.2%), 4624 (84.2%), 798 (89.6%), 741 (93.1%), 4550 (95.2%).

**669 — narrowed twice, so read the final version only.** I first saw 1.2% on
engineers and took it for a track-specific tariff. Measuring the full population
killed that: it is not דירוג-dependent. I then took it for a period-varying
component needing a pulse table like 5270. The full sixteen-file sweep killed
that too. The actual result:

- `tosafot!X7:X234` is a flat ₪51.09 across all 228 codes, and **that value is
  correct in fifteen of sixteen files** — 12/2009 through 12/2023 all show 51.09
  as the modal full-time amount at 96–99%.
- **12/2008 alone** pays ₪2,596.31 to 2,875 full-timers out of 8,053 carriers,
  50× the חוקה value, with ₪1,947.28 (75%) and ₪1,298.28 (50%) alongside.

A 98% drop between 12/2008 and 12/2009 does not read as a tariff update; a
one-off arbitration settlement paid that December is the likelier story, **but
that is a hypothesis, not a measurement** — `PROGIM_FIXES` §23 states it as
such and gives the user both branches. Either way, 8,053 workers currently fail
669 in that file and only the trust gate keeps them out of the report.

Noted, unexamined: 669's carrier count collapses from 5,630 (12/2013) to 199
(12/2014), a 96% drop in one year, and stays at 200–360 after.

## 0bs. 1622 out of scope — the first batch the workbook explicitly backs

On the user's instruction. Unlike the previous twelve batches, this one is not
justified by the workbook's silence — `מאפייני רכיבי שכר` row 375 declares 1622
with **משכורת קובעת = לא** (and לא for both minimum tiers and both gross
columns). The other checks are clean too: no column in tosafot/SACHAR/
SACHAR4643, no rule of its own, referenced by no other rule.
`NON_PENSIONABLE` is now **48**, py/js element-wise equal.

**Measured effect:** 1622 was the single largest item in 12/2023's coverage
gap. Re-running that file takes it from **11 codes / ₪101,369** to **10 codes /
₪56,088** — a ₪45,281 drop, exactly 1622.

**⚠ Name mismatch, unresolved:** the workbook calls 1622 "מנהל בחירות"; the
גולמי files call it "15% ש.ממושך". Same code, two unrelated names. If the code
was repurposed, someone should confirm the `משכורת קובעת = לא` declaration
describes the *current* use and not the old one.

## 0br. Engineers track opened — and it immediately found a bug in our 4550

The user sent an 01/2008 extract that is **100% engineers** — 1,275 workers, all
דירוג 12 — to start a track-specific workstream. Result: 1,275 workers, 1,230
valid, **0 true errors**, ₪0 exposure. Partition closes (24 no-base + 7 ותק קטוע
+ 3 base + 10 gmul + 1 דריכות + 1,230 valid).

**Do not report that 0 as "engineers are paid correctly."** On this file only
**8 of 22 components are actually checked**. Eight are silenced for `n < 20`
(626, 630, 642, 728, 805, 853, 907, 4406 — the file is too small for a
population signal) and six for falling under 97%: **4550 at 42.1% on 1,084
carriers**, 4544 at 96.8% on 1,251, 4651 96.7%, 756 95.6%, 628 93.6%, 4624
92.3%. The two most-carried components in the file are both muted. **A
track-scoped file trips the trust gate far harder than a full monthly file** —
that is the standing lesson for this workstream.

**What it found: our 4550 was wrong.** 42.1% with *every* failure in the same
direction (slip below computed) reads as a bad formula, not mass underpayment.
The `4550` sheet says
`D13 = IF(K14=1, 0, MAX(D9-D11, 0, K4-D11))` — the floor term is the ministry
maximum **minus the same deductions**. We used `ministry max × job%`, never
subtracting them and scaling where the sheet does not. Fixed in `main.py` and
`engine.js`; `base_codes` also corrected from `[1, 2, 10002, 4624]` (1 and 2
were extraction debris) to `[10002, 658, 678, 4624]`.

Measured: engineers 42.1% → **94.2%**, 12/2023 54.4% → **76.8%**, 12/2018 49.0%
→ **71.8%**. The base_codes half changed nothing (658/678 are zero for these
engineers) — the whole gain is the floor term. It clears 97% nowhere, so **no
worker changed verdict**: the re-run gave the same 21 invalid and the same
98.32%. Fidelity, not new flags. `PROGIM_FIXES` §22.

**Open on this track:** the 24 no-base workers are not a pay-table gap (0 grades
missing from lookups) and are undiagnosed; `ותק מקסימלי` is blank for engineers
in `DERUG` (filled only for tracks 1, 2, 7) so no seniority ceiling is enforced;
and 4550 still has `K14` (not-entitled ministries → 0) unimplemented, plus an
unexplained `K` vs `L` column pair in its ministry table.

**Verified how:** `python3 -m pytest tests/ -q` → 34 passed; `node --check
engine.js` → clean; engineers file re-run unchanged at 21/98.32%.

## 0bq. 5270 fixed — and the fix confirms the dating a second time

The user shipped a workbook that does exactly what `PROGIM_FIXES` §21 asked.
`tosafot` CW3/CX3/CY3 went from flat literals to
`VLOOKUP($C$4,$CV$6:$DA$234,n,0)` over a new month-code pulse table, and the two
tiers the measurement had found missing — 0.66 and 0.80 — are now levels 3 and
4. The component has five levels, not three.

**Effect, measured month-aware (each slip against the band in force for its own
month):**

| file | carriers | gaps before | gaps after |
|---|---|---|---|
| 12/2013 | 86 | 86 | **2** |
| 12/2014 | 79 | 79 | **2** |
| 12/2015 | 89 | 89 | **4** |
| 12/2016 | 90 | 90 | **6** |
| 12/2017 | 83 | 83 | **4** |
| 12/2018 | 226 | 226 | **48** (₪405 total) |
| 12/2019 | 213 | 213 | **47** |
| 12/2020 | 205 | 205 | 202 ← band error |
| 12/2021 | 190 | 190 | 190 ← band error |
| 12/2022 | 180 | 180 | **42** |
| 12/2023 | 166 | 166 | **10** |

**Two independent confirmations fall out of the table itself**, from a source I
did not write: it lands exactly on `code = (year−2008)×12 + month` (61 = 1.2013,
181 = 1.2023, 228 = 12.2026), and ₪904.99 — which §21 had flagged as a *guessed*
2024 value — sits in the 1.2024–12.2024 band.

**Four defects remain, all in §21:**

1. **Circular reference across all of 2024.** Rows 199–210 hold `=+$CW$3` and
   `=+$CX$3` in levels 1 and 2 — pointing at the VLOOKUP cells that read this
   very table. `'Netunei Gimlai'!B6` is currently **204 = 12.2024**, so those two
   levels are broken in the workbook as shipped.
2. **Codes 1–60 (1.2008–12.2012) are still empty** while 164 slips live there —
   83 in 12/2011 at ₪200, 81 in 12/2012 at ₪300. They report "לא ניתן לבדוק".
3. **The 813 pulse is cut short and ₪817.88 was never paid.** The table puts 813
   at codes 133–144, 817.88 at 145–167, 835.05 from 168. But 12/2020 (code 156)
   and 12/2021 (code 168) both pay **813** — 152 and 138 full-timers — and
   12/2022 (code 180) does pay 835.05. So 813 should run through code 168 and
   835.05 should start at 169; 817.88 has no support in any slip. This alone is
   392 of the 470 remaining gaps.
4. **A ₪803 cohort with no tier.** From 12/2018 on, a stable group pays ₪803 —
   40, 39, 37, 35, 34 workers — while everyone else pays that year's level 5.
   ₪803 ≈ 2017's level 5 (803.4) and the group shrinks monotonically, which
   reads as a frozen cohort eroding through retirement. That is interpretation,
   not measurement: the data shows the group, not the reason. If frozen, it
   needs a declared tier; if not, 34–40 workers are underpaid every month.

**Rule change:** 5270 moved `reported` → `shekel`, 103 rules. Its `amounts` is
the **flat union** of all pulses, so it catches gross errors but *cannot* catch a
correct amount from the wrong era — the engine still has no month-aware check.
The per-band table is stored beside it as `amounts_by_code` for when that lands.
The gap report is month-aware in its own script, so its numbers are sound; the
engine's are weaker. This is the same architectural gap as 0bm.

**Workbook side-effects handled:** three columns were inserted in `tosafot`,
moving 22 components. Four rules cited old addresses in prose (4180, 4244, 5536,
5548); each was repointed and the new address verified to hold the expected
value. `tosafot!B4` still mislabels `C4` as "חודש פרישה" — §14's finding stands.

**Verified how:** `python3 -m pytest tests/ -q` → 34 passed; `node --check
engine.js` → clean.

## 0bp. 5270 ותק פעילות — defined in the workbook, never checked, and nothing matches

The user asked for a per-employee gap report on 5270. Building it needed a
standard value, so I opened `tosafot!CV` — and it is there in full:

```
CV2 = IF(MISRAD!W2=1, IF('Netunei Gimlai'!G28=TRUE, CV3,
                      IF(G29=TRUE, CW3, IF(G30=TRUE, CX3, 0))), 0)
```

`CV3 = 181` (רמה 1), `CW3 = 362` (רמה 2, exactly 2×181), `CX3 = 904.99`
(רמה 3 — 5×181 is 905, so the workbook is one agora short). All three are
declared fixed across all 228 month codes (`CV6:CX6 = =+$CV$3`).

The engine's rule was nevertheless `reported` — accepted as-is, never
validated, carrying the same wrong auto-note about an unresolvable VLOOKUP.
**Seventh component found this way**, after 738, 737, 5251, 5253, 5340, 1063.

**Measured against those three levels, essentially nothing matches:** 12/2011
1 of 83; 12/2012 0 of 81; 12/2013 0 of 86; 12/2014 0 of 79; 12/2015 0 of 89;
12/2016 0 of 90; 12/2017 0 of 83; 12/2018 0 of 226. The component is absent
before 12/2011. **The full 1,771-slip measurement then explained it, and the
structure in the workbook turns out to be half right:**

- The **tier ratios are correct** — 181/904.99 = 0.20 and 362/904.99 = 0.40, and
  ratios of 0.2 / 0.4 / 1.0 do recur in every file.
- The **base is not constant**. Measured on full-timers: ₪200 (12/2011) → ₪300
  → ₪640 → ₪815 → ₪813 → ₪805 → ₪803 → ₪806.60 → ₪813 (12/2019–21) → ₪835.05
  (12/2022) → ₪878.97 (12/2023). **₪904.99 appears in no file at all**; the
  trend suggests it is a 2024+ value, but that is a guess, not a measurement.
- **Two tiers are missing from the workbook**: 0.80 (₪646.30 of ₪806.60, ₪704.26
  of ₪878.97 — and in 12/2018 it is the *largest* group, 103 workers) and 0.66
  (₪533 of ₪803, ₪583.06 of ₪878.97). The חוקה declares three levels; five are
  paid.
- From 12/2018 on, ₪803 and ₪813 run **side by side** (35–40 workers vs
  139–155). Frozen cohort or payment error — undetermined.

All of it is written up as `PROGIM_FIXES` §21 with the measured table.

Do not convert 5270 to a `shekel` rule on these three values. At a ~0% match it
would be silenced by the trust gate anyway, and if it ever passed it would flag
every carrier. What it needs first is a pulse table, or confirmation from the
user that 181/362/904.99 are era-specific.

**Also unresolved:** the level (1/2/3) comes from three manually-ticked flags in
`Netunei Gimlai`, and the גולמי file carries no field saying which level a
worker is on. The report infers the level from the amount paid, which cannot
catch a worker placed on the wrong level — stated in §21 as a gap to close.

## 0bo. Seventh neutralization column — 697, and it moves the headline more than any other

The user asked for a "שגויי תוספת מיוחדת" bucket for 697, placed immediately
after "שגויי תוספת 1999". Built in all four places (`meyuhedet` after `h1999`
in the `err_cat` chain, the dashboard order, both front-ends). Dashboard is now
**27 columns**; trailing indices shifted again (אמיתיים 24→25, % 25→26 so the CF
range moved Y→Z, תקין 26→27, front-end red bar X→Y).

This is the **earliest slot** any component bucket has been given — position 8
of 19 — so it pulls from many later buckets. Measured on four files first:

| file | catches | ₪ | taken from | true errors before → after |
|---|---|---|---|---|
| 12/2023 | 8 | ₪3,050 | 7 real, 1 גמול מנהל | **8 → 1** |
| 12/2022 | 12 | ₪1,703 | 12 real | **24 → 12** |
| 12/2016 | 8 | ₪2,400 | 7 real, 1 גמול מנהל | **18 → 11** |
| 12/2020 | 1 | ₪105 | 1 real | 15 → 14 |

**It swallows almost nothing** — unlike the 5340 and 5524 buckets. Of the 29
workers it takes across the four files, only **2** carry a second failing code,
both of them 4983 (גמול מינהל), one in 12/2023 and one in 12/2016. Separately,
697 keeps failing for workers claimed *earlier* in the chain (2 / 1 / 6 in those
files, under גמול and תוספת 1999); the bucket never sees them.

**The open question, and it is the important one.** 697's rule is sourced —
7.5% in the חוקה — so the workers this bucket takes are genuinely failing a
validated check. The bucket does not prove them innocent; it relabels them from
"true error" to "known cause". **If 697 really is being mispaid, this bucket
hides ₪7,258 across those four files alone.** Nobody has checked whether 697's
deviations are retro multiples (neutralizing is right) or arbitrary amounts
(neutralizing hides money). That check is not done and should be.

## 0bn. Sixth neutralization column — 1063, and it reads zero in every file

The user asked for a "שגויי מנמ"ש 2022" bucket for 1063, placed immediately
after "שגויי בית חולים מאוחדת". Built in all four places (`mnmsh22` in the
`err_cat` chain right after `bmeuhedet`, the dashboard order, and both
front-ends). Dashboard is now **26 columns**; trailing indices shifted again
(אמיתיים 23→24, % 24→25 so the CF range moved X→Y, תקין 25→26, and the
front-end's own red data bar W→X). The gap table's anchor is derived from
`len(labels)`, so it followed automatically this time.

**Measured before shipping: at that position the bucket catches 0 workers** — in
12/2023 and in 12/2022, the only two files where 1063 exists. True errors are
unchanged (8 and 24).

It swallows nothing, but it also shows nothing, because all of 1063's failures
are already claimed by buckets **earlier** in the chain:

| claimed today by | 12/2023 | 12/2022 |
|---|---|---|
| תוספת 1999 | 98 | 77 |
| בית חולים מאוחדת | 15 | 16 |
| גמול השתלמות | 14 | 15 |
| גמול מנהל | 5 | 1 |
| שכר בסיס | 1 | 4 |
| **total 1063 failures** | **133** | **113** |

**Do not read the 0 as "1063 is clean."** The same dashboard's gap table lists
1063 at 133 gaps / ₪29,619 for 12/2023. This is the 738 trap again — a zero in a
neutralization column means "nobody landed here", never "no errors".

**To make the column show a number** it has to move ahead of `h1999` in the
chain. Measured: it would then take 118 workers in 12/2023, 98 of them out of
the תוספת 1999 column, which would nearly empty it. Not done — that is the
user's call.

## 0bm. ‼ The pulse-table dating is solved — and my earlier "refutation" was wrong

**Read this before touching any `shekel` rule with an `amounts` list.**

Twice this session I claimed the code→date mapping could not be derived, and
wrote it into `PROGIM_FIXES` §14 as a refutation with a proof. **The proof was
built on a mislabelled cell.** Every pulse `VLOOKUP` reads `tosafot!C4`, and
`tosafot!C4 = 'Netunei Gimlai'!$B$6`. But in `Netunei Gimlai`:

- `B5` is labelled **חודש פרישה** (= 1)
- **`B6`** is labelled **חודש לחישוב רטרו תלוש הגמלה** (= 168)

`tosafot!B4` labels `C4` "חודש פרישה" — the name of a *different cell*. I read
the label, concluded the tables were indexed by retirement cohort, and built a
refutation on it instead of opening `C4`. Same failure mode as the 738 mistake:
**open the cell, do not trust the label next to it.**

**The mapping is in the workbook, explicit and contiguous** — `MANMASH 2022!A5:B232`:
code 1 = 1.2008, 169 = 1.2022, 181 = 1.2023, 228 = 12.2026. So

> **code = (year − 2008) × 12 + month**

`Netunei Gimlai` confirms itself: `B6=168` → 12.2021, `B7=228` → 12.2026.

**Verified against 12 independent measurements** — 805 in 12/2013, 12/2016,
12/2018, 12/2019, 12/2023; 657's six bands 12/2018→12/2023; 1063 in 12/2022 and
12/2023. Every one predicted the amount actually paid.

**One point disagrees, and it is a table error, not a model error.** 12/2009 is
code 24; 805's table opens 100.59 there but 89 carriers pay 95.80, while
12/2010 (code 36) does pay 100.59. The hand-filled band boundary is off by one
row: 95.80 should cover codes 1–24, 100.59 codes 25–36. One cell in `tosafot!BC`.

**What is NOT done:** the engine still accepts *any* pulse in a rule's `amounts`
list. With this mapping it could check only the band in force for the slip's
month, which would tighten every `shekel` rule with a pulse table — 805, 808,
657, 737, 5251, 5253, 1063. That is the highest-value open item on this branch.
It needs a payslip-month input threaded into `check_worker_components`, which
today only has `job_pct`, `ministry_code`, `darga_label`, `droog`.

## 0bl. 1063 ת. מנמ"ש 2022 — the largest unchecked component, now checked

The user said 1063 is a variable amount taken from the Progim. Checked, and
they are right: `MANMASH 2022!E1 = INDEX(D5:G232, B1, B2)` — row by month code,
column by דירוג — with a fully populated table (codes 1–168 = 0; 169–180 =
450/450/200/200; 181–228 = 720/420/320/320).

It had been `reported`, i.e. **accepted as-is and never validated** — **₪10.13M
across 19,009 rows** in the sixteen files, the single biggest line in the "not
checked" list. Converted to `shekel` with `amounts [200, 320, 420, 450, 720]`;
`component_rules.json` is now **103** rules.

**Verified before converting:** 6,848 full-timers pay exactly 450 in 12/2022 and
6,849 pay exactly 720 in 12/2023 — the workbook's values for those month codes.
After converting: **98.6% match in 12/2023, 98.8% in 12/2022**, comfortably over
the trust gate, on 9,439 and 9,380 carriers.

**Effect on the 16-file unified report, measured before and after:** the
"מוזן מהקובץ" line drops from 15 codes / ₪24,469,420 to 14 codes / ₪14,335,789
— exactly 1063's ₪10,133,631 — while true errors stay at 231 and valid stays at
304,119. All 133 of 1063's 12/2023 mismatches land on workers already invalid
for another reason (the same partial-month workers 5524 catches), so coverage
grew without adding a single new flag. That is the outcome to want.

This is the **sixth** component that was properly defined in the workbook yet
never validated (after 738, 737, 5251, 5253, 5340) and by far the most
expensive. The standing conclusion holds: **every remaining `reported` rule is
suspect until someone opens its sheet by hand.** Its residual deviations are the
same day-proration pattern as 5524 — exact multiples of ₪720/30 = ₪24.

## 0bk. Fifth neutralization column — 5524, and what it costs

The user asked for a bucket for **5524 תוספת שקלית 2023**, placed immediately
after "שגויי תוספת בית משפט". Built in all four places: the `err_cat` chain in
`tools/unified_report.py` (`shk2023`, right after `bmish`), the dashboard column
order, and the mirrored chain in `index.html` and `salary_frontend.html`.
Adding one column shifted the dashboard's trailing indices — אמיתיים 22→23,
% 23→24 (`rng` moved `W`→`X`), תקין 24→25 — and both formatting loops were
updated to match. The dashboard is now **25 columns**.

**Why it is justified.** 5524's tariff is right: 14,623 of 14,816 full-timers
pay exactly the חוקה's ₪400. Its 279 gaps are 77 retro reversals plus 131 exact
multiples of ₪400/30 — day proration the workbook never defines (`PROGIM_FIXES`
§19). None of them is a wrong amount.

**‼ What it costs — measured before shipping, on 12/2023:**

| | before | after |
|---|---|---|
| true errors | 40 | **8** |
| true-error exposure | ₪10,967 | ₪1,092 |

The bucket takes **32 workers / ₪9,875**. Two of those 32 carry a second
failing code, and that is the damage:

- **1096 (תוס מנמ"ש מטה 2022) had 2 workers in the true-error list; both are
  swallowed. It now shows zero.**
- 736 (תוספת מנהל) goes 3 → 1.

After the change the entire true-error list for 12/2023 is 697 (7 workers) and
736 (1). Anyone investigating 736 or 1096 must filter the per-employee sheet on
`neutral_he = "תוספת שקלית 2023"`, not read the אמיתיים column.

**Blast radius:** 5524 exists **only in 12/2023** — 17,922 carriers there, 0 in
each of the other fifteen files (measured directly off the raw rows). The column
changes exactly one row of the unified report.

## 0bj. The 12/2023 file — the trust gate is the story, not the error count

**Run:** `18,289` workers · `17,380` valid · `40` true errors (`0.22%`) ·
exposure `₪10,967`. Partition verified — the seventeen buckets plus `תקין`
sum to exactly `18,289`.

**The workbook update that came with it.** The user shipped a workbook adding
two 657 bands (`181–192 = 907.76`, `193–204 = 934.63`) — a 24-cell diff, all in
`tosafot!AV`. Installed; `component_rules.json` 657 now carries six amounts.
Verified: **389 of 446 carriers pay exactly ₪907.76.**

**Three findings, all measured on this file:**

1. **805 is 100% right and was silenced anyway.** It sits at 93.3%, below
   `TRUST_MIN_MATCH`, so it was not checked at all. Every one of its 7 failures
   is a **negative** amount (a retro reversal); all 98 positive rows are
   correct. Written up as `PROGIM_FIXES` §20 — the workbook has no declaration
   that a negative amount is a reversal rather than a payment.
2. **738 slid under the gate.** 97.0% (12/2021) → 96.4% (12/2022) → 94.8%
   (12/2023). Its neutralization column reads **0 in 12/2023 while 2,007
   workers carry the code** — the rule is muted, not clean. **A zero in a
   neutralization column is not evidence of correctness.** This is the exact
   hazard the gate was flagged for when it was introduced.
3. **5524 is the biggest gap in the file and none of it is a wrong tariff.**
   17,641 carriers, 279 gaps, ₪73,146, and the source of **32 of the 40 true
   errors**. 14,623 of 14,816 full-timers pay exactly ₪400 — the חוקה value.
   Of the 279: 77 negative (retro), **131 exact multiples of ₪400/30**, 71
   combinations. It is day-proration, which the workbook never defines for a
   fixed shekel component. `PROGIM_FIXES` §19.

So the honest reading of this file is **~8 real errors, not 40**. Say that
before anyone quotes the headline.

**657 still does not pass.** The two new bands lifted it 89.2% → 92.2%. The
blocker is unchanged: the missing **60.02%** tier, now measured across **six
consecutive years** (₪500.00 / ₪504.00 / ₪507.02 / ₪507.02 / ₪517.60 / ₪544.83),
and in 12/2023 **all 21 carriers of ₪544.83 are full-timers** — so it is a
declared partial entitlement, not a job-percentage artifact. §18 has the table.

**Verified how:** `python3 -m pytest tests/ -q` → 34 passed; `node --check
engine.js` → clean; `NON_PENSIONABLE` py/js element-wise equal at 47/47; the two
front-ends' embedded scripts hash identically (`85f0ba73…`).

## 0bi. 4438 ימי אבל out of scope — and the family argument is now overwhelming

Passes all three checks **cleanly**: not in `component_rules.json`, no column in
`tosafot`, `SACHAR` or `SACHAR4643`, and **no entry in `מאפייני רכיבי שכר` at
all**, so no pensionability declaration either way. `NON_PENSIONABLE` is now
**47 codes**, Python and JS in sync. Footprint: one row, ₪3.95, in 12/2022 only.

**The "ימי X" absence family now occupies six codes** — 4436 (חופשה), 4437
(מחלה), 4438 (אבל), 5271 (חג), 5272 (מחלה), 5273 (בחירה) — added across **five
separate batches over two days**, plus 4123 (100% ש.מחלה) making "sick days"
alone span three codes.

That is the strongest form of §15's argument. After **47 codes in 12 batches**,
the list will keep growing one code per file for as long as the workbook has no
declared `פנסיוני` column. The vehicle already exists — the 295-row table in
`sminimum` — and needs exactly one more column. **Lead with this whenever the
user asks what to fix; it is the only change that stops the list growing.**

## 0bh. 657's table filled — and the 12/2022 file

**The workbook update (283 cells) closes 657, partially.** `AV3` moved from the
literal 0 to **`VLOOKUP(C4,AR7:AV234,5,0)`** and the table was filled **exactly
with the values reported from the slips**: 121-132 = 833.33, 133-144 = 839.66,
145-168 = 844.70, 169-180 = 862.40. The rule is converted to `shekel`.

**Result: from not checked at all to 89-92%** — 423/466, 422/459, 372/417 and
391/428 across 12/2018-12/2021.

**‼ It still sits below the 97% gate and is silenced**, and nearly the whole gap
is **the second tier I flagged when reclassifying it**: ₪500.00 / ₪504.00 /
₪507.02, exactly 60% of the main amount, 32-35 carriers a month. **Adding the 60%
step is the difference between 90% and 100%** and is what would push 657 over the
gate into actually being checked. §18 carries the instruction.

**Structural change to watch:** a column was inserted in `MISRAD` (code 5268,
"ליווי אח"מים"), shifting every eligibility reference — 88 cells in `tosafot`,
184 in `MISRAD`. **I verified §11 survived:** `BC2` and `BR2` still point at
`BC1`/`BR1` and 738's `BZ3` is still a `VLOOKUP`. This is exactly the hazard
§11's prevention rule exists for — moving columns breaks hardcoded indices — and
nothing broke precisely because they now reference index cells.

**The 12/2022 file:** **18,775 workers · 97.53% · 24 true errors · ₪11,261**;
partition closes. Leading codes 697 (12, ₪1,703), **5253 (4, ₪5,283)**, 736 (3),
737 (2, ₪722), 805 (1, ₪1,164). Buckets: בית משפט 21, בית חולים מאוחדת 16,
אחוז יום 0. Coverage gap **9 codes / ₪19,669**, led by 4221 (₪9,069) and 4220
(₪3,216) — **the first time those two appear in a December file**; previously
they were only in `golmi.xlsx`.

## 0bg. 4538 out of scope against the workbook, and 657 reclassified

**4538 — the second entry that contradicts the Progim.** `מאפייני רכיבי שכר`
declares 4538 "שבת 100%" with **משכורת קובעת = כן**, and the גולמי label is
**"שבת%100-פנס"** — the `-פנס` suffix says pensionable too. Added on the user's
instruction, as with 4140, and recorded alongside it in §17. **Footprint is
negligible: 1 row / ₪281.44 across 15 files** (12/2018 only), so the practical
effect is nil while the contradiction is identical. `NON_PENSIONABLE` is now
**46 codes**, two of which contradict the workbook.

Note the routine that catches these: check `מאפייני רכיבי שכר` for
`משכורת קובעת` before adding any code. It cleared 4192/1152/1153 and flagged
4140 and 4538.

**657 תוספת מעונות reclassified to `varies`,** as instructed — and the reason it
matters is that **its table is completely empty**: `tosafot!AV3` holds 0 and
`AV7:AV234` is blank in all 228 rows, while eligibility is defined and points at
that non-existent amount.

Measured from the slips, it genuinely varies, and there are **two tiers**:

| month | main tier | carriers | second tier | carriers |
|---|---|---|---|---|
| 12/2018 | **₪833.33** | 411 | ₪500.00 | 35 |
| 12/2019 | **₪839.66** | 409 | ₪504.00 | 34 |
| 12/2020 | **₪844.70** | 363 | ₪507.02 | 32 |
| 12/2021 | **₪844.70** | 376 | ₪507.02 | 32 |

The second tier is **exactly 60% of the first** in every month, on values already
normalised to full-time, so it is a defined entitlement rather than a job-fraction
artefact.

**Deliberately not done:** these numbers were **not** turned into a validation
rule. They come from payslips with no Progim source, and `CLAUDE.md` forbids
deriving a rule from the data — the same trap as the pulse-table dating. 657 stays
`reported`, so **417-466 slips a month remain unchecked**, and the numbers are
filed in `PROGIM_FIXES.md` §18 as the evidence for filling `AV7:AV234`. Fill the
table and the component becomes checkable; do not shortcut it in the engine.

## 0bf. 4192, 1152, 1153, 651 out of scope — three backed by the workbook

On the user's instruction, off the 12/2020 and 12/2021 coverage lists. All four
pass the checks, and **three are explicitly supported by the workbook** — the
opposite of the 4140 case:

| code | workbook name | `משכורת קובעת` |
|---|---|---|
| **4192** | ביטוח מקיף - ידני | **לא** ✓ |
| **1152** | ש.נ. 125% | **לא** ✓ |
| **1153** | ש.נ. 150% | **לא** ✓ |
| 651 | not listed | no declaration |

None of the four has a column in `tosafot`, `SACHAR` or `SACHAR4643`, and none
appears in `component_rules.json`. `NON_PENSIONABLE` is now **45 codes**; Python
and JS in sync, 34 tests pass.

**Checking `מאפייני רכיבי שכר` is now part of the routine** for every scope
request — it is what caught the 4140 contradiction and what confirms these three.
Do it before adding any code.

**Note on 4192:** the workbook calls it **"ביטוח מקיף - ידני"** while the גולמי
shows **"ימים סגורים"**. Two different names for one code, possibly repurposed
over the years. It does not change the decision but is worth knowing.

Coverage gaps: 12/2020 **11 codes / ₪619,292 → 7 / ₪494,107**; 12/2021 **14 /
₪41,199 → 10 / ₪21,122**. Partitions close, true errors unchanged at 15 and 11.
**What is left in 12/2020 is essentially one code** — 633 ת.מפ. בזק ב at
₪478,579, 97% of the remainder.

## 0be. A neutralization column for 738 — the clean kind

Requested: a **"שגויי תוספת אחוז יום"** column immediately after "שגויי מקצועית
מיסים". Delivered in all three places, HTML files byte-identical. The dashboard
is now **24 columns**; indices, the `V`/`W` formatting ranges, the banner merge
and the side table at `Y` all shifted. Partitions close.

**Measured before building: 26 workers / ₪1,132** — 14 in 12/2018, 12 in 12/2021,
zero in 12/2019 and 12/2020. **It swallows nothing**: every one of the 26 carries
738 alone, like the 4140 bucket and unlike 5340. After it, 12/2018 goes 30 → 16
true errors and 12/2021 goes 23 → 11.

**All four buckets added today, side by side:**

| column | code | absorbs | swallows? |
|---|---|---|---|
| תוספת בית משפט | 875 | 64 | no (each carried 875 alone) |
| משכ. בסיסית | 4140 | 8 | **no** |
| בית חולים מאוחדת | 5340 | 70 | **yes — 27 workers with 626/728/959** |
| תוספת אחוז יום | 738 | 26 | **no** |

Three of four are clean; **5340 is the only one that swallows**, and the offer to
move it later in the chain is still open.

**Context that matters when reading any of these:** 738 and 5340 only became
checkable today, and their two columns neutralize most of what those conversions
surfaced. That is a legitimate choice, but **those components are not "clean" —
they are neutralized.** Anyone reading the dashboard must look at the bucket
columns, not only at "שגיאות אמת". This is now true of four columns, so it is
worth stating in any summary sent to the user.

## 0bd. The 12/2021 file — and a `--no-per-employee` flag

Fifteenth file: **December 2021**, **19,048 workers**. **97.50% · 23 true errors ·
₪3,488**; partition closes. Docs only apart from the flag below.

**First file where both new buckets fire together:** בית חולים מאוחדת = **24**
and תוספת בית משפט = **7**, so 31 workers leave the true-error count in one file.

**738 is the largest error source at 52%** — 12 of 23 true errors, ₪669. That is
the component I reported yesterday as "₪1.2M of coverage gap in the workbook"
when it was in fact fully defined and merely unreachable by our extractor. Since
it became checkable it produces most of this file's findings. Then 736 (5,
₪2,098), 756 (2), 805 (2, ₪547), 858 (1).

Coverage gap **14 codes / ₪41,199**: 651 (₪19,815 over 141 rows), 634 (₪6,971),
633 (₪4,875), 4536 (₪4,172), 4951 (₪2,500). **633 fell from ₪478k in 12/2020 to
₪4,875 here**, its population dropping from 249 rows to 14 — a reminder that the
expensive coverage codes are **not stable month to month**, so no single file
should drive the priority list. 4536 remains the open question raised on 4.8 (it
is 4537's twin, and 4537 is already out of scope).

**New tool flag: `--no-per-employee`.** The 14-file unified report came to
**31.5 MB** and could not be delivered (30 MB limit); the `פר עובד` sheet alone
was 288,641 rows and ~307 MB of XML. The flag skips that sheet and the same run
produces **2 MB** with dashboard, coverage, classification, work queue,
status-changes, by-cause, ministries and month-over-month all intact. Use it for
any multi-year run.

## 0bc. New unified report over 14 files, with everything applied

**288,640 workers · 272,059 valid · 212 true errors (0.0734%) · ₪64,247
exposure** (₪40,299 under, ₪23,948 over). **All 15 partitions close.** Written to
`דוח_מאוחד_14_קבצים_05.08.2026.xlsx`.

Per file true errors: 01/2008 10, 12/2008 15, 12/2009 12, 12/2010 11, 12/2011 11,
12/2012 15, 12/2013 11, 12/2014 17, 12/2015 17, 12/2016 18, 12/2017 19, 12/2018
30, 12/2019 11, 12/2020 15. Bucket totals across the series: **4140 → 8, 5340 →
70, 875 → 64**.

**The components reclassified today now lead the error list.** By count: 697 (46),
**5253 (38)**, 736 (35), 756 (17), 4651 (15), **738 (14)**. By exposure: 736
(₪15,276), **5253 (₪11,831)**, 4651 (₪7,832), 756 (₪7,199). 5253 is second on
both lists and **was not checked at all before this morning**; 738 is new to the
list too. That is the day's work showing up as findings.

**Coverage gap: 29 codes / ₪1,201,165, down from ₪1,874,571.** 738 alone removed
₪1.2M by becoming a checked component, while 12/2018 and 12/2020 contributed 633
(₪478,579), 1622 (₪261,436), 1631 (₪207,244), 4192 (₪115,412) and 1623 (₪77,082).
**Four codes are ₪1.06M of the ₪1.2M — 88%** — and remain the highest-return fix
list.

## 0bb. A neutralization column for 5340 — and this one swallows

The user asked for a **"שגויי בית חולים מאוחדת"** column immediately after
"שגויי תוספת בית חולים". Delivered in all three places, HTML files
byte-identical, dashboard now **23 columns** with indices, the `U`/`V` formatting
ranges, the banner merge and the side table at `X` all shifted. Partitions close.

**Measured before building: 64 workers / ₪18,424** — 17 in 12/2014, 16 in
12/2016, 14 in 12/2018, 16 in 12/2019, 1 in 12/2020.

**‼ Unlike the 4140 bucket, this one swallows other components' errors.** Of the
64, **27 carry another failing code**: **626 (15), 728 (8), 959 (2), 736 (1),
5216 (1)**. Those errors leave the headline not because they were neutralized on
their own merits but because 5340 precedes them in the chain. 626 appears
consistently in the true-error list across the whole series, and **15 of its
cases are now hidden**.

**What would reduce it:** move 5340 later in the chain, after 626 and 728, so it
only catches workers carrying 5340 alone. Offered to the user; not done
unilaterally.

**Context worth keeping:** 5340 only became checkable today (`reported` →
`shekel`), and this bucket cancels most of what that conversion surfaced — 64 of
roughly 70 errors it added. A legitimate choice, but the two changes should be
read together, not separately.

## 0ba. ⚠ 4140 declared out of scope, against the workbook's own flag

On the user's instruction, and **contradicting the Progim** — the only entry on
the 41-code list that does. Recorded separately as `PROGIM_FIXES.md` §17.

`מאפייני רכיבי שכר` declares 4140 "משכורת בסיסית שעתיים" with **משכורת קובעת =
כן**, i.e. **pensionable**. I put that flag in front of the user before changing
anything and asked whether to proceed, skip, or fix the workbook first; the
answer was to add it anyway. That is their call and it is done — but it must not
be quietly inherited as fact.

**Consequences, on the record:**
- **42 rows / ₪90,200** across 13 files leave the coverage gap **and every
  check**. 4140 had been the most persistent coverage-gap item, in eight files.
- The report's `סיווג סמלי שכר` sheet now labels 4140 **"מחוץ לתחולת ה-Progim —
  רכיב שאינו פנסיוני (תקין)"**, which is **the opposite** of what the workbook
  says. A future reader will assume the workbook agrees. **It does not.**
- The "שגויי משכ. בסיסית 4140" neutralization column **still works** —
  `NON_PENSIONABLE` is applied only in `tools/unified_report.py`'s reporting
  layer and never filters components off the slip. Verified after the change:
  the column still catches 1, 1 and 2 workers in 12/2018-12/2020.

**Resolve it one way or the other:** either set `משכורת קובעת = לא` in the
workbook so code and product agree, or drop 4140 from the list and give it a
formula as was done for 738. Leaving both as they are means the product and the
software state opposite things about the same code.

## 0az. 5340 — a fixed amount that was never checked at all

The user stated 5340 is a fixed amount and that this is how the workbook defines
it. Verified: **`tosafot!AP3` = 480.1, a plain literal**, and its retirement-month
table is filled 228/228 with that single value.

**Our rule had it as `reported`** — accepted as reported and **never validated** —
carrying an auto-generated note claiming the extraction "could not resolve a
VLOOKUP / eligibility condition chain". There is no VLOOKUP and no chain; there
is a number. Corrected to `shekel` with amount 480.1.

**Verification:** 480.10 full-time in every file where it appears, from 12/2014
onward — 98.5% of 7,936 carriers in 12/2014, 97.8% of 7,902 in 12/2016, 98.4% of
9,512 in 12/2018, 98.7% of 9,504 in 12/2019 and 98.7% of 9,474 in 12/2020.
Trusted in all five. **Between 7,900 and 9,500 slips a month passed unchecked
until now.**

**The effect is large and it is the point.** True errors: 12/2014 **14 → 34**
(₪1,090 → ₪5,691), 12/2016 **20 → 34** (₪9,187 → ₪12,416), 12/2018 **33 → 44**
(₪3,004 → ₪6,683), 12/2019 **20 → 27** (₪3,377 → ₪9,289), 12/2020 unchanged at 16.
**5340 is now the single largest error source** in the two files examined in
detail: 17 workers / ₪4,898 in 12/2014 (50% of true errors) and 16 / ₪6,006 in
12/2019 (59%). Not a regression — a component with ~10,000 monthly carriers moved
from "accepted as-is" to "checked at 98%", and the non-matching remainder
surfaced. Report it that way.

**The pattern, now five deep.** 738, 737, 5251, 5253 and 5340 were all properly
defined in the workbook and all went unvalidated here. **Three of them (5251,
5253, 5340) carried the same wrong auto-note about a failed extraction.**
**Next step worth taking: audit every remaining `reported` rule** — each one is a
population passing without a check, and today suggests several are misclassified
rather than genuinely unresolvable.

## 0ay. The 12/2020 file — the conversions pay off immediately

Fourteenth file: **December 2020**, **19,542 workers**. **96.71% · 16 true
errors · ₪6,159**; partition closes. Docs only.

**Yesterday's conversions validate and already find money.** 737 is 97.2%
trusted with modal full-time 364.00 against a table step of 364; 5251 is 98.5%
at 257.50; 5253 is 97.3% at 490.80 — all exact. And **737 (4 workers, ₪1,603)
and 5253 (4, ₪1,603) are now 8 of the file's 16 true errors**, on components that
were accepted unchecked until yesterday. That is what the reclassification was
for.

Worth noting: 737, 5251 and 5253 show **the same table steps in 12/2020 as in
12/2019** — the cohort did not advance. More evidence the tables are keyed on
**retirement month**, not payslip month, consistent with §14 and with the dating
model that was refuted in 0as.

**5402's fifth anchor — the ramp has stopped.** 0.90375 → **₪303.66**, against
₪301.85 in 12/2019: a growth factor of **×1.006** after 1.536, 1.539 and 1.909.
The component climbed and then plateaued at ~₪303, which is 90.4% of the ₪336 the
workbook knows — strengthening the reading that ₪336 is the mature value. §7 now
has five measured rows.

**Coverage gap: 12 codes / ₪626,202, with two expensive newcomers.** **633
ת.מפ. בזק ב at ₪478,579 over 249 rows** and **4192 ימים סגורים at ₪115,412 over
195 rows**, then 890 (₪11,429), 651 (₪9,364) and 4140 (₪6,911). 633 had appeared
in the union list at just ₪59.68 over two rows; here it is ₪478k.

**This time I checked before claiming.** After the 738 mistake I opened the
`tosafot` code row and the `SACHAR`/`SACHAR4643` component rows for all twelve
codes: **none has a `tosafot` column and none has a component column in either
SACHAR sheet.** These are genuine coverage gaps, not extractor misses. Do the
same check before reporting any future gap.

Other: 805 is 97.1% trusted at 116.41; 738 slipped to 95.8% and is silenced; 875
is 96.9% and silenced, so its bucket is empty — 3 of 14 files. **דריכות errors
hit 112**, the highest measured, and גמול 174. Calibration silenced 27 of 51
rules, ₪2,144,127, led by 4550 at ₪1.28M (50.2%, as always) and 5402 at ₪636k.

## 0ax. 737, 5251, 5253: fixed amounts were actually period tables

Third 05.08 workbook, installed. The user flagged that several components marked
as fixed amounts are really period-varying, and the workbook now replaces each
literal with a `VLOOKUP` over a month-code table. Rules updated to match.

| code | name | was | now |
|---|---|---|---|
| **737** | הטמעת פריון | literal 405.18 | **8 pulses** 121.3-418.3 (codes 109-228) |
| **5251** | ת. מבקר חשב' | literal 286.63 | **14 pulses** 250-303.73 (codes 52-228) |
| **5253** | תוספת שכר מיסים | `=+CM6` → 546.33 | **14 pulses** 475-578.93 (codes 52-228) |

**5251 and 5253 were typed `reported`** — accepted as-is and **never validated**.
Both are now `shekel` and checked. 5253 alone is ~2,300 slips a month that went
unexamined until now.

**The tables are exact.** The modal full-time value each month lands precisely on
the table step, five months running for each component: 5253 gives
491/486/485/487/490.8 against table 491/486/485/487/490.8; 5251 gives
258/255/254/255.5/257.5 matching; 737 gives 242.6 and 364 in 12/2018-12/2019
matching. After the update all are trusted — 737 at 99%, 5251 at 99-100%, 5253
at 99%.

**Also in this workbook: 738's base shrank.** `SACHAR!AY11` dropped **600 (תוספת
בית חולים) and 626 (ס. פסיכיאטריה)**, so the rule's base goes from 18 codes to
16. 738 still validates at 97%.

**1062 added per the workbook, with no effect.** Column CM is tagged "1062 /
5253", so 1062 joins that rule's codes. It appears in **none of the 13 sample
files**, so the addition is faithful to the workbook and changes nothing.

Effects: 12/2015 true errors 13 → **20**, 12/2016 19 → **20**, 12/2019 19 → **20**;
12/2017 and 12/2018 unchanged at 19 and 33. Coverage gaps 12/2015 3/₪6,883,
12/2016 3/₪10,365, 12/2017 3/₪3,880, 12/2018 8/₪582,406, 12/2019 4/₪26,654. All
partitions close. **The small rise in true errors is the desired outcome** —
components that were previously waved through are now checked.

**The pattern of the day, worth carrying forward:** 738, 737, 5251 and 5253 all
looked "missing" or "fixed" and all four were **fully defined in the workbook**.
They failed to reach the engine only because `tosafot` row 3 held a literal or a
formula instead of pointing at a table. Now that all four use `VLOOKUP`, the
structure is uniform — which is exactly §11's prevention rule. **When a component
looks undefined, open its `tosafot` column before saying so.**

## 0aw. ‼ 738: the workbook was right and I was wrong — rule added

**Retracting 0av entirely.** I reported that 738 has no formula in the workbook
and presented ₪1.2M as a product coverage gap. The user pointed me at
`tosafot!BZ` and the component is **fully defined there**:

```
tosafot!BZ3  rate, VLOOKUP(C4,BV7:BZ234,5,0)   0.94% / 2.44% / 3.94% by month code
tosafot!BZ2  eligibility: MISRAD!I2=1 AND 'Netunei Gimlai'!G11=TRUE
SACHAR!AY11  = (AA11+DB11+AC11+AD11+AE11+AF11+AR11+AZ11+BM11+CB11+CE11
                +DG11+CZ11+DH11+DK11+DA11+DJ11) * AY7      — a 17-component base
```

**How I got it wrong:** my sweep *did* find 738 in `tosafot` — it printed the
sheet — but I rendered the row context badly, read it as incidental, and never
opened the column. Detection worked; interpretation failed. Open the column
before concluding a component is undefined.

**The real defect was ours.** `tools/extract_rules.py` reads the rate from
`tosafot` row 3 as a literal; that cell held a conditional formula resolving to
0 in an unpopulated workbook, `valid_rate` rejected it, no rule was produced,
and 738 was classified not-computable. **₪1.2M was reported as a Progim gap
while the Progim was correct.**

**Verification against the workbook's own base and rates:** 12/2018 — median
ratio **2.4400%**, **97.2% of 2,565 carriers** exactly on 2.44%; 12/2019 —
median **3.9400%**, **96.3% of 2,471** exactly on 3.94%. Quartiles flat.
Eligibility matches 100%: all 5,041 rows are מס הכנסה and מכס ומע"מ. The "two
conflicting rates" I reported in 0av are also withdrawn — 0.94% and 3.94% are
two steps of one schedule.

**Rule added by hand** to `component_rules.json` (now **103 rules**): three
rates, 18 base codes. Effect: 12/2018 coverage gap **₪1,059,174 → ₪582,406**
with true errors **19 → 33**; 12/2019 **₪756,489 → ₪26,654**, true errors
unchanged at 19. 738 now validates at 97.4% (trusted) and 96.8% (just under the
gate). The rise to 33 is checking working, not a regression — say it that way.

**The corrected workbook (second 05.08 upload, 57 cells):** `BZ3` moves from a
hardcoded `IF` chain to **`VLOOKUP(C4,BV7:BZ234,5,0)`** — a per-month-code table
like 805/808, which is exactly §11's prevention rule; rates unchanged.
`tos reforma 4147` gains five values that were 0 (4147 is `reported` with no
rule, so no result changes). `Netunei Gimlai`'s 48 cells are sample-worker data.

**⚠ New trap: never regenerate.** After the fix `BZ3` resolves to **0.0244**,
because the sample worker's month code lands in 121-132. The extractor would now
pick up **a single rate chosen at random by the demo data** and be wrong for
every other year. The hand-written rule holds all three.

## 0av. What the 738 gap actually is — new `PROGIM_FIXES.md` §16

The user asked what the gaps are on code 738, the largest coverage item. Answer:
**it is not a measured discrepancy at all** — the engine cannot compute 738, so
₪1,202,498 is **unvalidated, not wrong**. Distinguish those two when reporting.

**Where it appears:** only **12/2018 (2,566 rows, ₪472,663) and 12/2019 (2,475
rows, ₪729,835)**, zero in the other eleven files. All 5,041 rows belong to
**נציבות מס הכנסה (2,872)** and **מכס ומע"מ (2,169)**.

**The workbook is not silent on it — that was my earlier framing and it was too
strong.** 738 appears in eight sheets with full metadata: `רכיבים` gives type
**אחוז** and a note "מיום 01/01/2017: 0.94%"; `מאפייני רכיבי שכר` names it
"רשות חדשה אחוזית **3.94%**" and marks **משכורת קובעת: כן**; `Netunei Gimlai`
lists the eligible bodies — which the data confirms exactly; `simlei sachar` and
`המרת סמלי שכר` carry its indices. **The only missing piece is the formula** —
no `tosafot` column, no `SACHAR` calculation — so the extractor never produced a
rule and the engine classifies it as neither computable nor referenced.

**Two contradictions, both recorded in §16:**
1. The workbook states **two different rates**, 3.94% and 0.94%-from-2017.
2. **Neither reproduces the slips.** Ratio to the combined salary: median
   **4.275%** in 12/2018 (2.9% of carriers match 3.94%, none match 0.94%) and
   **6.903%** in 12/2019 (none match either). The ratio itself moves 4.28% →
   6.90% in one year, so 738 is **not a fixed percentage of the combined
   salary**. The name "אחוז-**יום**" suggests a day-based base the גולמי does
   not carry. **I did not try to reverse-engineer the rule** — that is the
   mistake made twice today on the dating, and §16 says so explicitly.

**⚠ Do not declare 738 out of scope.** `מאפייני רכיבי שכר` sets **משכורת
קובעת: כן** — it is pensionable. Removing it would close the coverage gap on
paper while leaving ₪1.2M of pensionable pay silently unchecked. Given how many
codes have been declared out of scope today, this one needs the explicit "no".

## 0au. The complete 13-file unified report

The user re-uploaded 12/2013 and 12/2014, so the series is whole: the 0108
reference plus **twelve consecutive Decembers, 2008 through 2019**. Written to
`דוח_מאוחד_13_קבצים_05.08.2026.xlsx` and sent.

**269,098 workers · 254,266 valid · 175 true errors (0.0650%) · ₪48,260
exposure** (₪28,399 under, ₪19,861 over). **All 14 partitions close.**

**The two recovered files confirm the prose written while they were lost.**
12/2013 gives 11 true errors and ₪2,157; 12/2014 gives 14 and ₪1,090 — exactly
the figures documented in 0ad and 0ag before the uploads vanished. The
documentation held up; the coverage gaps are now smaller (12/2013 3 codes /
₪10,401, 12/2014 4 / ₪11,548) purely because of the scope batches added since.

**True errors, count vs money.** By count: 697 (45), 736 (31), 626 (18), 756
(17), 4651 (14). By exposure: **736 ₪12,550**, 756 ₪7,199, 4651 ₪6,781, 697
₪4,543, 858 ₪1,126. 626 makes the point — 18 workers but ₪387 in total, about ₪21
each. **Work the money, not the count**; the docs say so in both files.

**Coverage gap: 21 codes / ₪1,874,571, and 93% of it is four codes.** 738 ת.
אחוז-יום is ₪1,202,498 over 5,041 rows — **64% alone** — then 1622 (₪261,436),
1631 (₪207,244), 4140 (₪90,200 over 42 rows) and 1623 (₪77,082). This remains the
shortest, highest-return work list in the workbook and is what to lead with when
asked what to fix next.

Across the whole series the two new neutralization columns catch: **875 → 64
workers** in 3 of 13 files (12/2012, 12/2016, 12/2018), **4140 → 6 workers** in 5
files. Both behave as measured when they were built.

## 0at. Unified report across all 11 available files

One run over everything on hand: the 0108 reference plus ten Decembers from 2008
to 2019. Written to `דוח_מאוחד_11_קבצים_05.08.2026.xlsx` and sent to the user.

**229,426 workers · 216,509 valid · 150 true errors (0.0654%) · ₪45,013
exposure** (₪26,631 under, ₪18,381 over). **All 12 partitions close.**

Per file: 01/2008 98.21% (10 errors), 12/2008 98.76% (15), 12/2009 98.59% (12),
12/2010 98.40% (11), 12/2011 97.62% (11), 12/2012 97.90% (2), 12/2015 97.21%
(13), 12/2016 97.85% (19), 12/2017 97.65% (19), 12/2018 97.89% (19), 12/2019
98.21% (19).

**12/2013 and 12/2014 are missing** — their גולמי uploads vanished in the
rollback described in 0al and cannot be re-run. Their findings survive only as
prose.

**True errors rank differently by count and by money — use money.** By count:
697 (38), 736 (26), 756 (17), 4651 (13), 626 (12). By exposure: **628 at ₪14,926
across only 8 workers** (~₪1,866 each), 736 ₪11,254, 756 ₪7,199, 4651 ₪6,693,
4169 ₪3,809. 626 is the opposite extreme — 12 workers, ₪121 total. 4651 appearing
at 13 workers / ₪6,693 is the §11 component the workbook could not compute at all
until yesterday.

**Union coverage gap: 21 codes / ₪1,852,622 — and 94% of it is four codes.**
738 ת. אחוז-יום is **₪1,202,498 over 5,041 rows, 65% on its own**, then 1622
(₪261,436), 1631 (₪207,244) and 1623 (₪77,082); 4140 follows at ₪73,508 across 33
rows. That is a four-line work list and currently the highest-return investment
available in the workbook — worth leading with when the user asks what to fix
next.

The new 4140 column caught **6 workers** across all 11 files. The cross-month
sheets hold 2,811 and 2,844 rows and are chronologically valid, since every file
now has either a date column or an MMYY name.

## 0as. The 12/2019 file — the dating model is dead, and it cannot be revived

Thirteenth file: **December 2019**, **20,041 workers**. **98.21% · 19 true errors
· ₪3,308**; partition closes. Best verdict of any December file. Docs only.

**‼ The pulse-table dating is refuted — the constraint set is empty.** 805 pays
**116.41** here (107 of 107, a perfect match), which is the codes **144-228**
value, so c+132 ≥ 144 requires **c ≥ 12**. But 12/2009 requires **c ≤ 11**. No c
satisfies both. Running all twelve months together yields **no solution at all**,
and 12/2019 also skips the 140-143 band entirely.

**This is not imprecision, it is a contradiction, and it kills the model.** The
assumption that the pulse value tracks the *payslip* month is simply wrong. The
tables are keyed on **`חודש פרישה`** — retirement month — so a December file's
modal 805 value reflects the retirement cohort of its carriers, which drifts but
need not advance 12 codes a year.

**Second retraction on this, and this one is final.** I retracted a dating claim
at 12/2009, then in 0an said 12/2016 narrowed c to [7,11] — **that was also
wrong**, resting on the same assumption that has now collapsed. Do not attempt
this again from payslip data; §14 (fix the `חודש פרישה` sheet) is the only route,
and `PROGIM_FIXES.md` §14 now says so with the empty-constraint proof.

**5402 gets a fourth anchor — and the growth rate I flagged breaks:**

| month | ratio | measured full-time | growth |
|---|---|---|---|
| 12/2016 | 0.19905 | ₪66.88 | — |
| 12/2017 | 0.30571 | ₪102.72 | ×1.536 |
| 12/2018 | 0.47054 | ₪158.10 | ×1.539 |
| **12/2019** | **0.89836** | **₪301.85** | **×1.909** |

The measurement itself is as strong as ever — 97.7% of 19,430 carriers within
±0.0005 of the ratio. But in 0ap I wrote that the growth rate "looks like a
defined schedule" after two matching factors; **the fourth point refutes that.**
Good thing no formula was derived from it. What does strengthen: **₪301.85 is
89.8% of the ₪336 the workbook knows**, supporting the reading that ₪336 is the
mature pulse the component climbs toward. §7 now has **four measured rows**.

Coverage gap **5 codes / ₪756,489**, of which **738 alone is ₪729,835 over 2,475
rows** — the second consecutive month where 738 is nearly the whole gap. Then
4140 (₪19,076), 1132 (₪3,803), 1623 (₪2,453), 5315 (₪1,321). The new 4140 column
caught one worker. 805 is 107/107 and trusted; 875 is 96.8% and silenced; 4651 is
97.0%, exactly on the line, silenced.

## 0ar. A neutralization column for 4140 — and 5374 out of scope

The user asked for a **"שגויי משכ. בסיסית 4140"** column immediately after
"שתי שורות שכר משולב" — i.e. **first in the neutralization chain**. Delivered in
all three places that must agree: `tools/unified_report.py`, `index.html`,
`salary_frontend.html`, with the HTML files byte-identical. The dashboard is now
**22 columns**; every index shifted, the conditional-formatting ranges moved to
`T`/`U`, the banner merge to 21 and the side table to `W`. Partitions close.

**How it detects:** not by a failing rule — 4140 has no formula in the workbook
so it can never fail — but by **the code being present on the slip**, the same
pattern already used for 5527 and 1711.

**What it absorbs, measured before building:** 5 invalid workers across eight
files — 12/2012 (1, from 1999), 12/2015 (1, from base), 12/2016 (2, from base),
12/2018 (1, from base). Zero in 12/2008, 12/2010, 12/2017 and 0108.

**None of them is currently a "real" error.** All five are already neutralized
elsewhere, so **the true-error count does not move in any file** — 13, 19 and 19
for 12/2015, 12/2016 and 12/2018 before and after. The column **re-attributes**;
it does not neutralize anything new. Say that plainly if anyone reads the new
column as an improvement in the headline.

**Unlike the 875 column, this one has a justification.** 4140 is a *base-salary*
component with no formula, so a slip carrying it has a base the חוקה cannot
reproduce — attributing the gap to 4140 instead of to "שגויי בסיס" points at the
root rather than the symptom. It also swallows nothing: every worker it takes was
already in a neutralization bucket. **What retires it:** giving 4140 a formula in
the workbook. It is the most persistent coverage-gap item there is (eight files).

**5374 (תוספת מו"מ) out of scope**, eighth batch, passing both checks — absent
from the workbook and from every rule, seen in 12/2016 (₪780), 12/2017 (₪802)
and 12/2018 (₪821). `NON_PENSIONABLE` is now **40 codes**, Python and JS in sync.

Coverage gaps after the last two batches: 12/2015 **3 / ₪6,883**, 12/2016 **3 /
₪10,365**, 12/2018 **9 / ₪1,055,069**. What remains in 12/2018 cannot be solved
by declaring scope: 738 (₪472,663), 1622 (₪261,436), 1631 (₪207,244), 1623
(₪74,629) and 4140 (₪26,309) are pay components — **₪1.04M of real coverage gap.**

## 0aq. 5438, 5273, 4436, 4437 out of scope — batches six and seven

On the user's instruction, off the 12/2016-12/2018 coverage lists. Both pass the
two checks cleanly: absent from the workbook in every sheet, absent from
`component_rules.json` in every field. 5438 סטודנט לומד appears in 12/2016
(₪781), 12/2017 (₪297) and 12/2018 (₪779); 5273 ימי בחירה only in 12/2016
(₪116). 4436 ימי חופשה appears in 12/2017 (₪75) and 12/2018 (₪2,505); 4437 ימי
מחלה only in 12/2017 (₪74). `NON_PENSIONABLE` is now **39 codes**; Python and JS compared
element-wise and in sync, 34 tests pass, `node --check` clean.

Coverage gaps: 12/2016 **6 → 4 codes, ₪12,042 → ₪11,145**; 12/2017 **7 → 4,
₪5,128 → ₪4,682**; 12/2018 **12 → 10, ₪1,059,174 → ₪1,055,890**. Partitions close
and verdicts are unchanged (97.85% · 97.65% · 97.89%).

**5273 completes a whole family:** 5271 (ימי חג), 5272 (ימי מחלה), 5273 (ימי
בחירה) — three consecutive codes, one category, added in **three separate
batches** over the course of the day. That is the cleanest demonstration yet that
scope is decided code by code rather than by rule, and that each new file
uncovers another family member. §15 records it.

**What remains in 12/2018's gap is not out-of-scope material:** 738 (₪472,663),
1622 (₪261,436), 1631 (₪207,244), 1623 (₪74,629), 4140 (₪26,309), 1703
(₪10,630). These are pay components — **₪1.06M of genuine coverage gap in the
workbook**, which declaring codes out of scope will not solve.

**The family pattern is now unmistakable.** "ימי מחלה" occupies **two** codes on
the list (5272 and 4437) and "ימי חופשה" two others (4122 and 4436), on top of
דמי הבראה's four (1260/1265/1266/1269) and the 5271/5272/5273 run. **Four
benefit families spread across 11 of the 39 codes**, each added a code at a time
as a new file surfaced it. That is the argument for §15's `פנסיוני` column in
`sminimum` — the list will keep growing one code per file until the workbook
declares scope itself.

## 0ap. The 12/2018 file — the coverage gap explodes to ₪1.06M

Twelfth file: **December 2018**, **20,387 workers**. **97.89% · 19 true errors ·
₪2,541**; partition closes. Docs only.

**Coverage gap: 12 codes / ₪1,059,174** — against ₪5,128 in 12/2017, and by far
the largest of any December file. Four codes carry almost all of it:

| code | name | rows | ₪ |
|---|---|---|---|
| **738** | ת. אחוז-יום | 2,566 | **₪472,663** |
| **1622** | 15% ש.ממושך | 35 | **₪261,436** |
| **1631** | 10% פקח עיר | 46 | **₪207,244** |
| **1623** | מאמץ-עוז גנ | 9 | **₪74,629** |
| 4140 | משכ.בסיסית | 9 | ₪26,309 |
| 1703 | פרטי/משא/קל | 1 | ₪10,630 |

Note the density: 1622 is ₪261k over **35 rows**, about ₪7,470 each. These are
not marginal components.

**This also corrects something I wrote earlier.** I said 738 was "entirely inside
`golmi.xlsx`". True of the files I had then, but **738 appears here too — 2,566
rows** — while being absent from 12/2016, 12/2017 and the 0108 reference. So it
is a later-period component, not a quirk of one sample. At ₪472k in a single
month it is the most expensive item in any coverage list so far and deserves a
decision.

**5402 gets a third anchor, and the growth rate is itself consistent:**

| month | ratio | measured full-time | growth |
|---|---|---|---|
| 12/2016 | 0.19905 | **₪66.88** | — |
| 12/2017 | 0.30571 | **₪102.72** | ×1.536 |
| 12/2018 | 0.47054 | **₪158.10** | ×1.539 |

Again 0 of 19,779 match, ₪3,337,209 silenced, ratio constant across tiers. Two
successive growth factors within 0.003 of each other is not noise; it looks like
a defined schedule. **I did not try to reverse-engineer the formula** — that is
the mistake I made with the dating — but three measured points with a uniform
rate is a strong basis for whoever holds the agreement text. §7 gets a third row.

**⚠ Second consecutive month where 805's only true error is an exact multiple.**
805 is trusted (98.1%); one carrier was flagged at ₪224.94 against a 112.47 tier,
and **224.94 ÷ 112.47 = exactly 2.0000**. In 12/2017 it was exactly ×3. Two in a
row is a pattern: **worth considering a check that marks an exact integer
multiple on a trusted component as "retro — manual review" rather than an
error.** Not implemented; it changes flagging rules and needs the user's
decision.

Other: the 875 bucket fired a third time (97.9%, trusted) catching **24
workers** — 3 of 12 files. 805 pays 112.47 (codes 126-139); c+120 ∈ [126,139]
gives c ∈ [6,19], adding nothing to c ∈ [7,11]. **"שתי שורות שכר משולב" jumped to
67** from the usual 12-20 — worth watching if it recurs. Calibration silenced 30
of 49 rules, ₪5,764,123, led by 5402 (₪3.34M) and 4550 (₪1.49M).

## 0ao. The 12/2017 file — a second 5402 anchor, and it ramps

Eleventh file: **December 2017**, **20,135 workers**. **97.65% · 19 true errors ·
₪6,752** (₪5,663 under, ₪1,088 over); partition closes. Docs only.

**5402 gets its second anchor, and the two together settle §7.** Same test, same
clean result: **0 of 19,671 match**, ₪4,334,696 silenced, and the ratio is
constant across every tier — 0.30571 at ₪336 (16,413 carriers), ₪252 (1,598),
₪168 (836) and ₪268.80 (108).

| month | ratio | **measured full-time amount** |
|---|---|---|
| 12/2016 | 0.19905 | **₪66.88** |
| 12/2017 | 0.30571 | **₪102.72** |

**The amount climbs year over year** — exactly how a phased agreement behaves.
That confirms §7 unambiguously: 5402 is a period-varying shekel component with
no amount table, and the single ₪336 the workbook knows is a later pulse. There
are now **two measured rows** to fill that table with, each backed by ~19k slips.

**Dating: consistent, no further narrowing.** 805 pays 110.85 (96 carriers), the
codes 112-125 value. c+108 ∈ [112,125] gives c ∈ [4,17], which adds nothing to
c ∈ [7,11]. Code 1 stays **August-December 2008**.

**⚠ One flagged 805 worker is almost certainly not an error.** 805 is trusted
here (98.1%) so it is checked, and one carrier was reported as a true error at
**₪332.55**. But 332.55 ÷ 110.85 = **exactly 3.0000** — three months compressed
into one line, the classic retro signature. The גולמי carries no retro flag so
the engine cannot separate it. Under the standing rule about never flagging a
correctly-paid worker, **an exact integer multiple on a trusted component
deserves a manual look before it reaches a work queue.** Worth considering as a
general check.

Coverage gap **7 codes / ₪5,128**: 4140 (₪1,791 — its **eighth** file), 1132
(₪1,649), 5374 (₪802), 5315 (₪440), 5438 (₪297), **4436 ימי חופשה** (₪75),
**4437 ימי מחלה** (₪74). The last two look like out-of-scope candidates by the
user's own earlier logic — 4437 is a twin of 5272 (already listed) and 4436 of
4122 — but neither was added; that is the user's call.

The 875 bucket is empty again (94.9%, silenced): it has fired in 2 of 11 files.

## 0an. The 12/2016 file — 5402 gets a measured anchor, and the dating narrows

Tenth file: **December 2016**, **19,141 workers**. **97.85% · 19 true errors ·
₪2,820**; partition closes. Docs only.

**The result to act on: 5402's amount is off by a constant factor of 5.0239.**
This is the first December file that contains 5402 at all — **18,634 carriers,
97% of the file** — where every other December file and the 0108 reference have
**zero**. That fits the component's name: "תוספת שקלית **2016**" starts in 2016.

**None of the 18,578 checked match — 0.0%**, ₪4,733,498 silenced, the largest
silenced figure measured in any single file, larger than 4550. But the gap is
perfectly constant:

| expected | carriers | paid/expected |
|---|---|---|
| ₪336.00 | 15,732 | 0.19905 |
| ₪252.00 | 1,423 | 0.19905 |
| ₪168.00 | 804 | 0.19905 |
| ₪294.00 | 98 | 0.19905 |
| ₪210.00 | 29 | 0.19905 |

**98.4% of carriers sit within ±0.0005 of 0.19905.** The tier structure (₪336 ×
job fraction) is **right**; only the scale is wrong, by one uniform factor.

So **5402's full-time amount in December 2016 is ₪66.88, not ₪336** — which is
exactly what §7 claims: the component varies by period and has no amount table,
and ₪336 is presumably a later pulse. §7 now has a measured anchor to fill one
row with: **12/2016 = ₪66.88 full-time.** With 18,578 slips behind it this is by
far the strongest evidence collected today — compare the single carrier behind
every 808 observation.

**The dating narrows for the first time since 12/2009.** 805 pays **108.96** here
(97 carriers plus clean job fractions 81.72 = 0.75 and 68.10 = 0.625) — the
codes **103-111** value, a band not seen before. c+96 ∈ [103,111] gives
c ∈ [7,15]; with the existing c ∈ [1,11]:

> **c ∈ [7,11] — code 1 is a month between August and December 2008.**

Five possibilities instead of eleven. Still not certainty, and §14 (fix the
sheet) remains the right answer, but it is the first file since 12/2009 to add a
constraint.

**The 875 bucket fired for the second time:** 875 matches 98.2%, is trusted, and
the column catches **15 workers**. Two files out of ten (12/2012, 12/2016). 4651
is back to 98.1% and trusted after 96.4% and silenced in 12/2015.

Coverage gap **6 codes / ₪12,042**: 4140 (₪9,751 — its **seventh** file), 5438
סטודנט לומד (₪781), 5374 (₪780), 5315 (₪440), 507 (₪173 — **all ten files**),
5273 ימי בחירה (₪116).

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
