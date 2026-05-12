"""Utilities for loading outfit images and labels."""
from pathlib import Path
from typing import List


def get_image_paths(directory: str | Path) -> List[Path]:
    """Return image files from a directory."""
    directory = Path(directory)
    if not directory.exists():
        return []
    return sorted([path for path in directory.rglob("*") if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}])
