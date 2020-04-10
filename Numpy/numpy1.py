import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

print()

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

print()

c = np.zeros((2,2))   # Create an array of all zeros
print(c)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

print()

d = np.ones((1,2))    # Create an array of all ones
print(d)              # Prints "[[ 1.  1.]]"

print()

e = np.full((2,2), 7)  # Create a constant array
print(e)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

print()

f = np.eye(2)         # Create a 2x2 identity matrix
print(f)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

print()

g = np.random.random((2,2))  # Create an array filled with random values
print(g)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"