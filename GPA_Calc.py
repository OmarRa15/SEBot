from IOption import IOption

counter = 0


class GPA_Calc(IOption):
    optionName = 'GPA Calc'
    author = 'Baghdadi'
    requirements = {
        'input_count': 'Infinite',
        'message': 'Enter a course grade'
    }
    options: [] = []

    def runIt(self):
        total_grades = 1
        for i in range(1, 5):
            total_grades *= i
        return f'Hi, your total grades is: {total_grades}'
