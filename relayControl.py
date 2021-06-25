import RPi.GPIO as GPIO
import time

relay = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)


while (1):
    GPIO.output(relay, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(relay, GPIO.LOW)
    time.sleep(2)
    


