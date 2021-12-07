#import paho.mqtt.client as mqtt
import subprocess
import os
import time
from datetime import datetime
import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BOARD)
#switch = 7
#GPIO.setup(switch, GPIO.IN)
#switch2 = 13
#GPIO.setup(switch2, GPIO.IN)
 
# Rpi pin connected to relay ouytput at 734
read = 40
GPIO.setup(read, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.add_event_detect(read, GPIO.FALLING, callback=log, bouncetime=300)

def log(x):
	print (x) #Pin 40
	now = datetime.now() # current date and time
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	with open("data.txt",'a+') as file:
		file.write("Succesful read:LOL")
	print("HIT!!")
	#remocw add event
	#time.sleep
	#add evewnt

def start_test():
	#while GPIO.input(switch) or GPIO.input(switch2) == 0:
    # Move forward
        os.system("python3 CONTROL_backward.py")
	print("sanity check")
        os.system("python3 CONTROL_backward.py")
        time.sleep(5)
    # If message backward move backward
        os.system("python3 CONTROL_forward.py")
        os.system("python3 CONTROL_forward.py")
        time.sleep(5)

GPIO.add_event_detect(read, GPIO.FALLING, callback=log, bouncetime=6000)
i=0
while True:
	i+=1
	start_test()
	print("Cycle:%d", i)

