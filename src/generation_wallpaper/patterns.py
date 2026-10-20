import random
from . import config


def generate_walk(steps: int) -> list[tuple[int, int]]:
    x, y = 0, 0
    result = [(x, y)]

    for _ in range(steps):
        dx, dy = random.choice(config.DIRECTIONS)
        x += dx
        y += dy
        result.append((x, y))

    return result