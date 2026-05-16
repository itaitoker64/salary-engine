"""
calculator.py — computes the full salary breakdown for one worker.

The salary model (grade type מנהלי / droog 1) works as follows:

  שכר משולב (combined base, code 10002):
    = grade_base(kod_darga) × vatek_multiplier(vatek) × job_pct

  All other components are stored as pre-calculated amounts in the raw data.
  The engine takes those amounts as-is and sums them for the total salary.

  In the future, once we reverse-engineer each component's formula,
  this module will compute them from scratch instead.
"""

from dataclasses import dataclass, field
from typing import Optional
from .lookups import get_grade_base, get_vatek_multiplier


@dataclass
class WorkerInput:
    """All input parameters needed to calculate one worker's salary."""
    worker_id: int
    ministry_code: int
    ministry_name: str
    droog: int                  # grade type (קוד דרוג) — 1 = מנהלי
    job_pct: float              # חלקיות חודש משרה (1.0 = full time)
    kod_darga: int              # grade code (קוד דרגה)
    darga_label: str            # grade label (דרגה), e.g. '18', '19+'
    vatek: float                # seniority years (ותק לחישוב שכר)
    # Components from raw data: list of (component_code, component_name, amount, pensionable)
    components: list = field(default_factory=list)


@dataclass
class ComponentResult:
    """One salary component in the output breakdown."""
    code: int
    name: str
    amount: float
    pensionable: bool
    calculated: bool            # True = we computed it; False = taken from raw data
    expected: Optional[float] = None   # raw data amount (for verification)
    diff: Optional[float] = None


@dataclass
class SalaryResult:
    """Full salary calculation result for one worker."""
    worker_id: int
    ministry_code: int
    ministry_name: str
    droog: int
    kod_darga: int
    darga_label: str
    vatek: float
    job_pct: float
    components: list[ComponentResult]
    total: float
    expected_total: Optional[float] = None
    total_diff: Optional[float] = None
    grade_base: Optional[float] = None
    vatek_multiplier: Optional[float] = None
    errors: list[str] = field(default_factory=list)


def calculate(worker: WorkerInput, lookups: dict) -> SalaryResult:
    """
    Calculate the full salary for one worker.

    Currently computes שכר משולב (code 10002) from grade + seniority tables,
    and takes all other components directly from the raw data amounts.
    """
    errors = []
    component_results = []
    total = 0.0

    # Look up grade base salary
    grade_base = get_grade_base(lookups, worker.kod_darga)
    if grade_base is None:
        errors.append(f"Unknown kod_darga: {worker.kod_darga}")

    vatek_mult = get_vatek_multiplier(lookups, worker.vatek)
    if vatek_mult is None:
        errors.append(f"Unknown vatek: {worker.vatek}")

    for comp_code, comp_name, raw_amount, pensionable in worker.components:
        amount = raw_amount or 0.0
        calculated = False
        expected = raw_amount
        diff = None

        if comp_code == 10002:
            # שכר משולב — calculate from grade + seniority
            if grade_base is not None and vatek_mult is not None:
                computed = round(grade_base * vatek_mult * (worker.job_pct or 1.0), 2)
                diff = round(computed - (raw_amount or 0.0), 4)
                amount = computed
                calculated = True
            else:
                amount = raw_amount or 0.0

        total += amount
        component_results.append(ComponentResult(
            code=int(comp_code),
            name=comp_name or "",
            amount=amount,
            pensionable=(pensionable == "כן"),
            calculated=calculated,
            expected=expected,
            diff=diff,
        ))

    expected_total = sum(
        (c[2] or 0.0) for c in worker.components
    )
    total_diff = round(total - expected_total, 4)

    return SalaryResult(
        worker_id=worker.worker_id,
        ministry_code=worker.ministry_code,
        ministry_name=worker.ministry_name,
        droog=worker.droog,
        kod_darga=worker.kod_darga,
        darga_label=worker.darga_label,
        vatek=worker.vatek,
        job_pct=worker.job_pct,
        components=component_results,
        total=round(total, 2),
        expected_total=round(expected_total, 2),
        total_diff=total_diff,
        grade_base=grade_base,
        vatek_multiplier=vatek_mult,
        errors=errors,
    )
