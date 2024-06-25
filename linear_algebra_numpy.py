# Linear Algebra with NumPy

import numpy as np

# 1. Dot Product
a = np.array([1, 2])
b = np.array([3, 4])
dot_product = np.dot(a, b)
print("Dot Product of a and b:", dot_product)

# 2. Matrix Multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix1, matrix2)
print("Matrix Product:\n", matrix_product)

# 3. Determinant
matrix = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(matrix)
print("Determinant of the matrix:", determinant)

# 4. Eigenvalues and Eigenvectors
values, vectors = np.linalg.eig(matrix)
print("Eigenvalues:\n", values)
print("Eigenvectors:\n", vectors)

# 5. Inverse of a Matrix
inverse_matrix = np.linalg.inv(matrix)
print("Inverse of the matrix:\n", inverse_matrix)
