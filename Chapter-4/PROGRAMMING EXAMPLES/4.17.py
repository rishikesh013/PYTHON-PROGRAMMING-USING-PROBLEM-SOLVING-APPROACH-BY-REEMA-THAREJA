# 4.17 Program to print 20 horizontal asterisks(*)

twenty_asterisks = ['*' for i in range(20)]

idx = 0
while idx < 20:
    print(twenty_asterisks[idx], end=' ')
    idx += 1
print()
# Easy implementation
j = 0
while j < 20:
    print('*', end=' ')
    j +=1