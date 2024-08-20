import telebot
from config import TOKEN
from handlers import registration

# import schedule
# import requests

bot = telebot.TeleBot(TOKEN)

registration.register_handlers(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)
