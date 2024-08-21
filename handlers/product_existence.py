from telebot import types
from psycopg2 import sql
import psycopg2
from config import db_name, user, password, host


class ProductExistence:
    def __init__(self):
        self.product_name = ""

    @staticmethod
    def get_db_connection():
        return psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host
        )

    def start_search(self, bot, message):
        if message.text == '/product':
            bot.send_message(message.from_user.id, 'Какой товар вас интересует?')
            bot.register_next_step_handler(message, lambda msg: self.get_product_name(bot, msg))
        else:
            bot.send_message(message.from_user.id, 'Для начала диалога воспользуйтесь кнопкой Меню')

    def get_product_name(self, bot, message):
        self.product_name = message.text


def search_handlers(bot):
    product_existence = ProductExistence()

    @bot.message_handler(content_types='[text]')
    def handle_text(message):
        product_existence.start_search(bot, message)
