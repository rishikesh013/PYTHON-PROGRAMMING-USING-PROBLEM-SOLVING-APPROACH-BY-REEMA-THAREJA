# 8.48 Write a program that combines the list to a dictionary

keys = ['Name', 'Age', 'Martial Status']
values = ['Om', 38, 'Married']
details = zip(keys, values)
print(list(details))
new_dict = dict(details)
print(new_dict)