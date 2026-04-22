from picamera2 import Picamera2
import cv2
import time

camera = Picamera2()
config = camera.create_video_configuration(main={"format": "BGR888", "size": (1280, 720)})
camera.configure(config)

camera.set_controls({
    "AwbEnable": False,
    "ColourGains": (2.0, 1.0),
    "ExposureTime": 20000,
    "AnalogueGain": 4.0
})

camera.start()
time.sleep(1)

print("Recording... press 'q' to stop")

while True:
    image = camera.capture_array()
    image = cv2.flip(image, -1)

    # draw lines first
    cv2.line(image, (640, 0), (640, 720), (0, 150, 150), 1)
    cv2.line(image, (0, 360), (1280, 360), (0, 150, 150), 1)

    for i in range(50, 1300, 50):
        cv2.line(image, (i, 0), (i, 720), (0, 255, 0), 3)

    # then display
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

camera.stop()
cv2.destroyAllWindows()
