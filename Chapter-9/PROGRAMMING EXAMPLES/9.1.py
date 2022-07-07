# 9.1 Write a program that uses class to store the name and marks of students Use list to store the marks in three
# subjects

class Students:
    student_no = 0

    def __init__(self, name):
        self.name = name
        self.marks = []
        Students.student_no += 1
        print(f'Hello {self.name}!! Welcome to the school..')

    def enter_marks(self):
        for i in range(1, 4):
            m = int(input(f"Enter the marks obtained by {self.name} in subject{i}:  "))
            self.marks.append(m)

    @staticmethod
    def no_of_student():
        return f'Total number of students are {Students.student_no}'

    def __str__(self):
        return f'{self.name}: {self.marks}'


s1 = Students('Raizo')
s1.enter_marks()
print(s1.student_no)
s2 = Students('Branav')
s2.enter_marks()
print(s2.__str__())
print(Students.no_of_student())
