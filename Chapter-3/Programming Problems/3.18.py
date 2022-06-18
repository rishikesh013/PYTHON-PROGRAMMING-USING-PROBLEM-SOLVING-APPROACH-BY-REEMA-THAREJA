# 3.18 Write a program to calculate number of seconds in a day

def seconds_in_a_day(day: int) -> int:
    hours = day * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds


print(f"Number of seconds in a day is {seconds_in_a_day(1)}")
