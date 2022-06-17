# 3.10 Write a program to print average of two numbers .Print their deviation

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

avg = (a + b) / 2
print(f"Average of two numbers are {avg}")
print(f"Deviation of first number is {a - avg}")
print(f"Deviation of the second number is {b - avg}")
