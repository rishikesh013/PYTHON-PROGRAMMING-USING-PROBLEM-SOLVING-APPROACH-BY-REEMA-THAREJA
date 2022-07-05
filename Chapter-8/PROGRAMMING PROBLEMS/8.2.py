# 8.2 Make a list of five random numbers

import random
import string

needed_list = [random.randint(1, 1000) for x in range(1, 6)]
print(needed_list)

new_list = ''
needed_string = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

new_list += ''.join(random.sample(needed_string, 8))
print(new_list)

first_ten_char = [chr(x) for x in range(97, 108)]
print(first_ten_char[len(first_ten_char) // 2:len(first_ten_char) // 2 + 3:])


