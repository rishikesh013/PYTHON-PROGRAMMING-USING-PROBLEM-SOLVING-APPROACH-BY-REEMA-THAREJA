# 4.23 Write a program that prints surface area and volume of sphere
import math


def calculate_sphere(r):
    surface_area = 4 * math.pi * r * r
    volume = (4 / 3) * math.pi * r ** 3
    return surface_area, volume


result = calculate_sphere(9)
s, v = result
print(s, v)