"""Fast synthetic checks; no notebook cells or external data are executed."""
import json
import tempfile
import unittest
from pathlib import Path

from scripts.notebook_quality_report import quality_report


class NotebookQualityReportTests(unittest.TestCase):
    def test_counts_executed_cells_and_saved_errors_independently(self):
        notebook = {
            "nbformat": 4,
            "cells": [
                {"cell_type": "markdown", "source": ["Introduction"]},
                {"cell_type": "code", "execution_count": 1, "outputs": [
                    {"output_type": "stream", "text": ["done"]}
                ]},
                {"cell_type": "code", "execution_count": 2, "outputs": [
                    {"output_type": "error", "ename": "ValueError"}
                ]},
                {"cell_type": "code", "execution_count": None, "outputs": []},
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic.ipynb"
            path.write_text(json.dumps(notebook), encoding="utf-8")
            self.assertEqual(quality_report(path), {
                "code_cells": 3,
                "unexecuted_code_cells": 1,
                "cells_with_error_outputs": 1,
                "cells_with_saved_outputs": 2,
            })

    def test_rejects_invalid_notebook_major_version(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.ipynb"
            path.write_text(json.dumps({"nbformat": 3, "cells": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                quality_report(path)


if __name__ == "__main__":
    unittest.main()
