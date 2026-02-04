"""Preprocessing utilities for sign_mnist data."""

from typing import Tuple, Dict

import numpy as np
import pandas as pd


def preprocess_sign_mnist(
    train_df: pd.DataFrame, test_df: pd.DataFrame, flatten: bool = False
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[int, int]]:
    """Prepare pixel arrays and remap labels to contiguous ints.

    Returns (X_train, X_train_reshaped, y_train, X_test, X_test_reshaped, y_test, label_map)
    """
    if "label" not in train_df.columns:
        raise ValueError("Expected a 'label' column in train_df")

    X_train = train_df.drop(columns=["label"]).to_numpy(dtype=np.float32) / 255.0
    y_train = train_df["label"].to_numpy()
    X_test = test_df.drop(columns=["label"]).to_numpy(dtype=np.float32) / 255.0
    y_test = test_df["label"].to_numpy()

    # Create mapping from raw labels to contiguous indices
    unique = np.unique(y_train)
    label_map = {int(v): i for i, v in enumerate(unique)}
    y_train_mapped = np.vectorize(label_map.get)(y_train).astype(np.int64)
    y_test_mapped = np.vectorize(label_map.get)(y_test).astype(np.int64)

    if flatten:
        X_train_reshaped = X_train
        X_test_reshaped = X_test
    else:
        X_train_reshaped = X_train.reshape(-1, 28, 28, 1)
        X_test_reshaped = X_test.reshape(-1, 28, 28, 1)

    return (
        X_train,
        X_train_reshaped,
        y_train_mapped,
        X_test,
        X_test_reshaped,
        y_test_mapped,
        label_map,
    )
