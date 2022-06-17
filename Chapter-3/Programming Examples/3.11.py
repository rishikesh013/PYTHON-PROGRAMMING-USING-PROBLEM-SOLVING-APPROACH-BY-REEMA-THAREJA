# 3.11 Write a program to print the digit at one's place of a number

num = int(input("Please enter an number: "))
# num2 = str(num)
# print(f"Number at ones place is {num2[-1]}")
print(f"Number at ones place is {num % 10}")
