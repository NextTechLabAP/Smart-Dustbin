import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(7,GPIO.IN)#echo1
GPIO.setup(8,GPIO.OUT)#Trig1
GPIO.setup(16,GPIO.OUT)#Servo Motor


GPIO.setup(20,GPIO.OUT)#Trigger2
GPIO.setup(21,GPIO.IN)#Echo2

GPIO.output(8, False)
time.sleep(2)

print( "Calculating distance")

GPIO.output(8, True)
time.sleep(0.00001)
GPIO.output(8, False)

while GPIO.input(7)==0:
    pulse_start_time = time.time()
    
while GPIO.input(7)==1:
    pulse_end_time = time.time()
    
pulse_duration = pulse_end_time - pulse_start_time
distance = round(pulse_duration * 17150, 2)
print ("Distance:",distance,"cm")