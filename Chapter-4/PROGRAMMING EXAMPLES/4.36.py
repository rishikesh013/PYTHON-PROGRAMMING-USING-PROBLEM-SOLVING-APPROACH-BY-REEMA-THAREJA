# 4.36 Program that displays all leap years from 1900 - 2101
for i in range(1900, 2102):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i, end=' ')

