import telepot
import telebot
import time
import sys

import RPi.GPIO as GPIO
def Setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)


    GPIO.setup(3,GPIO.IN) #Right IR 

    GPIO.setup(4,GPIO.OUT) # Wheel1 
    GPIO.setup(14,GPIO.OUT) # Wheel 1 

    GPIO.setup(17,GPIO.OUT) #Wheel 2
    GPIO.setup(18,GPIO.OUT) # Wheel 2 

    #GPIO.setup(24,GPIO.IN)#echo1
    #GPIO.setup(23,GPIO.OUT)#Trig1
    #GPIO.setup(16,GPIO.OUT)#Servo Motor


    GPIO.setup(20,GPIO.OUT)#Trigger2
    GPIO.setup(21,GPIO.IN)#Echo2

    #GPIO.setup(19,GPIO.OUT) #Lid Motor
    #GPIO.setup(26,GPIO.OUT) #Lid Motor
Setup()

bot= telepot.Bot('812318556:AAEcVpsMRR9HE9Ee8TW3YipykpgnKU1GGL4')

def Dist():
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

d= Dist()
print(d)
while(1):
    a=bot.getUpdates()[-1]
    time.sleep(1)
    y=(a['message']['text'])
      
    if y == "Come" or y== "COME"or y== "come":
        bot.sendMessage(680782323,'there in a minute')
        print(y)
        while(1):
            d= Dist()
            print(d)

                    #"Move Forward"
            if( GPIO.input(3)==False and d>30): 
                    GPIO.output(4,True) 
                    GPIO.output(14,False) 
                    GPIO.output(17,True) 
                    GPIO.output(18,False)
                    
            elif (GPIO.input(3)==False and d<30):
                    GPIO.output(4,True) #STOPS FOR 1 SEC IF OBSTACLE
                    GPIO.output(14,True) 
                    GPIO.output(17,True) 
                    GPIO.output(18,True)
                    time.sleep(1)
                    GPIO.output(4,True) #TAKES LEFT
                    GPIO.output(14,True) 
                    GPIO.output(17,True) 
                    GPIO.output(18,False)
                    time.sleep(2)
                    
                    GPIO.output(4,True) #Forward
                    GPIO.output(14,False) 
                    GPIO.output(17,True) 
                    GPIO.output(18,False)
                    
            elif(GPIO.input(3)==True):
                    GPIO.output(4,True) #stop
                    GPIO.output(14,True) 
                    GPIO.output(17,True) 
                    GPIO.output(18,True)
                   
                

    elif y== "go" or y== "Go" or y== "GO" or y== "Nikal Lavde" or y== "NIKAL LAVDE" or y== "nikal lavde" or y== "NIKAL LAWDE" or y== "Nikal Lawde" or y== "nikal lawde" or y== "Nikal lawde":
            bot.sendMessage(680782323,'Thik hai Lavde')
            print(y)
            if(GPIO.input(3)==True): 
                GPIO.output(4,True) #TAKE U TURN
                GPIO.output(14,False) 
                GPIO.output(17,True) 
                GPIO.output(18,True) 
                time.sleep(3)
            while(1):
                d= Dist()
                print(d)
                if( GPIO.input(3)==False and d>30): 
                        GPIO.output(4,True) 
                        GPIO.output(14,False) 
                        GPIO.output(17,True) 
                        GPIO.output(18,False)
                        
                elif (GPIO.input(3)==False and d<30):
                        GPIO.output(4,True) #STOPS FOR 1 SEC IF OBSTACLE
                        GPIO.output(14,True) 
                        GPIO.output(17,True) 
                        GPIO.output(18,True)
                        time.sleep(1)
                        GPIO.output(4,True) #TAKES LEFT
                        GPIO.output(14,True) 
                        GPIO.output(17,True) 
                        GPIO.output(18,False)
                        time.sleep(2)
                        
                        GPIO.output(4,True) #Forward
                        GPIO.output(14,False) 
                        GPIO.output(17,True) 
                        GPIO.output(18,False)
                        
                elif(GPIO.input(3)==True):
                        GPIO.output(4,True) #stop
                        GPIO.output(14,True) 
                        GPIO.output(17,True) 
                        GPIO.output(18,True)
         
