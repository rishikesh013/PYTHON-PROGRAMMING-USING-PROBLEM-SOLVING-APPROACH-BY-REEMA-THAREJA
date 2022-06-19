# 4.9 Write an program to print the greatest among the three numbers

a = int(input("Enter the number one of the three numbers:"))
b = int(input("Enter the number two of the three numbers:"))
c = int(input("Enter the number three of the three numbers:"))

if a > b and a > c:
    print(f"{a} is the greatest number")
elif b > a and b > c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")

