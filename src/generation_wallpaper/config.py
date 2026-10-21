import math

WIDTH = 5740
HEIGHT = 3240
PADDING = 450

LINE_WIDTH = 6
SUPERSAMPLING = 3

STEP_RANGES = {
    "rectangular": (10_000, 30_000),
    "triangular": (3_000, 10_000),
    "circular": (1_500, 2_500),
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
        "colors": ("#9275FF", "#C084FC", "#67E8F9"),
    },
    {
        "background": "#101B24",
        "colors": ("#438FC2", "#56BFE5", "#A0F5D5"),
    },
    {
        "background": "#21151F",
        "colors": ("#CE6597", "#F49DBB", "#FFD3A5"),
    },
    {
        "background": "#101C19",
        "colors": ("#4FAD89", "#91D5A5", "#D5E8A0"),
    },
    {
        "background": "#43302E",
        "colors": ("#FFF1B5", "#C1DBE8"),
    },
    {
        "background": "#EFEAD4",
        "colors": ("#5C1E1F", "#677178"),
    },
    {
        "background": "#E2DBCC",
        "colors": ("#9E2C44", "#0F748D"),
    },
)