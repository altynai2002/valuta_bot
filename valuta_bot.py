import os
from telebot import TeleBot, types
import config
import datetime
import valuta 


valuta.main()

bot = TeleBot(config.TOKEN)
# инлайн клавиатура с валютами Америка, Европа, Россия, Казахстан
main_keyboard = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton("USD", callback_data="usd")
btn2 = types.InlineKeyboardButton("EUR", callback_data="eur")
btn3 = types.InlineKeyboardButton("RUB", callback_data="rus")
btn4 = types.InlineKeyboardButton("KZT", callback_data="kzt")
main_keyboard.add(btn1, btn2, btn3, btn4)

valuta = None # переменная валюты
pok_prod = None # переменная покупка или продажа
today = (datetime.datetime.today()).strftime("%d/%m/%Y %H:%M:%S")


# Вызывается клавиатура с валютами
@bot.message_handler(commands = ['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"КУРСЫ ВАЛЮТ НА {today} В БИШКЕКЕ", reply_markup=main_keyboard)



@bot.callback_query_handler(func = lambda x: True)
def choose_1(x):
    global valuta
    valuta = x.data # значение переменной меняется
    print('Выбранная валюта -', valuta)
    # Клавиатура покупка и продажа
    pokupka_prodaja = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Покупка")
    btn2 = types.KeyboardButton("Продажа")
    pokupka_prodaja.add(btn1, btn2)
    msg3 = bot.send_message(x.message.chat.id , "Выберите категорию" , reply_markup=pokupka_prodaja)


@bot.message_handler(content_types=['text'])
def choose_2(message):
    global pok_prod
    pok_prod = message.text # значение переменной меняется
    print('Выбранная категория -', pok_prod)
    chat_id = message.chat.id
    # Клавиатура лучшая цена или json файл
    the_best_json = types.ReplyKeyboardMarkup(True, True)
    btn1 = types.KeyboardButton("Лучшая цена")
    btn2 = types.KeyboardButton("json файл")
    the_best_json.add(btn1, btn2)
    msg = bot.send_message(chat_id , "Что вам выслать?" , reply_markup=the_best_json)
    bot.register_next_step_handler(msg, get_category) # переходим на функцию get_category

import csv_json
def get_category(message):
    if message.text == "Лучшая цена":
        a = csv_json.value_of_valuta(valuta, pok_prod)
        bot.send_message(message.chat.id, f'{a}\nДо свидания!')
    else:
        with open('test.json', 'rb') as f:
            bot.send_document(message.chat.id, f)

    os.remove('test.json') # удаляет файл
    os.remove('valuta.csv') # удаляет файл
    os._exit(0) # закрывает файл










bot.polling()