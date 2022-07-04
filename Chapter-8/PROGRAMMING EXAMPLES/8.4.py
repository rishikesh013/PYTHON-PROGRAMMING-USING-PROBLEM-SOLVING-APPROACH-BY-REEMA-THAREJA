# 8.4 Write a program to carate a list of numbers in the range 1 - 10. Then delete all the even numbers from the list
# print the final list

# needed_list = list(map(int, range(1, 11)))
needed_list = [x for x in range(1, 11)]
print(needed_list)

# remove_even = [needed_list.pop(i) for i in range(len(needed_list)) if needed_list[i] % 2 == 0]
# print(remove_even)

for index, value in enumerate(needed_list):
    if value % 2 == 0:
        needed_list.pop(index)

print(needed_list)