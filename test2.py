import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x41)

#kit.servo[2].angle = 92

# kit.continuous_servo[4].throttle = -0.2
# time.sleep(1)
# kit.continuous_servo[4].throttle = 0.0
# time.sleep(1)
# kit.continuous_servo[5].throttle = 0.2
# time.sleep(1)
# kit.continuous_servo[5].throttle = 0.0

def turnLeft():
        print("Robot is turning")
        for pos1 in range(92,181,8):
            time.sleep(0.2)
            kit.servo[0].angle = pos1
            #kit.servo[3].angle = pos1
            kit.continuous_servo[4].throttle = -0.15
            #kit.continuous_servo[9].throttle = -0.15     
        kit.continuous_servo[4].throttle = 0.0
        #kit.continuous_servo[9].throttle = 0.0
        time.sleep(1)
        for pos1 in range(92,181,8):
            time.sleep(0.2)
            #kit.servo[0].angle = pos1
            kit.servo[3].angle = pos1
            #kit.continuous_servo[4].throttle = -0.15
            kit.continuous_servo[9].throttle = -0.15     
        #kit.continuous_servo[4].throttle = 0.0
        kit.continuous_servo[9].throttle = 0.0
        time.sleep(1)
        for pos2 in range(92,0,-9):
            time.sleep(0.2)
            kit.servo[1].angle = pos2
            #kit.servo[2].angle = pos2
            kit.continuous_servo[5].throttle = 0.15
            #kit.continuous_servo[8].throttle = 0.15      
        kit.continuous_servo[5].throttle = 0.0
        #kit.continuous_servo[8].throttle = 0.0
        time.sleep(1)
        for pos2 in range(92,0,-9):
            time.sleep(0.2)
            #kit.servo[1].angle = pos2
            kit.servo[2].angle = pos2
            #kit.continuous_servo[5].throttle = 0.15
            kit.continuous_servo[8].throttle = 0.15      
        #kit.continuous_servo[5].throttle = 0.0
        kit.continuous_servo[8].throttle = 0.0

        def runWheels(AmtOfTime, Acceleration):
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

        time.sleep(1)
        runWheels(2, 0.5)
        time.sleep(1)

        for pos1 in range(180,91,-8):
            time.sleep(0.2)
            #kit.servo[0].angle = pos1
            kit.servo[3].angle = pos1
            #kit.continuous_servo[4].throttle = 0.15
            kit.continuous_servo[9].throttle = 0.15     
        #kit.continuous_servo[4].throttle = 0.0
        kit.continuous_servo[9].throttle = 0.0
        time.sleep(1)
        for pos1 in range(180,91,-8):
            time.sleep(0.2)
            kit.servo[0].angle = pos1
            #kit.servo[3].angle = pos1
            kit.continuous_servo[4].throttle = 0.15
            #kit.continuous_servo[9].throttle = 0.15     
        kit.continuous_servo[4].throttle = 0.0
        #kit.continuous_servo[9].throttle = 0.0
        time.sleep(1)
        for pos2 in range(0,93,9):
            time.sleep(0.2)
            #kit.servo[1].angle = pos2
            kit.servo[2].angle = pos2
            #kit.continuous_servo[5].throttle = -0.15
            kit.continuous_servo[8].throttle = -0.15      
        #kit.continuous_servo[5].throttle = 0.0
        kit.continuous_servo[8].throttle = 0.0
        time.sleep(1)
        for pos2 in range(0,93,9):
            time.sleep(0.2)
            kit.servo[1].angle = pos2
            #kit.servo[2].angle = pos2
            kit.continuous_servo[5].throttle = -0.15
            #kit.continuous_servo[8].throttle = -0.15      
        kit.continuous_servo[5].throttle = 0.0
        #kit.continuous_servo[8].throttle = 0.0

#turnLeft()
def turnRight():
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

        time.sleep(1)
        runWheels(2, 0.5)
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

t= time.time()
while time.time()- t < 2:
    print(time.time()-t)
    #distance = sensor.distance * 100
    #if distance < 5: #if distance from sensor
    #    objectDetection = True
    #    break