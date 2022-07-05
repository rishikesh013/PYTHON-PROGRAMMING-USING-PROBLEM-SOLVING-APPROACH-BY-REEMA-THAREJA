# 8.45 Write a program that print a histogram of frequencies of characters occurring in a message

given_string = "Hello All, Good Morning... Welcome to the World of Python".lower()
new_dict = {}

for i in given_string.casefold():
    new_dict[i] = new_dict.setdefault(i, 0) + 1

new_list = sorted(new_dict)
# for keys, values in new_dict.items():
for i in new_list:
    print(f"{i.upper()}: {new_dict[i]}")

for key, values in new_dict.items():
    print(f'{key}: {"*" * values}')

# Write a program that prompts the user to enter a file name. Open the file and print the frequency of each word in it.

filename = input("Enter the file name: ") + '.txt'
new_dict2 = {}

try:
    with open(filename, 'r') as f:
        a = f.read()
        for i in a.casefold():
            new_dict2[i] = new_dict2.setdefault(i, 0) + 1

except FileNotFoundError:
    print('This file does not exist')
else:
    new_list = sorted(new_dict2)

    for i in new_list:
        print(f"{i.upper()}: {new_dict2[i]}")

    for key, values in new_dict2.items():
        print(f'{key}: {"*" * values}')

if new_dict == new_dict2:
    print('True')