from functools import reduce

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(given_list))
print(max(given_list))
print(given_list.count(7))
print(sum(given_list))
given_list.append("HEllo World")
given_list *= 2
print(given_list)
print(given_list.index(5))  # Index returns values keeping 0 as starting position
given_list.insert(2, 2)
print(given_list)
given_list.pop()
given_list.pop(2)  # Pop takes the index position to pop the elements
print(given_list)
del given_list[10:]
print(given_list)
# del given_list[45]
given_list.remove(7)  # if we want to remove elements directly without specifing the index then remove is used
given_list.append(7)
given_list.append(7)
given_list.append(7)
given_list.append(7)
given_list.append(7)
print(given_list)
given_list.remove(7)
print(given_list)
# given_list.append("Hello world")
# print(given_list)
given_list.sort(reverse=True)  # Sorts according to the ascending or descending order
print(given_list)

cubes_on_list = [x ** 3 for x in range(1, 10)]
print(cubes_on_list)
print([x ** 3 for x in range(1, 10)])
new_list = list(filter(lambda x: x > 20, cubes_on_list))
print(new_list)


# list_of_names = list(map(int, input("Enter the name: ").split()))
# print(list_of_names)


def add(x: int, y: int) -> int:
    return x + y


new_list2 = [1, 2, 3, 4, 5]

# reduced_values = reduce(lambda x: x+=5, new_list2)
# print(reduced_values)
# check_list = list(1, 3, 2, 4, 4, 2, 2, 2)
# print(check_list)

print(dir(new_list2))

empty_list = ()
print(empty_list)
print(type(empty_list))

quo, rem = divmod(20, 2)
print(quo, rem)

new_tuple = (1, 2, 3, 4, 5, 6, 7)
print(id(new_tuple))
new_tuple += (8, 9)
print(id(new_tuple))
print(sum(new_tuple))
print(new_tuple)

print('-----------------')
new_list2 = [1, 2, 3, 4, 5]
print(id(new_list2))
new_list2 += [21, 41]
print(id(new_list2))

new_tuple = (1, [5, 3, 9, [12, 13]])
print(len(new_tuple))
# print(new_tuple[len(new_tuple) - 1][3][1])
print(new_tuple.count(12))

new_tuple2 = (x * 2 for x in new_tuple)
print(next(new_tuple2))
print(next(new_tuple2))
# print(next(new_tuple2))
# print(next(new_tuple2))

new_list3 = [1, 'jew', '1', 53, "hello"]
print(new_list3)
