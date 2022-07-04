# 8.18 Write a program to find the largest value in a list using reduce() function

from functools import reduce

num_list = [4, 1, 8, 2, 9, 3, 0]


def max_ele(x, y):
    if x > y:
        return x

    return y


num_list1 = reduce(max_ele, num_list)
print(num_list1)