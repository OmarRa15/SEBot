from IOption import IOption
from SE.Certificates import Certificates
from SE.Learning_Resources import Learning_Resources


class SE(IOption):
    optionName = 'SE'
    author = 'Baghdadi'

    setup = {
        'message': 'Welcome to SE Major/Minor panel!',
        'input': False,
        'rerun': False
    }

    def __init__(self):
        certificates = Certificates()
        Certificates.parent = SE
        learningResources = Learning_Resources()
        Learning_Resources.parent = SE

        self.options: [] = [learningResources, certificates]

    def runIt(self, *args):
        return ''
