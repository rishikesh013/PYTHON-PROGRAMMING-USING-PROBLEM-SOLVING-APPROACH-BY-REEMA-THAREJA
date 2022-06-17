# 3.2 Write a program to read and print values of variables of different datatypes

num_int = int(input("Enter the integer number: "))
num_float = float(input("Enter the floating point number"))
word = input("Enter the word of characters")

print(f"The num_int is of the type {type(num_int)} and the value is {num_int:2}")
print(f"The num_float is of the type {type(float)} and the value is {num_int:2}")
print(f"The word is of the type {type(word)} and the string is {word}")
