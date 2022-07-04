# 8.17 Write a program that converts a list of temperature in celsius into fahrenheit

def convert(c):
    return (9 / 5) * c + 32


def faren(f):
    return (f - 32) * (5 / 9)


temp_in_c = [36.5, 37, 37.5, 39]

temp_in_f = list(map(convert, temp_in_c))
print(temp_in_f)

temp_to_c = list(map(faren, temp_in_f))
print(temp_to_c)
