# 9.4 Write a program that has a class Circle. Use a class variable to define the value of constant PI. Use this
# class variable to calculate area and circumference of a circle with specified radius

class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return float(f'{Circle.PI * self.radius * self.radius: .2f}')

    def circumference(self):
        return 2 * Circle.PI * self.radius


c = Circle(7.53)
print(f'Area: {c.area()}')
print(f'Circumference: {c.circumference()}')