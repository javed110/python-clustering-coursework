# Clustering foundations in Python

**Portfolio category: historical learning exercise.** This repository records foundations used in later health-data research. It is presented with its original scope and execution limits.

Agglomerative hierarchical clustering and K-means on small embedded two-dimensional examples.

Start with [Clustering .ipynb](Clustering%20.ipynb).

## Reproduction

Create a dedicated Python environment and install the notebook's libraries:

```bash
python -m venv .venv
python -m pip install numpy pandas matplotlib scikit-learn jupyterlab
python -m jupyter lab
```

Restore the exact original source files and expected columns when local datasets are required. Read the notebook before executing it. These setup commands are starting instructions, not a tested dependency lock or a claim that the historical notebook is currently runnable.

## Review status and limits

The notebook uses an older AgglomerativeClustering affinity argument, unseeded K-means and a reused plot filename. Existing pull requests already address related issues; they require review. This portfolio pass does not merge those pull requests or claim a current-environment rerun.

The October 2026 portfolio review inspected notebook code, syntax, stored errors and repository contents. It did not obtain missing datasets or independently re-execute every exercise. Original teaching provenance and source links remain authoritative for attribution and dataset rights.

For applied research, see the [dental AI survey](https://github.com/javed110/dental-ai-survey-pakistan) and [causal-method benchmark](https://github.com/javed110/parvovirus-b19-causal-ml-benchmark). Those projects document their methods, uncertainty and data-access boundaries separately.
