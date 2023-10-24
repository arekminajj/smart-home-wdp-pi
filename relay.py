import RPi.GPIO as GPIO

relay_ch = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_ch, GPIO.OUT)

def low():
	GPIO.output(relay_ch, GPIO.LOW)
def high():
	GPIO.output(relay_ch, GPIO.HIGH)
#GPIO.cleanup()
