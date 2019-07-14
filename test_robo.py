import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.IN) #Left IR 
GPIO.setup(3,GPIO.IN) #Right IR 

GPIO.setup(4,GPIO.OUT) # Motor 1 
GPIO.setup(14,GPIO.OUT) # Motor 1 

GPIO.setup(17,GPIO.OUT) #Motor 2
GPIO.setup(18,GPIO.OUT) # Motor 2


"Move Forward"
#if(GPIO.input(2)==True and GPIO.input(3)==True):
GPIO.output(4,True) #1A+
GPIO.output(14,False) #1B-
GPIO.output(17,True) #2A+
GPIO.output(18,False) #2B-
time.sleep(3)

GPIO.cleanup()
    