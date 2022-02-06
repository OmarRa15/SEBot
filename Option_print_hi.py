from IOption import IOption


class Say_Hi(IOption):
    optionName = 'Say_Hi'
    optionCommand = 'SayHi'
    author = 'Baghdadi'
    requirements = {'': ''}

    def runIt(self):
        return 'Hi'