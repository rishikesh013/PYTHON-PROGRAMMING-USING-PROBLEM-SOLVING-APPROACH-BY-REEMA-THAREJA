# 5.30 Write a function to cobvert temperatyre given in celsius to fahrenheit

def cel_to_far(c):
    return f"{(c * 9 / 5) + 32}°F"


print(cel_to_far(26))