# 4.3 Write a program that determines weather an alphabet, digit or a whitespace was entered

no_of_lower = no_of_upper = no_of_digit = 0
while True:
    char_to_check = input("Enter a single character to check: ")[0]
    if char_to_check.isalpha():
        print("The character is an alphabet")
        if char_to_check.isupper():
            # print("\tThe character is in uppercase")
            no_of_upper += 1
        else:
            # print(f"\tThe character is in lowercase")
            no_of_lower += 1
    elif char_to_check.isdigit():
        print(f"The character is a digit")
        no_of_digit += 1
    elif char_to_check.isspace():
        print(f"This is a white space")
    else:
        break

print(f"The number of upper character is {no_of_upper}")
print(f"The number of lower character is {no_of_lower}")
print(f"The number of digits is {no_of_digit}")