# 4.14 Write a program to take input from the user and then check weather it is a number or a character. If it is a
# character, determine whether it is in uppercase or lowercase

ch = input("Enter the character to check: ")[0]

if ch.islower():
    print(f"It is a lower case character converted to uppercase is {ch.upper()}")
elif ch.isupper():
    print(f"It is a uppercase character, converting to lowercase: {ch.lower()}")
else:
    print(f"The above character is a digit {ch}")

# check_list = ['Hello', 'World']
# # check_list.sort(reverse=True)
# new_list = sorted([i[::-1] for i in check_list])
# # new_list = check_list.reverse()
# print(f'{new_list}')
lst = [11, 18, 9, 12, 23, 4, 17]
lost = []
lost1 = list()
for idx in range(len(lst)):
    val = lst[idx]
    if val > 15:
        lost.append(val)
        lst[idx] = 15

lost1 = [val for val in lst if val > 15]
# lost1.append
print(lost1)
print("______________________")
print(lst)
