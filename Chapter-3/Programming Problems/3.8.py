# 3.8 Implicit and explicit type casting
# Implicit type casting :- In this type the python automatically convert's from one data type to another

first_no = 7
second_no = 8.7

third_no = first_no + second_no # Note here the type is automatically converted to float

print(f"Type of first_no: {type(first_no)}")
print(f"Type of second_no: {type(second_no)}")
print(f"Type of third_no: {type(third_no)}")

# Explicit type conversion:- In this type the users are involved in the type conversion
print("-----------------------------------------------------------------------")
first_no = 4
second_no = float(first_no)
print(f"The type of the second_no is {type(second_no)}")
