<!-- head: facd0eb -->
# Handoff — branch `claude/employee-simulator-validation-pl128n`

Written 31.7.2026. Read `CLAUDE.md` first; it carries the standing rules.

## State

Restarted from `origin/main` at `573c435` after PR #61 merged, then merged
`origin/main` again at `23f5028` (the other session's site-routing work — that
history is preserved below under "From `main`"). Not merged back yet.

Four topics on this branch, newest first:

1. **חוקה amounts split into fixed vs period-varying** in the classification sheet
2. **1711 out of scope, plus its own neutralization bucket**
3. **The dashboard partition covers the whole file**, not full-timers only
4. **4319 / 4427 are in the Progim** and the engine now computes them

## 1. חוקה amounts: fixed vs varies

"סכום לפי חוקה" became three labels — `סכום קבוע לכל התקופה` (46),
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

Classification: 35 formula · 46 חוקה-fixed · 8 חוקה-varies · 1 חוקה-unsettled ·
7 manual · 11 out-of-scope · 12 undefined. Verdicts 21,167 / 382 throughout —
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

## From `main` — site routing (the other session, merged in here)

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
