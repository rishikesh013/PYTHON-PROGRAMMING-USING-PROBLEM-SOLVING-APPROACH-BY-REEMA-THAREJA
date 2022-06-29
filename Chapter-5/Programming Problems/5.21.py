# 5.21 Write a program to calculate x to the power of y, where y can be either negative or positive

def calculate_power(x, y):
    return x ** y


print(calculate_power(2, 3))

new_text = "Hello world this is crazy"
# print()
new_list = " ".join(sorted(new_text.split(), reverse=True))
new_list2 = new_text.split()
# new_list.sort(reverse=True)
# new_list2.reverse()
# print(" ".join(new_list)[::-1])

print(new_text[::-1])
print(new_list)
print(new_list2)