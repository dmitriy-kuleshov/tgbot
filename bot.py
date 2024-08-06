import telebot
from telebot import types

bot = telebot.TeleBot('7187442707:AAE269XiCH13-F72cjWZL-QkZwE5j7IZnps')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем могу помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Поздоровайся чёрт")
    else:
        bot.send_message(message.from_user.id, "Ты что глупый кок?, напиши /help.")


bot.polling(none_stop=True, interval=0)
