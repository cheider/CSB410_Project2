"""Data loading helpers for the sign_mnist CSVs."""

import time
from pathlib import Path
from typing import Tuple
from functools import wraps
import pandas as pd


def time_method(func):
    """Decorator to measure and log the execution time of a method."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)  # Calls the original method
        duration = time.time() - start_time
        print(f"--- Method '{func.__name__}' took {duration:.4f} seconds ---")
        return result
    return wrapper


class DataLoader:
    def __init__(self, data_dir: str = "data/raw"):
        self.data = {}
        self.data_dir = data_dir

    def _preprocess(self, df):
        """Standard preprocessing for Sign Language MNIST CSV data."""
        # extract labels and values
        labels = df['label'].values
        values = df.drop('label', axis=1).values

        # Normalize values values to [0, 1] range
        values_normalized = values.astype('float32') / 255.0

        # Reshape for CNN input
        values_reshaped = values_normalized.reshape(-1, 28, 28, 1)

        return values, values_reshaped, labels

    def load_and_preprocess(self):
        try:
            # Load raw dataframes
            train_df, test_df = load_sign_mnist(self.data_dir)

            # Process Train and Test sets
            X_train, X_train_reshaped, y_train = self._preprocess(train_df)
            X_test, X_test_reshaped, y_test = self._preprocess(test_df)

            self.data = {
                'X_train': X_train,
                'X_train_reshaped': X_train_reshaped,
                'y_train': y_train,
                'X_test': X_test,
                'X_test_reshaped': X_test_reshaped,
                'y_test': y_test
            }

            print(f"Preprocessed: Train {X_train_reshaped.shape}, Test {X_test_reshaped.shape}")
            return self.data

        except FileNotFoundError as e:
            print(f"File Error: {e}")
            return None


def load_sign_mnist(data_dir: str = "data/raw") -> Tuple[pd.DataFrame,
                                                         pd.DataFrame]:
    """Load sign_mnist train and test CSV files from `data_dir`.

    Raises FileNotFoundError if the expected CSVs are not present.
    """
    base = Path(data_dir)
    train_file = base / "sign_mnist_train.csv"
    test_file = base / "sign_mnist_test.csv"

    if not train_file.exists():
        raise FileNotFoundError(f"Missing train CSV: {train_file}")
    if not test_file.exists():
        raise FileNotFoundError(f"Missing test CSV: {test_file}")

    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)

    return train_df, test_df
