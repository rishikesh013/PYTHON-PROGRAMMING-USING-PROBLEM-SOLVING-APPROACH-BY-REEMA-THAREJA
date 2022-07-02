# 6.23 Write a program that validates a mobile phone number. The number should start with 7, 8, or 9 followed by 9 dig

import re

pattern = r'^[789]\d{9}'
list_of_no = ['7838456789', '1234567890', '9876543210', '8901234567', '4567890123']
for i in list_of_no:
    result = re.findall(pattern, i)
    if result:
        print(result, end=' ')