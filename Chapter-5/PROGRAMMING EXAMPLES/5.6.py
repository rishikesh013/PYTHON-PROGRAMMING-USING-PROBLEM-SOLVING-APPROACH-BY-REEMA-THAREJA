# 5.6 Write a function that convert time into minutes

def convert_to_minute(hrs, minutes):
    return hrs * 60 + minutes


h = int(input("Enter the hours: "))
m = int(input("Enter the minutes: "))
m = convert_to_minute(h, m)

print(f"Minutes = {m}")
