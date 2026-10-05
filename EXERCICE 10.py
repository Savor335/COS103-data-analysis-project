import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])   # 2D array (matrix)
zeros = np.zeros(5)          # [0. 0. 0. 0. 0.]
ones = np.ones((2, 3))       # 2x3 array of ones
range_arr = np.arange(0, 10, 2)   # [0 2 4 6 8]

print("1D array:", a)
print("2D array:\n", b)
print("Shape of b:", b.shape)      # (2, 3) -> 2 rows, 3 columns
print("Data type:", a.dtype)

# Manipulating
a_reshaped = np.arange(6).reshape(2, 3)   # reshape into 2 rows, 3 cols
print("Reshaped:\n", a_reshaped)

a_sorted = np.sort(np.array([3, 1, 4, 1, 5]))
print("Sorted:", a_sorted)

combined = np.concatenate((a, [6, 7]))
print("Concatenated:", combined)

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("Addition:", a + b)          # [11 22 33 44]
print("Subtraction:", b - a)       # [9 18 27 36]
print("Multiplication:", a * b)    # [10 40 90 160] (element-wise)
print("Division:", b / a)          # [10. 10. 10. 10.]

print("Sum:", np.sum(a))           # 10
print("Mean:", np.mean(a))         # 2.5
print("Max:", np.max(a))           # 4
print("Min:", np.min(a))           # 1


#

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication (NOT the same as A * B, which is element-wise)
result = np.dot(A, B)
# or equivalently: result = A @ B

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A × B:\n", result)