"""
main.py — FastAPI application for the salary calculation engine.

Endpoints:
  GET  /                        health check
  GET  /api/info                engine metadata (loaded grades, vatek entries)
  POST /api/calculate           calculate salary for one worker
  POST /api/batch               run engine over an uploaded גולמי Excel file
  GET  /api/components          list all known salary component codes
  GET  /docs                    auto-generated Swagger UI
"""

import os
import io
import time
import tempfile
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from engine.lookups import load_lookups, get_grade_base, get_vatek_multiplier
from engine.calculator import WorkerInput, calculate
from engine.batch import load_golmi, run_batch, print_report

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(
    title="Salary Engine API",
    description="Israeli civil service salary calculation engine (מנהלי grade type)",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Load lookup tables on startup (from bundled data file)
# ---------------------------------------------------------------------------

DATA_FILE = Path(__file__).parent / "data" / "golmi.xlsx"
_lookups: dict | None = None


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
        print(f"✓ Lookups loaded — grades: {len(lk['grade'])}, vatek: {len(lk['vatek'])}")
    except Exception as e:
        print(f"✗ Failed to load lookups: {e}")


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------

class ComponentInput(BaseModel):
    code: int = Field(..., description="Salary component code (קוד רכיב שכר)")
    name: str = Field("", description="Component name (רכיב שכר)")
    amount: float = Field(0.0, description="Pre-calculated amount from raw data")
    pensionable: str = Field("כן", description="'כן' or 'לא'")


class CalculateRequest(BaseModel):
    worker_id: int = Field(..., example=11021106)
    ministry_code: int = Field(..., example=170)
    ministry_name: str = Field("", example="מכס ומע\"מ")
    droog: int = Field(1, description="Grade type (1 = מנהלי)")
    job_pct: float = Field(1.0, description="Job fraction (1.0 = full time)")
    kod_darga: int = Field(..., example=202, description="Grade code (קוד דרגה)")
    darga_label: str = Field("", example="18")
    vatek: float = Field(..., example=33.75, description="Seniority years")
    components: list[ComponentInput] = Field(
        default_factory=list,
        description="Salary components from raw data. If empty, only שכר משולב is calculated.",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "worker_id": 11021106,
                "ministry_code": 170,
                "ministry_name": "מכס ומע\"מ",
                "droog": 1,
                "job_pct": 1.0,
                "kod_darga": 202,
                "darga_label": "18",
                "vatek": 33.75,
                "components": [
                    {"code": 10002, "name": "שכר משולב", "amount": 4158.5, "pensionable": "כן"},
                    {"code": 4544,  "name": "3.6% ת. שכר", "amount": 228.77, "pensionable": "כן"},
                    {"code": 1699,  "name": "תוספת חוק מינימום", "amount": 165.29, "pensionable": "לא"},
                ],
            }
        }
    }


class ComponentResult(BaseModel):
    code: int
    name: str
    amount: float
    pensionable: bool
    calculated: bool
    expected: Optional[float]
    diff: Optional[float]


class CalculateResponse(BaseModel):
    worker_id: int
    ministry_code: int
    ministry_name: str
    droog: int
    kod_darga: int
    darga_label: str
    vatek: float
    job_pct: float
    grade_base: Optional[float]
    vatek_multiplier: Optional[float]
    components: list[ComponentResult]
    total: float
    expected_total: Optional[float]
    total_diff: Optional[float]
    errors: list[str]


class InfoResponse(BaseModel):
    status: str
    grades_loaded: int
    vatek_entries: int
    data_file: str
    version: str


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/", tags=["health"])
def health():
    return {"status": "ok", "service": "salary-engine"}


@app.get("/api/info", response_model=InfoResponse, tags=["meta"])
def info():
    lk = get_lookups()
    return InfoResponse(
        status="ok",
        grades_loaded=len(lk["grade"]),
        vatek_entries=len(lk["vatek"]),
        data_file=DATA_FILE.name,
        version="0.1.0",
    )


