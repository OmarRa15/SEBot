import telebot
from os import environ
from log import log_message

API_KEY = environ['TEL_API_KEY']

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    log_message(message)
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('/start','hi')
    user_markup.row('/test','another Test','hop')
    rsp = "Hi There, Say Hi"
    bot.reply_to(message, rsp)


# @bot.message_handler(commands=['Hi'])
# def hello(message):
#     log_message(message)
#     bot.send_message(message.chat.id, "Hi Hi")


def boolean_func(message):
    return message.text.lower() == 'hi'


@bot.message_handler(func=boolean_func)
def hi(message):
    log_message(message)
    bot.send_message(message.chat.id, "Hi, I am SE Bot")


bot.polling()
