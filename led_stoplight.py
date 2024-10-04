import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Red Light = 18
GPIO.setup(18, GPIO.OUT)
#Green Light = 23
GPIO.setup(23, GPIO.OUT)
#Yellow Light = 6
GPIO.setup(6, GPIO.OUT)

#Green Light for five seconds
GPIO.output(23, GPIO.HIGH)
print("Green Light")
time.sleep(5)

#Yellow Light for 1 second
GPIO.output(23, GPIO.LOW)
GPIO.output(6, GPIO.HIGH)
print("Yellow Light")
time.sleep(1)

#Red Light for 4 seconds
GPIO.output(6, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)
print("Red Light")
time.sleep(4)

#End of Program
GPIO.output(18, GPIO.LOW)
print("Done")
