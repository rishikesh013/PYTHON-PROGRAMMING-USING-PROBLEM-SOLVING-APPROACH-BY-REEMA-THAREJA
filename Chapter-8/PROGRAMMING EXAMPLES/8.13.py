# 8.13 Create a list that has both positive and negative number and use filter function to filter only positive number

given_list = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]

needed_list = list(filter(lambda x: x > 0, given_list))
print(needed_list)

list1 = ['HELLO', 'WELCOME', 'TO', "PYTHON"]
list2 = list(map(lambda x: x.lower(), list1))
print(list2)

for i in list1:
    print(i)


square_of_number = list(map(lambda x: x ** 2, range(1, 11)))
print(square_of_number)

print([(x, y) for x in [10, 20, 30, 50] for y in [35, 40, 55, 60] if x % y == 0 or y % x == 0])