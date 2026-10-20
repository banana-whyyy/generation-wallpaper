import math

WIDTH = 1920
HEIGHT = 1080
PADDING = 150

BACKGROUND_COLOR = "#151820"
LINE_WIDTH = 2

MIN_STEPS = 10_000
MAX_STEPS = 15_000
IMAGE_COUNT = 10
OUTPUT_DIR = "img"

DIRECTIONS = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)


TRIANGULAR_DIRECTIONS = (
    (1, 0),
    (-1, 0),
    (0.5, math.sqrt(3) / 2),
    (-0.5, math.sqrt(3) / 2),
    (0.5, -math.sqrt(3) / 2),
    (-0.5, -math.sqrt(3) / 2),
)


PALETTES = (
    ("#7353FF", "#B36BFF", "#45D9EF"),
    ("#154D71", "#33A1CC", "#7FFFD4"),
    ("#A73D72", "#EF709D", "#FFD3A5"),
    ("#236B58", "#62B885", "#D5E8A0"),
)