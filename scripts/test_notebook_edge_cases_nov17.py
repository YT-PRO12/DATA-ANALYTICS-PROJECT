"""Negative structural tests against disposable notebook documents."""
import json
import tempfile
import unittest
from pathlib import Path

from validate_notebook import validate_notebook


def sample():
    return {"nbformat": 4, "cells": [
        {"id": "intro", "cell_type": "markdown", "source": ["# Intro"]},
        {"id": "code", "cell_type": "code", "source": ["print(1)"],
         "execution_count": None, "outputs": []},
    ]}


class NotebookEdgeCaseTests(unittest.TestCase):
    def verify(self, notebook):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic.ipynb"
            path.write_text(json.dumps(notebook), encoding="utf-8")
            return validate_notebook(path)

    def test_valid_notebook(self):
        self.assertEqual(self.verify(sample()), 2)

    def test_duplicate_ids_rejected(self):
        notebook = sample()
        notebook["cells"][1]["id"] = "intro"
        with self.assertRaisesRegex(ValueError, "duplicate cell ID"):
            self.verify(notebook)

    def test_non_string_cell_line_rejected(self):
        notebook = sample()
        notebook["cells"][0]["source"] = ["Valid", 17]
        with self.assertRaisesRegex(ValueError, "Invalid source"):
            self.verify(notebook)

    def test_non_list_code_outputs_rejected(self):
        notebook = sample()
        notebook["cells"][1]["outputs"] = {}
        with self.assertRaisesRegex(ValueError, "execution metadata"):
            self.verify(notebook)


if __name__ == "__main__":
    unittest.main()
