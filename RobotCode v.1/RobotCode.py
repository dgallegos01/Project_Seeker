from robotNorth import *
from picamera import PiCamera
from datetime import datetime

heading = 145
now = datetime.now() # current date and time
date_time = now.strftime("_%m_%d_%Y_%H_%M_%S")

camera = PiCamera()
camera.rotation = 180
camera.start_recording(f'/home/pi/Robot_Challenge_Recordings/RobotVideo{date_time}.h264')

while True:
    goDirection(heading)
#goNorth()
