# !/bin/python

# Simple script for shutting down the Raspberry Pi at the press of a button.

# by Inderpreet Singh

 

import RPi.GPIO as GPIO
import time
import os
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x41)

kit.servo[10].angle = 100
kit.servo[11].angle = 115

# Use the Broadcom SOC Pin numbers

# Setup the pin with internal pullups enabled and pin in reading mode.

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

 

# Our function on what to do when the button is pressed

def Shutdown(channel):

    print("Shutting Down")

    kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[6].throttle = 0.0
    kit.continuous_servo[7].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0

    time.sleep(5)

    os.system("sudo shutdown -h now")

 

# Add our function to execute when the button pressed event happens

GPIO.add_event_detect(21, GPIO.FALLING, callback=Shutdown, bouncetime=2000)

 

# Now wait!

while 1:

    time.sleep(1)