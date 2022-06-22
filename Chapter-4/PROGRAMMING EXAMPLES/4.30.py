# 4.30 Write a program to print the multiplication table of n, where n is entered by the user

n = int(input("Enter the value of n: "))

for i in range(1, 11):
    print(f"{n:2} * {i:^2} = {n * i:^5}")
