# 4.38 Write a program to sum the series - 1/1^2 + 1/2^2 + 1/n^2

n = int(input("Enter the value of n: "))
sum_of_value = float(0)

for i in range(1, n + 1):
    a = 1.0 / i ** 2
    sum_of_value += a

print(f"Sum of values is {sum_of_value}")