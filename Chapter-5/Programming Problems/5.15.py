# 5.15 Write a program to compute F(m, n) where F(m, n) can be recursively defined

def F(m, n):
    if m == 0 or m >= n >= 1:
        return 1
    else:
        return F(m - 1, n) + F(m - 1, n - 1)


print(F(12, 13))