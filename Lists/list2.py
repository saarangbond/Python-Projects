print()

l1 = ["oranges", "lemons", "tomatoes", "potatoes", 1, 4, -2, "tomatoes"]
print(l1)
l2 = l1[0:3]
print(l2)
l3 = l1[::-1]
print(l3)

print()

list = [-5, 3, 7, 19]
print(list)
list1 = [42, -45]
list.extend(list1)
print(list)
list.insert(0, "apple")
print(list)
list.remove("apple")
print(list)
list.pop()
print(list)
list.pop(0)
print(list)

print()

list3 = [0, 1, 2, 3, 4, 1]
print(list3.index(1))
print(list3.count(1))