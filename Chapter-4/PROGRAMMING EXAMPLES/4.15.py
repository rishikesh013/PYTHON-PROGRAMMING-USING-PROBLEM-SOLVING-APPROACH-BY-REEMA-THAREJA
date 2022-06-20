# 4.15 Write a program to calculate roots of a quadratic equation

from math import sqrt, pow
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = pow(b, 2) - (4 * a * c)
deno = 2 * a
if d > 0:
    print(f"Real roots: ")
    root1 = -b + sqrt(d)/ deno
    root2 = -b - sqrt(d) / deno
    print(f"Root1 is {root1}, Root2 is {root2}")
elif d == 0:
    print("Equal Root")
    root1 = -b / deno
    print(f"{root1}")
else:
    print("Imaginary Root")