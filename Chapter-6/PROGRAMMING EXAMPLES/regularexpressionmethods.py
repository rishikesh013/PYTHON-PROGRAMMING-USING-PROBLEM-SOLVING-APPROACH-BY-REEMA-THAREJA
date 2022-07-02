import re

given_string = 'She Sells sea shells on the sea sells shore'
pattern1 = 'sells'

print(re.match("She", given_string))
print(re.search(pattern1, given_string))
print(re.sub(pattern1, 'Hi', given_string))

match = re.findall(pattern1, given_string, flags=re.I)
if match:
    # print(x for x in match)
    for i in match:
        print(i)
    print(match)
else:
    print("No match found")

match_iter = re.finditer(pattern1, given_string)

for mat in match_iter:
    print(mat.start())
    print(mat.end())
    print(mat.span())