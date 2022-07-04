# 7.1 Write a program that copies First 10 bytes of a binary file into another

given_String = 'Hello world, How are you doing, hope everything is fine \n with you famm'

with open('file1.txt', 'wb+') as f1:
    byte_conversion = bytearray(given_String, 'UTF-8')
    f1.write(byte_conversion)


with open('file1.txt', 'rb') as f1:
    with open('file2.txt', 'wb+') as f2:
        a = f1.read()
        f2.write(a)
        print(a)# Check the branching