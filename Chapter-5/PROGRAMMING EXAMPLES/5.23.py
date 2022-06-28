# 5.23 Write a program that prompts the user the getpass module to prompt the user for a password without echoing what
# they typed to the console

import getpass
password = getpass.getpass(prompt="Enter the password: ")
if password == 'Welcome':
    print("Welcome to the world of python")
else:
    print("Incorrect password please try again later  ")

# Note Run this code in any CMD or terminal to actually see the working