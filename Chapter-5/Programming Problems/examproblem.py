from itertools import combinations

a, b = map(int, input().split())
k = list(map(int, input().split()))
print(k)
comb = combinations(k, 4)
print(list(comb))
for i in list(comb):
    if sum(list(i)) == b:
        print(1)
        exit()
print(0)
