import time
from adafruit_servokit import ServoKit
from DFRobot_RaspberryPi_DC_Motor import DFRobot_DC_Motor_IIC as Board

kit = ServoKit(channels=8)
board = Board(1, 0x10)
board.set_moter_pwm_frequency(1000)

time.sleep(5)
board.motor_movement([board.M1], board.CW, 90) # DC motor 1 movement, orientation clockwise
board.motor_movement([board.M2], board.CCW, 90) # DC motor 2 movement, orientation count-clockwise
#kit.servo[0].angle = 180
#time.sleep(4)
board.motor_stop(board.ALL)
#kit.servo[0].angle = 0
#time.sleep(2)
board.motor_movement([board.M1], board.CCW, 90) # DC motor 1 movement, orientation clockwise
board.motor_movement([board.M2], board.CW, 90) # DC motor 2 movement, orientation count-clockwise
#kit.servo[0].angle = 92
#time.sleep(4)
board.motor_stop(board.ALL)