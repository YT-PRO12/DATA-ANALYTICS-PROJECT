# Zomato Restaurant Data Analysis

Exploratory analysis of restaurant data in Python, focused on ratings, online ordering, restaurant types, and customer behavior.

## Project contents

- [Data analysis notebook](DATA%20ANALYTICS%20PROJECT.ipynb) — the primary analysis and visualizations.
- This repository's README explains how to review and reproduce the notebook.

## Run locally

1. Install Python 3.10 or newer and create a virtual environment.
2. Install the notebook dependencies:

   ```bash
   python -m pip install jupyter pandas matplotlib
   ```

3. Open `DATA ANALYTICS PROJECT.ipynb` in Jupyter or VS Code.
4. Check the notebook's data-loading cell and supply the referenced dataset at the expected path before running all cells.
5. Restart the kernel and run cells in order; investigate missing columns and parsing errors rather than silently changing the input data.

## Analysis questions

- How are restaurant ratings distributed?
- Do online-ordering and dining categories differ in the observed dataset?
- Which restaurant types appear most frequently?
- What patterns are visible in the data, and which might be explained by missing values or sampling?

## Reproducibility and interpretation

This is an **exploratory notebook**, not a live restaurant recommendation or a causal study. Observed patterns depend on the dataset snapshot, cleaning choices, and missing-data handling. Verify inputs and re-run all plots before quoting numbers. Do not treat ratings or correlations as proof of restaurant quality or causal effects.

No production deployment, automated data refresh, or independent statistical validation is claimed.
