# $.35 Write a program to calculate pow(x, n)

num = int(input("Enter the number whose power to be calculated: "))
n = int(input("Till which power to calculate: "))

result = 1
for i in range(n):
    result *= num

print(f"{num} raised to {n} is {result}")