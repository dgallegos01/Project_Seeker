import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x41)

getAngle = 92

# def turnWheelsTest(leftRight):
#     if leftRight == True:
#         print(range(181))
#         for pos in range(92,181,8):
#             # print(pos)
#             time.sleep(0.1)
#             kit.servo[0].angle = pos
#             #kit.servo[1].angle = pos
#             kit.servo[2].angle = pos
#             #kit.servo[3].angle = pos
#             kit.continuous_servo[4].throttle = -0.1
#             kit.continuous_servo[5].throttle = -0.1
#             kit.continuous_servo[6].throttle = 0.1
#             kit.continuous_servo[7].throttle = 0.1
#         kit.continuous_servo[4].throttle = 0.0
#         kit.continuous_servo[5].throttle = 0.0
#         kit.continuous_servo[6].throttle = 0.0
#         kit.continuous_servo[7].throttle = 0.0
    
#     else:
#         print(range(181))
#         for pos in range(92,0,-9):
#             # print(pos)
#             time.sleep(0.1)
#             kit.servo[0].angle = pos
#             kit.servo[1].angle = pos
#             kit.servo[2].angle = pos
#             kit.servo[3].angle = pos
#             kit.continuous_servo[4].throttle = 0.1
#             kit.continuous_servo[5].throttle = 0.1
#             kit.continuous_servo[6].throttle = -0.1
#             kit.continuous_servo[7].throttle = -0.1
#         kit.continuous_servo[4].throttle = 0.0
#         kit.continuous_servo[5].throttle = 0.0
#         kit.continuous_servo[6].throttle = 0.0
#         kit.continuous_servo[7].throttle = 0.0

#     return pos


def turnWheels():
    print(range(181))
    for pos1 in range(92,181,8):
        time.sleep(0.1)
        kit.servo[0].angle = pos1
        kit.servo[3].angle = pos1
        kit.continuous_servo[4].throttle = -0.15
        kit.continuous_servo[9].throttle = -0.15     
    kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos2 in range(92,0,-9):
        time.sleep(0.1)
        kit.servo[1].angle = pos2
        kit.servo[2].angle = pos2
        kit.continuous_servo[5].throttle = 0.15
        kit.continuous_servo[8].throttle = 0.15      
    kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0

def runWheels(AmtOfTime, Acceleration):
    kit.continuous_servo[4].throttle = Acceleration
    kit.continuous_servo[5].throttle = Acceleration
    kit.continuous_servo[6].throttle = Acceleration
    kit.continuous_servo[7].throttle = Acceleration
    kit.continuous_servo[8].throttle = Acceleration
    kit.continuous_servo[9].throttle = Acceleration
    time.sleep(AmtOfTime)
    kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[6].throttle = 0.0
    kit.continuous_servo[7].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0
    time.sleep(AmtOfTime)
    kit.continuous_servo[4].throttle = -Acceleration
    kit.continuous_servo[5].throttle = -Acceleration
    kit.continuous_servo[6].throttle = -Acceleration
    kit.continuous_servo[7].throttle = -Acceleration
    kit.continuous_servo[8].throttle = -Acceleration
    kit.continuous_servo[9].throttle = -Acceleration
    time.sleep(AmtOfTime)
    kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[6].throttle = 0.0
    kit.continuous_servo[7].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0

def center():
    print(range(181))
    for pos1 in range(180,91,-8):
        time.sleep(0.1)
        kit.servo[0].angle = pos1
        kit.servo[3].angle = pos1
        kit.continuous_servo[4].throttle = 0.15
        kit.continuous_servo[9].throttle = 0.15     
    kit.continuous_servo[4].throttle = 0.0
    kit.continuous_servo[9].throttle = 0.0
    time.sleep(1)
    for pos2 in range(0,93,9):
        print(pos2)
        time.sleep(0.1)
        kit.servo[1].angle = pos2
        kit.servo[2].angle = pos2
        kit.continuous_servo[5].throttle = -0.15
        kit.continuous_servo[8].throttle = -0.15      
    kit.continuous_servo[5].throttle = 0.0
    kit.continuous_servo[8].throttle = 0.0

    # return pos1, pos2

# def center(angle):
#     if angle == 180:
#         print(range(181))
#         for pos in range(angle,91,-8):
#             # print(pos)
#             time.sleep(0.1)
#             kit.servo[0].angle = pos
#             kit.servo[1].angle = pos
#             kit.servo[2].angle = pos
#             kit.servo[3].angle = pos
#             kit.continuous_servo[4].throttle = 0.1
#             kit.continuous_servo[5].throttle = 0.1
#             kit.continuous_servo[6].throttle = -0.1
#             kit.continuous_servo[7].throttle = -0.1
#         kit.continuous_servo[4].throttle = 0.0
#         kit.continuous_servo[5].throttle = 0.0
#         kit.continuous_servo[6].throttle = 0.0
#         kit.continuous_servo[7].throttle = 0.0
#     else:
#         print(range(181))
#         for pos in range(angle,93,9):
#             # print(pos)
#             time.sleep(0.1)
#             kit.servo[0].angle = pos
#             kit.servo[1].angle = pos
#             kit.servo[2].angle = pos
#             kit.servo[3].angle = pos
#             kit.continuous_servo[4].throttle = -0.1
#             kit.continuous_servo[5].throttle = -0.1
#             kit.continuous_servo[6].throttle = 0.1
#             kit.continuous_servo[7].throttle = 0.1
#         kit.continuous_servo[4].throttle = 0.0
#         kit.continuous_servo[5].throttle = 0.0
#         kit.continuous_servo[6].throttle = 0.0
#         kit.continuous_servo[7].throttle = 0.0

#     return pos


#getAngle = center()
time.sleep(1)
getAngle = turnWheels()
time.sleep(1)
runWheels(1, 0.4)
time.sleep(1)
getAngle = center()
#print("The angle is: ", getAngle)
# time.sleep(2)
# getAngle = turnWheels(True)
# time.sleep(2)
# getAngle = center(getAngle)

# kit.servo[0].angle = 92
# time.sleep(3)
# turn1(False)
# turn2()
# time.sleep(1)
# turn3()
# time.sleep(1)
# turn4()