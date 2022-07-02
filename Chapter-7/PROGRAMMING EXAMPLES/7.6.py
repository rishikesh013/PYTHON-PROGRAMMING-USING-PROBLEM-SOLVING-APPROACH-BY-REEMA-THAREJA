# 7.6 Write a program that computes the total size of all the files in c:\Python34 folder

import os
total_Size = 0
for file in os.listdir(r"D:\Personalportfolio(main)"):
    total_Size += os.path.getsize(os.path.join(r"D:\Personalportfolio(main)", file))

print(total_Size)