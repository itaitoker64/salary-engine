<!-- head: 6aa1243 -->
# Handoff — branch `claude/employee-simulator-validation-pl128n`

Written 31.7.2026. Read `CLAUDE.md` first; it carries the standing rules.

## State

Restarted from `origin/main` at `573c435` after PR #61 merged, then merged
`origin/main` again at `23f5028` (the other session's site-routing work — that
history is preserved below under "From `main`"). Not merged back yet.

Five topics on this branch, newest first:

0. **Upgraded to the Progim 31.07.2026 workbook** — 956/957 newly defined there
1. **חוקה amounts split into fixed vs period-varying** in the classification sheet
2. **1711 and 4120 out of scope**; 1711 also gets its own neutralization bucket
3. **The dashboard partition covers the whole file**, not full-timers only
4. **4319 / 4427 are in the Progim** and the engine now computes them

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
