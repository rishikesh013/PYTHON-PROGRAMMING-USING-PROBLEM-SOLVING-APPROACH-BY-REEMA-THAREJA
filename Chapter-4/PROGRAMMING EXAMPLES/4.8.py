# 4.8 Write a program to check weather a given year is a leap year or not

check_for_leap = int(input("Enter a year: "))

if (check_for_leap % 4 == 0 and check_for_leap % 100 != 0) or (check_for_leap % 400 == 0):
    print(f"{check_for_leap} is a leap year")
else:
    print(f"{check_for_leap} is not a leap year")
