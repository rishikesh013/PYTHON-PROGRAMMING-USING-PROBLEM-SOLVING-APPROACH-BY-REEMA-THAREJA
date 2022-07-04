# 8.19 Write a program that has a list of functions that scales a number by a factor of 2, 3 and 4. Call each
# function on the given number

l = [lambda x: x * 2, lambda x: x * 3, lambda x: x * 4]

for f in l:
    print(f(5))
print(l[0](100))