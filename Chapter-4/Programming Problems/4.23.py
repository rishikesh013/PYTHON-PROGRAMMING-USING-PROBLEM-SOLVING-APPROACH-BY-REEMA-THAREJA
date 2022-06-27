# 4.23 Write a program to read two numbers. Then find out whether the first number is a multiple of the second number

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

if num1 % num2 == 0:
    print(f"They are multiples of each others")
else:
    print(f"They are not the multiples of each other")