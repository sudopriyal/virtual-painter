import cv2 as cv

def get_largest_contour(contours):

    """Return the largest contour and its area."""

    largest_contour = None
    max_area = 0.0
    
    for contour in contours:
        area = cv.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour = contour

    return largest_contour, max_area

def get_contour_center(contour):

    """Return the center of the largest contour."""

    M = cv.moments(contour)

    if M["m00"] == 0:
        return None

    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    return (cx, cy)