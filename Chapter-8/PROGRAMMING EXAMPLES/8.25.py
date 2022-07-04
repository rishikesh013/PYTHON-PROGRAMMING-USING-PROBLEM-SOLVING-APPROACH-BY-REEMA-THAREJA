# 8.25 Write a program using a function that returns the area and circumference of a circle whose radius is passed as
# an argument

from math import pi


def calc_a_r(radius):
    a = pi * radius * radius
    c = 2 * pi * radius

    return a, c


radius = int(input("Enter the radius: "))
area, circumference = calc_a_r(radius)
print(f"Area of the circle is : {area:.2f}")
print(f"Circumference of the circle is {circumference:.2f}")

# Write a program that scans an email address and forms a tuple of user name and domain

addr = 'abc@gmail.com'
user_name, domain = addr.split('@')
print(user_name)
print(domain)