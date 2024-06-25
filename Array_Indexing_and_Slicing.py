# Array Indexing and Slicing

import numpy as np

# 1. Indexing
array = np.array([10, 20, 30, 40, 50])

print("Element at index 0:", array[0])
print("Element at index 4:", array[4])

# 2. Slicing
print("Elements from index 1 to 3:", array[1:4])
print("Elements from start to index 2:", array[:3])
print("Elements from index 2 to end:", array[2:])

# 3. Indexing and Slicing in 2D Arrays
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Element at row 1, column 2:", array_2d[1, 2])
print("First row:", array_2d[0, :])
print("First column:", array_2d[:, 0])
print("Sub-array (first two rows and columns):\n", array_2d[:2, :2])
