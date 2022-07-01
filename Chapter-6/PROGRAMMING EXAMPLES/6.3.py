# 6.3 Write a program that encrypts a message by adding a key value to every character

message = "Hello World"
for i in message:
    print(chr(ord(i) + 3), end=' ')


# Program to split multiple line string

letter = """Hii how are you,
Hope everything is fine with you there and really wish i could be there
things are getting out of hands here and i coudn't control anything
you know gravity is awersome and it makes us live"""

print(letter)
print(letter.split('\n'))