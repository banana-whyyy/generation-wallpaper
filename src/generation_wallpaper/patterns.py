import random
from . import config


def generate_walk(
    steps: int,
    directions: tuple[tuple[float, float], ...],
) -> list[tuple[float, float]]:
    x, y = 0, 0
    result = [(x, y)]

    for _ in range(steps):
        dx, dy = random.choice(directions)
        x += dx
        y += dy
        result.append((x, y))

    return result