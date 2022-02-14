from IOption import IOption


class Back(IOption):
    optionName = 'Back'
    author = ''
    options: [] = []

    setup = {
        'message': '',
        'input': False,
        'rerun': False
    }

    def runIt(self):
        return ''
