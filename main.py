import telebot
from os import environ
from log import log_message

API_KEY = environ['TEL_API_KEY']

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Hello'])
def hello(message):
    log_message(message)
    bot.reply_to(message, "Hi There")


@bot.message_handler(commands=['Hi'])
def hello(message):
    log_message(message)
    bot.send_message(message.chat.id, "Hi Hi")


def boolean_func(message):
    return message.text.lower() == 'who are you'


@bot.message_handler(func=boolean_func)
def whoami(message):
    log_message(message)
    bot.send_message(message.chat.id, "I am SE Bot")


bot.polling()
