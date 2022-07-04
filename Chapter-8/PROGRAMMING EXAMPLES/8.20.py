# 8.20 Write a program to generate in the fibonacci sequence and store it in a list then find the sum of the even
# valued terms

def fibbonachi(n):
    if n <= 1:
        return n
    else:
        return fibbonachi(n - 1) + fibbonachi(n - 2)


no_of_terms = int(input("Enter the number of terms: "))
new_list = []
for i in range(no_of_terms):
    new_list.append(fibbonachi(i))

print(new_list)

sum_of_values = 0
for i in range(0, len(new_list), 2):
    sum_of_values += new_list[i]

print(sum_of_values)
print(sum(new_list[i] for i in range(0, len(new_list), 2)))