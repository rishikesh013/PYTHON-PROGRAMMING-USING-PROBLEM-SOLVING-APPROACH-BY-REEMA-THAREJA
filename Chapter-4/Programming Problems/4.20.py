# 4.20 Write a program to print the prime factors of a number

# Python program to print prime factors

import math


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i and divide n
        while n % i == 0:
            print(i),
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


# Driver Program to test above function

n = 1092
primeFactors(n)

no = int(input("Enter the number: "))

for i in range(no):
    for k in range(no, i, -1):
        print(" ", end='')
    for j in range(i + 1):
        print('*', end='')

    print()

# no2 = int(input("Enter the number: "))
no2 = 4
for i in range(1, no2 + 1):
    # print(" ", end='')
    for k in range(no2, i, -1):
        print(" ", end='')
    for j in range(1, i + 1):
        print('*', end=' ')
    print()

