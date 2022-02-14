from IOption import IOption


class GPA_Calc2(IOption):
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

    optionName = 'GPA Calc2'
    author = 'Baghdadi'
    options: [IOption] = []
    setup = {
        'message': '''2Enter your course grades
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
                return 'Wrong input, try again' + '''\nEnter your course grades
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


class GPA_Calc3(IOption):
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

    optionName = 'GPA Calc3'
    author = 'Baghdadi'
    options: [IOption] = []
    setup = {
        'message': '''3Enter your course grades
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
                return 'Wrong input, try again' + '''\nEnter your course grades
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


class GPA_Calc(IOption):
    optionName = 'GPA Calc1'
    author = 'Baghdadi'
    setup = {
        'message': '''1Enter your course grades
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

    def __init__(self):
        self.options: [IOption] = []
        self.c2 = GPA_Calc2()
        self.c2.parent = GPA_Calc
        self.c3 = GPA_Calc3()
        self.c3.parent = GPA_Calc
        self.options.append(self.c2)
        self.options.append(self.c3)
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
        for i in courses:
            if not i:
                continue
            i = i.replace(' ', '').upper()
            i = i.split("-")
            if len(i) < 2:
                self.setup['rerun'] = True
                return 'Wrong input, try again' + '''\nEnter your course grades
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
