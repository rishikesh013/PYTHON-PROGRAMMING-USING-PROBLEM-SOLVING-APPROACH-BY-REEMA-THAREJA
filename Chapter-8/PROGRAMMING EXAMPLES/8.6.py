# 8.6 Write a program that creates a list of words by combining the words in two individual list
given_list1 = ['Hello', 'World']
given_list2 = ['Python', 'Programming']

new_list = [x + y for x in given_list1 for y in given_list2]
print(new_list)

list_of_char = [x[0] for x in new_list]
print(list_of_char)