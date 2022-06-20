# 4.22 Write a program to enter a decimal number. Calculate and display the binary equivalent of this number

decimal_val = int(input("Enter the decimal value to convert: "))
# binary_val = 0
# i = float(0)
# while decimal_val != 0:
#     remainder = decimal_val % 2
#     # binary_val += remainder * (10 ** i)
#     binary_val = binary_val + remainder * (10 ** i)
#     decimal_val /= 2
#     i += 1

print(f"The binary equivalent of the value is {decimal_val:b}")  # Simplest way to convert to binary not sure about loop

# bin() is used to convert to binary but it returns prefix 0b in front of the value,so use replace method to remove that
print(f"The binary equivalent of the value is {bin(decimal_val).replace('0b', '')}")


print(f"Octal value of the decimal number is {oct(decimal_val)}")
print(f"Hexadecimal value of the decimal number is {hex(decimal_val)}")
