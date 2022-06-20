# 4.24 Write a program to read a character until a * is encountered. Also count the number of uppercase, lowercase,
# and numbers entered by the user

lower_count = upper_count = digit_count = 0
while True:
    ch = input("Enter the character to be read: ")[0]
    if ch == "*":
        break
    elif ch.islower():
        lower_count += 1
    elif ch.isupper():
        upper_count += 1
    else:
        digit_count += 1

print(f"No of lowercase character are: {lower_count}")
print(f"No of uppercase character are: {upper_count}")
print(f"No of digit character are: {digit_count}")