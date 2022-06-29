# 5.17 Write a program using a function that calculates the hypotenuse of a right angled triangle
import math


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


first_side = int(input("Enter the value of the first side: "))
second_side = int(input("Enter the value of the second side: "))
print(f"The value of the third side is {hypotenuse(first_side, second_side):f}")