# ENME489Y: Remote Sensing
from picamera2 import Picamera2
import numpy as np
import time
import cv2

# initialize camera
camera = Picamera2()
config = camera.create_video_configuration(main={"format": "RGB888", "size": (1280, 720)})
camera.configure(config)
camera.start()
time.sleep(1)

# Enter distance from wall
d = input("Please enter distance from wall, in inches: ")
print("Confirming the distance you entered is: ", d)

while True:
    image = camera.capture_array()
    image = cv2.flip(image, -1)

    # semi-crosshairs
    cv2.line(image, (640, 0), (640, 720), (0, 150, 150), 1)
    cv2.line(image, (600, 360), (1280, 360), (0, 150, 150), 1)

    # display distance
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    red = (0, 0, 255)
    cv2.putText(image, d, (800, 200), font, 10, red, 10)

    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF

    # press q to quit
    if key == ord("q"):
        break

    # press m to save jpg with distance as filename
    if key == ord("m"):
        d = int(d)
        filename = "%d.jpg" % d
        cv2.imwrite(filename, image)
        break

camera.stop()
cv2.destroyAllWindows()
