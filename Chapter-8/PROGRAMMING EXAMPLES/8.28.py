# Write a program that has a list of numbers(both positive and negative numbers) .Make a new tuple that has only
# positive values from the list

given_tuple = (-10, 1, 2, -9, 3, 4, -8, 5, 6)
new_tuple = tuple()

for i in given_tuple:
    if i > 0:
        new_tuple += (i, )

print(new_tuple)

# Write a program that accepts different number of arguments and returns sum of only the positive values to it.


def sum_of_positive(*args):
    tot = 0
    print(type(args))
    for i in args:
        if i > 0:
            tot += i

    return tot


print(sum_of_positive(1, -9, 2, -8, 3, -7, 4, -6, 5))