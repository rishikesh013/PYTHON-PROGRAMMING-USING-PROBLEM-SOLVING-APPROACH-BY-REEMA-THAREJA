# 4.28 Write a program that accepts the current date and the date of birth of the user. Then calculate the age of the
# user and display it on the screen.

from datetime import date


def calculate_age(born):
    today = date.today()
    age = today.year - born.year - ((today.month, born.day) < (born.month, born.day))

    return age


print(calculate_age(date(1997, 2, 3)), "years")

