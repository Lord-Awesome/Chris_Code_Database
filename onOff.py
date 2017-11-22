import RPi.GPIO as GPIO
import time
try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(12, GPIO.LOW)
	while True:
		time.sleep(1)
		#print "Changing value"
		#print GPIO.input(12)
		if GPIO.input(16):
			#print "Setting high"
			GPIO.output(12, GPIO.HIGH)
			GPIO.output(16, GPIO.LOW)
		else:
			#print "Setting low"
			GPIO.output(12, GPIO.LOW)
			GPIO.output(16, GPIO.HIGH)
except Exception as ex:
	print(ex)
	#print "Error Encountered"
finally:
	GPIO.cleanup()
