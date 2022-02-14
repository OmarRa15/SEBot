from datetime import datetime

import telebot

from Back_Option import Back
from DATA import bot
from IOption import IOption
from Start import Start


def prepare_message(message):
    if not message:
        return 'Update keyboard'
    return message


class Bot:
    REST_WORDS = ['/start', 'back to home']

    def __init__(self, message, ):
        self.message = message
        self.currentState: IOption = Start()
        self.last_update = datetime.now()
        self.set_last_update()
        self.input_count = -1

    def serve_it(self):
        self.check_commands_boolean()
        self.run_it()
        self.fill_keyboard()
        self.set_last_update()

    def fill_keyboard(self):
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        if self.currentState.parent is not None:
            options_types = [type(i) for i in self.currentState.options]
            back_obj = Back()
            if type(back_obj) not in options_types:
                self.currentState.options.append(Back())
        optionNames = [option.optionName for option in self.currentState.options]
        keyboard.add(*optionNames, row_width=2)

        bot.send_message(self.message.chat.id, prepare_message(""), reply_markup=keyboard)

    def set_last_update(self):
        self.last_update = datetime.now()

    def check_commands_boolean(self):
        if self.message.text in self.REST_WORDS:
            self.reset()
            return
        if self.message.text == Back.optionName:
            print("self.message.text == Back.optionName:", self.message.text == Back.optionName)

            self.currentState = self.currentState.parent()
            return
        for option in self.currentState.options:
            if option.optionName == self.message.text:
                self.currentState = option
                self.input_count = 0
                return True

    def run_it(self):
        _message = self.currentState.setup.get('message')
        print("_message:", _message, not self.input_count)
        if _message and not self.input_count:
            if _message.strip():
                bot.send_message(self.message.chat.id, _message)
        if self.currentState.setup.get('input'):
            if self.input_count:
                rsp = self.currentState.runIt(self.message.text)
                rsp = str(rsp)
                if rsp:
                    if rsp.strip():
                        bot.send_message(self.message.chat.id, rsp)
        else:
            rsp = self.currentState.runIt()
            if rsp:
                if rsp.strip():
                    bot.send_message(self.message.chat.id, rsp)
        self.input_count += 1

    def need_input(self):
        return self.currentState.setup.get('input')

    def reset(self):
        self.currentState: IOption = Start()
        self.last_update = datetime.now()
        self.set_last_update()
        self.input_count = -1
