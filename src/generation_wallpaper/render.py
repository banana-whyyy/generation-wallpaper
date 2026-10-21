import random
from . import config

from PIL import Image, ImageDraw, ImageColor
from pathlib import Path


def lerp_color(
    start: tuple[int, int, int],
    end: tuple[int, int, int],
    t: float,
) -> tuple[int, int, int]:
    return tuple(
        round(a + (b - a) * t)
        for a, b in zip(start, end)
    )


def render_wallpaper(
    points: list[tuple[float, float]],
    output_path: Path,
) -> None:
    theme = random.choice(config.THEMES)

    # Границы
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)

    walk_width = max_x - min_x
    walk_height = max_y - min_y

    # Масштаб
    scale = min(
        (config.WIDTH - 2 * config.PADDING) / max(walk_width, 1),
        (config.HEIGHT - 2 * config.PADDING) / max(walk_height, 1),
    )

    offset_x = (config.WIDTH - walk_width * scale) / 2
    offset_y = (config.HEIGHT - walk_height * scale) / 2

    image_points = [
        (
            (x - min_x) * scale + offset_x,
            (y - min_y) * scale + offset_y,
        )
        for x, y in points
    ]

    image = Image.new(
        "RGB",
        (config.WIDTH, config.HEIGHT),
        color=theme["background"],
    )
    draw = ImageDraw.Draw(image)

    colors = [
        ImageColor.getrgb(color)
        for color in theme["colors"]
    ]
    segment_count = len(image_points) - 1

    for i, (start, end) in enumerate(
        zip(image_points, image_points[1:])
    ):
        progress = i / max(segment_count - 1, 1)

        # Положение в палитре: от 0 до 2 для трёх цветов
        position = progress * (len(colors) - 1)
        color_index = min(int(position), len(colors) - 2)
        t = position - color_index

        color = lerp_color(
            colors[color_index],
            colors[color_index + 1],
            t,
        )

        draw.line([start, end], fill=color, width=config.LINE_WIDTH)
        
    image.save(output_path)