"""
main.py — Salary Engine API v0.2 (self-contained, flat structure)
"""

import os, io, time, json, tempfile
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field
from collections import defaultdict

import openpyxl
import pandas as pd
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse, JSONResponse
from pydantic import BaseModel, Field

MATCH_THRESHOLD = 1.0

# Default seniority track (קוד דרוג): 1 = מינהלי.
DEFAULT_TRACK = 1

# Base-salary component codes seen in the raw payroll dumps.
#   10002 = שכר משולב   — the combined base (base × seniority-multiplier × job%)
#       1 = יסוד משולב  — base at seniority 0 (× job%)
#       2 = תוספת ותק   — the seniority increment, base × (multiplier - 1) × job%
# The first form appears in older מנהלי files; the 1+2 split is used by the
# מנהלת הגמלאות (Pension Authority) dumps. Both reconstruct to base × mult × job%.
CODE_COMBINED_BASE = 10002
CODE_YESOD = 1
CODE_VETEK_TOSEFET = 2


def load_lookups(json_path: str) -> dict:
    """Load the multi-track lookup tables from lookups.json (built from Progim).

    Returns:
      - label_to_base:  {grade_label -> base salary at seniority 0}
      - vetek_by_track: {track_code -> {seniority_years -> multiplier}}
      - track_max:      {track_code -> max seniority years (cap)}
      - tracks:         {track_code -> track name}
    """
    raw = json.loads(Path(json_path).read_text(encoding="utf-8"))
    label_to_base = {str(k): float(v) for k, v in raw["darga"].items()}
    vetek_by_track = {
        int(track): {float(y): float(m) for y, m in table.items()}
        for track, table in raw["vetek"].items()
    }
    track_max = {int(k): float(v) for k, v in raw.get("track_max", {}).items()}
    tracks = {int(k): str(v) for k, v in raw.get("tracks", {}).items()}
    return {
        "label_to_base": label_to_base,
        "vetek_by_track": vetek_by_track,
        "track_max": track_max,
        "tracks": tracks,
    }


def get_grade_base(lookups, darga_label):
    """Base salary (seniority 0) for a grade label, e.g. '18', '42+'."""
    if darga_label is None:
        return None
    return lookups["label_to_base"].get(str(darga_label).strip())


def get_vatek_multiplier(lookups, vatek, track=DEFAULT_TRACK):
    """Seniority multiplier for a given track and seniority (years).

    The multiplier is capped at the track's maximum seniority (e.g. מינהלי
    caps at 37 yrs, מח"ר at 40); beyond that the cap value is reused. For
    off-grid seniority values the nearest lower table key is used.
    """
    track = int(track)
    table = lookups["vetek_by_track"].get(track) or lookups["vetek_by_track"].get(DEFAULT_TRACK)
    if not table:
        return None
    vatek = float(vatek)
    cap = lookups["track_max"].get(track)
    if cap is not None:
        vatek = min(vatek, cap)
    if vatek in table:
        return table[vatek]
    lower = [k for k in table if k <= vatek]
    if lower:
        return table[max(lower)]
    return table[min(table)]

@dataclass
class WorkerInput:
    worker_id: int
    ministry_code: int
    ministry_name: str
    droog: int
    job_pct: float
    pension_pct: float
    kod_darga: int
    darga_label: str
    vatek_mandatory: float
    vatek_regular: float
    vatek_msc: float
    vatek_calculated: float
    calc_month: int
    retro_month: int
    retro_count: int
    components: list = field(default_factory=list)

@dataclass
class ComponentResult:
    code: int
    name: str
    amount: float
    pensionable: bool
    calculated: bool
    expected: Optional[float] = None
    diff: Optional[float] = None

@dataclass
class SalaryResult:
    worker_id: int
    ministry_code: int
    ministry_name: str
    droog: int
    kod_darga: int
    darga_label: str
    vatek_calculated: float
    job_pct: float
    pension_pct: float
    components: list
    total: float
    expected_total: Optional[float] = None
    total_diff: Optional[float] = None
    total_match: Optional[bool] = None
    grade_base: Optional[float] = None
    vatek_multiplier: Optional[float] = None
    errors: list = field(default_factory=list)

