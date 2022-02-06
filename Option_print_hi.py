from IOption import IOption


class Say_Hi(IOption):
    optionCommand = 'SayHi'
    author = 'Baghdadi'
    requirements = {'': ''}

    def runIt(self):
        return 'Hi'