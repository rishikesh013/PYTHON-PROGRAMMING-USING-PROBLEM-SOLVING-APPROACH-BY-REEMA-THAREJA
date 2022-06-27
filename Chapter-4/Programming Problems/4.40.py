# 4.40 Write a program to generate the following pattern

# hollow square pattern
size = 5
for i in range(size):
    for j in range(size):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

val = [1, 12.5, 'a', 'python']
print(val[1:2:3])
print()

size = 5
for i in range(size):
    for j in range(size):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            if i == j:
                print('$', end=' ')
            else:
                print('*', end=' ')
        else:
            if i == j:
                print('$', end=' ')
            else:
                print(' ', end=' ')
    print()
