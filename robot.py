import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.IN) #Left IR 
GPIO.setup(3,GPIO.IN) #Right IR 

GPIO.setup(4,GPIO.OUT) # Motor 1 
GPIO.setup(14,GPIO.OUT) # Motor 1 

GPIO.setup(17,GPIO.OUT) #Motor 2
GPIO.setup(18,GPIO.OUT) # Motor 2 

GPIO.setup(24,GPIO.IN)#echo1
GPIO.setup(23,GPIO.OUT)#Trig1
GPIO.setup(16,GPIO.OUT)#Servo Motor


GPIO.setup(20,GPIO.OUT)#Trigger2
GPIO.setup(21,GPIO.IN)#Echo2

def Turn():
    GPIO.output(20, False)
    time.sleep(2)

    print( "Calculating distance")

    GPIO.output(20, True)
    time.sleep(0.00001)
    GPIO.output(20, False)

    while GPIO.input(21)==0:
        pulse_start_time = time.time()
    
    while GPIO.input(21)==1:
        pulse_end_time = time.time()
    
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    return distance
   # print ("Distance:",distance,"cm")
    
while(1):
    d=Turn()
    
    print(d)
#"Move Forward"
    if( GPIO.input(3)==True and d>30 ): 
        GPIO.output(4,True) 
        GPIO.output(14,False) 
        GPIO.output(17,True) 
        GPIO.output(18,False) 
    elif (GPIO.input(3)==True and d<30):
        GPIO.output(4,True) 
        GPIO.output(14,True) 
        GPIO.output(17,True) 
        GPIO.output(18,True)
#"Move Left"
    #elif(GPIO.input(3)==False): 
     #   GPIO.output(4,True) 
     #  GPIO.output(14,True) 
     #   GPIO.output(17,True) 
     #   GPIO.output(18,False) 
    
#"Move Right"
   # elif(  GPIO.input(3)==True): 
        #GPIO.output(4,True) 
        #GPIO.output(14,False) 
        #GPIO.output(17,True) 
        #GPIO.output(18,True) 
        
#"Stop"
    #elif (GPIO.input(3)==False): 
     #   GPIO.output(4,True) 
      #  GPIO.output(14,True) 
       # GPIO.output(17,True) 
        #GPIO.output(18,True) 
        
#"Lid Open"


def Lid():
   
    GPIO.output(23, False)
    time.sleep(2)

    print( "Calculating distance")

    GPIO.output(23, True)
    time.sleep(0.00001)
    GPIO.output(23, False)

    while GPIO.input(24)==0:
        pulse_start_time = time.time()
    
    while GPIO.input(24)==1:
        pulse_end_time = time.time()
    
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print ("Distance:",distance,"cm")
"Servo Motor"
#if distance is <50:

GPIO.cleanup()
