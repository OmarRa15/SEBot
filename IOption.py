from abc import ABC, abstractmethod, abstractproperty


class IOption(ABC):
    optionCommand = ''
    author = ''
    requirements = {}

    @abstractmethod
    def runIt(self):
        print("Test")
