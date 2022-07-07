# 9.11 Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the
# product. The program must display the years, months, and days that are left for expiry

import datetime


class Product:
    def __init__(self):
        self._manufacture = datetime.datetime.strptime(input('Enter the manufacturing date(mm/dd/yyyy):'), '%m/%d/%Y')
        self._expiry = datetime.datetime.strptime(input('Enter the expiry date(mm/dd/yyyy):'), '%m/%d/%Y')

    def time_to_expire(self):
        today = datetime.datetime.today()
        if today > self._expiry:
            print('Product has already expired  ')
        else:
            time_left = self._expiry.date() - datetime.datetime.now().date()
            print('Time left: ', time_left)

    def show(self):
        print('Expiry', self._expiry)
        print('Manufacturing', self._manufacture)


x = Product()
x.time_to_expire()