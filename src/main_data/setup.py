"""Environment and reproducibility helpers for the project."""

from __future__ import annotations

import random
import sys
from typing import Dict, Any

import numpy as np


def setup_environment(seed: int = 42, style: str = "seaborn-v0_8-darkgrid") -> Dict[str, Any]:
    """Set seeds and plotting style to make experiments reproducible.

    Returns a small dict of detected package versions.
    """
    random.seed(seed)
    np.random.seed(seed)

    # Try to set TensorFlow seed if available (optional)
    try:
        import tensorflow as _tf  # type: ignore

        _tf.random.set_seed(seed)
        tf_version = _tf.__version__
    except Exception:
        tf_version = None

    # Defer matplotlib import so this file stays lightweight unless plotting used
    try:
        import matplotlib

        matplotlib.style.use(style)
        mpl_version = matplotlib.__version__
    except Exception:
        mpl_version = None

    versions = {
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "matplotlib": mpl_version,
        "tensorflow": tf_version,
    }

    return versions
