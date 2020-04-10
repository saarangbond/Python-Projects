print()

l = [-2, -1, 20, 50, 35]
print(l)
l1 = sorted(l)
print(l1)
print(min(l))
print(max(l))
print(sum(l))

print()

l2 = ["bananas", "lemons", "grapes", "oranges"]
print(l2)
print(sorted(l2))
print(min(l2))
print(max(l2))

print()

for index, item in enumerate(l2) :
    print(index, item)
    
print()

ms = ", ".join(l2)
print(ms)