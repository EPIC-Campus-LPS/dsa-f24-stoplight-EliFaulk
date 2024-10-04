import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Green Light
GPIO.setup(18, GPIO.OUT)
#Red Light
GPIO.setup(23, GPIO.OUT)
#Button
GPIO.setup(22, GPIO.IN)

#Checks for input until button is pressed
while True:
	if GPIO.input(22) == 0:
		#Green Light
		GPIO.output(18, GPIO.HIGH)
		print("Green Light")
		time.sleep(5)
		
		#Yellow Light
		GPIO.output(23, GPIO.HIGH)
		print("Yellow Light")
		time.sleep(1)
		
		#Red Light
		GPIO.output(18, GPIO.LOW)
		print("Red Light")
		time.sleep(4)
		
		#End of Cycle
		GPIO.output(23, GPIO.LOW)
		print("Done")
		break


