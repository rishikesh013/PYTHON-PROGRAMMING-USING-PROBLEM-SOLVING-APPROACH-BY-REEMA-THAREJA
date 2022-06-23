# 4.1 Write a program to input two numbers and check whether they are equal or not

number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))

if number1 == number2:
    print(f"They are equal")
else:
    print(f"They are not equal")


a = 5
print(id(a))
a += 2
print(id(a))