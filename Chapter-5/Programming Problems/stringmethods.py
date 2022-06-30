# Capitalize is used to capitalize the first character of the string
str1 = "hello"
print(str1.capitalize())

# center(width, fillcharacter) is used to center the character to the given width and fill the empty space with fillchar
print(str1.capitalize().center(100, '*'))

# count(str, beg, end) used to search for a character in a sequence from the beginig and the end values specified
char = "hi"
given_str = "hi my name is rishikesh and hi again to increase the count lol hi once more"
given_str2 = """hi my name is rishikesh and
hi again to increase the count lol hi once more"""
print(given_str.count(char))

# endswith(suffix, beg, end) is used to check if the string ends with the given suffix return True or False
print(given_str.endswith("re"))

# startswith(prefix, beg, end) checks if the given string starts with the given prefix and returns True if so
print(given_str.startswith("Hi"))
# find(str, beg, end) checks id the str is present in the string. If found it returns the position at which str
# occurs in string, otherwise returns -1
print(given_str.find('rishi'))
# index(str, beg, end) same as find but raises an error if the character is not found
print(given_str.index('rishi'))
# rfind(str, beg, end) same as find but starts searching from the right
print(given_str.rfind('hi'))

# rindex(Str, beg, end) same as index but searches from the end
print(given_str.rindex("hi"))

# ljust(width, fillcharacter) is used to left justify the total width columns. columns without character are padded
# with the character specified in the fill character

print(str1.ljust(10, "*"))

# rjust(width , fillcharacter) is just opposite of the ljust and does it on the right side

print(str1.rjust(10, '*'))

# zfill(width) returns a string with left padded with zeros to a total of width characters.
print(str1.zfill(10))

# strip() removes all the leading and trailing whitespace in string if any argument passed it removes that
print(given_str.strip("h"))

# lstrip() and rstrip() as the name suggest removes the left add right characters from the string
print(given_str2.lstrip('h'))
print(given_str.rstrip('h'))

# max() and min() when dealing with the str returns the character with highest and lowest ascii values
print(max(given_str))

# replace(old, new, max) is used to replace a character from the string and max is used to set the limit on how many
# times these characters should be replaced
print(given_str.replace('hi', 'bye', 2))

# title() is used to capatalize all the first characters in a string while capatilize is used just for the first char
print(given_str.title())
print(given_str.capitalize())

# swapcases() is used to swap cases like upper to lower and lower to upper
print(given_str.swapcase())

str_check = ''
print(str_check.isidentifier())


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


a = str(input("Enter the string to be reversed: "))
print(reverse(a))