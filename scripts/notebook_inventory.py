"""Report reproducible notebook structure without running any cells."""
import json
from pathlib import Path

NOTEBOOK = Path(__file__).resolve().parents[1] / "DATA ANALYTICS PROJECT.ipynb"


def inventory(path=NOTEBOOK):
    notebook = json.loads(Path(path).read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
        raise ValueError("Expected a Jupyter notebook v4 with cells")

    cells = notebook["cells"]
    code = [cell for cell in cells if cell.get("cell_type") == "code"]
    return {
        "total_cells": len(cells),
        "code_cells": len(code),
        "markdown_cells": sum(cell.get("cell_type") == "markdown" for cell in cells),
        "executed_code_cells": sum(cell.get("execution_count") is not None for cell in code),
        "code_cells_with_outputs": sum(bool(cell.get("outputs")) for cell in code),
    }


if __name__ == "__main__":
    print(json.dumps(inventory(), indent=2))
