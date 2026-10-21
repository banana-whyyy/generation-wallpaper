import math

WIDTH = 1920
HEIGHT = 1080
PADDING = 150

LINE_WIDTH = 2

STEP_RANGES = {
    "rectangular": (10_000, 30_000),
    "triangular": (3_000, 10_000),
    "circular": (500, 1_500),
}

PATTERN = "triangular"

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


THEMES = (
    {
        "background": "#151820",
        "colors": ("#7353FF", "#B36BFF", "#45D9EF"),
    },
    {
        "background": "#101B24",
        "colors": ("#154D71", "#33A1CC", "#7FFFD4"),
    },
    {
        "background": "#21151F",
        "colors": ("#A73D72", "#EF709D", "#FFD3A5"),
    },
    {
        "background": "#101C19",
        "colors": ("#236B58", "#62B885", "#D5E8A0"),
    },
    {
        "background": "#43302E",
        "colors": ("#FFF1B5", "#C1DBE8"),
    },
    {
        "background": "#5C1E1F",
        "colors": ("#EFEAD4", "#677178"),
    },
    {
        "background": "#E2DBCC",
        "colors": ("#9E2C44", "#0F748D"),
    },
)