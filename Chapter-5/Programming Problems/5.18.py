# 5.18 Write a function that accepts a number n as input and returns the average of numbers from 1 to n

def avg(n):
    len_of_numbers = len(range(1, n + 1))
    sum_of_number = sum(x for x in range(1, n + 1))
    return sum_of_number / len_of_numbers


print(avg(100))


# 5.20 Calculate the area of a triangle

def triangle_area(base, height):
    return int(0.5 * base * height)


print(triangle_area(4, 3))
