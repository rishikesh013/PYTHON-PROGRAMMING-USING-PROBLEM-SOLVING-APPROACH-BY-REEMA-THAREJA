# 5.16 Write a program to print the fibonacci series using recursion
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


no = int(input("Enter the number of terms: "))
for i in range(no + 1):
    print(f"Fibonacci({no}) = {fibonacci(i)}")