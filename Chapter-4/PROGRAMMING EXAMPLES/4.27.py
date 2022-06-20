# 4.27 Write a program to print the reverse of a number

num = int(input("Enter the number: "))
print("The reversed number is :", end='')
while num != 0:
    temp = num % 10
    print(temp, end='')
    num //= 10

# simplest form for this without using loop

print()
num1 = int(input("Enter the number: ")[::-1])
print("The number in reverse form is: {}".format(num1))
