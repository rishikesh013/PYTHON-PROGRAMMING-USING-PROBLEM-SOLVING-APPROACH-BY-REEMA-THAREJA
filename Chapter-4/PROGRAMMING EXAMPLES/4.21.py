# 4.21 Write a program to check weather a given number is an armstrong number or not
from math import pow
number_to_check = int(input("Enter a number to check: "))
r = 0
n = number_to_check
k = 0
while n > 0:
    r = n % 10
    k += r ** 3
    n //= 10

if number_to_check == k:
    print(f"It's an armstrong number.")
else:
    print(f"It is not an armstrong number.")
