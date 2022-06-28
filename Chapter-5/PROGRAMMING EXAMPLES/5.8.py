# 5.8 Write a program to calculate the volume of a cuboid using default arguments

def vol_of_cuboid(l, w=3, h=4):
    print(f"The length is {l} and the width is {w} and the height is {h}")
    return l * w * h


print(f"Volume: {vol_of_cuboid(4, 6, 2)}")
print(f"Volume: {vol_of_cuboid(4)}")
print(f"Volume: {vol_of_cuboid(4, w=6)}")