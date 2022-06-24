# 4.12 Write a program that prints a number, its square, and cube repeatedly in the range (1, n)

from math import pow

value_of_n = int(input("Enter the value of n: "))

for i in range(1, value_of_n + 1):
    print(f"Square of {i} is {int(pow(i, 2))}")
    print(f"Cube of {i} is {int(pow(i, 3))}")

string_to_check = "Hello"
print(len(string_to_check))

given_text = "oxford university press"
given_list = ["OXFORD", "UNIVERSITY", "PRESS"]
# for i in given_text.upper():
#     print(i, end='')
# print()
# for i in given_text.lower():
#     print(i, end='')
# print()
# for i in given_list:
#     i.upper()
#     if i[0].isupper():
#         i[0].lower()
#     print(i, end=' ')

print(x.upper() for x in given_list)

for i in given_list:
    print(i.upper(), end=' ')


print("------------------------")
new_list = [x.lstrip().lower() for x in given_list]
print(new_list)


# print(new_list)

print(given_text.capitalize())

new_list = [s[0].lower() + s[1:] for s in given_list]
print(new_list)