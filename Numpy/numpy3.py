import numpy as np

d = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])

for i in range (0, d.shape[0]):
    for j in range (0, d.shape[1]):
        
print()

for (x, y), value in np.ndenumerate(d):
    print (d[x, y])


print()
print(d)