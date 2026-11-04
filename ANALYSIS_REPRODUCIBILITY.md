# Reproducing the restaurant analysis

Use the repository's [analysis notebook](DATA%20ANALYTICS%20PROJECT.ipynb) as the source of executed transformations and figures. Before rerunning, note the exact input dataset filename, snapshot date, source, and columns.

## Data-quality checks

1. Inspect total rows and columns immediately after loading; record missing values by column.
2. Verify rating fields are parsed consistently, especially string ratings, missing entries, and categorical labels.
3. Review duplicate rows and repeated restaurant identifiers before deduplicating.
4. Preserve a copy of the raw dataset; perform cleaning on a separate DataFrame.
5. Clearly state the denominator used in each percentage, group comparison, and chart.
6. Restart the kernel and execute all notebook cells from top to bottom to catch hidden state.

## Interpretation boundaries

Online ordering, restaurant type, and rating associations are descriptive. They do not establish causation, freshness, or restaurant recommendations. Visualizations should explicitly label units, count-based sample sizes, and missing-data exclusions.

This checklist describes a reproducible review process; it is not a claim that the notebook, external dataset, or its outputs were rerun as part of this documentation change.
