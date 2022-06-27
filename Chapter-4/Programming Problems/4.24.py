# 4.24 Write a program to display the sin(x) value where x ranges from 0 to 360 in steps of 15

from math import sin, cos, tan

for i in range(0, 361, 15):
    print(sin(i))

print('----------------------------------------')
for i in range(0, 361, 15):
    print(cos(i))


print('----------------------------------------')

for i in range(0, 361, 15):
    print(tan(i))