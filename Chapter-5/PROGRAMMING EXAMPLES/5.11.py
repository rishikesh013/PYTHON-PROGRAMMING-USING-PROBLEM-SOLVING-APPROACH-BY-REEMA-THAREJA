# 5.11 Write a program that uses docstring and variable length of arguments to add the values passed to the function

def addition_of_digits(*args):
    """Function to add numbers """
    sum_of_values = 0
    for i in args:
        sum_of_values += i

    return sum_of_values


print(f"Sum = {addition_of_digits(12, 42,12, 23, 53, 21, 43)}")
print(addition_of_digits.__doc__)