@app.get("/api/components", tags=["meta"])
def list_components():
    """Return all known salary component codes and their names from the reference data."""
    lk = get_lookups()
    # Pull component list from reference if available, else return known codes
    known = [
        {"code": 10002, "name": "שכר משולב",         "computed": True},
        {"code": 4544,  "name": "3.6% ת. שכר",       "computed": False},
        {"code": 4994,  "name": "תוספת 2011",         "computed": False},
        {"code": 5401,  "name": "אחוזית-2016",        "computed": False},
        {"code": 5402,  "name": "שקלית-2016",         "computed": False},
        {"code": 5524,  "name": "שקלית-2023",         "computed": False},
        {"code": 5533,  "name": "אחוזית-2024",        "computed": False},
        {"code": 4550,  "name": "תוספת 2001",         "computed": False},
        {"code": 4983,  "name": "גמול מינהל",         "computed": False},
        {"code": 647,   "name": "גמול השתלמות",       "computed": False},
        {"code": 1699,  "name": "תוספת חוק מינימום",  "computed": False},
        {"code": 741,   "name": "בוררות-מסים",        "computed": False},
        {"code": 737,   "name": "הטמעת פריון",        "computed": False},
        {"code": 738,   "name": "ת. אחוז-יום",        "computed": False},
        {"code": 705,   "name": "מקצועית מיסים",      "computed": False},
    ]
    return {"components": known, "note": "computed=true means the engine calculates from inputs; false means raw amount is used"}


@app.post("/api/calculate", response_model=CalculateResponse, tags=["calculate"])
def calculate_one(req: CalculateRequest):
    """
    Calculate the full salary for a single worker.

    Pass the worker's parameters and their list of salary components.
    Component 10002 (שכר משולב) will be computed from grade + seniority;
    all other components use the amount provided.
    """
    lk = get_lookups()

    worker = WorkerInput(
        worker_id=req.worker_id,
        ministry_code=req.ministry_code,
        ministry_name=req.ministry_name,
        droog=req.droog,
        job_pct=req.job_pct,
        kod_darga=req.kod_darga,
        darga_label=req.darga_label,
        vatek=req.vatek,
        components=[
            (c.code, c.name, c.amount, c.pensionable)
            for c in req.components
        ],
    )

    result = calculate(worker, lk)

    return CalculateResponse(
        worker_id=result.worker_id,
        ministry_code=result.ministry_code,
        ministry_name=result.ministry_name,
        droog=result.droog,
        kod_darga=result.kod_darga,
        darga_label=result.darga_label,
        vatek=result.vatek,
        job_pct=result.job_pct,
        grade_base=result.grade_base,
        vatek_multiplier=result.vatek_multiplier,
        components=[
            ComponentResult(
                code=c.code,
                name=c.name,
                amount=c.amount,
                pensionable=c.pensionable,
                calculated=c.calculated,
                expected=c.expected,
                diff=c.diff,
            )
            for c in result.components
        ],
        total=result.total,
        expected_total=result.expected_total,
        total_diff=result.total_diff,
        errors=result.errors,
    )


@app.post("/api/batch", tags=["batch"])
async def batch_calculate(file: UploadFile = File(...)):
    """
    Upload a גולמי Excel file (.xlsx) and run the engine over all workers.

    Returns a CSV file with one row per worker: totals, match status, and diffs.
    Processing ~7,000 workers takes about 10-15 seconds.
    """
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="File must be a .xlsx Excel file")

    lk = get_lookups()
    content = await file.read()

    # Write to a temp file (openpyxl needs a path)
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        t0 = time.time()
        summary_df, detail_df = run_batch(tmp_path)
        elapsed = round(time.time() - t0, 1)

        # Return summary CSV as download
        buf = io.StringIO()
        summary_df.to_csv(buf, index=False, encoding="utf-8-sig")
        buf.seek(0)

        total = len(summary_df)
        matched = int(summary_df["total_match"].sum())

        return StreamingResponse(
            io.BytesIO(buf.getvalue().encode("utf-8-sig")),
            media_type="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=salary_results.csv",
                "X-Workers": str(total),
                "X-Matched": str(matched),
                "X-Match-Pct": f"{matched/total*100:.1f}",
                "X-Elapsed-Sec": str(elapsed),
            },
        )
    finally:
        os.unlink(tmp_path)


@app.get("/api/grades", tags=["meta"])
def list_grades():
    """Return all loaded grade codes and their base salaries."""
    lk = get_lookups()
    return {
        "grades": [
            {"kod_darga": k, "base_salary": v}
            for k, v in sorted(lk["grade"].items())
        ]
    }


@app.get("/api/vatek/{years}", tags=["meta"])
def get_vatek(years: float):
    """Look up the seniority multiplier for a given number of years."""
    lk = get_lookups()
    mult = get_vatek_multiplier(lk, years)
    if mult is None:
        raise HTTPException(status_code=404, detail=f"No vatek entry for {years} years")
    return {"vatek": years, "multiplier": mult}
