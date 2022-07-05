given_string = "Hello world Whats up"
new_dict = {}

for i in given_string.casefold():
    if not i.isspace():
        new_dict[i] = new_dict.setdefault(i, 0) + 1

new_list = sorted(new_dict)
# for keys, values in new_dict.items():
for i in new_list:
    print(f"{i.upper()}: {new_dict[i]}")

print(len(new_dict))
print(str(new_dict))
new_dict2 = dict.fromkeys(new_list, 0)
print(new_dict2)
print(new_dict.get('54', 'Sorry that dosn\'t exit'))
print(new_dict.has_keys('h'))