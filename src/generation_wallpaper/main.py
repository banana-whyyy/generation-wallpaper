import random
from PIL import Image, ImageDraw
from pathlib import Path


directions = [
    (1, 0),  # вправо
    (-1, 0), # влево
    (0, 1),  # вниз
    (0, -1)  # вверх
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


def generate_wallpaper(output_path: Path):
    steps = random.randint(10000, 30000)
    points = generate_walk(steps)

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
    draw.line(image_points, fill="#9270ff", width=2)
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