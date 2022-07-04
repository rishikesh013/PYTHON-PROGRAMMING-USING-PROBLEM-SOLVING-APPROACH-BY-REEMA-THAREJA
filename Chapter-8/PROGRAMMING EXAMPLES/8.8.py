# 8.8 Write a program to remove all the duplicates from the list

given_list = list(map(int, input().split()))

new_list = list(set(given_list))
print(new_list)

new_list2 = list(dict.fromkeys(given_list))
print(new_list2)

