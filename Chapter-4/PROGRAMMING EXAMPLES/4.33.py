# 4.33 Write a program to classify the given number as prime or composite

given_no = int(input("Enter the given number: "))
comp_no = None
for i in range(2, given_no):
    if given_no % i == 0:
        comp_no = True

if comp_no:
    print("It is a composite number")
else:
    print("IT is a prime number")