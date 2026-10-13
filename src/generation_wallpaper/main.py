import random
from PIL import Image, ImageDraw, ImageColor
from pathlib import Path


directions = [
    (1, 0),  # вправо
    (-1, 0), # влево
    (0, 1),  # вниз
    (0, -1)  # вверх
]

PALETTES = [
    ("#7353FF", "#B36BFF", "#45D9EF"),  # фиолетовый → голубой
    ("#154D71", "#33A1CC", "#7FFFD4"),  # синий → мятный
    ("#A73D72", "#EF709D", "#FFD3A5"),  # розовый → персиковый
    ("#236B58", "#62B885", "#D5E8A0"),  # зелёный → светлый
]


def generate_walk(steps: int) -> list[tuple[int, int]]:
    x, y = 0, 0
    result = [(x, y)]

    for _ in range(steps):
        dx, dy = random.choice(directions)
        x += dx
        y += dy
        result.append((x, y))

    return result


def lerp_color(
    start: tuple[int, int, int],
    end: tuple[int, int, int],
    t: float,
) -> tuple[int, int, int]:
    return tuple(
        round(a + (b - a) * t)
        for a, b in zip(start, end)
    )


def generate_wallpaper(output_path: Path):
    steps = random.randint(10000, 30000)
    points = generate_walk(steps)
    palette = random.choice(PALETTES)

    # Границы
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)

    walk_width = max_x - min_x
    walk_height = max_y - min_y

    # Масштаб
    width, height = 1920, 1080
    padding = 150

    scale = min(
        (width - 2 * padding) / max(walk_width, 1),
        (height - 2 * padding) / max(walk_height, 1),
    )

    offset_x = (width - walk_width * scale) / 2
    offset_y = (height - walk_height * scale) / 2

    image_points = [
        (
            (x - min_x) * scale + offset_x,
            (y - min_y) * scale + offset_y,
        )
        for x, y in points
    ]

    image = Image.new("RGB", (width, height), color="#151820")
    draw = ImageDraw.Draw(image)

    colors = [ImageColor.getrgb(color) for color in palette]
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

        draw.line([start, end], fill=color, width=2)
        
    image.save(output_path)


def main():
    output_dir = Path("img")
    output_dir.mkdir(parents=True, exist_ok=True)

    for i in range(10):
        output_path = output_dir / f"wallpaper_{i + 1:03d}.png"
        generate_wallpaper(output_path)
        print(f"Сохранено: {output_path}")


if __name__ == "__main__":
    main()