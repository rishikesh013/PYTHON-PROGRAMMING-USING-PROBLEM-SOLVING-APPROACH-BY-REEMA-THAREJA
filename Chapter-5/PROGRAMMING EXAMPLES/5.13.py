# 5.13 Write a program to print the following pattern using default arguments

def pattern(typeof_design='%', n=6, r=1):
    for i in range(r):
        print()
        for j in range(n):
            print(typeof_design, end=' ')


char_to_display = input("Enter the character to be displayed: ")
n = int(input("Enter the number of rows:  "))
m = int(input("Enter the number of columns: "))
pattern()
pattern(char_to_display)
pattern(char_to_display, n)
pattern(char_to_display, n, m)