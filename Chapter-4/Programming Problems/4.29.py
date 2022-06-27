# 4.29 Write a program that display all the numbers from 1 - 100 that are not divisible by 2 and 3

for i in range(1, 101):
    if i % 2 != 0 and i % 3 != 0:
        print(i)

# Sum of all odd numbers from 1 to 100

sum_of_odd = sum(int(s) for s in range(1, 101, 2))
print(sum_of_odd)

# 4.36 Interactive program to read an integer. If it is positive then display the corresponding binary representation
# of that number. The user must enter 999 to stop the program and negative numbers will be ignored

while True:
    no = int(input("Enter the number to calculate binary and 999 to stop the program: "))
    if no == 999:
        break
    elif no < 0:
        continue
    else:
        print(f"Binary representation of {no} is {no: b}")
