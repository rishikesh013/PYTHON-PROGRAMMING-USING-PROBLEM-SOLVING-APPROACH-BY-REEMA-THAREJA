import re

string_pattern = 'She sells sea shells on the sea shore'
pattern1 = "she"

if re.sub(pattern1,"Hi", string_pattern):
    print("Yes")

print(re.sub(pattern1,"Hi", string_pattern, flags=re.IGNORECASE))