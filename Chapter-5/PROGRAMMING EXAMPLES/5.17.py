# 5.17 Write a program to count the number of times the recursive function is called

def recursive_fn(n, count=0):
    if n == 0:
        return count
    else:
        return recursive_fn(n -1, count+1)


print(f"The number of times the recursive function is invoked is {recursive_fn(100)}")