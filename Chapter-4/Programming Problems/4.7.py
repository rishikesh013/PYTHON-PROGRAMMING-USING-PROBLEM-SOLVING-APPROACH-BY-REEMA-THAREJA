# 4.7 Write a program that displays first 10 natural numbers using for loop

for i in range(1, 11):
    print(i)

# 4.9 Weather to check weather it is a leap year

year_to_check = int(input("Enter the year to check for the leap: "))

if year_to_check % 4 == 0 and year_to_check % 100 != 0 or year_to_check % 400 == 0:
    print(f"This is a leap year!!")
else:
    print(f"Not a leap year")

# 4.10 Write a program that finds the average of first n numbers using for loop

user_number = int(input("Enter the number to find the average: "))
sum_of_number = sum(int(x) for x in range(user_number + 1))
print(f"The average of the n numbers is {sum_of_number / user_number}")
