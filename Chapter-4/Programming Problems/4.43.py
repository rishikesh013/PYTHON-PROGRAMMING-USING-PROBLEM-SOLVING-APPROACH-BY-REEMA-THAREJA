# 4.43 Write a program to implement the following sequence of numbers

for i in range(1, 100):
    print(i ** 3)

for j in range(-5, 100, 3):
    print(j)


print('+++++++++++++++')
for x in range(2, 100, 2):
    print(-x)

# 4.44 Write a program that reads integers until the user wants to stop when the user stops entering the number
# display the largest of all the numbers entered

largest_no = 0
while True:
    no = int(input("Enter the numbers and -1 to stop the program: "))
    if no == -1:
        break

    if largest_no < no:
        largest_no = no

print(largest_no)