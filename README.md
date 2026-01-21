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

| Path | Type | Purpose / What to store |
| --- | --- | --- |
| `data/raw/` | directory | Original downloaded dataset files (CSV, ZIP). Keep raw files here and exclude from git via `.gitignore`. |
| `data/processed/` | directory | Preprocessed and cached artifacts (NumPy arrays, pickles, smaller CSVs). Safe to commit small caches; large caches can be excluded. |
| `src/` | package | Reusable project code and modules. Commit source files here. |
| `src/utils/` | package | Helper functions for data loading, preprocessing, and plotting. |
| `notebooks/` | directory | Primary Jupyter notebook(s) (e.g., `main.ipynb`). Prefer cleared outputs before committing. |
| `outputs/` | directory | Model checkpoints, figures, logs, and exported results. Large artifacts should be stored externally or added to `.gitignore`. |
| `outputs/models/` | directory | Saved model weights and checkpoints (`.h5`, `.ckpt`). |
| `tests/` | directory | Unit and integration tests (pytest). |
| `docs/` | directory | Project documentation, reports, and submission artifacts. |
| `environment.yml` | file | Conda environment specification. Commit for reproducibility. |
| `.gitignore` | file | Exclude raw data, large model artifacts, and other local files. |

Notes on storage
- Keep raw dataset files in `data/raw/` and exclude them from Git (use `.gitignore`).
- Store processed, small cache files in `data/processed/` for reproducible runs; consider excluding very large caches.
- Save large models/checkpoints and long-term artifacts in `outputs/` or external storage (Google Drive, S3); keep lightweight checkpoints in the repo only if necessary.
- Clear notebook outputs before committing to keep repo size manageable.

## Data & schema

- **Source:** Sign Language MNIST on Kaggle (https://www.kaggle.com/datasets/datamunge/sign-language-mnist). The raw CSVs included here are `sign_mnist_train.csv` and `sign_mnist_test.csv`.
- **CSV format:** first column is `label` (class index), remaining 784 columns are pixel values for a 28x28 grayscale image (row-major order). When converting to arrays we save as NumPy arrays of shape `(N, 28, 28)` or flattened `(N, 784)` depending on the pipeline step.
- **Where to store:** place original downloaded CSV/ZIP files in `data/raw/`. Put preprocessed NumPy arrays, pickles, and smaller cached artifacts in `data/processed/`.
- **Download (example using Kaggle CLI):**

```bash
# install and authenticate kaggle-cli first (https://github.com/Kaggle/kaggle-api)
kaggle datasets download -d datamunge/sign-language-mnist -p data/raw/ --unzip
```

If you cannot use the Kaggle CLI, download via the web UI and move the files into `data/raw/`.

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

## Project Components

**Data Loading & Preprocessing**
- Loaded Sign Language MNIST dataset (24 classes, letters A-Z excluding J and Z)
- Implemented data normalization and preprocessing pipeline
- Handled train/test split

**Data Augmentation**
- Implemented augmentation techniques to improve model generalization
- Applied rotation, shifts, zoom, and other transformations
- Strategically applied to training data

**Baseline Model**
- Built 3-layer dense neural network
- Trained with Adam optimizer
- Evaluated performance metrics

**Optimized Models**
- Compared multiple optimizers (Adam, SGD, RMSProp)
- Applied regularization techniques (Dropout, Batch Normalization, L2)
- Conducted hyperparameter tuning and experimentation

**Visualization & Analysis**
- Generated training/validation accuracy and loss curves
- Created confusion matrices
- Produced classification reports
- Analyzed class distribution
- Visualized sample images

**Environment Configuration**
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
- Formatting of the project structure to aid in bulk edits

## Troubleshooting

**Import Errors:** Ensure the conda environment is activated with `conda activate project2`

**Missing Data:** Download the Sign Language MNIST dataset from Kaggle and place CSV files in `data/raw/`

**Memory Issues:** If running locally with limited RAM, reduce batch sizes or use Colab with GPU runtime

**Colab Compatibility:** Upload both the notebook and dataset files when running on Colab