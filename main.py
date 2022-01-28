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
    return message.text.lower() == 'major\'s accredited certification'


@bot.message_handler(func=certifications_boolean)
def certifications(message):
    log_message(message)
    bot.send_message(message.chat.id, "To be added 😁")


def resources_boolean(message):
    return message.text.lower() == 'learning resources'


@bot.message_handler(func=resources_boolean)
def resources(message):
    log_message(message)
    bot.send_message(message.chat.id, "To be added 😁")


# For Administrators' Debugging
def message_id_boolean(message):
    return message.from_user.username.lower() == 'kasehomar'


@bot.message_handler(func=message_id_boolean)
def message_id(message):
    bot.reply_to(message, str(message.message_id))


bot.polling()
