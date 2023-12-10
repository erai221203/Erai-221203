import RPi.GPIO as GPIO
import time
ledPin=18
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
GPIO.setup(ledPin,GPIO.OUT)

i=0
while i<5:
    GPIO.output(ledPin,GPIO.HIGH)
    print('LED on')
    time.sleep(0.1)
    GPIO.output(ledPin,GPOI.LOW)
    print('LED off')
    time.sleep(0.5)
    i=i+1
    
