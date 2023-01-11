import time

from DFRobot_RaspberryPi_DC_Motor import DFRobot_DC_Motor_IIC as Board

board = Board(1, 0x10)

board.set_moter_pwm_frequency(1000)

board.motor_movement([board.M1], board.CW, 90) # DC motor 1 movement, orientation clockwise
board.motor_movement([board.M2], board.CCW, 90) # DC motor 2 movement, orientation count-clockwise
time.sleep(4)
board.motor_stop(board.ALL)
time.sleep(2)
board.motor_movement([board.M1], board.CCW, 90) # DC motor 1 movement, orientation clockwise
board.motor_movement([board.M2], board.CW, 90) # DC motor 2 movement, orientation count-clockwise
time.sleep(4)
board.motor_stop(board.ALL)

