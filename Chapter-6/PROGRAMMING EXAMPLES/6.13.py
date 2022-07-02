# 6.13 Write a program that uses a regular expression to match string which starts with a sequence of digits
# (at least one digit) followed by a blank and after this arbitary characters

import re

pattern = r'^[0-9]+ .*'

given_String = '12 abc'
match = re.search(pattern, given_String)
if match:
    print("YEs")