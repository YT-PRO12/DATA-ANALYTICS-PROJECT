"""Synthetic regression cases for the notebook inventory helper."""
import json
import tempfile
import unittest
from pathlib import Path

from notebook_inventory import inventory


class NotebookInventoryTests(unittest.TestCase):
    def test_repo_notebook_produces_consistent_counts(self):
        result = inventory()
        self.assertGreater(result["total_cells"], 0)
        self.assertGreater(result["code_cells"], 0)
        self.assertLessEqual(result["code_cells_with_outputs"], result["code_cells"])
        self.assertLessEqual(result["executed_code_cells"], result["code_cells"])

    def test_invalid_notebook_format_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "invalid.ipynb"
            path.write_text(json.dumps({"nbformat": 3, "cells": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                inventory(path)


if __name__ == "__main__":
    unittest.main()
