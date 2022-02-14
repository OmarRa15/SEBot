from IOption import IOption
from Tools.GPA_Calc import GPA_Calc


class Tools(IOption):
    optionName = 'Tools'
    author = 'Baghdadi'

    setup = {
        'message': '',
        'input': False,
        'rerun': False
    }

    def __init__(self):
        self.options = []
        self.setup['message'] = """
Welcome to SE Club tools
"""
        _GPA_Calc = GPA_Calc()
        GPA_Calc.parent = Tools

        self.options.append(_GPA_Calc)

    def runIt(self, *args):
        return ''
