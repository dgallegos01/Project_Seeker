import time
from adafruit_servokit import ServoKit
from gpiozero import DistanceSensor
from compassTest import *
#import numpy
import random
kit = ServoKit(channels=16, address=0x41)
sensor = DistanceSensor(trigger=17, echo=4)

direction = 145 # between -180-180
#objectDetection = False
def moveForward():
    
    print("Robot is moving")
    def runWheels1(AmtOfTime, Acceleration):
        objectDetection = False
        kit.continuous_servo[4].throttle = -Acceleration
        kit.continuous_servo[5].throttle = Acceleration
        kit.continuous_servo[6].throttle = Acceleration
        kit.continuous_servo[7].throttle = -Acceleration
        kit.continuous_servo[8].throttle = -Acceleration
        kit.continuous_servo[9].throttle = Acceleration
        #time.sleep(AmtOfTime)
        #print(objectDetection)
        t = time.time()
        while time.time()- t < AmtOfTime:
            distance = sensor.distance * 100
            #print(distance)
            if distance < 5: #if distance from sensor
                objectDetection = True
                print("Break")
                break
            
        #print(objectDetection)    
        kit.continuous_servo[4].throttle = 0.0
        kit.continuous_servo[5].throttle = 0.0
        kit.continuous_servo[6].throttle = 0.0
        kit.continuous_servo[7].throttle = 0.0
        kit.continuous_servo[8].throttle = 0.0
        kit.continuous_servo[9].throttle = 0.0
        time.sleep(1)

        if objectDetection :
            moveBackward()
            #HoleFinding()
            if abs(compassHeading() - direction) <10:

                rand = random.randint(1,2)
                if rand == 1:
                    turnLeft(direction - 45)
                else:
                    if(direction + 45 > 180):
                        temp = direction + 45 - 180
                        turnRight(-180 + temp)
                    else:
                        turnRight(direction + 45) 
            else:
                if compassHeading() > 0:
                    turnLeft(direction)
                else:
                    turnRight(direction)
            objectDetection = False
            moveForward()
            
    
    runWheels1(1, 0.5)
def moveBackward():
    print("Robot is moving")
    def runWheels2(AmtOfTime, Acceleration):
        kit.continuous_servo[4].throttle = Acceleration
        kit.continuous_servo[5].throttle = -Acceleration
        kit.continuous_servo[6].throttle = -Acceleration
        kit.continuous_servo[7].throttle = Acceleration
        kit.continuous_servo[8].throttle = Acceleration
        kit.continuous_servo[9].throttle = -Acceleration
        time.sleep(AmtOfTime)
        kit.continuous_servo[4].throttle = 0.0
        kit.continuous_servo[5].throttle = 0.0
        kit.continuous_servo[6].throttle = 0.0
        kit.continuous_servo[7].throttle = 0.0
        kit.continuous_servo[8].throttle = 0.0
        kit.continuous_servo[9].throttle = 0.0
        
    runWheels2(2, 0.5)
    time.sleep(1)

def turnLeft(direction):
    print("Robot is turning")
    for pos1 in range(92,181,8):
        time.sleep(0.1)
        kit.servo[0].angle = pos1
        #kit.servo[3].angle = pos1
        kit.continuous_servo[4].throttle = -0.15
        #kit.continuous_servo[9].throttle = -0.15     
    kit.continuous_servo[4].throttle = 0.0
    #kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos1 in range(92,181,8):
        time.sleep(0.1)
        #kit.servo[0].angle = pos1
        kit.servo[3].angle = pos1
        #kit.continuous_servo[4].throttle = -0.15
        kit.continuous_servo[9].throttle = -0.15     
    #kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos2 in range(92,0,-9):
        time.sleep(0.1)
        kit.servo[1].angle = pos2
        #kit.servo[2].angle = pos2
        kit.continuous_servo[5].throttle = 0.15
        #kit.continuous_servo[8].throttle = 0.15      
    kit.continuous_servo[5].throttle = 0.0
    #kit.continuous_servo[8].throttle = 0.0
    time.sleep(1)
    for pos2 in range(92,0,-9):
        time.sleep(0.1)
        #kit.servo[1].angle = pos2
        kit.servo[2].angle = pos2
        #kit.continuous_servo[5].throttle = 0.15
        kit.continuous_servo[8].throttle = 0.15      
    #kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0

    def runWheels3(AmtOfTime, Acceleration):
        kit.continuous_servo[4].throttle = -Acceleration
        kit.continuous_servo[5].throttle = -Acceleration
        kit.continuous_servo[6].throttle = -Acceleration
        kit.continuous_servo[7].throttle = -Acceleration
        kit.continuous_servo[8].throttle = -Acceleration
        kit.continuous_servo[9].throttle = -Acceleration
        while abs(compassHeading() - direction) > 5:
            pass
        #time.sleep(AmtOfTime)
        kit.continuous_servo[4].throttle = 0.0
        kit.continuous_servo[5].throttle = 0.0
        kit.continuous_servo[6].throttle = 0.0
        kit.continuous_servo[7].throttle = 0.0
        kit.continuous_servo[8].throttle = 0.0
        kit.continuous_servo[9].throttle = 0.0

    time.sleep(1)
    runWheels3(2, 0.5)
    time.sleep(1)

    for pos1 in range(180,91,-8):
        time.sleep(0.1)
        #kit.servo[0].angle = pos1
        kit.servo[3].angle = pos1
        #kit.continuous_servo[4].throttle = 0.15
        kit.continuous_servo[9].throttle = 0.15     
    #kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos1 in range(180,91,-8):
        time.sleep(0.1)
        kit.servo[0].angle = pos1
        #kit.servo[3].angle = pos1
        kit.continuous_servo[4].throttle = 0.15
        #kit.continuous_servo[9].throttle = 0.15     
    kit.continuous_servo[4].throttle = 0.0
    #kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos2 in range(0,93,9):
        time.sleep(0.1)
        #kit.servo[1].angle = pos2
        kit.servo[2].angle = pos2
        #kit.continuous_servo[5].throttle = -0.15
        kit.continuous_servo[8].throttle = -0.15      
    #kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0
    time.sleep(1)
    for pos2 in range(0,93,9):
        time.sleep(0.1)
        kit.servo[1].angle = pos2
        #kit.servo[2].angle = pos2
        kit.continuous_servo[5].throttle = -0.15
        #kit.continuous_servo[8].throttle = -0.15      
    kit.continuous_servo[5].throttle = 0.0
    #kit.continuous_servo[8].throttle = 0.0
    time.sleep(1)

