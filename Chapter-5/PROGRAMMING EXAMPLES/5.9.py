# 5.9 Write a program that computes p(n / r)

def factorial(no: int) -> int:
    """Function to calculate the factorial of a number"""
    if no == 0 or no == 1:
        return 1
    else:
        return no * factorial(no - 1)


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of n: "))
result = float(factorial(n) / float(factorial(r)))
print(f"P({n} / {r}) = {result}")
print("_______________________________________")

num = int(input("Enter the value of n: "))
s = 0.0
for i in range(1, num + 1):
    s += float(i ** i) / factorial(i)

print(f"Result: {s}")