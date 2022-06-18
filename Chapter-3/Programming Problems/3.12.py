# 3.12 Calculate the simple interest and the compound interest

principle = float(input("Enter the principle value: "))
rate = float(input("Enter the rate value: "))
time_for_calculation = float(input("Enter the time to calculate the formula: "))

simple_interest = (principle * rate * time_for_calculation) / 100
compound_interest = principle * ((1 + rate/100) ** time_for_calculation - 1)
print(f"The simple interest is {simple_interest}")
print(f"The compound interest is {compound_interest:f}")