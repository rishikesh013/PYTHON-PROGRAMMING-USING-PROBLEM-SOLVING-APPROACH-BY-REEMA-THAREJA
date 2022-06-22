# 4.51 Write a program to print the following pattern

N = 5
for i in range(1, N + 1):
    for k in range(N, i, -1):
        print(" ", end=' ')

    for j in range(1, i + 1):
        print(j, end=' ')

    print()

print("-----------------------------------------")

M = 5
for i in range(1, M + 1):
    for k in range(M, i, -1):
        print(" ", end=' ')

    for j in range(1, i + 1):
        print(j, end=' ')

    for ln in range(i - 1, 0, -1):
        print(ln, end=' ')

    print()

print("____________________________________________")

S = 5
for i in range(1, S + 1):
    for k in range(S, i, -1):
        print("", end=' ')

    for j in range(1, i + 1):
        print(i, end=' ')

    print()

