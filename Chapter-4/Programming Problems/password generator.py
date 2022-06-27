import random

available_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
available_digits = '1234567890'
available_symbols = '!@#$%^&*()_'

total_combination = available_letters + available_letters.lower() + available_symbols + available_digits

new_password = ''
for i in range(8):
    new_password += random.choice(total_combination)

print(new_password)

# length = 8
password = ''.join(random.sample(total_combination, int(input("Enter the length of the password: "))))
print(password)

new_number = random.randint(1, 13)
print(new_number)