def turnRight(direction):
    print("Robot is turning")
    for pos1 in range(92,181,8):
        time.sleep(0.1)
        kit.servo[0].angle = pos1
        #kit.servo[3].angle = pos1
        kit.continuous_servo[4].throttle = -0.15
        #kit.continuous_servo[9].throttle = -0.15     
    kit.continuous_servo[4].throttle = 0.0
    #kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos1 in range(92,181,8):
        time.sleep(0.1)
        #kit.servo[0].angle = pos1
        kit.servo[3].angle = pos1
        #kit.continuous_servo[4].throttle = -0.15
        kit.continuous_servo[9].throttle = -0.15     
    #kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos2 in range(92,0,-9):
        time.sleep(0.1)
        kit.servo[1].angle = pos2
        #kit.servo[2].angle = pos2
        kit.continuous_servo[5].throttle = 0.15
        #kit.continuous_servo[8].throttle = 0.15      
    kit.continuous_servo[5].throttle = 0.0
    #kit.continuous_servo[8].throttle = 0.0
    time.sleep(1)
    for pos2 in range(92,0,-9):
        time.sleep(0.1)
        #kit.servo[1].angle = pos2
        kit.servo[2].angle = pos2
        #kit.continuous_servo[5].throttle = 0.15
        kit.continuous_servo[8].throttle = 0.15      
    #kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0

    def runWheels4(AmtOfTime, Acceleration):
        kit.continuous_servo[4].throttle = Acceleration
        kit.continuous_servo[5].throttle = Acceleration
        kit.continuous_servo[6].throttle = Acceleration
        kit.continuous_servo[7].throttle = Acceleration
        kit.continuous_servo[8].throttle = Acceleration
        kit.continuous_servo[9].throttle = Acceleration
        while abs(compassHeading() - direction) > 5:
            pass
        #time.sleep(AmtOfTime)
        kit.continuous_servo[4].throttle = 0.0
        kit.continuous_servo[5].throttle = 0.0
        kit.continuous_servo[6].throttle = 0.0
        kit.continuous_servo[7].throttle = 0.0
        kit.continuous_servo[8].throttle = 0.0
        kit.continuous_servo[9].throttle = 0.0

    time.sleep(1)
    runWheels4(2, 0.5)
    time.sleep(1)

    for pos1 in range(180,91,-8):
        time.sleep(0.1)
        kit.servo[0].angle = pos1
        #kit.servo[3].angle = pos1
        kit.continuous_servo[4].throttle = 0.15
        #kit.continuous_servo[9].throttle = 0.15     
    kit.continuous_servo[4].throttle = 0.0
    #kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos1 in range(180,91,-8):
        time.sleep(0.1)
        #kit.servo[0].angle = pos1
        kit.servo[3].angle = pos1
        #kit.continuous_servo[4].throttle = 0.15
        kit.continuous_servo[9].throttle = 0.15     
    #kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos2 in range(0,93,9):
        time.sleep(0.1)
        kit.servo[1].angle = pos2
        #kit.servo[2].angle = pos2
        kit.continuous_servo[5].throttle = -0.15
        #kit.continuous_servo[8].throttle = -0.15      
    kit.continuous_servo[5].throttle = 0.0
    #kit.continuous_servo[8].throttle = 0.0
    time.sleep(1)
    for pos2 in range(0,93,9):
        time.sleep(0.1)
        #kit.servo[1].angle = pos2
        kit.servo[2].angle = pos2
        #kit.continuous_servo[5].throttle = -0.15
        kit.continuous_servo[8].throttle = -0.15      
    #kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0
    time.sleep(1)
