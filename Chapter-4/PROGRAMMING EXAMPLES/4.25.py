# 4.25 Write a program to enter a number and then calculate the sum of its digits

sumOfDigits = 0
num = int(input("Enter the number to find the sum: "))

n = num
while n != 0:
    rem = n % 10
    sumOfDigits += rem
    n //= 10

print(f"Sum of digits is : {sumOfDigits}")
j = sum(int(x) for x in str(num))
print(j)
