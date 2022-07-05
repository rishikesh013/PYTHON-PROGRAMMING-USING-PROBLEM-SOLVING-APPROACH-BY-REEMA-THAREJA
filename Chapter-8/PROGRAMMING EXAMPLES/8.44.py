# 8.44 Write a program that has dictionary of names of students and a list of their marks in 4 subjects. Create
# another dictonary from this dictionary that has na,e of the students and their total marks find out the topper and
# his score

marks = {'Neha': [97, 89, 94, 90], 'Mitul': [92, 91, 94, 87], 'Shefail': [67, 99, 88, 90]}
total = 0

new_marks = {}
for keys, values in marks.items():
    total = sum(values)
    new_marks[keys] = total

# print(new_marks)
# print(max(new_marks.values()))
topper = ''
for k, v in new_marks.items():
    if v == max(new_marks.values()):
        topper += k

print(f'Topper is : {topper} and the marks is: {new_marks[topper]} ')