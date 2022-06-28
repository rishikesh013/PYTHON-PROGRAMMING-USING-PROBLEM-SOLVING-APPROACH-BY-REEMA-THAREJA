# Write a program to calculate the exp(x, y) using recursive function

def exp(x, y):
    if y == 0:
        return 1
    else:
        return x * exp(x, y - 1)


n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
print(f"Result: {exp(n, m)}")
