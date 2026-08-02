import cv2 as cv
import numpy as np
from color_picker import create_trackbars, get_hsv_values
from utils import get_largest_contour, get_contour_center

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

create_trackbars()

canvas = None
prev_point = None

MIN_CONTOUR_AREA = 1000
BRUSH_SIZE = 5

kernel = np.ones((5,5), np.uint8)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read the frame.")
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    if canvas is None:
        canvas = np.zeros_like(frame)

    lower, upper = get_hsv_values()

    lower = np.array(lower)
    upper = np.array(upper)

    mask = cv.inRange(hsv, lower, upper)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

    contours, _ = cv.findContours(
        mask,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE
    )

    largest_contour, max_area = get_largest_contour(contours)
    
    if largest_contour is not None and max_area > MIN_CONTOUR_AREA:

        x, y, w, h = cv.boundingRect(largest_contour)

        current_point = get_contour_center(largest_contour)

        if prev_point is None:
            prev_point = current_point

        else:
            cv.line(
                canvas,
                prev_point,
                current_point,
                (0, 255, 0),
                BRUSH_SIZE
            )

            prev_point = current_point

        cv.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
        cv.circle(
            frame,
            current_point,
            5,
            (0, 0, 255),
            -1
        )

    else:
        prev_point = None

    output = cv.add(frame, canvas)

    cv.imshow("Virtual Painter", output)
    cv.imshow("Mask", mask)

    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()