# 6.1 Write a program to print the following pattern

for i in range(1, 7):
    print(end=' ')
    ch = "A"
    for j in range(1, i + 1):
        print(ch, end='')
        ch = chr(ord(ch) + 1)

    print()

print(ord("a"))