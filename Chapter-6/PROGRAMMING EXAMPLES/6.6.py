# 6.6 Write a program that accepts a string from the user and removes all the vowels from it

def remove_vowels(character):
    letter = ''
    for char in character:
        if char == "a" or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == "E" or \
                char == "I" or char == "O" or char == "U":
            continue
        else:
            letter += char

    return letter


def remove_vowels2(character):
    letter = ''
    for char in character:
        if char in "aeiouAEIOU":
            continue
        else:
            letter += char

    return letter


str_from_user = input("Enter a string: ")
print(f"The string without vowels is: {remove_vowels(str_from_user)}")
print(f"The string without vowels is: {remove_vowels2(str_from_user)}")