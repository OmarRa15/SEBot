from DATA import bot
from IOption import IOption


def boolean(message):
    print("message == '1':", message == '1')
    return message == '1'


class Decorator:
    def __init__(self, iOption: IOption):
        self.iOption = iOption

    def checkIt(self):
        print('checkIt:', self.iOption.optionName)

        @bot.message_handler(func=boolean)
        def runIt():
            self.iOption.runIt()
