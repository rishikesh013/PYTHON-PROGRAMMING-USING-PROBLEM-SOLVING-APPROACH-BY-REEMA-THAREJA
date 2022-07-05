# 8.37 Write a program that creates two dictonary. One that converts meters to centimeters and the other that stores
# values from centimeters to meters

m_cm = {x: x * 100 for x in range(1, 100)}
print(m_cm)

cm_m = {x: int(x / 100) for x in m_cm.values()}
print(cm_m)