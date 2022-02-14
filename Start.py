from IOption import IOption

from GPA_Calc import GPA_Calc


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

        _GPA_Calc = GPA_Calc()
        _GPA_Calc.parent = Start
        self.options.append(_GPA_Calc)

    def runIt(self, *args):
        return

