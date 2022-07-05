# Write a program that creates a dictionary of radius of a circle and its circumference

circumference = {}

while True:
    given_radius = int(input("Enter the radius and -1 to exit: "))
    if given_radius == -1:
        break
    calc = float(f"{2 * 3.14 * given_radius: .2f}")

    circumference[given_radius] = calc

print(circumference)
