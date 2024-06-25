# Statistical and Mathematical Operations

import numpy as np

# 1. Statistical Operations
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))

# 2. Mathematical Operations
array = np.array([1, 2, 3, 4, 5])

print("Sum:", np.sum(array))
print("Product:", np.prod(array))
print("Cumulative Sum:", np.cumsum(array))
print("Cumulative Product:", np.cumprod(array))