def calculate(worker: WorkerInput, lookups: dict) -> SalaryResult:
    errors = []
    component_results = []
    total = 0.0
    track = int(worker.droog or DEFAULT_TRACK)
    grade_base = get_grade_base(lookups, worker.darga_label)
    if grade_base is None:
        errors.append(f"Unknown grade label: {worker.darga_label!r} (kod_darga {worker.kod_darga})")
    vatek_mult = get_vatek_multiplier(lookups, worker.vatek_calculated, track)
    if vatek_mult is None:
        errors.append(f"Unknown vatek/track: {worker.vatek_calculated}/{track}")
    job_pct = worker.job_pct or 1.0
    for comp_code, comp_name, raw_amount, pensionable in worker.components:
        amount = raw_amount or 0.0
        calculated = False
        expected = raw_amount
        diff = None
        computed = None
        if grade_base is not None and vatek_mult is not None:
            if comp_code == CODE_COMBINED_BASE:
                # שכר משולב — full combined base
                computed = round(grade_base * vatek_mult * job_pct, 2)
            elif comp_code == CODE_YESOD:
                # יסוד משולב — base at seniority 0
                computed = round(grade_base * job_pct, 2)
            elif comp_code == CODE_VETEK_TOSEFET:
                # תוספת ותק — the seniority increment on top of יסוד
                computed = round(grade_base * (vatek_mult - 1.0) * job_pct, 2)
        if computed is not None:
            diff = round(computed - (raw_amount or 0.0), 4)
            amount = computed
            calculated = True
        total += amount
        component_results.append(ComponentResult(
            code=int(comp_code) if comp_code is not None else 0, name=comp_name or "", amount=amount,
            pensionable=(pensionable == "כן"), calculated=calculated,
            expected=expected, diff=diff,
        ))
    expected_total = sum((c[2] or 0.0) for c in worker.components)
    total_diff = round(total - expected_total, 4)
    total_match = abs(total_diff) <= MATCH_THRESHOLD
    return SalaryResult(
        worker_id=worker.worker_id, ministry_code=worker.ministry_code,
        ministry_name=worker.ministry_name, droog=worker.droog,
        kod_darga=worker.kod_darga, darga_label=worker.darga_label,
        vatek_calculated=worker.vatek_calculated, job_pct=worker.job_pct,
        pension_pct=worker.pension_pct, components=component_results,
        total=round(total, 2), expected_total=round(expected_total, 2),
        total_diff=total_diff, total_match=total_match,
        grade_base=grade_base, vatek_multiplier=vatek_mult, errors=errors,
    )

# Maps a גולמי column header to a canonical field name. Matching is by Hebrew
# keyword (substring), so it is robust to column reordering and to the layout
# differences between the older מנהלי dumps and the מנהלת הגמלאות dumps (which
# carry two blank header rows and a different column order). Order matters:
# more specific patterns are checked first (e.g. "קוד דרגה" before "דרגה").
def _classify_header(h: str) -> Optional[str]:
    h = str(h).strip()
    if "מסד" in h or "מסב" in h or ("מספר" in h and "עובד" in h):
        return "worker_id"
    if "קוד משרד" in h or "קוד גוף" in h or ("קוד" in h and "משרד/גוף" in h):
        return "ministry_code"
    if "שם משרד" in h or "שם גוף" in h or h in ("משרד/גוף", "משרד", "גוף"):
        return "ministry_name"
    if "דרוג" in h:
        return "droog"
    if "חלקיות" in h:
        return "job_pct"
    if "קוד דרגה" in h:
        return "kod_darga"
    if "קוד רכיב" in h:
        return "comp_code"
    if "רכיב" in h:
        return "comp_name"
    if "ותק" in h:
        return "vatek"
    if h == "דרגה" or ("דרגה" in h and "קוד" not in h):
        return "darga_label"
    if "פנסיו" in h:
        return "pensionable"
    if "סכום" in h or "סך" in h:
        return "amount"
    return None


