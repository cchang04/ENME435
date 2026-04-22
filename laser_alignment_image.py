from picamera2 import Picamera2
import cv2
import time

camera = Picamera2()
config = camera.create_video_configuration(main={"format": "BGR888", "size": (1280, 720)})
camera.configure(config)
camera.start()
time.sleep(1)

# Set up VideoWriter to save annotated frames
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, 25, (1280, 720))

print("Recording... press 'q' to stop")

while True:
    image = camera.capture_array()
    image = cv2.flip(image, -1)

    # crosshairs
    cv2.line(image, (640, 0), (640, 720), (0, 150, 150), 1)
    cv2.line(image, (0, 360), (1280, 360), (0, 150, 150), 1)

    # green vertical alignment lines
    for i in range(50, 1300, 50):
        cv2.line(image, (i, 0), (i, 720), (0, 150, 0), 3)

    # write annotated frame to video file
    out.write(image)

    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF
