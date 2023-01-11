from picamera import PiCamera
from time import sleep
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("_%m_%d_%Y_%H_%M_%S")

camera = PiCamera()
camera.rotation = 180

# camera.start_preview()
# sleep(20)
# #camera.capture('/home/pi/Desktop/image.jpg')
# camera.stop_preview()
camera.start_recording(f'/home/pi/Robot_Challenge_Recordings/RobotVideo{date_time}.h264')
sleep(10)
camera.stop_recording()