import telebot
from telebot import types

bot = telebot.TeleBot.TeleBot("6332328061:AAG2r6n888T7wb7WT9xa9RwZI-KUpN5oBoE")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
