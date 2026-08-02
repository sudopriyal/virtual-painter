import cv2 as cv

def print_hud(output, brush_color, brush_size, mode):
    hud = output.copy()

    # Compact panel
    cv.rectangle(
        hud,
        (5, 5),
        (130, 85),
        (40, 40, 40),
        -1
    )

    output = cv.addWeighted(hud, 0.55, output, 0.45, 0)

    cv.rectangle(
        output,
        (5, 5),
        (130, 85),
        (255, 255, 255),
        1
    )

    # Mode color
    if mode == "draw":
        mode_color = (0, 255, 0)
    elif mode == "eraser":
        mode_color = (0, 0, 255)
    else:
        mode_color = (0, 255, 255)

    # Mode
    cv.putText(
        output,
        mode.upper(),
        (20, 30),
        cv.FONT_HERSHEY_DUPLEX,
        0.7,
        mode_color,
        2
    )

    # Brush preview
    cv.circle(
        output,
        (30, 60),
        max(brush_size // 2, 2),
        brush_color,
        -1
    )

    cv.circle(
        output,
        (30, 60),
        max(brush_size // 2, 2),
        (255, 255, 255),
        1
    )

    cv.putText(
        output,
        f"{brush_size}px",
        (45, 65),
        cv.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        1
    )

    cv.putText(
        output,
        "[H] Help",
        (10, output.shape[0] - 15),
        cv.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255,255,255),
        1
    )

    return output

def print_fps(output, fps):

    cv.putText(
            output,
            f"FPS: {fps}",
            (output.shape[1] - 100, 30),
            cv.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 185, 0),
            2
        )

    return

def draw_help_overlay(output):

    cv.rectangle(output, (5,105), (180,220), (40,40,40), -1)
    cv.rectangle(output, (5,105), (180,220), (255,255,255), 1)

    cv.putText(output, "Controls", (15,125),
                cv.FONT_HERSHEY_SIMPLEX, 0.55, (0,255,255), 1)

    cv.putText(output, "D Draw", (15,145),
               cv.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 1)

    cv.putText(output, "E Eraser", (15,165),
               cv.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 1)

    cv.putText(output, "I Idle", (15,185),
               cv.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 1)

    cv.putText(output, "C Clear", (95,145),
               cv.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 1)

    cv.putText(output, "S Save", (95,165),
               cv.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 1)

    cv.putText(output, "Q Quit", (95,185),
               cv.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 1)