import telebot
from config import TOKEN
from registration import RegistrationUser
from product_existence import ProductExistence

bot = telebot.TeleBot(TOKEN)

user_registration = RegistrationUser()
product_existence = ProductExistence()


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '/reg':
        user_registration.start_registration(bot, message)
    elif message.text == '/product':
        product_existence.start_search(bot, message)
    else:
        bot.send_message(message.from_user.id, 'Неизвестная команда. Используйте /reg или /product.')


# Обработчики для callback_query можно добавить здесь, если они требуются

if __name__ == '__main__':
    print("Bot is polling...")
    bot.polling(none_stop=True)
