# 4.7 Bonus of 5% if its a male employee or 10% if it is a female employee and additional bonus of 2% if the salary
# is less than 10000

sex_of_employee = input("Enter the sex of the employee(m or f): ")[0].casefold()
sal = int(input("Enter the salary of the employee: "))

bonus = 0
if sex_of_employee == 'm':
    bonus += 5/100 * sal
else:
    bonus += 10/100 * sal

total_salary = bonus + sal
if total_salary <= 10000:
    total_salary += 2/100 * sal

print(f"The total salary of the employee is {total_salary}")
