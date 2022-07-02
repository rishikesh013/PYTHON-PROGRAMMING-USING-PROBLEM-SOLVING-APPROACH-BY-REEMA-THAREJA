# 6.20 Write a program to extract a date from a given string
import re
given_string = "Hello, my name is srishti and my date of joining is 11-15-1990 and have experience of more than 17" \
    "years"
result = re.findall(r'\d{2}-\d{2}-\d{2}', given_string)
print(result)

# Modify the program to get the year from the same string

result1 = re.findall(r'\d{4}', given_string)
print(result1)

# Modify to print the words which starts with vowels

result2 = re.findall(r'\b[aeiou]\w+', given_string)
print(result2)