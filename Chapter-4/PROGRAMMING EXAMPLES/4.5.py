# 4.5 Write a program to check weather a given number is odd or even

number_to_check = int(input("Enter the number to check: "))

if number_to_check % 2 == 0:
    print(f"The number {number_to_check} is even")
else:
    print(f"The number {number_to_check} is odd")
