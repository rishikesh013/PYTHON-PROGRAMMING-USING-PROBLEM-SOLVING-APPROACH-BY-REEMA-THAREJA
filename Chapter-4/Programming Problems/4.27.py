# 4.27 Write a program to read an angle from the user and then display its quadrant
from math import pi

user_angle = int(input("Enter the angle in degree: "))

if 0 < user_angle < 90:
    print("First quadrant")
elif 90 < user_angle < 180:
    print("Second Quadrant")
elif 180 < user_angle < 270:
    print("Third Quadrant")
elif 270 < user_angle < 360:
    print("Fourth quadrant")
else:
    print("It doesn't belong to any quadrant or is a border value")