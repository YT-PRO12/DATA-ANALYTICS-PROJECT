"""Fail a source-only notebook check when saved cell outputs contain errors.

This does not execute cells or claim that external datasets are available.
"""
from notebook_quality_report import quality_report


def main():
    report = quality_report()
    errors = report["cells_with_error_outputs"]
    if errors:
        raise SystemExit(f"FAIL: {errors} notebook cells contain saved error outputs")
    print(
        "PASS: no saved notebook execution errors; "
        f"{report['unexecuted_code_cells']} code cells have no execution count"
    )


if __name__ == "__main__":
    main()
