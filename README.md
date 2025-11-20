# Project 2 — Optimizing Deep Learning Pipelines

This repository contains materials and starter structure for Project 2: Optimizing Deep Learning Pipelines. The goal is to explore optimizer and regularization techniques to improve model accuracy and generalization on the Sign Language MNIST dataset.

## Overview

You will build baseline and optimized neural network models and compare training behaviour and evaluation metrics. Specifically, the project covers:

- Data loading and preprocessing for the Sign Language MNIST dataset (24 classes)
- Exploration and visualization (class distributions, sample images)
- A baseline dense model (3 layers) trained with Adam
- Optimized models using different optimizers (Adam, SGD, RMSProp) and regularization (Dropout, BatchNorm, L2)
- Evaluation: accuracy/loss curves, confusion matrix, classification report
- Reflection and discussion of results and ethical considerations

Source dataset: https://www.kaggle.com/datasets/datamunge/sign-language-mnist

## Folder structure

- `src/` — Python package code. Place reusable modules and helper functions here.
  - `src/utils/` — utility functions for data loading, preprocessing, and plotting.
- `notebooks/` — Jupyter notebooks (one primary `.ipynb` with organized sections; include a README cell at the top explaining how to run it).
- `data/`
  - `data/raw/` — place original downloaded datasets here (do not commit large raw files to GitHub).
  - `data/processed/` — preprocessed data and cache files.
- `outputs/` — saved models, figures, logs, and exported results.
- `tests/` — unit and integration tests (pytest-friendly).
- `scripts/` — helper scripts for downloading data, preprocessing, or training runs.
- `docs/` — project documentation, reports, or artifacts for submission.

## Requirements & Environment

This project was designed to run within a Conda environment. Provide an `environment.yml` or `requirements.txt` for reproducibility. Typical packages include:

- python (3.8+)
- numpy, pandas
- matplotlib, seaborn
- tensorflow (or keras)
- scikit-learn
- jupyter

Example (conda) environment file should be named `requirements.yml` or `environment.yml` as requested in the assignment.

## How to run

1. Create and activate the conda environment (example):

```bash
conda env create -f environment.yml
conda activate project2
```

2. Open the primary notebook in `notebooks/` (or in Google Colab). Ensure all cells are run and outputs saved before submission.

3. Use `scripts/` to run data download or preprocessing steps if provided:

```bash
python scripts/download_data.py
python scripts/preprocess.py
```

4. Run tests:

```bash
pytest -q
```

## Deliverables

- A single `.ipynb` notebook containing code, results, and reflections (with a top README cell explaining how to run in Colab)
- Optional `.py` utility modules in `src/`
- `environment.yml` or `requirements.yml` for environment reproducibility
- README (this file)

## Notes & Best Practices

- Keep large datasets out of the repository; store only pointers or small samples.
- Commit checkpoints and model artifacts to `outputs/` or store them externally (e.g., Google Drive).
- Use `notebook.gitignore` and `.gitignore` (already provided) to avoid committing sensitive or large files, including Claude/Anthropic export files.

---

If you'd like, I can also:

- Create a sample `environment.yml` matching the required libraries
- Add a minimal example notebook skeleton under `notebooks/` with the required sections
- Add a simple example test in `tests/` and a GitHub Actions workflow to run it

Tell me which of those you want next and I will implement it.