import telebot
from config import TOKEN
#from handlers import registration, product_existence
# import schedule
# import requests
from registration import register_handlers
from product_existence import search_handlers
bot = telebot.TeleBot(TOKEN)

register_handlers(bot)
search_handlers(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)
