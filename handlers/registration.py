from telebot import types
from psycopg2 import sql
import psycopg2
from config import db_name, user, password, host


class RegistrationUser:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.age = 0
        self.gender = ''

    @staticmethod
    def get_db_connection():
        return psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host
        )

    def start_registration(self, bot, message):
        if message.text == '/reg':
            bot.send_message(message.from_user.id, "Как тебя зовут?")
            bot.register_next_step_handler(message, lambda msg: self.get_name(bot, msg))
        else:
            bot.send_message(message.from_user.id, 'Для начала диалога воспользуйтесь кнопкой Меню')

    def get_name(self, bot, message):
        self.name = message.text
        bot.send_message(message.chat.id, 'Какая у тебя фамилия?')
        bot.register_next_step_handler(message, lambda msg: self.get_surname(bot, msg))

    def get_surname(self, bot, message):
        self.surname = message.text
        keyboard_gender = types.InlineKeyboardMarkup()
        keyboard_gender.add(types.InlineKeyboardButton('Муж.', callback_data='option1'))
        keyboard_gender.add(types.InlineKeyboardButton('Жен.', callback_data='option2'))
        bot.send_message(message.from_user.id, 'Выбери свой пол', reply_markup=keyboard_gender)

    def callback_for_options(self, bot, call):
        if call.data == 'option1':
            self.gender = 'Мужской'
        elif call.data == 'option2':
            self.gender = 'Женский'

        bot.send_message(call.message.chat.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(call.message, lambda msg: self.get_age(bot, msg))

    def get_age(self, bot, message):
        try:
            self.age = int(message.text)
        except ValueError:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
            bot.register_next_step_handler(message, lambda msg: self.get_age(bot, msg))
            return

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)

        question = f'Тебе {self.age} лет, тебя зовут {self.name} {self.surname}, пол: {self.gender}. Всё верно?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    def callback_worker(self, bot, call):
        if call.data == "yes":
            self.save_to_db()
            bot.send_message(call.message.chat.id,
                             f'Имя твоё запомню я: {self.name} {self.surname} - любитель наяривать по вечерам')
        elif call.data == "no":
            bot.send_message(call.message.chat.id, 'Давай попробуем еще раз. Сколько тебе лет?')
            bot.register_next_step_handler(call.message, lambda msg: self.get_age(bot, msg))

    def save_to_db(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            insert_query = sql.SQL("""
                INSERT INTO users (name, surname, age, gender)
                VALUES (%s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (self.name, self.surname, self.age, self.gender))
            conn.commit()
            print("Data successfully inserted")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


def register_handlers(bot):
    user_registration = RegistrationUser()

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        user_registration.start_registration(bot, message)

    @bot.callback_query_handler(func=lambda call: call.data in ['option1', 'option2'])
    def handle_gender_callback(call):
        user_registration.callback_for_options(bot, call)

    @bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
    def handle_confirmation_callback(call):
        user_registration.callback_worker(bot, call)
