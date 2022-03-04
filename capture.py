import cv2 as cv
import numpy
import time

# 1. Create an object. Zero for external camera
# argument for videocapture function references to the internal camera index
video = cv.VideoCapture(0)

a = 0

while True:

    a = a + 1

    # Create a frame object and check
    check, frame = video.read()
    print(check)
    print(frame)

    # Convert frame into grayscale image
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Builder input filter
    # TODO: calibration to determine the best color to use for tracking
    # remove R B channels
    frame[:, :, 0] = 0
    frame[:, :, 1] = 0

    # filter values below certain threshold

    # Show the frame
    cv.imshow("Captureing", frame)

    # For press any key to exit
    # cv.waitKey(0)

    # For fun
    key = cv.waitKey(1)

    if key == ord('q'):
        break

print(a)

# Shutdown the camera
video.release()

cv.destroyAllWindows