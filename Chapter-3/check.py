t = ['a', 'b', 5, 6, 7, 'c']
t2 = 'x', 'y', 'z'
print(t, )
print(*t * 20)
# print(t + t2)
print(type(t2))
print(type)

new_list = [*""]
with open('check1.txt', 'r') as file:
    a = file.read().strip().split()
    a.sort(reverse=True, key=str.casefold)
    b = [x[::-1] for x in a]
    # for f in file:
    #     new_word = f[::-1].strip()
    #     new_list.append(new_word)
    #
    # print(new_list)
    print(a)
    print(b)

with open('check1.txt', 'a') as file1:
    file1.write("Hey his is a dummy text to add")


