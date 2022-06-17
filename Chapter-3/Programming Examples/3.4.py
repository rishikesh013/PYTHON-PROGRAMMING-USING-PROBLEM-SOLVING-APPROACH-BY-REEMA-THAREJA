# 3.4 Program to calculate the distance between two points

from math import sqrt
x1 = int(input("Enter the x coordinate of the First point: "))
x2 = int(input("Enter the x coordinate of the Second point: "))
y1 = int(input("Enter the y coordinate of the First point: "))
y2 = int(input("Enter the y coordinate of the Second point: "))

d = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(f"Distance is {d:3.6f}")
