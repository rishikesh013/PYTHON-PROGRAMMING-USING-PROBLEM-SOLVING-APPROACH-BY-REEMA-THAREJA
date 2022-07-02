# 6.24 Write a program that replaces ,,;,- from a string with black space character

import re
result = re.sub(r'[,;-]',' ', "Hello! My name- is Srishit.; My date-of-birth is 11-15-1999 abd have experience of,"
                             "more than 17 years;")
print(result)