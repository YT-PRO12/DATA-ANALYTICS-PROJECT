"""Validate notebook structure offline without running data-dependent cells."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "DATA ANALYTICS PROJECT.ipynb"


def validate_notebook(path=NOTEBOOK):
    """Validate required Jupyter v4 structure; return the number of cells."""
    notebook = json.loads(Path(path).read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4:
        raise ValueError("Expected Jupyter notebook major version 4")

    cells = notebook.get("cells")
    if not isinstance(cells, list) or not cells:
        raise ValueError("Notebook must contain a nonempty cell list")

    code_count = 0
    ids = set()
    for index, cell in enumerate(cells):
        if not isinstance(cell, dict) or cell.get("cell_type") not in {"code", "markdown", "raw"}:
            raise ValueError(f"Invalid cell type at index {index}")
        source = cell.get("source")
        if not isinstance(source, (str, list)) or (
            isinstance(source, list) and not all(isinstance(line, str) for line in source)
        ):
            raise ValueError(f"Invalid source at cell {index}")
        cell_id = cell.get("id")
        if cell_id is not None:
            if not isinstance(cell_id, str) or not cell_id or cell_id in ids:
                raise ValueError(f"Invalid or duplicate cell ID at index {index}")
            ids.add(cell_id)
        if cell["cell_type"] == "code":
            code_count += 1
            if not isinstance(cell.get("outputs"), list) or "execution_count" not in cell:
                raise ValueError(f"Invalid code-cell execution metadata at index {index}")

    if code_count == 0:
        raise ValueError("Notebook must contain code cells")
    return len(cells)


def main():
    total = validate_notebook()
    print(f"PASS: notebook structure ({total} cells); datasets not executed")


if __name__ == "__main__":
    main()
