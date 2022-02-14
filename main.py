from threading import Thread

import telebot

from Bot import Bot
from DATA import bot

from IOption import IOption
from GPA_Calc import GPA_Calc


# @bot.message_handler(commands=['start'])
# def start(message):
#     keyboard = fill_keyboard(options)
#     rsp = "Welcome to SE Bot!"
#     bot.send_message(message.chat.id, rsp, reply_markup=keyboard)


# def check_commands_boolean(message):
#     global currentState
#     for option in options:
#         if option.optionName == message.text:
#             currentState = option
#             return True


# def next_handler(pm):
#     print("next_handler:", pm)
#     msg_text = pm.text
#     rsp = currentState.runIt(msg_text)
#     bot.send_message(pm.chat.id, rsp)
#     if currentState.setup.get('rerun', ''):
#         bot.register_next_step_handler(pm, next_handler)  # Next message will call the name_handler function


# @bot.message_handler(func=check_commands_boolean)
# def runIt(message):
#     sent_msg = bot.send_message(message.chat.id, currentState.setup.get('message', ''))
#     keyboard = None
#     print("currentState.options1:", currentState.options)
#     if currentState.options:
#         print("currentState.options:", currentState.options)
#         keyboard = fill_keyboard(options)
#
#     if currentState.setup.get('input'):
#         bot.register_next_step_handler(sent_msg, next_handler)  # Next message will call the name_handler function
#     else:
#         rsp = currentState.runIt()
#         bot.send_message(message.chat.id, rsp, reply_markup=keyboard)

connectedClients = {}


@bot.message_handler()
def manager(message):  # if none of above handlers run
    print('[RECEIVED] request')
    _bot = connectedClients.get(message.chat.id, Bot(message))
    connectedClients[message.chat.id] = _bot
    _bot.message = message
    Thread(target=_bot.serve_it).start()


bot.polling()
