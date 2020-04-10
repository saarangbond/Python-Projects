l1 = ["tomatoes", "apples", "pears"]

print(l1[0])
print(len(l1))

print()

l2 = list()
print(l2)
l2.append(3)
l2.append(17)
print(l2)
l2 = []
print(l2)

print()

l3 = [3, 5, 7, 9, 11]

total = 0
for i in range (0, len(l3)):
    total += l3[i]
    
print(total)

print()
l4 = ["grapes", "bananas", "cherries"]
print(l4)
l4 += "cheese"
print(l4)
l4 += ["cheese"]
print(l4)
l4.append(["cheese"])
print(l4)