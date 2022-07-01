# 6.7 Write a program that finds whether a given character is present in a string or not. In case it is present it
# prints the index at which it is present. Do not use builtin find functions to search the character

def check_char(character, letter_to_find):
    for index, value in enumerate(character):
        if value == letter_to_find:
            return f"I found in string at {index}"

    return "Character not found"


given_string = input("Enter the string: ")
character_to_check = input("Enter a single character to check: ")[0]

print(check_char(given_string, character_to_check))
print(given_string.find(character_to_check))

# Write a program that emulates the rfind function


def same_like_rfind(character, letter_to_find):
    for i in range(len(character))[::-1]:
        if character[i] == letter_to_find:
            return f"I found in string at {i}"

    return "Character not found"


print(same_like_rfind(given_string, character_to_check))
print(given_string.rfind(character_to_check))

# Count the occurance of a character in a string without using the count function


def count_char(sequence, letter_to_find):
    num_of_occ = 0
    for i in sequence:
        if i == letter_to_find:
            num_of_occ += 1

    return f"The character {letter_to_find} occurred {num_of_occ} times"


print(count_char(given_string, character_to_check))
print(given_string.count(character_to_check))


def count_from_loc(sequence, letter_to_find, start):
    num_of_occ = 0
    for i in range(start, len(sequence)):
        if sequence[i] == letter_to_find:
            num_of_occ += 1

    return f"The character {letter_to_find} occurred {num_of_occ} times"


position_to_start = int(input("Enter the position to start: "))
print(count_from_loc(given_string, character_to_check, position_to_start))