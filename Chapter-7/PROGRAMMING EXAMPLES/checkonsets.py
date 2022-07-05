s = {1, 2, 3, 4, 5, 7}
t = {6, 7, 8, 4}
s.update(t)
print(s)
s.add(25)
print(s)
s.remove(7)  # Removes the element if not present returns an error
s.discard(70)  # Removes the element if not present dosen't return an error
print(s)
#s.pop()
#s.clear()  # Removes all the elements from the set
print(s)
# s.union(t)

print(s.intersection(t))
print(s)
print(s.symmetric_difference(t))
print(s)
s.add(7)
print(s)
print(t)
print(s >= t)  # issuperset returns true if every element of t is present in s
print(t <= s)  # issubset returns true if every element of t is present in s
print(s & t)
print(s - t)
print(s ^ t)
print(max(s))
print(sum(s))

new_dict = dict(list(s))
print(new_dict)