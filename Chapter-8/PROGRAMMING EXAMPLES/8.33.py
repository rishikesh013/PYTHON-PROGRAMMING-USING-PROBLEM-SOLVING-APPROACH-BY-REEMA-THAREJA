# 8.33 Write a program that creates two sets squares and cubes in range 1- 10. Demonstrate the use of update(),
# pop() , remove(), add(), and clear() functions.

squares_set = set([x ** 2 for x in range(1, 10)])
cube_set = set([x ** 3 for x in range(1, 10)])
print(squares_set)
print(cube_set)
squares_set.update(cube_set)
print(f"Updated: {squares_set}")
print(f"Pop(): {squares_set.pop()}")
squares_set.remove(4)
print(f"Removed 4 from the set: {squares_set}")
squares_set.add(11 * 11)
squares_set.add(11 * 11 * 11)
print(f"Added values: {squares_set}")
squares_set.clear()
print(F"Cleared all the values: {squares_set}")