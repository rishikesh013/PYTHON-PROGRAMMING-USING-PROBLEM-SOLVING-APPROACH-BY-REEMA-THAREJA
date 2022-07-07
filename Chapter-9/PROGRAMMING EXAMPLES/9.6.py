# 9.6 Write a class Rectangle that has attributes length and breadth and a method area which returns the area of the
# rectangle

class Rectangle:
    def get_data(self):
        Rectangle.length = int(input("Enter the length of the rectangle: "))
        Rectangle.width = int(input('Enter the width of the rectagle: '))

    def area(self):
        print('Area = ', Rectangle.length * Rectangle.width)


# rect = Rectangle()
# rect.get_data()
# rect.area()


class Check:
    __role_no = 101

    def __init__(self):
        self.__name = 'Hello world'
        self._year = 2001

    def _year_change(self):
        self._year += 5


c = Check()
print(dir(c))
print(c._Check__name)
c._year_change()
print(c._year)