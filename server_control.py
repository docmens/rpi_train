#		PWM Waveform
#		============
#
# In this program a SERVO motor is controlled with a PWM signal.
#
#

# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set port 17 as an output, and set servo1 as port 17 as PWM
GPIO.setup(17,GPIO.OUT)
servo1 = GPIO.PWM(17,50) # Note 17 is port, 50 = 50Hz pulse

# start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print "waiting for 2 seconds"
time.sleep(2)

#Lets move the servo
print "Rotating 180 degrees in 10 steps" 

# Define variable duty 
duty = 2

# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 12:
	servo1.ChangeDutyCycle(duty)
	time.sleep(0.7)
	servo1.ChangeDutyCycle(0)
	time.sleep(0.3)
	duty = duty + 2

# wait a couple of seconds
time.sleep(2)

# return to zero position
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print "Goodbye"
