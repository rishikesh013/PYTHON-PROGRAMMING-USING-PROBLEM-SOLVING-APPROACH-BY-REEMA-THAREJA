# 5.2 Write a program that prints the time taken to execute a program in python
import time


def time_taken():
    return time.time()


start_time = time_taken()
for i in range(100000):
    print(i ** 2)

end_time = time_taken()

print(f"Total time of execution is {end_time - start_time}")

# Function that returns the absolute value of a number


def absolute_value(no):
    return abs(no)


print(f"Absolute value of 100 is {absolute_value(100)}")