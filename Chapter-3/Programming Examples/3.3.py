# 3.3 Write a program to calculate area of the triangle using heron's formula

from math import sqrt
a = float(input("Enter the 1'st side of the triangle: "))
b = float(input("Enter the 2'nd side of the triangle: "))
c = float(input("Enter the 3'rd side of the triangle: "))

s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is {area:.2f}")
