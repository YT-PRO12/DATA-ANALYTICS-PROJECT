"""Inspect committed Jupyter cells without executing external data sources."""
import json
from pathlib import Path

NOTEBOOK = Path(__file__).resolve().parents[1] / "DATA ANALYTICS PROJECT.ipynb"


def quality_report(path=NOTEBOOK):
    notebook = json.loads(Path(path).read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4:
        raise ValueError("Expected a Jupyter notebook version 4")
    cells = notebook.get("cells")
    if not isinstance(cells, list):
        raise ValueError("Notebook must have a cells list")
    code = [cell for cell in cells if cell.get("cell_type") == "code"]
    return {
        "code_cells": len(code),
        "unexecuted_code_cells": sum(cell.get("execution_count") is None for cell in code),
        "cells_with_error_outputs": sum(
            any(output.get("output_type") == "error" for output in cell.get("outputs", []))
            for cell in code
        ),
        "cells_with_saved_outputs": sum(bool(cell.get("outputs")) for cell in code),
    }


if __name__ == "__main__":
    print(json.dumps(quality_report(), indent=2))
