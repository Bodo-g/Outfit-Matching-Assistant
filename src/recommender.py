"""Recommendation logic for matching outfit colors."""
from typing import List, Tuple


COLOR_RULES = {
    "black": ["white", "beige", "gray"],
    "white": ["black", "navy", "blue"],
    "blue": ["white", "gray", "khaki"],
}


def recommend_colors(dominant_color: str) -> List[str]:
    """Return suggested matching colors for a detected dominant color."""
    return COLOR_RULES.get(dominant_color.lower(), ["black", "white", "gray"])
