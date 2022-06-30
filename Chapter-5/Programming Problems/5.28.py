# 5.28 Calculate fibonacci using recursion

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(5):
    print(fibonacci(i))

# Without using recursion
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
no_of_terms = int(input("Enter the number of terms: "))
while no_of_terms - 2:
    c = a + b
    a = b
    b = c
    print(c)
    no_of_terms -= 1