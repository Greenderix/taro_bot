import random

import telebot
from telebot import types
from strings import card_desc, way, colors_array
from settings import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    """"Запуск меню бота с вариацией выбора действий"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🔮 Аркан дня')
    item2 = types.KeyboardButton('🎱 Число дня')
    item3 = types.KeyboardButton('🧿 Цвет дня')
    item4 = types.KeyboardButton('Другое...')
    # 🎱🔮📿🧿

    markup.add(item1, item2, item3, item4)
    text = 'Hi, {0.first_name}! '
    bot.send_message(message.chat.id, text.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    """Команды для чата в личных сообщениях"""
    if message.chat.type == 'private':
        """Просмотр числа дня"""
        if message.text == '🎱 Число дня':
            temp_daynum = random.randint(1, 77)
            bot.send_message(message.chat.id, '✨Ваше число дня✨: ' + str(temp_daynum))
            """Просмотр аркана дня"""
        elif message.text == '🔮 Аркан дня':
            temp_daycard = random.randint(0, 21)
            bot.send_message(message.chat.id, '✨Ваш аркан дня✨: ' + str(temp_daycard))
            bot.send_message(message.chat.id, '✨Описание вашего аркана дня✨: \n')
            img = open(way + str(temp_daycard) + '.jpeg', 'rb')
            bot.send_photo(message.chat.id, img, caption=card_desc[temp_daycard])
            """Просмотр цвета дня"""
        elif message.text == '🧿 Цвет дня':
            bot.send_message(message.chat.id, '✨Ваш цвет дня✨: ' + str(random.choice(colors_array)))
            """Дополнительная кнопка, чтобы добавить новые функции"""
        elif message.text == 'Другое...':
            bot.send_message(message.chat.id,
                             'Я начинающий маг, поэтому другие возможности покажу позже...\nНажмите /start и попробуйте снова✨')
        else:
            """Если пользователь ввел неверные символы, то ему бот выдаст ошибку"""
            bot.send_message(message.chat.id,
                             'Проводя различные манипуляции с магией, я перестал Вас понимать,\nнажмите /start и попробуйте снова✨')

            """Команды бота для групповых чатов"""
            """Описание функций одинаковое, но убрано реагирование бота на обычные сообщения"""
    if message.chat.type != 'private':
        if message.text == '🎱 Число дня':
            temp_daynum = random.randint(1, 77)
            bot.send_message(message.chat.id, '✨Ваше число дня✨: ' + str(temp_daynum))
        elif message.text == '🔮 Аркан дня':
            temp_daycard = random.randint(0, 21)
            bot.send_message(message.chat.id, '✨Ваш аркан дня✨: ' + str(temp_daycard))
            bot.send_message(message.chat.id, '✨Описание вашего аркана дня✨: \n')
            img = open(way + str(temp_daycard) + '.jpeg', 'rb')
            bot.send_photo(message.chat.id, img, caption=card_desc[temp_daycard])
        elif message.text == '🧿 Цвет дня':
            bot.send_message(message.chat.id, '✨Ваш цвет дня✨: ' + str(random.choice(colors_array)))
        elif message.text == 'Другое...':
            bot.send_message(message.chat.id,
                             'Я начинающий маг, поэтому другие возможности покажу позже...\nНажмите /start и попробуйте снова✨')


bot.polling(none_stop=True)
