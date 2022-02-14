from IOption import IOption


class Certificates(IOption):
    optionName = 'Certificates'
    author = ''

    setup = {
        'message': '',
        'input': False,
        'rerun': False
    }

    def __init__(self):
        self.setup['message'] = """
These some resources to have a certificates in SE Major:

https://www.coursera.org/specializations/java-programming

https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer
"""

    def runIt(self, *args):
        return ''
