# 4.47 Write a program to print the following pattern

for i in range(1, 6):
    print(end=' ')
    for j in range(i):
        print('*', end=' ')

    print()


print("___________________________________________________")

for i in range(1, 6):
    print(end='')
    for j in range(i):
        print(j + 1, end=' ')

    print()


print("__________________________________________________________")

for i in range(1, 6):
    print(end='')
    for j in range(i):
        print(i, end=' ')

    print()


print("__________________________________________________________")

count = 0
for i in range(1, 6):
    print(end='')
    for j in range(i):
        print(count, end=' ')
        count += 1
    print()