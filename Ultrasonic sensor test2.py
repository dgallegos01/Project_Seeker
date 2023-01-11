import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIGGER=17
ECHO=4

GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.output(TRIGGER,0)

GPIO.setup(ECHO,GPIO.IN)

time.sleep(0.1)

print("Starting measurement...")

GPIO.output(TRIGGER,1)
time.sleep(0.00001)
GPIO.output(TRIGGER,0)

while GPIO.input(ECHO) == 0:
    pass
start = time.time()

while GPIO.input(ECHO) == 1:
    pass
stop = time.time()

print((stop - start) * 17000)

GPIO.cleanup()