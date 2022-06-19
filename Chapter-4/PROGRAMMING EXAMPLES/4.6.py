# 4.6 Write a program to enter any character. If the entered character is in lowercase then convert it into uppercase
# and if tt is an lowercase character, then convert it into lowercase

given_char = input("Enter a character to check: ")[0]

if given_char.islower():
    given_char = given_char.upper()
else:
    given_char = given_char.lower()

print("The given character is {}".format(given_char))
