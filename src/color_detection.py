"""Color detection utilities for outfit images."""
from collections import Counter
from pathlib import Path
from typing import Iterable, Tuple


def extract_dominant_color(pixels: Iterable[Tuple[int, int, int]]) -> Tuple[int, int, int]:
    """Return the most common RGB color from a pixel iterable."""
    counts = Counter(pixels)
    if not counts:
        return (0, 0, 0)
    return counts.most_common(1)[0][0]
