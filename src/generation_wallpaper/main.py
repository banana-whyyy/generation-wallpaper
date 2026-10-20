from .render import render_wallpaper
from .patterns import generate_pattern
import random
from . import config

from pathlib import Path




def main():
    output_dir = Path(config.OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    for i in range(config.IMAGE_COUNT):
        output_path = output_dir / f"wallpaper_{i + 1:03d}.png"
        pattern = random.choice(tuple(config.STEP_RANGES))
        min_steps, max_steps = config.STEP_RANGES[pattern]
        steps = random.randint(min_steps, max_steps)

        points = generate_pattern(pattern, steps)
        points = generate_pattern(pattern, steps)
        render_wallpaper(points, output_path)
        print(f"Сохранено: {output_path}")


if __name__ == "__main__":
    main()