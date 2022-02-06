from abc import ABC, abstractmethod


class IOption(ABC):
    optionName = ''
    optionCommand = ''
    author = ''
    requirements = {}

    @abstractmethod
    def runIt(self):
        print("Test")
