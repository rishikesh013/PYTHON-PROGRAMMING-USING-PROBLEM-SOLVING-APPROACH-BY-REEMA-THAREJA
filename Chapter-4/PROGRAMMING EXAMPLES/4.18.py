# 4.18 Write a program to calculate the sum of numbers from m to n
m = int(input("Enter the value of numbers from m: "))
n = int(input("Enter the value of numbers from n: "))

sum_of_numbers = 0
while m <= n:
    sum_of_numbers += m
    m += 1

print(f"Sum = {sum_of_numbers}")
