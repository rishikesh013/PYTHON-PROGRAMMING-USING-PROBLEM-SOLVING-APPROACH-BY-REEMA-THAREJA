# 4.37 Write a program that accepts any number and prints the number of digits in that number

no = int(input("Enter the number: "))
r = no
sum_of_no = 0
while no:
    k = no % 10
    sum_of_no += k
    no //= 10

print(sum_of_no)

sum_of_no2 = sum(int(s) for s in str(r))
#
# for x in str(r):
#     print(x)
print(sum_of_no2)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# 4.38 Write a program that prints numbers from 20 to 1 (count downwards)

for i in range(1, 21)[::-1]:
    print(i)