# 8.2 Write a program using filter function to a list of square of numbers from 1 - 10. Then use the for .. in
# constructor to sum the elements in the list generated

needed_list = list(map(lambda x: x ** 2, range(1, 11)))
print(needed_list)
print(sum(needed_list))