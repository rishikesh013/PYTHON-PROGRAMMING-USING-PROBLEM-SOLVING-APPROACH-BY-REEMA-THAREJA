# 5.16 Write a proram using function to perform calcuator operations such as adding, subtracting, multiplication,
# and division

def calculator(x, y, choice):
    if choice == 1:
        return x + y
    elif choice == 2:
        return x - y
    elif choice == 3:
        return x * y
    elif choice == 4:
        return x // y
    else:
        return "Invalid selection"


val1 = int(input("Enter the value 1 to be calculated: "))
val2 = int(input("Enter the value 2 to be calculated: "))

operation_to_perform = int(input("1. Addition \n2. Subtraction \n3. "
                                 "Multiplication \n4. Division \n Enter the operation to perform: ")[0])

print(calculator(val1, val2, operation_to_perform))