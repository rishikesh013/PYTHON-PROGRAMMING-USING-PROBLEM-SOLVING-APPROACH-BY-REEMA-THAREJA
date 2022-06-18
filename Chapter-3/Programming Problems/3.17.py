# 3.17 Momentum is calculated as, e=mc^2, where m is the mass of the object and c is it's velocity. Write a program
# that accepts an object an objects mass and velocity and display its momentum

mass = float(input("Enter the mass in kilogram: "))
c = float(input("Enter the velocity in meter per second: "))

e = (mass * c) ** 2
print(f"Momentum is :{e}")



