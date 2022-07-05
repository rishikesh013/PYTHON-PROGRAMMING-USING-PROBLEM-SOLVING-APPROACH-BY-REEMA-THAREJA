# 8.31 Write a program that generates a set of prime numbers and another set of odd numbers. Demonstrate the result
# of union, intersection, difference and symantic difference operations on these sets


def is_prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


new_list = []
for j in range(100):
    if is_prime(j):
        new_list.append(j)


def odd_no(n):
    if n % 2 != 0:
        return True


odd_set = set([x for x in range(1, 20) if odd_no(x)])
prime_set = set([y for y in range(1, 20) if is_prime(y)])
print(prime_set)
print(odd_set)
print(f"Union: {odd_set | prime_set}")
print(f"Union: {odd_set.union(prime_set)}")
print(f"Intersection: {odd_set & prime_set}")
print(f"Intersection: {odd_set.intersection(prime_set)}")
print(f"Difference: {odd_set - prime_set}")
print(f"Difference: {odd_set.difference(prime_set)}")
print(f"Semantic Difference: {odd_set ^ prime_set}")
print(f"Semantic Difference: {odd_set.symmetric_difference(prime_set)}")