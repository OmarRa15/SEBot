import telebot

from DATA import bot

from IOption import IOption
from GPA_Calc import GPA_Calc

O_sayHI = GPA_Calc()
options = [O_sayHI]
currentState: IOption = None


def fill_keyboard(_options: [IOption]):
    starting_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    optionNames = [option.optionName for option in _options]
    starting_keyboard.add(*optionNames, row_width=2)
    return starting_keyboard


def start_boolean(message):
    return message.text.lower() == 'back to start!'


@bot.message_handler(commands=['start'])
@bot.message_handler(func=start_boolean)
def start(message):
    keyboard = fill_keyboard(options)
    rsp = "Welcome to SE Bot!"
    bot.send_message(message.chat.id, rsp, reply_markup=keyboard)


def check_commands_boolean(message):
    global currentState
    for option in options:
        if option.optionName == message.text:
            currentState = option
            return True


@bot.message_handler(func=check_commands_boolean)
def runIt(message):

    rsp = currentState.runIt()
    bot.send_message(message.chat.id, rsp)


@bot.message_handler()
def _else(message):  # if none of above handlers run
    rsp = '/start'
    bot.send_message(message.chat.id, rsp)


bot.polling()
