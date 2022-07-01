# 6.5 Write a program to generate an Abecedarian series
# Abecedarian refers to a series or list in which the elements appear in alphabetical order

import string


given_word = 'ate'
for i in string.ascii_uppercase:
    print(i + given_word)

