# 5.25 Write a program to reverse a string without using recursion

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


print(reverse_string(input("Enter a string to reverse: ")))

# Write a program to calculate the exponential using recursive function


def exp(x, y):
    if y == 0:
        return 1
    else:
        return x * exp(x, y - 1)

# Program to calculate the exponential without using recursion


def exp_without_rec(x, y):
    result = 1
    for i in range(y):
        result *= x

    return result


print(exp_without_rec(5, 3))