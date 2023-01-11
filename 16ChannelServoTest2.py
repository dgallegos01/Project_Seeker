import time
from adafruit_servokit import ServoKit


# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16, address=0x41)
kit.continuous_servo[4].throttle = 0
kit.continuous_servo[5].throttle = 0
kit.continuous_servo[6].throttle = 0
kit.continuous_servo[7].throttle = 0
kit.continuous_servo[8].throttle = 0
kit.continuous_servo[9].throttle = 0
time.sleep(3)
kit.continuous_servo[4].throttle = -1
kit.continuous_servo[5].throttle = 1
kit.continuous_servo[6].throttle = -1
kit.continuous_servo[7].throttle = 1
kit.continuous_servo[8].throttle = 1
kit.continuous_servo[9].throttle = -1
time.sleep(1)
kit.continuous_servo[4].throttle = 0
kit.continuous_servo[5].throttle = 0
kit.continuous_servo[6].throttle = 0
kit.continuous_servo[7].throttle = 0
kit.continuous_servo[8].throttle = 0
kit.continuous_servo[9].throttle = 0
time.sleep(3)
kit.continuous_servo[4].throttle = 1
kit.continuous_servo[5].throttle = -1
kit.continuous_servo[6].throttle = 1
kit.continuous_servo[7].throttle = -1
kit.continuous_servo[8].throttle = -1
kit.continuous_servo[9].throttle = 1
time.sleep(1)
kit.continuous_servo[4].throttle = 0
kit.continuous_servo[5].throttle = 0
kit.continuous_servo[6].throttle = 0
kit.continuous_servo[7].throttle = 0
kit.continuous_servo[8].throttle = 0
kit.continuous_servo[9].throttle = 0

# kit.continuous_servo[0].throttle = 1
# time.sleep(5)
# kit.continuous_servo[0].throttle = 0
# time.sleep(2)
# kit.continuous_servo[0].throttle = -1
# time.sleep(2)
# kit.continuous_servo[0].throttle = 0

# kit.continuous_servo[0].throttle = 1
# time.sleep(5)
# kit.continuous_servo[0].throttle = 0
# time.sleep(2)
# kit.continuous_servo[0].throttle = -1
# time.sleep(2)
# kit.continuous_servo[0].throttle = 0

# kit.continuous_servo[0].throttle = 1
# time.sleep(5)
# kit.continuous_servo[0].throttle = 0
# time.sleep(2)
# kit.continuous_servo[0].throttle = -1
# time.sleep(2)
# kit.continuous_servo[0].throttle = 0