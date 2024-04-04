import random
from typing import Union

INDEX_COLORS = (
    'rgba(34, 9, 50, 1)',
    'rgba(255, 108, 50, 1)',
    'rgba(34, 60, 100, 1)',
    'rgba(234, 33, 69, 1)',
    'rgba(3, 189, 190, 1)',
)


def random_rgb():
    """Generate random RGB values."""
    return random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)


def generate_rgba(alpha: Union[float, int] = 1):
    """Generate a random rgba color string."""
    r, g, b = random_rgb()
    return f"rgba({r}, {g}, {b}, {alpha})"


def generate_index_rgba(index: int = None):
    if index is not None:
        if index < len(INDEX_COLORS):
            return INDEX_COLORS[index]

    return generate_rgba()
