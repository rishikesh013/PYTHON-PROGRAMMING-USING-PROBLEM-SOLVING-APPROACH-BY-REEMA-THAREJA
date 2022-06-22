# 4.40 Write a program to sum the series 1/1 + 2^2/2 + 3^3/3...+ n^n/n

from math import pow
n = int(input("Enter the value of n: "))
sum_of_values = 0.0

for i in range(1, n + 1):
    average = float(i ** i) / n
    sum_of_values += average

print(f"The sum of the series is {sum_of_values}")
