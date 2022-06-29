# 5.12 Write a program to compute F(x, y) where F(x, y) = F(x-y, y) + 1 if y <= x

def f(x, y):
    if y <= x:
        return f(x - y, y) + 1


print(f(12, 15))


def func_compute(n):
    return lambda x: x * n


result = func_compute(2)
print(result(15))