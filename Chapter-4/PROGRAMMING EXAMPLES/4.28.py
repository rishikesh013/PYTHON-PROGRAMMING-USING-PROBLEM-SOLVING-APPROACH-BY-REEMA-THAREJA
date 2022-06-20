# 4.28 Write a program to ask the user for a number, and print a countdown from that number to zero

no = int(input("Enter the number: "))
while no != 0:
    # temp = no % 10
    print(no, end=' ')
    no -= 1
