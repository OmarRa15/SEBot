from IOption import IOption


class Learning_Resources(IOption):
    optionName = 'Learning Resources'
    author = 'Baghdadi'

    setup = {
        'message': '',
        'input': False,
        'rerun': False
    }

    def __init__(self):
        self.setup['message'] = """
بعض المصادر للتعلم (سيتم إضافة مصادر بشكل مستمر):


CS111 Python:

English:

https://youtu.be/_uQrJ0TkZlc

https://www.w3schools.com/python/

https://www.udemy.com/share/103y9y3@sOtlS2jzcf7Yr0DUNLgoTGOiGCHtaiHGQQ7AU7VBAu4-NGRkEW5UFz43bZPbUURfIA==/
عربي:

https://satr.codes/paths/OTZExaETAH/view


CS112 Java:

https://youtu.be/eIrMbAQSU34

https://www.w3schools.com/java/


SE 342 Software Architecture:

https://www.developertoarchitect.com/lessons/


SE 323 Modeling and Design:

https://youtu.be/NU_1StN5Tkk
"""
        self.options: [] = []

    def runIt(self, *args):
        return ''
