import cv2 as cv
from datetime import datetime

from config import MODE_DRAW, MODE_ERASE, MODE_IDLE

def handle_key(key, mode, canvas):

    running = True

    # Save drawing
    if key == ord('s'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/drawing_{timestamp}.png"
        cv.imwrite(filename, canvas)
        print(f"Saved: {filename}")

    # Clear Canvas
    if key == ord('c'):
        canvas[:] = 0

    # Toggle Draw Mode
    if key == ord('d'):
        mode = MODE_DRAW

    # Toggle Idle Mode
    if key == ord('i'):
        mode = MODE_IDLE

    # Toggle Eraser Mode
    if key == ord('e'):
        mode = MODE_ERASE

    # Quit Program
    if key == ord('q'):
        running = False

    return mode, running