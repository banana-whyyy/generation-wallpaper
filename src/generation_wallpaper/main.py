from .render import render_wallpaper
from . import config

from pathlib import Path




def main():
    output_dir = Path(config.OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    for i in range(config.IMAGE_COUNT):
        output_path = output_dir / f"wallpaper_{i + 1:03d}.png"
        render_wallpaper(output_path)
        print(f"Сохранено: {output_path}")


if __name__ == "__main__":
    main()