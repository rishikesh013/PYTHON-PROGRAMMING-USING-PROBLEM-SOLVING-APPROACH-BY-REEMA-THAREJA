# 4.1 Write a program to determine whether a person is eligible to vote
age = int(input("Enter your age: "))

if age > 18:
    print(f"You are eligible to vote!!")

if age < 18:
    print(f"You can only vote after {18 - age} years!!")