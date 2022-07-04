# 8.5 Write a program to print index at which a particular value exists. It the value exists at multiple locations in
# the list, then print all the indices. also count the number of times that value is repeated in the list

num_list = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

num = int(input("Enter the value to be searched: "))
count_times = 0
for i in range(len(num_list)):
    if num_list[i] == num:
        print(f"Index at {i}")
        count_times += 1

print(f"Count is {count_times}")
print()
print('______________________________')
for index, val in enumerate(num_list):
    if val == num:
        print(f"Index at {index}")
        count_times += 1

print(f"Count is {count_times}")