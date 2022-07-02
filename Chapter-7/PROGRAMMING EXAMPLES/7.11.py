# 7.11 Write a program that fetches data from a specified url and writes it in a file

import urllib.request

x = urllib.request.urlopen('https://www.google.com/')
print(x.read())

with open('file2.txt', 'w') as f2:
    f2.write(str(x.read()))