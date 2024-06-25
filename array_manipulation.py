# Array Manipulation

import numpy as np

# 1. Reshaping Arrays
array = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = array.reshape((2, 3))
print("Original Array:\n", array)
print("Reshaped Array (2x3):\n", reshaped_array)

# 2. Concatenation and Stacking
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6]])

concatenated_array = np.concatenate((array1, array2), axis=0)
stacked_array = np.vstack((array1, array2))

print("Concatenated Array:\n", concatenated_array)
print("Stacked Array:\n", stacked_array)

# 3. Splitting Arrays
array = np.array([1, 2, 3, 4, 5, 6])
split_array = np.split(array, 3)
print("Split Array into 3 parts:\n", split_array)
