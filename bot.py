import telebot
from config import TOKEN
from handlers import registration

# import schedule
# import requests

bot = telebot.TeleBot(TOKEN)


registration.register_handlers(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)

# def get_db_connection():
#     return psycopg2.connect(
#         dbname=config.db_name,
#         user=config.user,
#         password=config.password,
#         host=config.host
#     )


# schedule.every().day.at('15.46').do(start)

# class RegistrationUser:
#     def __init__(self):
#         self.name = ''
#         self.surname = ''
#         self.age = 0
#         self.gender = ''
#
#     def start_registration(self, message):
#         # print("Получено сообщение:", message.text)
#         if message.text == '/reg':
#             bot.send_message(message.from_user.id, "Как тебя зовут?")
#             bot.register_next_step_handler(message, self.get_name)
#         else:
#             bot.send_message(message.from_user.id, 'Напиши /reg')
#
#     def get_name(self, message):
#         self.name = message.text
#         bot.send_message(message.chat.id, 'Какая у тебя фамилия?')
#         bot.register_next_step_handler(message, self.get_surname)
#
#     def get_surname(self, message):
#         self.surname = message.text
#         keyboard_gender = types.InlineKeyboardMarkup()
#         keyboard_gender.add(types.InlineKeyboardButton('Муж.', callback_data='option1'))
#         keyboard_gender.add(types.InlineKeyboardButton('Жен.', callback_data='option2'))
#         bot.send_message(message.from_user.id, 'Выбери свой пол', reply_markup=keyboard_gender)
#
#     def callback_for_options(self, call):
#         if call.data == 'option1':
#             self.gender = 'Мужской'
#         elif call.data == 'option2':
#             self.gender = 'Женский'
#
#         bot.send_message(call.message.chat.id, 'Сколько тебе лет?')
#         bot.register_next_step_handler(call.message, self.get_age)
#
#     def get_age(self, message):
#         try:
#             self.age = int(message.text)
#         except ValueError:
#             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#             bot.register_next_step_handler(message, self.get_age)
#             return
#
#         keyboard = types.InlineKeyboardMarkup()
#         key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
#         keyboard.add(key_yes)
#         key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#         keyboard.add(key_no)
#
#         question = f'Тебе {self.age} лет, тебя зовут {self.name} {self.surname}, пол: {self.gender}. Всё верно?'
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
#     def callback_worker(self, call):
#         if call.data == "yes":
#             self.save_to_db()
#             bot.send_message(call.message.chat.id,
#                              f'Имя твоё запомню я: {self.name} {self.surname} - любитель наяривать по вечерам')
#         elif call.data == "no":
#             bot.send_message(call.message.chat.id, 'Давай попробуем еще раз. Сколько тебе лет?')
#             bot.register_next_step_handler(call.message, self.get_age)
#
#     def save_to_db(self):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         try:
#             insert_query = sql.SQL("""
#                 INSERT INTO users (name, surname, age, gender)
#                 VALUES (%s, %s, %s, %s)
#             """)
#             cursor.execute(insert_query, (self.name, self.surname, self.age, self.gender))
#             conn.commit()
#         except Exception as e:
#             print(f"Error: {e}")
#         finally:
#             cursor.close()
#             conn.close()
#
#
# # Создаем экземпляр класса
# user_registration = RegistrationUser()
#
#
# # Регистрируем обработчики
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     user_registration.start_registration(message)
#
#
# @bot.callback_query_handler(func=lambda call: call.data in ['option1', 'option2'])
# def handle_gender_callback(call):
#     user_registration.callback_for_options(call)
#
#
# @bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
# def handle_confirmation_callback(call):
#     user_registration.callback_worker(call)


