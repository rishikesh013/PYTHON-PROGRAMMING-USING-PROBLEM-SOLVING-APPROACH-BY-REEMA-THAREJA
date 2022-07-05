# 8.35 Write a program that has a dictonary of states and their codes. Add another state in the predefined
# dictionary, print all the items in the dictonary and try to print code for a state that does not exist. Set a
# default value prior to printing

states ={'Delhi': 'DL',
         'Haryana': 'HR',
         'Maharashtra': 'MH',
         'Rajasthan': 'RJ'}

print()
states["TamilNadu"] = 'TN'
print(states.get('Karnataka', 'Sorry that doesn\'t exist'))

for key, value in states.items():
    print(f"{key}: {value}")
