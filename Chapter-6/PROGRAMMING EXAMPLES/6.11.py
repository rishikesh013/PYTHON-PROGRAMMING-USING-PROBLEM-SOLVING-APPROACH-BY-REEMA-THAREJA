# 6. 11 Write a program to reverse a string

def reverse_string(sequence):
    new_sequence = ''
    for i in range(len(sequence))[::-1]:
        new_sequence += sequence[i]

    return new_sequence


given_str = input("Enter the sequence: ")
print(reverse_string(given_str))
print(given_str[::-1])