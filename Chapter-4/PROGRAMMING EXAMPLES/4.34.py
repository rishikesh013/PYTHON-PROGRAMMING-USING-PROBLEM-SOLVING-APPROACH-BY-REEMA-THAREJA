# 4.34 Write a program to count the number of prime and composite until user types -1

no_of_prime = 0
no_of_composite = 0

while True:
    ch = int(input("Enter the value and '*' to exit: "))
    if ch == -1:
        break
    for i in range(2, ch + 1):
        if ch % i == 0:
            no_of_composite += 1
            break
        else:
            no_of_prime += 1
            break

print(f"Total number of prime numbers is {no_of_prime}")
print(f"Total number of composite numbers is {no_of_composite}")