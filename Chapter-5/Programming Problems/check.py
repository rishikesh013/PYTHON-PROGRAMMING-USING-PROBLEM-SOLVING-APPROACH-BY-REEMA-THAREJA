from math import sqrt


def perfect_square(n: int) -> bool:
    """Function to check if the given number is a perfect square"""
    result = int(sqrt(n))
    if result * result == n:
        return True
    return False


print(perfect_square(998001))
print(sqrt(25))
print(25 ** 0.5)
