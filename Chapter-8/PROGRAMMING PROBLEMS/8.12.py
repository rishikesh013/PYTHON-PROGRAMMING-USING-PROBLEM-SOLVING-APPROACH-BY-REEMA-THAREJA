# 8.12 Write a program that has a dictionary of your friends name and dob in a sorted order. Prompt the user to enter
# a name and check if it is present in the dictionary. If the name does not exit, then ask the user to enter DOB. Add
# the details in the dictionary

friends = {'Abi': 0o6 - 10 - 2001,
           'pranav': 0o4 - 0o7 - 2001
           }

sorted_list = sorted(friends)

for i in sorted_list:
    print(f"{i}: {friends[i]}")

name_to_check = input("Enter the name to check: ")

if friends.get(name_to_check, False):
    print(f"{name_to_check}: {friends[name_to_check]}")
else:
    print("The person does not exist would you like to add ")
    b = input("Enter name: ")
    c = input('Enter DOB: ')
    friends[b] = c
    print(f'{b}: {c}')


