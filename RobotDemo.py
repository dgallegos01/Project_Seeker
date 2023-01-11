import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x41)

class RobotDemo:
    def __init__(self):
        print("""
Welcome to the Robot Demo!!

Here, you will get to control the robot rover, known as "Seeker" using the command line.

Commands for the robot:
[1] - move robot forward
[2] - move robot backward
[3] - turn robot left
[4] - turn robot right
[5] - end demo

Have Fun!!!
        """)
        session = True
        while session:
            userCommand = input("Enter a number(1-5) to control Seeker: ")
            if userCommand == "1":
                self.moveForward()

            elif userCommand == "2":
                self.moveBackward()

            elif userCommand == "3":
                self.turnLeft()

            elif userCommand == "4":
                self.turnRight()

            elif userCommand == "5":
                print("Thanks for checking out the demo!")
                session = False

            else:
                print("INVALID COMMAND!")


    def moveForward(self):
        print("Robot is moving")
        def runWheels(AmtOfTime, Acceleration):
            kit.continuous_servo[4].throttle = -Acceleration
            kit.continuous_servo[5].throttle = Acceleration
            kit.continuous_servo[6].throttle = Acceleration
            kit.continuous_servo[7].throttle = -Acceleration
            kit.continuous_servo[8].throttle = -Acceleration
            kit.continuous_servo[9].throttle = Acceleration
            time.sleep(AmtOfTime)
            kit.continuous_servo[4].throttle = 0.0
            kit.continuous_servo[5].throttle = 0.0
            kit.continuous_servo[6].throttle = 0.0
            kit.continuous_servo[7].throttle = 0.0
            kit.continuous_servo[8].throttle = 0.0
            kit.continuous_servo[9].throttle = 0.0
        
        runWheels(2, 0.5)

    def moveBackward(self):
        print("Robot is moving")
        def runWheels(AmtOfTime, Acceleration):
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
        
        runWheels(2, 0.5)

    def turnLeft(self):
        print("Robot is turning")
        for pos1 in range(92,181,8):
            time.sleep(0.2)
            kit.servo[0].angle = pos1
            kit.servo[3].angle = pos1
            kit.continuous_servo[4].throttle = -0.15
            kit.continuous_servo[9].throttle = -0.15     
        kit.continuous_servo[4].throttle = 0.0
        kit.continuous_servo[9].throttle = 0.0
        time.sleep(1)
        for pos2 in range(92,0,-9):
            time.sleep(0.2)
            kit.servo[1].angle = pos2
            kit.servo[2].angle = pos2
            kit.continuous_servo[5].throttle = 0.15
            kit.continuous_servo[8].throttle = 0.15      
        kit.continuous_servo[5].throttle = 0.0
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
            kit.servo[0].angle = pos1
            kit.servo[3].angle = pos1
            kit.continuous_servo[4].throttle = 0.15
            kit.continuous_servo[9].throttle = 0.15     
        kit.continuous_servo[4].throttle = 0.0
        kit.continuous_servo[9].throttle = 0.0
        time.sleep(1)
        for pos2 in range(0,93,9):
            time.sleep(0.2)
            kit.servo[1].angle = pos2
            kit.servo[2].angle = pos2
            kit.continuous_servo[5].throttle = -0.15
            kit.continuous_servo[8].throttle = -0.15      
        kit.continuous_servo[5].throttle = 0.0
        kit.continuous_servo[8].throttle = 0.0

    def turnRight(self):
        print("Robot is turning")
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

        time.sleep(1)
        runWheels(2, 0.5)
        time.sleep(1)

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
            time.sleep(0.1)
            kit.servo[1].angle = pos2
            kit.servo[2].angle = pos2
            kit.continuous_servo[5].throttle = -0.15
            kit.continuous_servo[8].throttle = -0.15      
        kit.continuous_servo[5].throttle = 0.0
        kit.continuous_servo[8].throttle = 0.0


robot = RobotDemo()
