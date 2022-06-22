# 4.54 Write a program to calculate square root of a number. Demonstrate the use of break and continue statements

from math import sqrt

while True:
    number_to_calculate = int(input("Enter the number to calculate: "))

    if number_to_calculate == 999:
        break
    elif number_to_calculate < 0:
        print("Can't take square root for number less than 0")
        continue

    else:
        print(f"Square root of the number is {int(sqrt(number_to_calculate))}")