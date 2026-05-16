"""
batch.py — reads the גולמי sheet, groups rows by worker, and runs the engine
over all workers. Returns a summary DataFrame and a detailed diff CSV.
"""

import openpyxl
import pandas as pd
from collections import defaultdict
from .lookups import load_lookups
from .calculator import WorkerInput, calculate


def load_golmi(excel_path: str) -> dict[int, list]:
    """
    Read the גולמי sheet and group rows by worker_id.
    Returns {worker_id: [(ministry_code, ministry_name, droog, job_pct,
                          kod_darga, darga_label, vatek,
                          comp_code, comp_name, pensionable, amount), ...]}
    """
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


def run_batch(excel_path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Run the salary engine over all workers in the file.

    Returns:
      - summary_df: one row per worker with totals and match status
      - detail_df:  one row per component with individual diffs
    """
    print("Loading lookup tables...")
    lookups = load_lookups(excel_path)
    print(f"  Grades loaded: {len(lookups['grade'])}")
    print(f"  Vatek entries: {len(lookups['vatek'])}")

    print("Loading worker data...")
    workers_raw = load_golmi(excel_path)
    print(f"  Workers: {len(workers_raw):,}")

    summary_rows = []
    detail_rows = []

    print("Running calculations...")
    for i, (worker_id, rows) in enumerate(workers_raw.items()):
        if i % 500 == 0:
            print(f"  {i:,} / {len(workers_raw):,} workers processed...")

        # Use first row for worker-level fields
        first = rows[0]
        ministry_code, ministry_name, droog, job_pct, kod_darga, darga_label, vatek = first[:7]

        components = [
            (r[7], r[8], r[10], r[9])  # (comp_code, comp_name, amount, pensionable)
            for r in rows
        ]

        worker = WorkerInput(
            worker_id=worker_id,
            ministry_code=ministry_code or 0,
            ministry_name=ministry_name or "",
            droog=droog or 1,
            job_pct=job_pct or 1.0,
            kod_darga=kod_darga or 0,
            darga_label=darga_label or "",
            vatek=vatek or 0.0,
            components=components,
        )

        result = calculate(worker, lookups)

        # Summary row
        summary_rows.append({
            "worker_id":       result.worker_id,
            "ministry_code":   result.ministry_code,
            "ministry_name":   result.ministry_name,
            "droog":           result.droog,
            "kod_darga":       result.kod_darga,
            "darga_label":     result.darga_label,
            "vatek":           result.vatek,
            "job_pct":         result.job_pct,
            "grade_base":      result.grade_base,
            "vatek_mult":      result.vatek_multiplier,
            "total_calculated":result.total,
            "total_expected":  result.expected_total,
            "total_diff":      result.total_diff,
            "total_match":     abs(result.total_diff or 0) < 0.02,
            "n_components":    len(result.components),
            "errors":          "; ".join(result.errors),
        })

        # Detail rows
        for comp in result.components:
            detail_rows.append({
                "worker_id":   result.worker_id,
                "ministry_code": result.ministry_code,
                "comp_code":   comp.code,
                "comp_name":   comp.name,
                "pensionable": comp.pensionable,
                "calculated":  comp.calculated,
                "amount":      comp.amount,
                "expected":    comp.expected,
                "diff":        comp.diff,
                "match":       abs(comp.diff or 0) < 0.02 if comp.calculated else None,
            })

    summary_df = pd.DataFrame(summary_rows)
    detail_df = pd.DataFrame(detail_rows)
    return summary_df, detail_df


def print_report(summary_df: pd.DataFrame, detail_df: pd.DataFrame):
    """Print a human-readable verification report."""
    total = len(summary_df)
    matched = summary_df["total_match"].sum()
    unmatched = total - matched

    print("\n" + "="*60)
    print("SALARY ENGINE — BATCH VERIFICATION REPORT")
    print("="*60)
    print(f"Total workers:     {total:>8,}")
    print(f"Total match:       {matched:>8,}  ({matched/total*100:.1f}%)")
    print(f"Total mismatch:    {unmatched:>8,}  ({unmatched/total*100:.1f}%)")
    print(f"Avg diff (all):    {summary_df['total_diff'].mean():>8.4f}")
    print(f"Max abs diff:      {summary_df['total_diff'].abs().max():>8.4f}")

    # שכר משולב (10002) match rate
    base_comps = detail_df[detail_df["comp_code"] == 10002]
    if len(base_comps) > 0:
        base_match = base_comps["match"].sum()
        print(f"\nשכר משולב (10002):")
        print(f"  Workers with component: {len(base_comps):,}")
        print(f"  Matched:   {base_match:,} ({base_match/len(base_comps)*100:.1f}%)")
        print(f"  Avg diff:  {base_comps['diff'].mean():.4f}")
        print(f"  Max diff:  {base_comps['diff'].abs().max():.4f}")

    # Ministry breakdown
    print("\nMatch rate by ministry (top 10 by worker count):")
    ministry_stats = summary_df.groupby("ministry_name").agg(
        workers=("worker_id", "count"),
        matched=("total_match", "sum"),
    ).sort_values("workers", ascending=False).head(10)
    ministry_stats["match_pct"] = (ministry_stats["matched"] / ministry_stats["workers"] * 100).round(1)
    print(ministry_stats.to_string())

    if len(summary_df[~summary_df["total_match"]]) > 0:
        print("\nSample mismatches:")
        mismatches = summary_df[~summary_df["total_match"]].head(5)
        for _, r in mismatches.iterrows():
            print(f"  worker={r['worker_id']} grade={r['darga_label']} "
                  f"vatek={r['vatek']} calc={r['total_calculated']:.2f} "
                  f"expected={r['total_expected']:.2f} diff={r['total_diff']:.4f}"
                  f"{' errors='+r['errors'] if r['errors'] else ''}")
