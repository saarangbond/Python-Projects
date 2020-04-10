'''
sets are internally implemented as hashmaps
dictionaries are also implemented similarly
however, dictionaries have key-value pairs,
while sets have just keys
sets are maintained ordered
'''

##empty sets cannot be created by using {}
##set removes duplicate elements

s = set()
s = {1, 2, 3}
print(s)
print(3 in s)
print(10 in s)

print()

s1 = {"Denmark", "Holland", "France", "Russia"}
s2 = {"Denmark", "Germany", "France", "Sweden"}

print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))


