# 5.14 Write a program to calculate GCD using recursion function

def gcd(num1, num2):
    rem = num1 % num2
    if not rem:
        return num2
    else:
        return gcd(num2, rem)


if __name__ == '__main__':

    n = int(input("Enter the first number: "))
    m = int(input("Enter the second number: "))
    print(f"The GCD of the number is {gcd(n, m)}")