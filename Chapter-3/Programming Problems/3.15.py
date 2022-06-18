# 3.15 Write a program to calculate salary of an employee given hos basic pay(To be entered by the user), HRA = 10
# per cent of basic pay, TA = 5 percent of basic pay. Define HRA and TA as constants and use them to calculate the
# the salary of the employee

basic_pay = float(input("Enter the basic pay: "))
HR = (10/100) * basic_pay
TA = (5/100) * basic_pay

print(F"Total salary is : {basic_pay + HR + TA}")  # Do recheck as am not sure with the how to calculate salary
