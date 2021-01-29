from time import sleep
from picamera import PiCamera
import os
from datetime import datetime

now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
snap_name = "docs/" + now + ".jpg" 
latest_name = "docs/latest.jpg"
os.makedirs(os.path.dirname(latest_name), exist_ok=True)

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.start_preview()
# Camera warm-up time
sleep(2)

# camera.capture(snap_name)
camera.capture(latest_name)
