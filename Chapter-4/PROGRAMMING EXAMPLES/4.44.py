# 4.44 Write a program to generate calender of a month given the start_day and the number of days in the month
import calendar

# start_dat = int(input("Enter the start day of the month: "))
# no_of_days = int(input("Enter the number of days in the month: "))
# print("SUN  MON  TUE  WED  THU  FRI  SAT")
# for i in range(start_dat - 1):
#     print("    ", end="")
# i = start_dat - 1
# for j in range(1, no_of_days + 1):
#     if i > 6:
#         print()
#         i = 1
#     else:
#         i += 1
#
#     print(str(j) + "  ", end=" ")

new_date = calendar.HTMLCalendar()
new_date.formatyear(2022, 20)

print(new_date)