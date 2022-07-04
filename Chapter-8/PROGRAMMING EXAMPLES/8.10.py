# 8.10 Write a program to create a list of 10 random integers. Then create two lists odd list and even list that has all odd and even values in the list respectively

import random


random_list = []
# random_list = [random.randint(1, 100) for i in range(10)]
# print(random_list)
for i in range(10):
    random_list.append(random.randint(1, 100))

print(random_list)

odd_list = [x for x in random_list if x % 2 != 0]
even_list = [x for x in random_list if x % 2 == 0]
print(odd_list)
print(even_list)

odd_list_of_20 = [2 * i + 1 for i in range(20)]
print(odd_list_of_20)