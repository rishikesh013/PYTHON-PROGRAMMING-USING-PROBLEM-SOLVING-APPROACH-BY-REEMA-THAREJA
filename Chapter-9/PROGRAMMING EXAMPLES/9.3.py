# 9.3 Write a program that has a class person storing name and date of birth of a person. The program should subtract
# the DOB from todays date to find out whether a person is eligible to vote or not

import datetime


class Person:

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def check(self):
        today = datetime.datetime.today()
        calc_age = today.year - self.dob.year
        print(f'{calc_age}')
        if calc_age > 18:
            print(f"{self.name} is eligible to vote..")
        else:
            print(f"{self.name} is not eligible to vote")


per1 = Person('Raizo', datetime.date(2003, 1, 11))
per1.check()
b = datetime.datetime.today()
print(type(b))
