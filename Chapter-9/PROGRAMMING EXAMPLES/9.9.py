# 9.9 Write a program that has a class numbers with values stored in a list. Write a class method to find the largest
# value

class Numbers:
    def __init__(self):
        self.values = []

    def max_value(self):
        return max(self.values)

    def insert_ele(self):
        self.values.append(int(input('Enter the values to insert: ')))


x = Numbers()

while True:
    x.insert_ele()
    ch = input("Do you want to continue Y?N: ")
    if ch.upper() == 'N':
        break

print(x.max_value())