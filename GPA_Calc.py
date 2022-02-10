from IOption import IOption


class GPA_Calc(IOption):
    GRADES = {"A+": 4,
              "A": 3.75,
              "B+": 3.5,
              "B": 3,
              "C+": 2.5,
              "C": 2,
              "D+": 1.5,
              "D": 1
              }
    COURSE_HOURS = {
        'MATH101': 4,
        'CS111': 4
    }

    optionName = 'GPA Calc'
    author = 'Baghdadi'
    options: [IOption] = []
    setup = {
        'message': '''Enter your course grades
        example:
        CS 111 - A+
        MATH 101 - A
        .
        .
        .
        ''',
        'input': True,
        'rerun': False
    }

    def runIt(self, courses_marks: str):
        counter = 0
        temp = 0

        courses = courses_marks.split('\n')
        for i in courses:
            if not i:
                continue
            i = i.replace(' ', '').upper()
            i = i.split("-")
            if len(i) < 2:
                self.setup['rerun'] = True
                return 'Wrong input, try again'+'''\nEnter your course grades
example:
CS 111 - A+
MATH 101 - A
.
.
.
'''
            course_id = i[0]
            course_grade = i[1]

            hours = self.COURSE_HOURS.get(course_id, '')
            GPA = self.GRADES[course_grade]

            print("hours:", hours)
            print("grade:", GPA)
            temp += GPA * hours
            counter += hours
        GPA = temp / counter
        self.setup['rerun'] = False

        return GPA
