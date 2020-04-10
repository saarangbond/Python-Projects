import numpy as np

## the * operator computes element-wise multiplication
## for matrix mulitplication, use the .dot function

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))


a = np.array([[1,2],[3,4]])

print(np.sum(a))  # Compute sum of all elements; prints "10"
print(np.sum(a, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(a, axis=1))  # Compute sum of each row; prints "[3 7]"