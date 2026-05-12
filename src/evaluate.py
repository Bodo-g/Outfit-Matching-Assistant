"""Evaluation helpers for trained models."""
from typing import Any, Dict


def evaluate_model(model: Any, test_data: Any) -> Dict[str, float]:
    """Return placeholder evaluation metrics."""
    _ = model, test_data
    return {"accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
