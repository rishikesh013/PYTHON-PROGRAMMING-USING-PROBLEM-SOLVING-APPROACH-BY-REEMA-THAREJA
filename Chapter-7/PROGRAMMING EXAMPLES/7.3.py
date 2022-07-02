# 7.3 Write a program that accepts filename as an input from the user. Open the file and count the number of times
# a character appears in the file

file_name = input("Enter the file name: ") + ".txt"
character_to_search = input("Enter the character to search: ")[0]
count = 0
try:
    with open(file_name, 'r') as f:
        a = f.read()
        for i in a:
            if i == character_to_search:
                count += 1

except FileNotFoundError:
    print("This file does not exists check again..")
else:
    print(f"Letter appeared {count} times")