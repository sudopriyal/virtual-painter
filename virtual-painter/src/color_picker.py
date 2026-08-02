import cv2 as cv


def nothing(x):
    pass


def create_trackbars():
    cv.namedWindow("Trackbars")

    cv.createTrackbar("H Min", "Trackbars", 0, 179, nothing)
    cv.createTrackbar("H Max", "Trackbars", 179, 179, nothing)

    cv.createTrackbar("S Min", "Trackbars", 0, 255, nothing)
    cv.createTrackbar("S Max", "Trackbars", 255, 255, nothing)

    cv.createTrackbar("V Min", "Trackbars", 0, 255, nothing)
    cv.createTrackbar("V Max", "Trackbars", 255, 255, nothing)

def get_hsv_values():

    h_min = cv.getTrackbarPos("H Min", "Trackbars")
    h_max = cv.getTrackbarPos("H Max", "Trackbars")

    s_min = cv.getTrackbarPos("S Min", "Trackbars")
    s_max = cv.getTrackbarPos("S Max", "Trackbars")

    v_min = cv.getTrackbarPos("V Min", "Trackbars")
    v_max = cv.getTrackbarPos("V Max", "Trackbars")

    return (
        (h_min, s_min, v_min),
        (h_max, s_max, v_max)
    )