import numpy as np

MIN_CONTOUR_AREA = 1000
BOX_COLOR = (0, 255, 0)
POINTER_COLOR = (0, 255, 0)
POINTER_RADIUS = 5

MODE_DRAW = "draw"
MODE_ERASE = "eraser"
MODE_IDLE = "idle"

KERNEL = np.ones((5, 5), np.uint8)