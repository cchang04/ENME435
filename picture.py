import cv2
from picamera2 import Picamera2
from datetime import datetime

picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration..align()
picam2.configure("preview")
picam2.start()

try:
  while True:
    now = datetime.now()
    today = now.strftime("%d-%m-%Y-%H_%M_%S")

    image = picam2.capture_array()
    cv2.imshow("Camera", image)

    key = cv2.waitKey(1)
    if key == ord('s'):
      cv2.imwrite(today + ".jpg", image)
      print(today)
      print("Image saved!")

    elif key == ord('q'):
      break

finally:
  cv2.destroyAllWindows()
  picam2.stop()
  picam2.close()
