# 4.32 Write a program to calculate the factorial of a number

fact_of_number = int(input("Enter the number to find the factorial: "))

fact_no = 1
for i in range(1, fact_of_number + 1):
    fact_no *= i

print(f"Factorial of the number {fact_of_number} is {fact_no}")
