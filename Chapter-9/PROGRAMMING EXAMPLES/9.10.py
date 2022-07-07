# 9.10 Write a class that stores a string and all its status details such as number of uppercase, vowels, consonants,
# spaces, etc

class String1:
    def __init__(self):
        self._vowels = 0
        self._upper = 0
        self._lower = 0
        self._space = 0
        self._consonant = 0
        self._given_string = input('Enter the needed string: ')

    def char_count(self):
        for i in self._given_string:
            if i in 'aeiouAEIOU':
                self._vowels += 1
            else:
                self._consonant += 1

            if i == ' ':
                self._space += 1

            if i.isupper():
                self._upper += 1
            if i.islower():
                self._lower += 1

    def __str__(self):
        return f'Vowels: {self._vowels}' \
               f'\n Consonants : {self._consonant}' \
               f'\n Spaces : {self._space}' \
               f'\n Upper : {self._upper}' \
               f'\n Lower : {self._lower}'


s = String1()
s.char_count()
print(s)