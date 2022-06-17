# 3.1 Write a program to enter a number and display it's hex and octal value equivalent and it's square root

num = int(input("Enter a number: "))

print(f"Hex value of the number is {hex(num)}")
print(f"Octal value of the number is {oct(num)}")
print(f"Square root of the number is {num ** 0.5}")
