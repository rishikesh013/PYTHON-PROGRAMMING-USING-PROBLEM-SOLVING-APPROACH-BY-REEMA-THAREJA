# 6.14 Write a program to extract each character from a string using regular expression

import re
# import regex
result = re.findall(r'.', 'Going Good')
print(result)

# 6.15 Program to extract each word from a string using regular expression

result2 = re.findall(r'\w+', 'Going good python')
print(result2)

# 6.16 Program to print the first word of a string

result3 = re.findall(r'^\w+', 'Going good python')
print(result3)

# 6.17 Program to print the Last word of a string

result4 = re.findall(r'\w+$', 'Going good python')
print(result4)

# 6.18 Write a program to print the characters in pairs

result5 = re.findall(r'[a-zA-z]{2}', "Going good python")
print(result5)

# 6.19 Write a program to print only the first two characters of every word
result6 = re.findall(r'\b[a-zA-z]{2}', "Going good python")
print(result6)