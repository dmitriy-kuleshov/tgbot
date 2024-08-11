import telebot
from telebot import types

# from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
# import schedule
# import requests

bot = telebot.TeleBot('7187442707:AAE269XiCH13-F72cjWZL-QkZwE5j7IZnps')

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем могу помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Поздоровайся чёрт")
#     else:
#         bot.send_message(message.from_user.id, "Ты что глупый кок?, напиши /help.")

bot.polling(none_stop=True, interval=0)


# schedule.every().day.at('15.46').do(start)


class RegistrationUser:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.age = 0
        self.gender = ''

    @bot.message_handler(content_types=['text'])
    def start(self, message):

        if message.text == '/reg':
            bot.send_message(message.from_user.id, "Как тебя зовут?")
            bot.register_next_step_handler(message, self.get_name)  # следующий шаг – функция get_name
        else:
            bot.send_message(message.from_user.id, 'Напиши /reg')

    def get_name(self, message):  # получаем имя
        global name
        name = message.text
        keyboard_gender = types.InlineKeyboardMarkup()
        keyboard_gender.add(types.InlineKeyboardButton('Муж.', callback_data='option1'))
        keyboard_gender.add(types.InlineKeyboardButton('Жен.', callback_data='option2'))
        bot.send_message(message.from_user.id, 'Выбери свой пол', reply_markup=keyboard_gender)

    @bot.callback_query_handler(func=lambda call: call.data in ['option1', 'option2'])
    def callback_for_options(self, call):
        global gender

        if call.data == 'option1':
            gender = 'Мужской'
            bot.send_message(call.message.chat.id, 'Мужчинский мужчина - уважаю')
        elif call.data == 'option2':
            gender = 'Женский'
            bot.send_message(call.message.chat.id, 'ААААААА женщина')

        # После выбора пола спрашиваем фамилию
        bot.send_message(call.message.chat.id, 'Какая у тебя фамилия?')
        bot.register_next_step_handler(call.message, self.get_surname)

    def get_surname(self, message):
        global surname
        surname = message.text
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, self.get_age)

    def get_age(self, message):
        global age
        try:
            age = int(message.text)  # Проверяем, что возраст введен корректно
        except ValueError:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
            bot.register_next_step_handler(message, self.get_age)
            return

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)

        question = f'Тебе {age} лет, тебя зовут {name} {surname}, пол: {gender}. Всё верно?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
    def callback_worker(self, call):
        global age
        if call.data == "yes":
            bot.send_message(call.message.chat.id,
                             f'Имя твоё запомню я: {name} {surname} - любитель наяривать по вечерам')
        elif call.data == "no":
            age = 0  # сброс возраста
        bot.send_message(call.message.chat.id, 'Давай попробуем еще раз. Сколько тебе лет?')
        bot.register_next_step_handler(call.message, self.get_age)
