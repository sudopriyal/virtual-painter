import cv2 as cv

def print_hud(output, brush_color, brush_size, mode):
    hud = output.copy()

# Semi-transparent Panel
    cv.rectangle(
        hud,
        (10, 10),
        (220, 260),
        (40, 40, 40),
        -1
    )
    
    output = cv.addWeighted(hud, 0.55, output, 0.45, 0)

    # Draw the border

    cv.rectangle(
        output,
        (10, 10),
        (220, 260),
        (255, 255, 255),
        2
    )

    # Add Title

    cv.putText(
        output,
        "Virtual Painter",
        (25, 35),
        cv.FONT_HERSHEY_DUPLEX,
        0.7,
        (255, 255, 255),
        1
    )

    # Brush Preview

    cv.putText(
        output,
        "Brush",
        (25, 70),
        cv.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255,255,255),
        1
    )

    cv.rectangle(
        output,
        (120, 50),
        (170, 100),
        brush_color,
        -1
    )

    cv.rectangle(
        output,
        (120, 50),
        (170, 100),
        (255,255,255),
        2
    )

    # Information

    cv.putText(
        output,
        f"Mode : {mode.capitalize()}",
        (25, 130),
        cv.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255,255,255),
        1
    )

    cv.putText(
        output,
        f"Size : {brush_size}px",
        (25, 155),
        cv.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255,255,255),
        1
    )

    # Controls

    cv.putText(output, "Controls", (25,190),
           cv.FONT_HERSHEY_SIMPLEX,0.55,(0,255,255),1)
    
    cv.putText(output, "D  Draw", (25,210),
               cv.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
    
    cv.putText(output, "E  Eraser", (25,225),
               cv.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
    
    cv.putText(output, "I  Idle", (25,240),
               cv.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
    
    cv.putText(output, "C  Clear", (110,210),
               cv.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
    
    cv.putText(output, "S  Save", (110,225),
               cv.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
    
    cv.putText(output, "Q  Quit", (110,240),
               cv.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)

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