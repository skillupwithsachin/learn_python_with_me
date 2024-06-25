# Introduction to NumPy

import numpy as np

# 1. Creating Arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:\n", array_1d)
print("2D Array:\n", array_2d)

# 2. Array Attributes
print("Shape of array_1d:", array_1d.shape)
print("Shape of array_2d:", array_2d.shape)
print("Data type of array_1d:", array_1d.dtype)

# 3. Array Initialization
zeros_array = np.zeros((3, 3))
ones_array = np.ones((2, 4))
identity_matrix = np.eye(3)

print("Zeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)
print("Identity Matrix:\n", identity_matrix)

# 4. Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 5. Universal Functions (ufunc)
print("Square root of a:", np.sqrt(a))
print("Exponential of b:", np.exp(b))
print("Sine of a:", np.sin(a))
