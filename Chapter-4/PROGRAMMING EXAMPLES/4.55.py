# 4.55 Write a program that prompts users to enter numbers. The process will repeat until user enters -1.
# Finally, the program prints the count of prime and composite numbers entered

prime_count = comp_count = 0

while True:
    n = int(input("Enter the number: "))
    if n == -1:
        break
    for i in range(2, n + 1):
        if n % i == 0:
            comp_count += 1
            break
        else:
            prime_count += 1
            break
print(f"Total prime numbers is: {prime_count}")
print(f"Total composite numbers is: {comp_count}")