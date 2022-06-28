# 5.1 Write a program to check weather two numbers are equal or not

def equal_check(x: int, y: int) -> bool:
    """Function to check weather two numbers are equal"""
    if x == y:
        return True
    else:
        return False


num1 = int(input("Enter the number 1 to check: "))
num2 = int(input("Enter the number 2 to check: "))

if equal_check(num1, num2):
    print("The two numbers are equal!!")
else:
    print("The two numbers are not equal")