"""Training entry point for the outfit matching models."""
from pathlib import Path

from src.model_scratch import build_cnn_scratch


def train(model_type: str = "scratch", output_dir: str | Path = "models"):
    """Train a model and return it."""
    _ = Path(output_dir)
    if model_type == "transfer":
        from src.model_transfer import build_transfer_model

        return build_transfer_model()
    return build_cnn_scratch()
