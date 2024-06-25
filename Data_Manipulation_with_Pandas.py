# Data Manipulation with Pandas

import pandas as pd

# 1. Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 2. Accessing Data
print("Names:\n", df['Name'])
print("Ages:\n", df['Age'])

# 3. Filtering Data
filtered_df = df[df['Age'] > 25]
print("Filtered DataFrame (Age > 25):\n", filtered_df)

# 4. Adding a New Column
df['Salary'] = [50000, 60000, 45000, 70000, 65000]
print("DataFrame with Salary column:\n", df)

# 5. Grouping Data
grouped_df = df.groupby('City').mean()
print("Grouped DataFrame by City:\n", grouped_df)
