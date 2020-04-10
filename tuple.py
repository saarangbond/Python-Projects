t = ()
## ^ this is a tuple - parentheses denote a tuple

t = ("coffee", "tea", "wheatgrass")
print(t)

## tuples aren't modifiable

'''
to modify a tuple, one must convert items
to a list, modify that list,
and convert it back to a tuple
'''

l = []
for item in t :
    l.append(item)
    
print(l)
l[0] = "canesugar"
l.append("chocolate")

t = tuple(l)
print(t)

'''
you cannot use the .sort() method on a tuple, 
as it modifies it
However, you can sort a tuple by using the sorted(@param) method
on a new tuple
'''

print()

t1 = tuple(sorted(t))
print(t1)