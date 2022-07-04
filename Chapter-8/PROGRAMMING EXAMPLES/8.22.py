# 8.22 Write a program to find the median of a list of numbers

given_list = list()
n = int(input("Enter the number of elements to be inserted in the list: "))

for i in range(n):
    given_list.append(int(input(f"Enter the number {i + 1}: ")))

given_list.sort()

print(given_list)

i = len(given_list) - 1
if n % 2 != 0:
    print("Median = ", given_list[i // 2])
else:
    print("Median = ", (given_list[i // 2] + given_list[i + 1 // 2]) / 2)