def load_golmi(excel_path: str) -> dict:
    """Read a גולמי sheet, locate its header row, and group rows by worker.

    Columns are mapped by Hebrew header name rather than fixed position, so the
    same code reads both the old מנהלי layout (header on row 1) and the Pension
    Authority layout (two blank rows, header on row 3, different column order,
    base split into יסוד משולב + תוספת ותק).
    """
    wb = openpyxl.load_workbook(excel_path, read_only=True, data_only=True)
    ws = wb["גולמי"] if "גולמי" in wb.sheetnames else wb[wb.sheetnames[0]]

    # Find the header row within the first few rows: the one that classifies the
    # most known fields (and at minimum has worker_id, a component and an amount).
    header_map, header_idx = None, None
    scan = list(ws.iter_rows(min_row=1, max_row=8, values_only=True))
    best_score = 0
    for i, row in enumerate(scan):
        mapping = {}
        for ci, cell in enumerate(row):
            if cell is None:
                continue
            field_name = _classify_header(cell)
            if field_name and field_name not in mapping:
                mapping[field_name] = ci
        score = len(mapping)
        if score > best_score and {"worker_id", "comp_code", "amount"} <= set(mapping):
            best_score, header_map, header_idx = score, mapping, i
    if header_map is None:
        wb.close()
        raise HTTPException(status_code=400,
                            detail="Could not find a recognizable גולמי header row in the file.")

    def cell(row, key):
        idx = header_map.get(key)
        return row[idx] if idx is not None and idx < len(row) else None

    workers = defaultdict(list)
    for row in ws.iter_rows(min_row=header_idx + 2, values_only=True):
        wid = cell(row, "worker_id")
        if wid is None:
            continue
        workers[wid].append((
            cell(row, "ministry_code"), cell(row, "ministry_name"),
            cell(row, "droog"), cell(row, "job_pct"),
            cell(row, "kod_darga"), cell(row, "darga_label"), cell(row, "vatek"),
            cell(row, "comp_code"), cell(row, "comp_name"),
            cell(row, "pensionable"), cell(row, "amount") or 0.0,
        ))
    wb.close()
    return dict(workers)

def run_batch(excel_path: str, lookups: Optional[dict] = None) -> tuple:
    # Lookups come from the bundled engine data (lookups.json), not the uploaded
    # file — the Pension Authority dumps contain only raw rows, no lookup tables.
    if lookups is None:
        lookups = get_lookups()
    workers_raw = load_golmi(excel_path)
    summary_rows, detail_rows = [], []
    for worker_id, rows in workers_raw.items():
        first = rows[0]
        ministry_code, ministry_name, droog, job_pct, kod_darga, darga_label, vatek = first[:7]
        components = [(r[7], r[8], r[10], r[9]) for r in rows]
        worker = WorkerInput(
            worker_id=worker_id, ministry_code=ministry_code or 0,
            ministry_name=ministry_name or "", droog=droog or 1,
            job_pct=job_pct or 1.0, pension_pct=0.0,
            kod_darga=kod_darga or 0, darga_label=darga_label or "",
            vatek_mandatory=0.0, vatek_regular=float(vatek or 0),
            vatek_msc=0.0, vatek_calculated=float(vatek or 0),
            calc_month=0, retro_month=0, retro_count=0,
            components=components,
        )
        result = calculate(worker, lookups)
        summary_rows.append({
            "worker_id": result.worker_id, "ministry_code": result.ministry_code,
            "ministry_name": result.ministry_name, "droog": result.droog,
            "kod_darga": result.kod_darga, "darga_label": result.darga_label,
            "vatek": result.vatek_calculated, "job_pct": result.job_pct,
            "grade_base": result.grade_base, "vatek_mult": result.vatek_multiplier,
            "total_calculated": result.total, "total_expected": result.expected_total,
            "total_diff": result.total_diff, "total_match": result.total_match,
            "n_components": len(result.components), "errors": "; ".join(result.errors),
        })
        for comp in result.components:
            detail_rows.append({
                "worker_id": result.worker_id, "ministry_code": result.ministry_code,
                "comp_code": comp.code, "comp_name": comp.name,
                "pensionable": comp.pensionable, "calculated": comp.calculated,
                "amount": comp.amount, "expected": comp.expected, "diff": comp.diff,
                "match": abs(comp.diff or 0) <= MATCH_THRESHOLD if comp.calculated else None,
            })
    return pd.DataFrame(summary_rows), pd.DataFrame(detail_rows)

