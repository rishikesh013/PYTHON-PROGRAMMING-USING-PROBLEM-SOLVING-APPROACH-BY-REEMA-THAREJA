# 7.4 Write a program that reads data from a file and calculates the percentage of vowels and consonants in the file

file_name = input("Enter the file name: ") + ".txt"
vowel_count = consonants_count = 0
try:
    with open(file_name, 'r') as f:
        a = f.read()
        for i in a:
            if i in 'aeiouAEIOU':
                vowel_count += 1
            else:
                consonants_count += 1

except FileNotFoundError:
    print("This file does not exists check again..")
else:
    print(f"No of vowels is {vowel_count}")
    print(f"No of consonants is {consonants_count}")
    print(f"Total length of the file is{len(a)}")
    print(f"Percentage of vowels is {vowel_count * 100 / len(a)}")
    print(f"Percentage of consonants is {consonants_count * 100 / len(a)}")
