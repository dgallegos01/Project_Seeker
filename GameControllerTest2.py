#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event1')

#button code variables (change to suit your device)
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

#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
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
            elif event.code == down:
                print("down")
            elif event.code == left:
                print("left")
            elif event.code == right:
                print("right")

            elif event.code == start:
                print("start")
            elif event.code == select:
                print("select")
            elif event.code == Home:
                print("Home")
                quit()

            elif event.code == lTrig:
                print("left Trigger")
            elif event.code == rTrig:
                print("right Trigger")
            elif event.code == LB:
                print("left bumper")
            elif event.code == RB:
                print("right bumper")