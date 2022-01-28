import telebot
from os import environ
from log import log_message

API_KEY = environ['TEL_API_KEY']

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    log_message(message)
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Major\'s Accredited Certification', 'Learning Resources')
    rsp = "Hi There!!"
    bot.send_message(message.chat.id, rsp, reply_markup=user_markup)


def certifications_boolean(message):
    return message.text.lower() == 'Major\'s Accredited Certification'


@bot.message_handler(func=certifications_boolean)
def certifications(message):
    log_message(message)
    bot.send_message(message.chat.id, "To be added 😁")


def resources_boolean(message):
    return message.text.lower() == 'Learning Resources'


@bot.message_handler(func=certifications_boolean)
def resources(message):
    log_message(message)
    bot.send_message(message.chat.id, "To be added 😁")


bot.polling()
