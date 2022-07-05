# 8.32 Write a program that creates two sets. One of even numbers in range 1 - 10 and the other has all composite
# numbers in range 1 - 20. Demonstrate the use of all(), issuperset(), len(), and sum() functions on the sets.

def is_prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True


composite_no = set([x for x in range(1, 21) if not is_prime(x)])
even_no = set([y for y in range(1, 11) if y % 2 == 0])

print(composite_no)
print(even_no)
print(f"All: {all(even_no)}")
print(f"Length of composite no is: {len(composite_no)}")
print(f"Length of all numbers in evens set: {sum(even_no)}")