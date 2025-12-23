import telebot
import requests
import datetime  
from telebot import types
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

help = (
    """Здравствуйте, вы попали в бот по теме глобального потепления.
    Команды:
    /help - показать это меню
    /cause - причины глобального потепления
    /solution - одно практическое решение
    /battle - как с ним бороться (шаги)
    /map - ссылка на сайт с картами и результатами потепления
    /time - ссылка на сайт с приблизительным оставшимся «временем» (carbon budget)"""
)

@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    bot.send_message(message.chat.id, help)

@bot.message_handler(commands=['cause'])
def causes(message):
    text = (
        """Основные причины глобального потепления:
        1) Сжигание ископаемого топлива (уголь, нефть, газ) → выбросы CO₂.
        2) Вырубка лесов и изменение землепользования (меньше поглотителей CO₂).
        3) Сельское хозяйство (метан от животных, удобрения).
        4) Промышленность и производство (парниковые газы, аэрозоли).
        5) Рост потребления и урбанизация — больше энергии и транспорта."""
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['solution'])
def solution(message):
    text = (
        """Одно практическое решение (масштабируемое):
        Переход энергосистемы на возобновляемые источники + энергосбережение.
        Конкретные шаги:"
        • Быстрое наращивание солнечных и ветровых мощностей.
        • Электрификация транспорта (грузовой и пассажирский).
        • Модернизация зданий для снижения потерь энергии (изоляция, умные сети).
        • Поддержка аккумуляторов и сетевой инфраструктуры.
        Эффект: заметное сокращение выбросов CO₂ при одновременном создании рабочих мест."""
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['battle'])
def battle(message):
    text = (
        """Как бороться с глобальным потеплением — практические уровни действий:
        1) Личные действия:
           - сократить использование личных машин, больше общественного транспорта и велосипеда;
           - экономить энергию дома (свет, отопление), выбирать энергоэффективную технику;
           - меньше мясных продуктов, меньше пищевых отходов.
        2) Общественные/политические:
           - поддерживать политику по сокращению выбросов и развитию ВИЭ;
           - участвовать в локальных инициативах по озеленению и устойчивому транспорту.
        3) Технологии и адаптация:
           - внедрять системы раннего оповещения, защиту при наводнениях и меры по адаптации;
           - инвестировать в исследование и развитие зелёных технологий."""
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['map'])
def send_map(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("NASA Climate — открытые источники по экологии от NASA", url="https://climate.nasa.gov/"))
    markup.add(types.InlineKeyboardButton("IPCC — отчёты и визуализации", url="https://flood.firetree.net/"))
    bot.send_message(message.chat.id, "Карта/данные и визуализации изменений климата:", reply_markup=markup)

@bot.message_handler(commands=['time'])
def send_time(message):
    data = requests.get("https://api.climateclock.world/v1/clock").json()
    time = data['data']['modules']['deadline1']['timestamp']
    time = datetime.datetime.fromisoformat(time.replace('Z', '+03:00'))
    bot.send_message(message.chat.id,
                    time - datetime.datetime.now(time.tzinfo))

@bot.message_handler(func=lambda m: True)
def default_response(message):
    bot.send_message(message.chat.id, "Не понял команду. Введите /help для списка доступных команд.")

if __name__ == "__main__":
    print("Bot started")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
