import time

from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
from evdev import InputDevice, categorize, ecodes

M_kit = MotorKit(0x40) # Motor hat i2c address
S_kit = ServoKit(channels=8, address=0x41) # Servo hat i2c address

gamepad = InputDevice('/dev/input/event3')
print(gamepad)

X_Btn = 304
O_Btn = 305
Diamond_Btn = 308
Triangle_Btn = 307

up = 544
down = 545
left = 546
right = 547

start = 315
select = 314
Home = 316

LB = 310
RB = 311

lTrig = 312
rTrig = 313

S_kit.servo[0].angle = 92
time.sleep(0.5)
S_kit.servo[1].angle = 92
time.sleep(0.5)
S_kit.servo[2].angle = 92
time.sleep(0.5)
S_kit.servo[3].angle = 92

M_kit.motor1.throttle = 0.0
M_kit.motor2.throttle = 0.0



for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == Triangle_Btn:
                print("Triangle")
            elif event.code == O_Btn:
                print("Circle")
            elif event.code == X_Btn:
                print("X")
            elif event.code == Diamond_Btn:
                print("Diamond")

            elif event.code == up:
                print("up")
                # M_kit.motor1.throttle = 1.0
                # M_kit.motor2.throttle = 1.0
            elif event.code == down:
                print("down")
                # M_kit.motor1.throttle = -1.0
                # M_kit.motor2.throttle = -1.0
            elif event.code == left:
                print("left")
                S_kit.servo[0].angle = 150
                time.sleep(0.5)
                S_kit.servo[1].angle = 150
                time.sleep(0.5)
                S_kit.servo[2].angle = 30
                time.sleep(0.5)
                S_kit.servo[3].angle = 30
                
            elif event.code == right:
                print("right")
                S_kit.servo[0].angle = 30
                time.sleep(0.5)
                S_kit.servo[1].angle = 30
                time.sleep(0.5)
                S_kit.servo[2].angle = 150
                time.sleep(0.5)
                S_kit.servo[3].angle = 150


            elif event.code == start:
                print("start")
            elif event.code == select:
                print("select")
            elif event.code == Home:
                print("Home")
                quit()

            elif event.code == lTrig:
                print("left Trigger")
                M_kit.motor1.throttle = -1.0
                M_kit.motor2.throttle = -1.0
            elif event.code == rTrig:
                print("right Trigger")
                M_kit.motor1.throttle = 1.0
                M_kit.motor2.throttle = 1.0
            elif event.code == LB:
                print("left bumper")
            elif event.code == RB:
                print("right bumper")
        elif event.value == 0:
            if event.code == up:
                print("up")
                # M_kit.motor1.throttle = 0.0
                # M_kit.motor2.throttle = 0.0
            elif event.code == down:
                print("down")
                # M_kit.motor1.throttle = 0.0
                # M_kit.motor2.throttle = 0.0
            elif event.code == lTrig:
                print("left Trigger")
                M_kit.motor1.throttle = 0.0
                M_kit.motor2.throttle = 0.0
            elif event.code == rTrig:
                print("right Trigger")
                M_kit.motor1.throttle = 0.0
                M_kit.motor2.throttle = 0.0
            elif event.code == left:
                print("left")
                S_kit.servo[0].angle = 92
                time.sleep(0.5)
                S_kit.servo[1].angle = 92
                time.sleep(0.5)
                S_kit.servo[2].angle = 92
                time.sleep(0.5)
                S_kit.servo[3].angle = 92

            elif event.code == right:
                print("right")
                S_kit.servo[0].angle = 92
                time.sleep(0.5)
                S_kit.servo[1].angle = 92
                time.sleep(0.5)
                S_kit.servo[2].angle = 92
                time.sleep(0.5)
                S_kit.servo[3].angle = 92
