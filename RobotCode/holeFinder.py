import board
import busio
import adafruit_vl53l0x
from adafruit_servokit import ServoKit
#import adafruit_ads1x15.ads1015 as ADS
#from adafruit_ads1x15.analog_in import AnalogIn
import signal
import time
import numpy as np
import math
from adafruit_motorkit import MotorKit
from compassTest import *

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)
kit = ServoKit(channels=16, address=0x41)
kit.servo[11].angle = 100 #Sets vertical angle


def largestHoleLocation(holes):
    for i in range(len(np.transpose(holes))):
        if(i==0):
            largest = i
        else:
            if(holes[0][i]>holes[0][largest]):
                largest = i
    #angle = holes[1][largest]
    return largest

def holeFinder(firstAngle, secondAngle, stepSize):
    numSteps = int((secondAngle-firstAngle)/stepSize)
    temp = (2,numSteps)
    #print(numSteps)
    blah = np.zeros(temp)#matrix to hold angles and distances
    holes = np.zeros(numSteps)#Matrix to show where holes are: \
#1 means there is a hole and 0 means no hole
    temp = (5,10)
    hLengths = np.zeros(temp) #0-hole size,1-rght side angle,2-left side angle
    #3-right side distance, 4- left side distance
    temp = (3,2)
    points = np.zeros(temp) #row represents different points. Column 0 is angle and column 1 is distance
    for i in range(0,secondAngle-firstAngle,stepSize): #loop that happens numScan times
        kit.servo[10].angle = i + firstAngle
        #time.sleep(1)
        blah[0][int(i/stepSize)] = i #Reports the angle
        blah[1][int(i/stepSize)] = sensor.range #Reports the distance
        time.sleep(0.1)
        #kit.servo[0].angle = i + firstAngle #sets the angle 
     #   print('Angle: ', blah[0][int(i/5)],'Distance: ' , blah[1][int(i/5)])
        if blah[1][int(i/stepSize)] > 8000: #Decides there is a hole if larger than 8000
            holes[int(i/stepSize)] = 1
            #print(i)
            #break
    angle1 = -100
    angle2 = -100
    state = 1
    hCounter = 0
    #print(blah)

    for j in range(1,numSteps): #finds beginning and ending angles and distances for holes
         x=0
         if state ==1:
             if holes[j] == 1:
                angle1 = blah[0][j-1]+firstAngle
                distance1 = blah[1][j-1]
                state = 0
                #print("loop1")
                #print(angle1,distance1,j)
         else:
            if holes[j] == 0:
                angle2 = blah[0][j] +firstAngle
                distance2 = blah[1][j]
                state = 1
                #print("loop2")
                #print(angle2)
                #print(angle2,distance2,j)
                if angle1==0:
                    distance1=distance2 #accounts for the fact that distance1 is originally a hole 
         #print(angle1)
         #print(angle2)
         if angle1 >= 0 and angle2 >= 0: #Calculates distance of hole
            #if angle1 < 90 and angle2 >90:
                #x1 = distance1*math.sin(math.radians(90-angle1))
                #x2 = distance2*math.sin(math.radians(angle2 - 90))
                #hLengths[0][hCounter] = x2+x1
                #hLengths[1][hCounter] = angle1
                #hLengths[2][hCounter] = angle2
                #hCounter = hCounter + 1

            #elif angle1 < 90 and angle2 <90:
                #x1 = distance1*math.cos(math.radians(angle1))
                #x2 = distance2*math.cos(math.radians(angle2))
                #hLengths[0][hCounter] = abs(x1 - x2)
                #hLengths[1][hCounter] = angle1
                #hLengths[2][hCounter] = angle2
                #hCounter = hCounter + 1
                
            #else:
                #x1 = distance1*math.cos(math.radians(180-angle1))
                #x2 = distance2*math.cos(math.radians(180-angle2))
                #hLengths[0][hCounter] = abs(x2 - x1)
                #hLengths[1][hCounter] = angle1
                #hLengths[2][hCounter] = angle2
                #hCounter = hCounter + 1
            hLengths[0][hCounter] = math.sqrt(distance1**2 + distance2**2- 2 * distance1*distance2*math.cos(math.radians(angle2-angle1)))
            hLengths[1][hCounter] = angle1
            hLengths[2][hCounter] = angle2
            hLengths[3][hCounter] = distance1
            hLengths[4][hCounter] = distance2
            hCounter = hCounter + 1

            angle1 = -100
            angle2 = -100

    i = largestHoleLocation(hLengths)
    points[0][0] = hLengths[1][i]#angle of right side of biggest hole
    points[1][0] = hLengths[2][i]#angle of left side of biggest hole
    points[0][1] = hLengths[3][i]#distance of right side of biggest hole
    points[1][1] = hLengths[4][i]#distance of left side of biggest hole
    #rAngle3 = (hLengths[1][i] +hLengths[2][i])/2#middle of hole
    #print(holes)
    
    #print(hLengths)
    turnLeft = False
    if(points[0][1] > points[1][1]):
        
        fAngle = np.arcsin((points[1][1]/hLengths[0][i])*math.sin(math.radians(points[1][0]-points[0][0])))
        #^^^ finds the angle of the farthest object
        tempDis = hLengths[0][i]/(2*math.cos(math.radians(fAngle)))
        #^^^ Distance from farthest object to desired point
        points[2][1] = points[0][1] - tempDis
        #^^^Distance from robot to desired point
        points[2][0] = points[0][0]
        #^^^ Angle where desired point is at
    else:
        fAngle = np.arcsin((points[0][1]/hLengths[0][i])*math.sin(math.radians(points[1][0]-points[0][0])))
        #^^^ finds the angle of the farthest object
        tempDis = hLengths[0][i]/(2*math.cos(math.radians(fAngle)))
        points[2][1] = points[1][1] - tempDis
        points[2][0] = points[1][0]
        turnLeft = True
    #print(blah)
    #print(points)
    #return points
    #print("return")
    #print( int(points[2][0]))
    kit.servo[10].angle = int(points[2][0])
    diff = abs(int(points[2][0])-90)
    direction = compassHeading()
    #print(direction)
    if int(points[2][0])> 90:
        direction = direction + diff
    else:
        direction = direction - diff
    return direction, points[2][1], turnLeft


#x1 = holeFinder(0,180,5)
#print("desired") 
#print(x1)
#kit.servo[10].angle=90

#print(x1)
#print(x[2])
#x2 = holeFinder(int(x1[0]),int(x1[1]),1)
#print(x2)
#kit.servo[0].angle = int(x1[2][0])

#dAngle = int(x1[2][0]) #Angle direction
#dDistance = x1[2][1]

#kit = MotorKit(0x40)

#if(dAngle <90):
    #Turns right
    #kit.motor2.throttle = -1.0
    #kit.motor1.throttle = 1.0
#else:
    #Turns left
    #kit.motor2.throttle = 1.0
    #kit.motor1.throttle = -1.0
    
#while(True):
 #   kit.motor1.throttle = 1.0

#time.sleep(5)