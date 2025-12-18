import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
@bot.message_handler (commands=['start', 'help'])
def pin (message):
    bot.send_message(message.chat.id,"""
здравствуйте вы попали на тг канал по глобальному потеплению 
команды:
    /help - вывести справочное меню
    /cause - вывести причины глобального потепления 
    /solution - вывест 1 решение 
    /battle - как с ним бороться
    /map - ссылка на сайт результаты потепления 
    /map_2 - ссылка сайт до приблизительное оставшееся время до "потопа"
    """)


bot.infinity_polling()









