"""
main.py — Salary Engine API v0.2 (self-contained, flat structure)
"""

import os, io, time, tempfile
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

def load_lookups(excel_path: str) -> dict:
    wb = openpyxl.load_workbook(excel_path, read_only=True, data_only=True)
    ws_darga = wb["דרגה"]
    label_to_base: dict[str, float] = {}
    for row in ws_darga.iter_rows(min_row=1, values_only=True):
        label, base = row[1], row[3]
        if label is not None and base is not None:
            label_to_base[str(label)] = float(base)
    ws_golmi = wb["גולמי"]
    kod_to_label: dict[int, str] = {}
    for row in ws_golmi.iter_rows(min_row=2, values_only=True):
        if row[0] is None:
            break
        if row[8] == 10002 and row[5] is not None and row[6] is not None:
            kod = int(row[5])
            if kod not in kod_to_label:
                kod_to_label[kod] = str(row[6])
    grade_lookup: dict[int, float] = {}
    for kod, label in kod_to_label.items():
        use_plus = (kod % 10 != 0)
        lookup_label = (label + '+') if use_plus else label
        base = label_to_base.get(lookup_label) or label_to_base.get(label)
        if base is not None:
            grade_lookup[kod] = base
    ws_vatek = wb["ותק"]
    vatek_lookup: dict[float, float] = {}
    for row in ws_vatek.iter_rows(min_row=3, values_only=True):
        vatek, _, mult = row[0], row[1], row[2]
        if vatek is not None and mult is not None:
            vatek_lookup[float(vatek)] = float(mult)
    wb.close()
    return {"grade": grade_lookup, "vatek": vatek_lookup, "label_to_base": label_to_base}

def get_grade_base(lookups, kod_darga):
    return lookups["grade"].get(int(kod_darga))

def get_vatek_multiplier(lookups, vatek):
    return lookups["vatek"].get(float(vatek))

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
    grade_base = get_grade_base(lookups, worker.kod_darga)
    if grade_base is None:
        errors.append(f"Unknown kod_darga: {worker.kod_darga}")
    vatek_mult = get_vatek_multiplier(lookups, worker.vatek_calculated)
    if vatek_mult is None:
        errors.append(f"Unknown vatek: {worker.vatek_calculated}")
    for comp_code, comp_name, raw_amount, pensionable in worker.components:
        amount = raw_amount or 0.0
        calculated = False
        expected = raw_amount
        diff = None
        if comp_code == 10002:
            if grade_base is not None and vatek_mult is not None:
                computed = round(grade_base * vatek_mult * (worker.job_pct or 1.0), 2)
                diff = round(computed - (raw_amount or 0.0), 4)
                amount = computed
                calculated = True
        total += amount
        component_results.append(ComponentResult(
            code=int(comp_code), name=comp_name or "", amount=amount,
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

def load_golmi(excel_path: str) -> dict:
    wb = openpyxl.load_workbook(excel_path, read_only=True, data_only=True)
    ws = wb["גולמי"]
    workers = defaultdict(list)
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] is None:
            break
        (worker_id, ministry_code, ministry_name, droog, job_pct,
         kod_darga, darga_label, vatek,
         comp_code, comp_name, pensionable, amount) = row[:12]
        workers[worker_id].append((
            ministry_code, ministry_name, droog, job_pct,
            kod_darga, darga_label, vatek,
            comp_code, comp_name, pensionable, amount or 0.0,
        ))
    wb.close()
    return dict(workers)

def run_batch(excel_path: str) -> tuple:
    lookups = load_lookups(excel_path)
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

DATA_FILE = Path(__file__).parent / "golmi.xlsx"
FRONTEND_FILE = Path(__file__).parent / "index.html"
_lookups: Optional[dict] = None

def get_lookups() -> dict:
    global _lookups
    if _lookups is None:
        if not DATA_FILE.exists():
            raise RuntimeError(f"Reference data file not found: {DATA_FILE}")
        _lookups = load_lookups(str(DATA_FILE))
    return _lookups

@app.on_event("startup")
async def startup():
    try:
        lk = get_lookups()
        print(f"Lookups loaded — grades: {len(lk['grade'])}, vatek: {len(lk['vatek'])}")
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
    return {"status": "ok", "grades_loaded": len(lk["grade"]),
            "vatek_entries": len(lk["vatek"]), "match_threshold": MATCH_THRESHOLD, "version": "0.2.0"}

@app.get("/api/grades")
def list_grades():
    lk = get_lookups()
    return {"grades": [{"kod_darga": k, "base_salary": v} for k, v in sorted(lk["grade"].items())]}

@app.get("/api/vatek/{years}")
def get_vatek(years: float):
    lk = get_lookups()
    mult = get_vatek_multiplier(lk, years)
    if mult is None:
        raise HTTPException(status_code=404, detail=f"No vatek entry for {years} years")
    return {"vatek": years, "multiplier": mult}

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
