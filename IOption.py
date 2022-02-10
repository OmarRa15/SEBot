from abc import ABC, abstractmethod


class IOption(ABC):
    optionName = ''
    author = ''
    options: [] = []

    setup = {
        'message': '',
        'input': False,
        'rerun': False
    }

    @abstractmethod
    def runIt(self, *args):
        return ''
