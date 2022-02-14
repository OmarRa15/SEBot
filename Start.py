from IOption import IOption
from SE.SE import SE

from Tools.GPA_Calc import GPA_Calc
from Tools.Tools import Tools


class Start(IOption):

    optionName = 'Welcome to SE Bot!\nwrite /start to start!!'
    author = 'SE Club'

    setup = {
        'message': '',
        'input': False,
        'rerun': False
    }

    def __init__(self):
        self.options: [] = []

        tools = Tools()
        Tools.parent = Start

        _SE = SE()
        SE.parent = Start

        self.options.append(tools)
        self.options.append(_SE)

    def runIt(self, *args):
        return

