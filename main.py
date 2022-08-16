from telebot import TeleBot
from telebot.types import Message
from configs import *
from currency_converter import CurrencyConverter
from telebot import types

bot = TeleBot(TOKEN)
c = CurrencyConverter()

@bot.message_handler(commands=['start'])
def start(message):
    full_name = message.from_user.full_name
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sum = types.KeyboardButton("ИЗ СУМ 💸")
    ruble = types.KeyboardButton("ИЗ РУБЛЯ 💸")
    dollar = types.KeyboardButton("ИЗ ДОЛЛАРА 💵")
    euro = types.KeyboardButton("ИЗ ЕВРО 💶")
    yen = types.KeyboardButton("ИЗ ЙЕН 💴")

    sum2 = types.KeyboardButton("В СУМ 💸")
    ruble2 = types.KeyboardButton("В РУБЛЬ 💸")
    dollar2 = types.KeyboardButton("В ДОЛЛАР 💵")
    euro2 = types.KeyboardButton("В ЕВРО 💶")
    yen2 = types.KeyboardButton("В ЙЕН 💴")

    markup.add(sum, ruble, dollar, euro, yen)
    markup2.add(sum2, ruble2, dollar2, euro2, yen2)


    from_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    to_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    from_mup = types.KeyboardButton("ИЗ КАКОЙ ВАЛЮТЫ")
    info_mup = types.KeyboardButton("ИНФОРМАЦИЯ")
    to_mup = types.KeyboardButton("В КАКУЮ ВАЛЮТУ")
    from_markup.add(from_mup)
    info_markup.add(info_mup)
    to_markup.add(to_mup)

    if message.text == '/start':
        bot.send_message(chat_id, f"Здарова {full_name}, я Телекуренси. Чтобы понять как работает бот, нажми на кнопку 'ИНФОРМАЦИЯ' 😉", parse_mode="html", reply_markup=info_markup)

        @bot.message_handler(content_types=['text'])
        def not_start(message):
            if message.text == 'ИНФОРМАЦИЯ':
                bot.send_message(chat_id, f'''Я - Телекуренси🤖, бот который может перевести одну валюту на другую. 
Выберите одну из валют, которую вы хотите перевести в другую:''', reply_markup=markup)
            elif message.text == sum or ruble or dollar or euro or yen:
                bot.send_message(chat_id, "Выберите в какую валюту мы будем переводить:", reply_markup=markup2)

            elif message.text == "В СУМ 💸" or "В РУБЛЬ 💸" or "В ДОЛЛАР 💵" or "В ЕВРО 💶" or "В ЙЕН 💴":
                bot.send_message(chat_id, "Сейчас покажем результат...")


bot.polling(none_stop=True)

