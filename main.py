import telebot
from telebot import types

bot = telebot.TeleBot("6332328061:AAG2r6n888T7wb7WT9xa9RwZI-KUpN5oBoE")


@bot.message_handler(content_types=['message'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я тебе расскажу как стать настоящим тестировщиком!")
    else:
        bot.send_message(message.from_user.id, "Напиши привет!")


bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