app = FastAPI(title="Salary Engine API", version="0.2.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

LOOKUPS_FILE = Path(__file__).parent / "lookups.json"
FRONTEND_FILE = Path(__file__).parent / "index.html"
_lookups: Optional[dict] = None

def get_lookups() -> dict:
    global _lookups
    if _lookups is None:
        if not LOOKUPS_FILE.exists():
            raise RuntimeError(f"Lookup data file not found: {LOOKUPS_FILE}")
        _lookups = load_lookups(str(LOOKUPS_FILE))
    return _lookups

@app.on_event("startup")
async def startup():
    try:
        lk = get_lookups()
        print(f"Lookups loaded — grades: {len(lk['label_to_base'])}, "
              f"tracks: {len(lk['vetek_by_track'])}")
    except Exception as e:
        print(f"Failed to load lookups: {e}")

class ComponentInput(BaseModel):
    code: int
    name: str = ""
    amount: float = 0.0
    pensionable: str = "כן"

class CalculateRequest(BaseModel):
    worker_id: int = Field(..., example=11021106)
    ministry_code: int = Field(..., example=170)
    ministry_name: str = Field("", example="מכס ומע\"מ")
    droog: int = Field(1)
    job_pct: float = Field(1.0)
    pension_pct: float = Field(0.4)
    kod_darga: int = Field(..., example=202)
    darga_label: str = Field("", example="18")
    vatek_mandatory: float = Field(0.0)
    vatek_regular: float = Field(0.0)
    vatek_msc: float = Field(0.0)
    vatek_calculated: float = Field(..., example=33.75)
    calc_month: int = Field(228)
    retro_month: int = Field(0)
    retro_count: int = Field(1)
    components: list[ComponentInput] = Field(default_factory=list)

class ComponentOut(BaseModel):
    code: int; name: str; amount: float; pensionable: bool
    calculated: bool; expected: Optional[float]; diff: Optional[float]

class CalculateResponse(BaseModel):
    worker_id: int; ministry_code: int; ministry_name: str; droog: int
    kod_darga: int; darga_label: str; vatek_calculated: float
    job_pct: float; pension_pct: float; grade_base: Optional[float]
    vatek_multiplier: Optional[float]; components: list[ComponentOut]
    total: float; expected_total: Optional[float]
    total_diff: Optional[float]; total_match: Optional[bool]; errors: list[str]

class AccuracyResponse(BaseModel):
    total_workers: int; matched: int; unmatched: int
    accuracy_pct: float; match_threshold: float
    avg_diff: float; max_diff: float
    by_ministry: list[dict]; elapsed_sec: float

@app.get("/", include_in_schema=False)
def root():
    if FRONTEND_FILE.exists():
        return FileResponse(str(FRONTEND_FILE))
    return JSONResponse({"status": "ok", "service": "salary-engine", "version": "0.2.0"})

@app.get("/healthz")
def health():
    return {"status": "ok", "service": "salary-engine", "version": "0.2.0"}

@app.get("/api/info")
def info():
    lk = get_lookups()
    return {"status": "ok", "grades_loaded": len(lk["label_to_base"]),
            "tracks_loaded": len(lk["vetek_by_track"]),
            "track_caps": lk["track_max"],
            "match_threshold": MATCH_THRESHOLD, "version": "0.3.0"}

@app.get("/api/grades")
def list_grades():
    lk = get_lookups()
    return {"grades": [{"darga_label": k, "base_salary": v}
                       for k, v in sorted(lk["label_to_base"].items())]}

@app.get("/api/tracks")
def list_tracks():
    lk = get_lookups()
    return {"tracks": [{"code": k, "name": lk["tracks"].get(k, ""),
                        "max_vatek": lk["track_max"].get(k)}
                       for k in sorted(lk["vetek_by_track"])]}

@app.get("/api/vatek/{years}")
def get_vatek(years: float, track: int = DEFAULT_TRACK):
    lk = get_lookups()
    mult = get_vatek_multiplier(lk, years, track)
    if mult is None:
        raise HTTPException(status_code=404, detail=f"No vatek entry for {years} years (track {track})")
    return {"vatek": years, "track": track, "multiplier": mult}

@app.post("/api/calculate", response_model=CalculateResponse)
def calculate_one(req: CalculateRequest):
    lk = get_lookups()
    worker = WorkerInput(
        worker_id=req.worker_id, ministry_code=req.ministry_code,
        ministry_name=req.ministry_name, droog=req.droog,
        job_pct=req.job_pct, pension_pct=req.pension_pct,
        kod_darga=req.kod_darga, darga_label=req.darga_label,
        vatek_mandatory=req.vatek_mandatory, vatek_regular=req.vatek_regular,
        vatek_msc=req.vatek_msc, vatek_calculated=req.vatek_calculated,
        calc_month=req.calc_month, retro_month=req.retro_month,
        retro_count=req.retro_count,
        components=[(c.code, c.name, c.amount, c.pensionable) for c in req.components],
    )
    result = calculate(worker, lk)
    return CalculateResponse(
        worker_id=result.worker_id, ministry_code=result.ministry_code,
        ministry_name=result.ministry_name, droog=result.droog,
        kod_darga=result.kod_darga, darga_label=result.darga_label,
        vatek_calculated=result.vatek_calculated, job_pct=result.job_pct,
        pension_pct=result.pension_pct, grade_base=result.grade_base,
        vatek_multiplier=result.vatek_multiplier,
        components=[ComponentOut(code=c.code, name=c.name, amount=c.amount,
            pensionable=c.pensionable, calculated=c.calculated,
            expected=c.expected, diff=c.diff) for c in result.components],
        total=result.total, expected_total=result.expected_total,
        total_diff=result.total_diff, total_match=result.total_match,
        errors=result.errors,
    )

@app.post("/api/accuracy", response_model=AccuracyResponse)
async def check_accuracy(file: UploadFile = File(...)):
    """Upload a גולמי Excel file. Returns accuracy % using ±1 ILS match threshold."""
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="File must be .xlsx")
    content = await file.read()
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
        tmp.write(content); tmp_path = tmp.name
    try:
        t0 = time.time()
        summary_df, _ = run_batch(tmp_path)
        elapsed = round(time.time() - t0, 1)
        total = len(summary_df)
        matched = int(summary_df["total_match"].sum())
        accuracy = round(matched / total * 100, 2) if total > 0 else 0.0
        avg_diff = round(float(summary_df["total_diff"].abs().mean()), 4)
        max_diff = round(float(summary_df["total_diff"].abs().max()), 4)
        by_ministry = (
            summary_df.groupby("ministry_name")
            .agg(workers=("worker_id", "count"), matched=("total_match", "sum"))
            .reset_index()
            .assign(accuracy_pct=lambda d: (d["matched"] / d["workers"] * 100).round(2))
            .sort_values("workers", ascending=False).head(20)
            .to_dict(orient="records")
        )
        return AccuracyResponse(
            total_workers=total, matched=matched, unmatched=total - matched,
            accuracy_pct=accuracy, match_threshold=MATCH_THRESHOLD,
            avg_diff=avg_diff, max_diff=max_diff,
            by_ministry=by_ministry, elapsed_sec=elapsed,
        )
    finally:
        os.unlink(tmp_path)

@app.post("/api/batch")
async def batch_calculate(file: UploadFile = File(...)):
    """Upload a גולמי Excel file, download full results as CSV."""
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="File must be .xlsx")
    content = await file.read()
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
        tmp.write(content); tmp_path = tmp.name
    try:
        t0 = time.time()
        summary_df, _ = run_batch(tmp_path)
        elapsed = round(time.time() - t0, 1)
        buf = io.StringIO()
        summary_df.to_csv(buf, index=False, encoding="utf-8-sig")
        buf.seek(0)
        total = len(summary_df); matched = int(summary_df["total_match"].sum())
        return StreamingResponse(
            io.BytesIO(buf.getvalue().encode("utf-8-sig")),
            media_type="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=salary_results.csv",
                "X-Workers": str(total), "X-Matched": str(matched),
                "X-Match-Pct": f"{matched/total*100:.1f}", "X-Elapsed-Sec": str(elapsed),
            },
        )
    finally:
        os.unlink(tmp_path)
