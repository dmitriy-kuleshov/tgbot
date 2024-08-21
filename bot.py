import telebot
from config import TOKEN
from handlers import registration, product_existence

# import schedule
# import requests

bot = telebot.TeleBot(TOKEN)

registration.register_handlers(bot)
product_existence.search_handlers(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)
