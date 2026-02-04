"""Small utilities"""

from typing import Any

# Small helper to pick best model key by reported accuracy
def best_model_name(results):
    return max(
        results, key=lambda k: results[k].get("accuracy", results[k].get("val_accuracy", 0))
    )

class ModelTrainer:
    """Thin wrapper around a model instance to standardize fit/eval/save.

    The wrapped `model` must implement `.fit`, `.evaluate`, and `.save`.
    """

    def __init__(self, model: Any, name: str | None = None, save_path: str | None = None):
        self.model = model
        self.name = name
        self.save_path = save_path
        self.history = None

    def fit(self, *args, **kwargs):
        """Call the underlying model.fit and store the history."""
        self.history = self.model.fit(*args, **kwargs)
        return self.history

    def evaluate(self, x, y, **kwargs):
        """Evaluate the wrapped model on data and return the result."""
        return self.model.evaluate(x, y, **kwargs)

    def save(self, path: str | None = None) -> str:
        """Save the model to `path` or to the configured `save_path`.

        Returns the path used.
        """
        target = path or self.save_path
        if not target:
            raise ValueError("No path provided for save()")
        self.model.save(target)
        return target
