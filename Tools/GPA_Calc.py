from IOption import IOption


class GPA_Calc(IOption):
    optionName = 'GPA Calc'
    author = 'Baghdadi'
    setup = {
        'message': '''Enter your course grades (Course name - hours - grade)
        example:
        CS 111 - 4 - A+
        MATH 101 - 4  - A
        .
        .
        .
        ''',
        'input': True,
        'rerun': False
    }

    def __init__(self):
        self.options: [IOption] = []
        self.GRADES = {"A+": 4,
                       "A": 3.75,
                       "B+": 3.5,
                       "B": 3,
                       "C+": 2.5,
                       "C": 2,
                       "D+": 1.5,
                       "D": 1
                       }
        self.COURSE_HOURS = {
            'MATH101': 4,
            'CS111': 4
        }

    def runIt(self, courses_marks: str):
        print("[runIt] GPA_Calc", courses_marks)
        counter = 0
        temp = 0

        courses = courses_marks.split('\n')
        try:
            for i in courses:
                if not i:
                    continue
                i = i.replace(' ', '').upper()
                i = i.split("-")
                if len(i) < 3:
                    self.setup['rerun'] = True
                    return 'Wrong input, try again' + '\n' + self.setup['message']
                course_id = i[0]
                hours = int(i[1])
                course_grade = i[2]

                # hours = self.COURSE_HOURS.get(course_id, '')
                GPA = self.GRADES[course_grade]

                temp += GPA * hours
                counter += hours
            GPA = temp / counter
            self.setup['rerun'] = False

            return f'Your GPA: {round(GPA, 2)}'
        except Exception as e:
            print(e)
