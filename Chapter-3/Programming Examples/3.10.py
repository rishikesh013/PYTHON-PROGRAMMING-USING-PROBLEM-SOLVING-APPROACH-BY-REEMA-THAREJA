# 3.10 Write an program to convert degrees fahrenheit into degree celsius

farn = float(input("Enter the degree in fahrenheit: "))
celc = (farn - 32) * (5 / 9)
print(f"The degree in celsius is {celc:.2f}")
