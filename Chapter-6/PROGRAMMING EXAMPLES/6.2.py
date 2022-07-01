# 6.2 Write a program that takes user name and pan card number as input validate the information usins isxfunction
# and print the details

def is_valid():
    while True:
        name = input("Enter the name of the applicant: ")
        if not name.isalpha():
            print("Invalid name!! please check the name and continue")
            break
        pan_no = input("Enter the pan card number: ")
        if not pan_no.isalnum():
            print("Invalid pan card number please check the number and try again  ")
            break

        return f"Your name: {name} and your pan card number: {pan_no}"


print(is_valid())