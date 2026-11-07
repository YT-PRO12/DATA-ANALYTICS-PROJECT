"""Validate the committed notebook structure without executing data-dependent cells."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "DATA ANALYTICS PROJECT.ipynb"


def main():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook.get("nbformat") == 4, "Expected notebook format 4"
    cells = notebook.get("cells")
    assert isinstance(cells, list) and cells, "Notebook must contain cells"
    assert any(cell.get("cell_type") == "code" for cell in cells)

    for index, cell in enumerate(cells):
        assert cell.get("cell_type") in {"code", "markdown", "raw"}, index
        assert isinstance(cell.get("source"), (str, list)), index
        if cell["cell_type"] == "code":
            assert isinstance(cell.get("outputs"), list), index
            assert "execution_count" in cell, index

    print(f"PASS: notebook structure ({len(cells)} cells); datasets not executed")


if __name__ == "__main__":
    main()
