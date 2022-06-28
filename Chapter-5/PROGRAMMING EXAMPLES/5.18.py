# 5.18 Write a program to add two numbers using the command line arguments
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
sum_of_numbers = a + b
print(f"Sum= {sum_of_numbers}")

# Note Run this code in any CMD or terminal to actually see the working