# 3.7 Write a program to swap two numners with the help of a temporary variable

number_1 = int(input("Enter the number one: "))
number_2 = int(input("Enter the number two: "))

temp = number_1
number_1 = number_2
number_2 = temp

print(f"The value of the number one is {number_1}")
print(f"The value of the number two is {number_2}")

# More Pythonic way of writing

number_1 = int(input("Enter the number one: "))
number_2 = int(input("Enter the number two: "))

number_1, number_2 = number_2, number_1
print(f"The value of the number one is {number_1}")
print(f"The value of the number two is {number_2}")
