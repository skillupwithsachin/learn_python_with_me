# Data Visualization with Matplotlib

import matplotlib.pyplot as plt

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 2. Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

plt.bar(categories, values)
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 3. Scatter Plot
x = [1, 2, 3, 4, 5]
y = [10, 14, 18, 22, 26]

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
