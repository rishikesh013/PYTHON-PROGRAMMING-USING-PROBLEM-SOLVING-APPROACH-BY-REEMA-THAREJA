# 3.5 Write a program to print the ascii value of the character

value_to_find = input("Enter the single character to find the ascii: ")[0]
print(f"The ascii value of the character is {ord(value_to_find)}")

# for a sequence of characters
sequence_of_char = input("Enter the sequence of the characters to find the ascii: ")
for i in sequence_of_char.strip():
    print(f"The ascii value of {i} is {ord(i)}")