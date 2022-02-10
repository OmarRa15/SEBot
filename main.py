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


def next_handler(pm):
    print("next_handler:", pm)
    msg_text = pm.text
    rsp = currentState.runIt(msg_text)
    bot.send_message(pm.chat.id, rsp)
    if currentState.setup.get('rerun', ''):
        bot.register_next_step_handler(pm, next_handler)  # Next message will call the name_handler function


@bot.message_handler(func=check_commands_boolean)
def runIt(message):
    sent_msg = bot.send_message(message.chat.id, currentState.setup.get('message', ''))
    if currentState.setup.get('input', ''):
        bot.register_next_step_handler(sent_msg, next_handler)  # Next message will call the name_handler function
    else:
        rsp = currentState.runIt()
        bot.send_message(message.chat.id, rsp)


@bot.message_handler()
def _else(message):  # if none of above handlers run
    rsp = '/start'
    bot.send_message(message.chat.id, rsp)


bot.polling()
