# 5.2 Write a program to swap two numbers

def swap_no(a: int, b: int):
    """Function to swap two numbers"""
    a, b = b, a
    return a, b


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1, num2 = swap_no(num1, num2)
print(f"The value of number 1 after swap is {num1}")
print(f"The value of number 2 after swap is {num2}")