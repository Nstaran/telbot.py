import telebot
import random


bot=telebot.TeleBot("5073492003:AAHk453E3wfm_kloCVkTDQyjhRGYOTlrzZQ")

@bot.message_handler(commands=['start'])
def hello(message):
    bot.reply_to(message,"welcome my bot")

bot.infinity_polling() 


@bot.message_handler(commands=['help'])
def komak(message):
	bot.reply_to(message, "How can i heip you?")

@bot.message_handler(commands=['game'])
def bazi(message):
  bot.reply_to(message, "guess a number between o and 100")
  num=random.randint(0,100)

@bot.message_handler(commands=['age'])
def age(message):
	HBD=bot.reply_to(message,"Please enter your birth date (example 1378/7/30)") 
	bot.register_next_step_handler(HBD,ExactAge)
def ExactAge(HBD):
    t=HBD.text.split('/')
    td=str(JalaliDatetime.now()-JalaliDatetime(t[0],t[1],t[2]))
    Te=int(td.split(' ')[0])//365
    bot.send_message(BDay.chat.id,'you are '+str(Te)+'years old.\nDays : '+str(td.split(' ')[0])) 

@bot.message_handler(commands=['max'])
def max1(message):
    array1=bot.send_message(message.chat.id,"( Enter the desired number to be declared the largest.in the form of(1 2,6,8)") 
    bot.register_next_step_handler(array1,max2)
def max2(message):
         array2=list(map(int,message.text.split(",")))
         bot.reply_to(message=message,text="بزرگترین مقدار "+str(max(array2)))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "این یک پیام عادی است")







bot.infinity_polling()



