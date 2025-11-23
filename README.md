# Project 2 — Optimizing Deep Learning Pipelines

This repository contains my implementation for Project 2: Optimizing Deep Learning Pipelines. The goal of this project is to explore optimizer and regularization techniques to improve model accuracy and generalization on the Sign Language MNIST dataset.

## Overview

This project involves building baseline and optimized neural network models and comparing their training behavior and evaluation metrics. Specifically, the project covers:

- Data loading and preprocessing for the Sign Language MNIST dataset (24 classes)
- Exploration and visualization (class distributions, sample images)
- A baseline dense model (3 layers) trained with Adam optimizer
- Optimized models using different optimizers (Adam, SGD, RMSProp) and regularization techniques (Dropout, BatchNorm, L2)
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

This project was designed to run within a Conda environment. An `environment.yml` file is provided for reproducibility. Required packages include:

- python (3.8+)
- numpy, pandas
- matplotlib, seaborn
- tensorflow (or keras)
- scikit-learn
- jupyter

## How to run

### Local Setup

1. Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate project2
```

2. Open the primary notebook `main.ipynb` in the root directory. This notebook contains all the code, visualizations, and analysis.

3. Run all cells in sequence. The notebook includes:
   - Data loading and exploration
   - Baseline model implementation
   - Optimized models with various optimizers and regularization techniques
   - Data augmentation implementation
   - Performance evaluation and visualization

### Google Colab Setup

The notebook is also compatible with Google Colab:

1. Upload `main.ipynb` to Google Colab
2. Upload the dataset files to the Colab session or mount Google Drive
3. Run all cells in sequence

**Note:** This project has been tested and runs successfully in both local and Colab environments.

## Deliverables

- A single `.ipynb` notebook containing code, results, and reflections (with a top README cell explaining how to run in Colab)
- Optional `.py` utility modules in `src/`
- `environment.yml` or `requirements.yml` for environment reproducibility
- README (this file)

## Implementation Status

### Completed Components

✅ **Data Loading & Preprocessing**
- Loaded Sign Language MNIST dataset (24 classes, letters A-Z excluding J and Z)
- Implemented data normalization and preprocessing pipeline
- Handled train/test split

✅ **Data Augmentation**
- Implemented augmentation techniques to improve model generalization
- Applied rotation, shifts, zoom, and other transformations
- Strategically applied to training data

✅ **Baseline Model**
- Built 3-layer dense neural network
- Trained with Adam optimizer
- Evaluated performance metrics

✅ **Optimized Models**
- Compared multiple optimizers (Adam, SGD, RMSProp)
- Applied regularization techniques (Dropout, Batch Normalization, L2)
- Conducted hyperparameter tuning and experimentation

✅ **Visualization & Analysis**
- Generated training/validation accuracy and loss curves
- Created confusion matrices
- Produced classification reports
- Analyzed class distribution
- Visualized sample images

✅ **Environment Configuration**
- Provided complete `environment.yml` with all required dependencies
- Tested compatibility with both local and Colab environments

### Dataset Notes

- **Source:** [Sign Language MNIST on Kaggle](https://www.kaggle.com/datasets/datamunge/sign-language-mnist)
- **Classes:** 24 (A-Y, excluding J and Z which require motion)
- **Format:** 28x28 grayscale images
- **Storage:** Keep raw dataset files in `data/raw/` (excluded from git via .gitignore)

## Notes

- Large dataset files are kept out of the repository (excluded via .gitignore)
- Model checkpoints and artifacts can be stored in `outputs/` or externally (e.g., Google Drive)
- The main notebook (`main.ipynb`) is located in the root directory for easy access
- All outputs are saved in the notebook to show results without re-running computationally expensive training

## AI Use
AI was used in the following workflows
- Suggesting ideas and flow of experiments
- Ensuring answers are accurate
- Generating Graphs and function options/syntax
- Formatting and review of Analysis

## Troubleshooting

**Import Errors:** Ensure the conda environment is activated with `conda activate project2`

**Missing Data:** Download the Sign Language MNIST dataset from Kaggle and place CSV files in `data/raw/`

**Memory Issues:** If running locally with limited RAM, reduce batch sizes or use Colab with GPU runtime

**Colab Compatibility:** Upload both the notebook and dataset files when running on Colab