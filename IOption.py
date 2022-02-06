from abc import ABC, abstractmethod


class IOption(ABC):
    optionName = ''
    author = ''
    setup = {}
    options: [] = []

    @abstractmethod
    def runIt(self, *args):
        return "Test"
