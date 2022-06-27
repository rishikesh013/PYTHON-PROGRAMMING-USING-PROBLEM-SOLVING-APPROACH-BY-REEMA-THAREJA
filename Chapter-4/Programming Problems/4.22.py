# 4.22 Write a program to print the Floyd's Triangle

no = int(input("Enter the number of rows: "))
count = 1
for i in range(1, no + 1):
    print(end='')
    for j in range(1, i + 1):
        print(count, end=' ')
        count += 1
    print()

