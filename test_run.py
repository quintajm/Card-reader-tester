import os
import time
from datetime import datetime
import RPi.GPIO as GPIO
import Data_database
 
# Rpi pin connected to relay output at 734
GPIO.setmode(GPIO.BOARD)
read = 40
GPIO.setup(read, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def log(x):
	print (x) #Pin 40
	now = datetime.now() # current date and time
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	# Record data
	Data_database.log_data(date_time,"Test", i)
	print("HIT!!")

def start_test():
	# Move forward
    os.system("python3 CONTROL_backward.py")
	os.system("python3 CONTROL_backward.py")
	time.sleep(5)
	# Move backward
	os.system("python3 CONTROL_forward.py")
	os.system("python3 CONTROL_forward.py")
	time.sleep(5)

# Create interrupt pin to record data
GPIO.add_event_detect(read, GPIO.FALLING, callback=log, bouncetime=6000)
i=0
while True:
	i+=1
	start_test()
	print("Cycle:%d", i)

