import RPi.GPIO as GPIO
import subprocess

print("Stopping script...")
subprocess.run(["bash","stopperScript.sh"])

print("Cleaning GPIO's...")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.cleanup()

print("CONTROL_stop.py is done!")
