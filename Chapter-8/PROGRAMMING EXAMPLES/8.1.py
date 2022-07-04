# 8.1 Write a program that creates a list of numbers from 1 to 20 that are either divisible by 2 or divisible by 4
# without using the filter function

needed_list = [x for x in range(1, 21) if x % 2 == 0 or x % 4 == 0]
print(needed_list)

