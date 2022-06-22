# 4.45 Write a program to print the following pattern

for i in range(1, 6):
    print(f"Pass {i}- ", end=' ')
    for j in range(1, 6):
        print(f"{j}", end=' ')

    print()