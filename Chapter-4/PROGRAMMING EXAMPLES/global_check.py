var = "Good"


def show():
    # var
    var = 'World'
    # print(locals())
    return locals()


print(show())
print(f"{var}")

a = 1, 2, 4, 4, 3, 32, 3, 43, 43, 4, 4, 3, 4, 34
print(a)
print(type(a))
new_dict = {x for x in a if x > 4}
print(type(new_dict))
print(new_dict)

sum_of_no = lambda x, y: x + y

print(sum_of_no(2, 5))

full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()

print(full_name('    Rishi', 'Kesh'))

print(list(range(50)).sort())