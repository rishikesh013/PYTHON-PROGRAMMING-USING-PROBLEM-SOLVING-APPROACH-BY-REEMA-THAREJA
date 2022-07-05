# 8.4 Write a program that converts a list of characters into their corresponding ASCII values using the map() function

import string
import functools

needed_character = list(string.ascii_lowercase)

needed_list = list(map(ord, needed_character))
print(needed_list)

# Write a program using reduce() function to calculate the sum of first 10 natural numbers


def add_no(x, y):
    return x + y


natural_number = [x for x in range(1, 11)]

needed_sum = functools.reduce(add_no, natural_number)

print(dir(natural_number))
print(natural_number)
print(needed_sum)
# 8.7
even_list = list(filter(lambda x: x % 2 == 0, natural_number))
print(even_list)

# 8.8
double_value = list(map(lambda x: x * 2, natural_number))
print(double_value)

needed_tuple = tuple(natural_number)
print(needed_tuple)

# 8.9
one_element_tuple = (('a', 'b', 'c'),)
print(len(one_element_tuple))