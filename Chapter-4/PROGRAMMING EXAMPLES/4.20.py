# 4.20 Write a program to read te numbers until -1 is encountered. Find the average of positive numbers and negative numbers entered by the user

no_of_negative = no_of_positive = zeros = 0
positive_sum = negative_sum = 0
while True:
    no = int(input("Enter the numbers and -1 to stop: "))
    if no == -1:
        break
    elif no > 0:
        no_of_positive += 1
        positive_sum += no
    elif no < 0:
        no_of_negative += 1
        negative_sum += no
    else:
        zeros += 1

print(f"The average positive values present is {positive_sum / no_of_positive:.2f}")
print(f"The average positive values negative is {negative_sum / no_of_negative:.2f}")