# 5.7 Calculate the simple interest . Suppose the customer is a senior citizen he is offered 12 percent rate for all
# other customers the interest is 10 percent

def simple_interest(p, t, s):
    if s == 'y':
        return float((p * t * 12) / 100)
    else:
        return float((p * t * 10) / 100)


principle = float(input("Enter the principle amount:  "))
y = float(input("Enter the number of years:  "))
senior = input("Is the customer senior citizen (y/n): ").casefold()
print(f"The simple interest is {simple_interest(principle, y, senior)}")