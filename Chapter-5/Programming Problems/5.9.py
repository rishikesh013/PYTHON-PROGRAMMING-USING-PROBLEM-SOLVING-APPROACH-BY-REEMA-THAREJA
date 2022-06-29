# 5.9 Write a program to concatenate two strings using recursion

def orderedConcat(a, b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    else:
        if a[0] < b[0]:
            return a[0] + orderedConcat(a[1:], b)
        else:
            return b[0] + orderedConcat(a, b[1:])


print(orderedConcat("Hello", "World"))


def reverse_int(n, r=0):
    if n == 0:
        return r
    else:
        return reverse_int(n // 10, r * 10 + n % 10)  # n = 35 r = r * 10 + 35 % 10
        # r = 5
        # r = 53
        # n %= 10
        # r *= 10
        # r += n
        # n //= 10


print(reverse_int(12))
