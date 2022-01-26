import telebot
from os import environ

API_KEY = environ['TEL_API_KEY']

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.reply_to(message, "Hi There")


bot.polling()
