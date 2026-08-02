import cv2 as cv
import numpy as np
from collections import deque
import time
from color_picker import create_trackbars, get_hsv_values, create_brush_color_trackbars, get_brush_color, get_brush_size
from utils import get_largest_contour, get_contour_center, create_mask
from config import *
from hud import print_hud, print_fps, draw_help_overlay
from input_handler import handle_key

# Initialize camera
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

create_trackbars()
create_brush_color_trackbars()

canvas = None
prev_point = None

points = deque(maxlen=5)

show_help = False

mode = MODE_IDLE

prev_time = time.time()

while True:

    # Read Frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read the frame.")
        break

    frame = cv.flip(frame, 1)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    if canvas is None:
        canvas = np.zeros_like(frame)

    lower, upper = get_hsv_values()

    lower = np.array(lower)
    upper = np.array(upper)

    # Create HSV Mask

    mask = create_mask(hsv, lower, upper, KERNEL)

    # Detect Contours

    contours, _ = cv.findContours(
        mask,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE
    )

    largest_contour, max_area = get_largest_contour(contours)

    brush_color = get_brush_color()
    brush_size = get_brush_size()
 
    if largest_contour is not None and max_area > MIN_CONTOUR_AREA:

        x, y, w, h = cv.boundingRect(largest_contour)

        current_point = get_contour_center(largest_contour)
        points.append(current_point)

        avg_x = sum(point[0] for point in points) // len(points)
        avg_y = sum(point[1] for point in points) // len(points)

        current_point = (avg_x, avg_y)

        if current_point is not None:

            if prev_point is None:
                prev_point = current_point

            else:

            # Draw/Erase On Canvas

                if mode != MODE_IDLE:

                    if mode == MODE_ERASE:
                        draw_color = (0, 0, 0)
                    else:
                        draw_color = brush_color

                    cv.line(
                        canvas,
                        prev_point,
                        current_point,
                        draw_color,
                        brush_size
                    )

                prev_point = current_point

            # Show Detected Object
            cv.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                BOX_COLOR,
                2
            )
            cv.circle(
                frame,
                current_point,
                brush_size//2 if brush_size else POINTER_RADIUS,
                brush_color if brush_color else POINTER_COLOR,
                -1
            )

    else:
        prev_point = None
        points.clear()

    output = frame.copy()

    gray = cv.cvtColor(canvas, cv.COLOR_BGR2GRAY)
    _, canvas_mask = cv.threshold(gray, 1, 255, cv.THRESH_BINARY)

    output[canvas_mask > 0] = canvas[canvas_mask > 0]

    output = print_hud(
        output,
        brush_color,
        brush_size,
        mode
    )

    # Calculating FPS

    current_time = time.time()
    fps = int(1 / (current_time - prev_time))
    prev_time = current_time

    # Printing FPS

    print_fps(output, fps)

    # Printing Controls if 'h' is pressed
    if show_help:
        draw_help_overlay(output)

    # Display Output

    cv.imshow("Virtual Painter", output)
    cv.imshow("Mask", mask)
    cv.imshow("Canvas", canvas_mask)

    key = cv.waitKey(1) & 0xFF

    mode, running, show_help = handle_key(
        key,
        mode,
        canvas,
        show_help
    )

    if not running:
        break

cap.release()
cv.destroyAllWindows()