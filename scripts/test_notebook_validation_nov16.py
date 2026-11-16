"""Offline validator tests using synthetic Jupyter v4 documents."""
import json
import tempfile
import unittest
from pathlib import Path

from validate_notebook import validate_notebook


def notebook():
    return {
        "nbformat": 4,
        "cells": [
            {"id": "intro", "cell_type": "markdown", "source": ["# Introduction"]},
            {"id": "code", "cell_type": "code", "source": ["print(1)"],
             "execution_count": None, "outputs": []},
        ],
    }


class NotebookSchemaValidationTests(unittest.TestCase):
    def validate(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.ipynb"
            path.write_text(json.dumps(data), encoding="utf-8")
            return validate_notebook(path)

    def test_valid_v4_notebook_reports_cell_count(self):
        self.assertEqual(self.validate(notebook()), 2)

    def test_duplicate_cell_identifiers_are_rejected(self):
        data = notebook()
        data["cells"][1]["id"] = "intro"
        with self.assertRaisesRegex(ValueError, "duplicate cell ID"):
            self.validate(data)

    def test_code_cells_require_list_outputs(self):
        data = notebook()
        data["cells"][1]["outputs"] = "not a list"
        with self.assertRaisesRegex(ValueError, "execution metadata"):
            self.validate(data)

    def test_source_lines_must_be_strings(self):
        data = notebook()
        data["cells"][0]["source"] = [1]
        with self.assertRaisesRegex(ValueError, "Invalid source"):
            self.validate(data)


if __name__ == "__main__":
    unittest.main()
