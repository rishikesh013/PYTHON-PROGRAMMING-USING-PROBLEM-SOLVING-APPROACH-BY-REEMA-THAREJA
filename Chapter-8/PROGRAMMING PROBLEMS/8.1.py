# 8.1 Use list comprehension to construct the following list

a = [f'{x}a' for x in range(1, 5)]
print(a)

b = [f'{chr(x)}{chr(y)}' for x in range(97, 99) for y in range(98, 101)]
print(b)
print(b[::2])

print([x for x in range(1, 1000) if x % 10 == 0])