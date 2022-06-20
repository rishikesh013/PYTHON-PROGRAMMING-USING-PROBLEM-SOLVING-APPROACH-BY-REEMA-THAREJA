# 4.19 Write a program to read numbers untill -1 is encountered. Also count the negative, positive and zeros entered
# by the user

# no_of_negative = 0
# no_of_positive = 0
# zeros = 0

no_of_negative = no_of_positive = zeros = 0
while True:
    no = int(input("Enter the numbers and -1 to stop: "))
    if no == -1:
        break
    elif no > 0:
        no_of_positive += 1
    elif no < 0:
        no_of_negative += 1
    else:
        zeros += 1

print(f"No of positives: {no_of_positive}")
print(f"No of negatives: {no_of_negative}")
print(f"No of zeros: {zeros}")
