import string
import random
a = 10
b = 20
if not 10 + 10 == b or a == 40 and 70 == 80:
    print("Yes")
elif a != b:
    print("No")

print(10 + 10 == b or a == 40 and 70 == 80)
# print(10 + 10 == b)
# print(a == 40)
print(10 + 10 == b or a == 40)
print(not True and 70 == 80)

for i in range(10):
    if not i % 2 == 0:
        print(i + 1)

    print(i)

# print(i)


print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.printable)
print("".join(random.sample(string.punctuation + string.ascii_letters, 12)))
# print(string.hexdigits)
# print(string.__doc__)
# print(string.punctuation)
# help(string.whitespace)

# a = list(map(int, input("Enter the values: ")))
# print(a)
print(string.whitespace)