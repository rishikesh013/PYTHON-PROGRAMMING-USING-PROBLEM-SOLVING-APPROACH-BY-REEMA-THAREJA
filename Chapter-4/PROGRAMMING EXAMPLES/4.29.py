# 4.29 Write a program using for loop to calculate the average of first n numbers

n = int(input("Enter the value for n: "))
sum_of_numbers = sum(int(x) for x in range(n + 1))
print(f"The sum of n natural numbers is : {sum_of_numbers}")
print(f"Average of the n natural numbers is : {bin(sum_of_numbers // n).replace('0b', '')}")  # In binary
print(f"Average of the n natural numbers is : {oct(sum_of_numbers // n)}")  # In Octal
print(f"Average of the n natural numbers is : {hex(sum_of_numbers // n)}")  # In Hexadecimal
print(f"Average of the n natural numbers is : {sum_of_numbers / n}")

