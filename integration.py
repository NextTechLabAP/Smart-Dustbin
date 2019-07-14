import telepot
import telebot
import time
import sys

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.IN) #Left IR 
GPIO.setup(3,GPIO.IN) #Right IR 

GPIO.setup(4,GPIO.OUT) # Motor 1 
GPIO.setup(14,GPIO.OUT) # Motor 1 

GPIO.setup(17,GPIO.OUT) #Motor 2
GPIO.setup(18,GPIO.OUT) # Motor 2

bot= telepot.Bot('812318556:AAEcVpsMRR9HE9Ee8TW3YipykpgnKU1GGL4')


a=bot.getUpdates()[-1]
y=(a['message']['text'])
  
if y == "Come" or y== "COME"or y== "come":
        bot.sendMessage(680782323,'there in a minute')
    
        "Move Forward"
        if(GPIO.input(2)==True and GPIO.input(3)==True):
            GPIO.output(4,True) 
            GPIO.output(14,False) 
            GPIO.output(17,True) 
            GPIO.output(18,False)
            
            
        "Stop"
        elif(GPIO.input(2)==True and GPIO.input(3)==True):
            GPIO.output(4,True) 
            GPIO.output(14,True) 
            GPIO.output(17,True) 
            GPIO.output(18,True) 
           
            

elif y== "go" or y== "Go" or y== "GO" or y== "Nikal Lavde" or y== "NIKAL LAVDE" or y== "nikal lavde" or y== "NIKAL LAWDE" or y== "Nikal Lawde" or y== "nikal lawde" or y== "Nikal lawde":
        bot.sendMessage(680782323,'Thik hai Lavde')
        "Move Right"
        if(GPIO.input(2)==False and GPIO.input(3)==True): 
            GPIO.output(4,True) 
            GPIO.output(14,False) 
            GPIO.output(17,True) 
            GPIO.output(18,True) 
            time.sleep(3)
            
            GPIO.output(4,True) 
            GPIO.output(14,False) 
            GPIO.output(17,True) 
            GPIO.output(18,False)
            
        elif (GPIO.input(2)==True and GPIO.input(3)==True):
            GPIO.output(4,True) 
            GPIO.output(14,True) 
            GPIO.output(17,True) 
            GPIO.output(18,True)