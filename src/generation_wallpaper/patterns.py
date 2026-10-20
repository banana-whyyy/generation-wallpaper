import random
from . import config
import math

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


def generate_circular_walk(
    steps: int,
    angle_step: float = math.pi / 12,
    radius_step: float = 1.0,
) -> list[tuple[float, float]]:
    radius = radius_step
    angle = 0.0
    points = [(radius_step, 0.0)]

    for _ in range(steps):
        action = random.choice(("clockwise", "counterclockwise", "out", "in"))

        if action in ("clockwise", "counterclockwise"):
            directions = 1 if action == "clockwise" else -1

            # Разбиваем дугу на короткие отрезки
            for _ in range(8):
                angle += directions * angle_step / 8
                points.append((
                    radius * math.cos(angle),
                    radius * math.sin(angle),
                ))
        else:
            if action == "out":
                radius += radius_step
            else:
                radius = max(radius_step, radius - radius_step)

            points.append((
                radius * math.cos(angle),
                radius * math.sin(angle),
            ))

    return points


def generate_pattern(
    pattern: str,
    steps: int,
) -> list[tuple[float, float]]:
    match pattern:
        case "rectangular":
            return generate_walk(steps, config.DIRECTIONS)
        case "triangular":
            return generate_walk(steps, config.TRIANGULAR_DIRECTIONS)
        case "circular":
            return generate_circular_walk(steps)
        case _:
            raise ValueError(f"Unknown pattern: {pattern}")