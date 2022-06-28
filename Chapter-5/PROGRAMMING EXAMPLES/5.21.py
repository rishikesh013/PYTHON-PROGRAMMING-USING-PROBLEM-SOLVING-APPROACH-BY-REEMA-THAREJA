# 5.21 Write a program to display the date and time using the time modele
import time
import calendar

local_time = time.asctime(time.localtime(time.time()))
print(local_time)
# print(time.time())
# print(type(time.localtime(time.time())))
# print(time.localtime(time.time()))

# Write a program to print the calendar of a particular month
print(calendar.month(2018, 11))