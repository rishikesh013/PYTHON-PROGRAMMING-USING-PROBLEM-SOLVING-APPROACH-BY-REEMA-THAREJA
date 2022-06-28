# 5.19 Write a program that prints the absolute value, square root and cube of a number

from math import sqrt, pow
import random


def cube(no: int) -> int:
    """Function to return the cube of a number"""
    return int(pow(no, 3))


a = int(input("Enter the value of a: "))
print(f"The absolute value is {abs(a)}")
print(f"The square root of the a is {sqrt(a)}")
print(f"The cube of a is {cube(a)}")

# Program to generate 10 random numbers between 1, 100

for i in range(10):
    random_no = random.randint(1, 100)
    print(random_no)
