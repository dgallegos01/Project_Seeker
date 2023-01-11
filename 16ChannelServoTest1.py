import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16, address=0x41)
time.sleep(1.5)
kit.continuous_servo[4].throttle = 0.4
time.sleep(1.5)
kit.continuous_servo[5].throttle = -0.4
time.sleep(1.5)
kit.continuous_servo[6].throttle = 0.4
time.sleep(1.5)
kit.continuous_servo[7].throttle = -0.4
time.sleep(1.5)
kit.continuous_servo[8].throttle = 0.4
time.sleep(1.5)
kit.continuous_servo[9].throttle = -0.4
# time.sleep(1.5)
# kit.continuous_servo[4].throttle = 0.0


time.sleep(2)
kit.servo[0].angle = 92
time.sleep(1.5)
kit.servo[1].angle = 92
time.sleep(1.5)
kit.servo[2].angle = 92
time.sleep(1.5)
kit.servo[3].angle = 92 
time.sleep(1.5)
kit.servo[0].angle = 0
time.sleep(1.5)
kit.servo[1].angle = 0
time.sleep(1.5)
kit.servo[2].angle = 0
time.sleep(1.5)
kit.servo[3].angle = 0
time.sleep(1.5)
kit.servo[0].angle = 92
time.sleep(1.5)
kit.servo[1].angle = 92
time.sleep(1.5)
kit.servo[2].angle = 92
time.sleep(1.5)
kit.servo[3].angle = 92
time.sleep(1.5)
# kit.servo[0].angle = 180
# time.sleep(1.5)
# kit.servo[1].angle = 180
# time.sleep(1.5)
# kit.servo[2].angle = 180
# time.sleep(1.5)
# kit.servo[3].angle = 180

# time.sleep(1.5)
# kit.continuous_servo[4].throttle = 0.4
time.sleep(1.5)
kit.continuous_servo[4].throttle = 0.0
time.sleep(1.5)
kit.continuous_servo[5].throttle = 0.0
time.sleep(1.5)
kit.continuous_servo[6].throttle = 0.0
time.sleep(1.5)
kit.continuous_servo[7].throttle = 0.0
time.sleep(1.5)
kit.continuous_servo[8].throttle = 0.0
time.sleep(1.5)
kit.continuous_servo[9].throttle = 0.0

