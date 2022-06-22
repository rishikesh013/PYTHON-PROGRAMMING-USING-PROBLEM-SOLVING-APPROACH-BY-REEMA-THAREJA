# 4.2 Write a program to sum of squares of even numbers

n = int(input("Enter the value of n: "))
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s += i ** 2

print(f"The sum of squares of even number is {s}")

