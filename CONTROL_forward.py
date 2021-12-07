import RPi.GPIO as GPIO
from time import sleep
import subprocess
from steps import * # includes "steps" variable
from step_time import * # includes "step_time" variable

wait = step_time # 0.00065

DIR = 37
STEP = 35
CW = 1
CCW = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)
GPIO.output(DIR, CW)


try:
    for i in range(steps):
        GPIO.output(STEP,GPIO.HIGH)
        sleep(wait)
        GPIO.output(STEP,GPIO.LOW)
        sleep(wait)

except Exception as err:
    print("EXCEPTION WAS CAUGHT: \n\n", err)
    print("\n\n\ncleanup:")
    GPIO.cleanup()

finally:
    GPIO.cleanup()

