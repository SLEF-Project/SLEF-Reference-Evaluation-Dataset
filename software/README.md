# SLEF analysis code

Version: 1.0.0 · Date: 2026-09-30
Changelog: 1.0.0 - first public release of the code that reproduces the tables and figures of the SLEF reference-experiment paper.

This folder contains the code that recomputes every table and figure of the paper
*Can Assigned Learner States Be Recovered from Synthetic Tutoring Dialogues? A Factorial Study with SLEF*
from the released records of the SLEF Reference Evaluation Dataset, located at the repository root (`..`).
The code reads the data and makes no model calls.

## Requirements

Python 3.12 (tested), with the packages listed in `requirements.txt`:

```
python -m pip install -r requirements.txt
```

## Usage

From this folder:

```
python slef_reference_analysis.py .. --output analysis_outputs
SLEF_OUTPUTS=analysis_outputs python -m pytest test_slef_reference_analysis.py
```

The first command reads the dataset from the repository root (`..`), verifies every entry of its `SHA256SUMS.txt`
and the declared design, and writes the results to `analysis_outputs/`. The second runs six consistency tests on those results.
Add `--no-figures` to skip the figures.

`expected_outputs/` contains the results we obtained. To check your run against ours, compare the CSV files:

```
diff -r --exclude="*.json" --exclude="*.png" --exclude="*.svg" analysis_outputs expected_outputs
```

No output means the results are identical. `analysis_manifest.json` records the dataset commit, software versions,
and the script hash, so it differs between environments; figures may differ slightly between matplotlib versions.

## Outputs and where they appear in the paper

| File | Paper |
|---|---|
| `execution_summary.csv` | Table 1 |
| `dimension_summary.csv` | Table 2, Section 5.1 |
| `core_knowledge_metacognition.csv` | Table 3, Table B2 |
| `sensitivity_knowledge_metacognition.csv` | Section 5.3 |
| `class_conditional_summary.csv` | Table 4, Section 5.4 |
| `paired_channel_summary.csv`, `paired_channel_transitions.csv` | Table 5, Section 5.5 |
| `termination_metacognition_low.csv` | Section 5.6 |
| `cell_weighting_intervals.csv` | Table B1 |
| `normalized_sessions.csv` | one row per session and condition, used by all of the above |
| `figure_1_core_recovery.*`, `figure_2_metacognition_outcomes.*` | Figures 1 and 2 |

The Knowledge-by-Metacognition, task-deletion, cell-weighting and paired-channel analyses are exploratory analyses
introduced after inspection of the original results; the script reports all of them, for every condition.

## License

Copyright 2026 Marco Iannacone. The code in this folder is released under the Apache License, Version 2.0
(see `LICENSE` and `NOTICE`). The dataset at the repository root is released separately under CC BY 4.0.

## Citation

Please cite the dataset: Iannacone, M. (2026). *SLEF Reference Evaluation Dataset* [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.22930175 (all versions).
