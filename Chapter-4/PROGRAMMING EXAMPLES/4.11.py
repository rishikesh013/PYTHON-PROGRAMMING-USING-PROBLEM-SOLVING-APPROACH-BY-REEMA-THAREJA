# 4.11 Write a program that prompts the user to enter a number between 1 to 7 and display the corresponding day

days_dict = {
    1: 'Sunday',
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

num = int(input("Enter an input from (1 - 7): "))
print(f"""For the number {num} it's {days_dict.get(num, "doesn't exists")}""")  # ignore the grammar
