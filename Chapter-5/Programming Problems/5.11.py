# 5.11 Write a program to swap two variables that are defined as global variables

var1 = int(input("Enter the variable: "))
var2 = int(input("Enter the variable: "))


def swap_var():
    global var1, var2
    var1, var2 = var2, var1


swap_var()
print(f"Variable 1 after swap is : {var1}")
print(f"Variable 2 after swap is : {var2}")

d = {1, 2, 3, 4, 5}
print(d)
d.add(12)
print(d)