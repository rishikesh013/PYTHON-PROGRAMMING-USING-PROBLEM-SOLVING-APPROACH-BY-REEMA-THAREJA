import calendar

year = int(input("Enter the year: "))

m = 1
print("\n ******************Calendar*****************")
cal = calendar.TextCalendar(calendar.SUNDAY)
i = 1
while i <= 12:
    cal.prmonth(year, i)
    i += 1
