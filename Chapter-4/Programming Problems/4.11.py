# 4.11 Write a program to sum the series 1^2 / 1 + 2^2 / 2 .... n^2/n

value_of_n = int(input("Enter the value of the n to find the sum: "))

sum_of_values = 0
for i in range(1, value_of_n + 1):
    sum_of_values += i ** 2 // i
print(f"The sum of the values is {sum_of_values}")