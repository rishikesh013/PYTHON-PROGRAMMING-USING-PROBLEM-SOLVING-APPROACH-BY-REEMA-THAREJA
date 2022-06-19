# 4.2 Write a program to determine the characters entered by the user
user_char = input("Enter the character")[0]
if user_char.isalpha():
    print(f"The entered character is {user_char} is an alphabet")

if user_char.isdigit():
    print(f"The entered character {user_char} is an digit")

if user_char.isspace():
    print(f"The entered character {user_char} is a space")

