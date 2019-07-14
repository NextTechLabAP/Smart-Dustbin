import telepot
import telebot
import time

bot= telepot.Bot('812318556:AAEcVpsMRR9HE9Ee8TW3YipykpgnKU1GGL4')
#print(bot.getMe())
#print (bot.getUpdates()[-1])

a=bot.getUpdates()[-1]

#print (a)
#print(a[-1])
#commands = bot.get_updates()
#print("test")

x=(a['message']['text'])
y=str(x)
print(y)

if y == 'Come' or y== "COME"or y== "come":
  bot.sendMessage(680782323,'there in a minute')
elif y== "Go" or y== "GO" or y== "Nikal Lavde" or y== "NIKAL LAVDE" or y== "nikal lavde" or y== "NIKAL LAWDE" or y== "Nikal Lawde" or y== "nikal lawde" or y== "Nikal lawde"
  bot.sendMessage(680782323,'Thik hai Lavde')

#bot.sendMessage(680782323,'Test')
print(a)

