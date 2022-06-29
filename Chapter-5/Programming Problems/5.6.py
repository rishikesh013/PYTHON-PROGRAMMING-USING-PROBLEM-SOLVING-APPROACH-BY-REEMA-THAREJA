# 5.6 Write a function is_prime() that returns a 1 if the argument passed to it is a prime a number and a 0 otherwise
import check
from calendar import isleap

def is_prime(n):
    if n <= 1:
        return 0

    for i in range(2, n):
        if n % i == 0:
            return 0
    else:
        return 1


# check_no = int(input("Enter the number to check:  "))
perfect_squares_list = []
count_of_perfect_squares = 0
for i in range(1, 1000):
    if is_prime(i):
        print(f"{i} This is a prime number")
    else:
        print(f"{i} This is not a prime number")
        if check.perfect_square(i):
            perfect_squares_list.append(i)
            count_of_perfect_squares += 1
            # print(f"{i} is also a perfect square")

print(f"Total number of perfect squares present are {count_of_perfect_squares}")
print(perfect_squares_list)


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def is_leap_year2(year: int) -> bool:
    """Leap year is calculated using the inbuilt module called calender"""
    if isleap(year):
        return True
    return False


if is_leap_year(int(input("\nEnter the year: "))):
    print("It is a leap year")
else:
    print("It is not a leap year")

if is_leap_year2(int(input("\nEnter the year: "))):
    print("It is a leap year")
else:
    print("It is not a leap year")