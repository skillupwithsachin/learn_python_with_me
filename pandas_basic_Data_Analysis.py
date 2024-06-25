# Basic Data Analysis

import pandas as pd

# 1. Load Data
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
df = pd.read_csv(url)

print("First 5 rows of the DataFrame:\n", df.head())

# 2. Summary Statistics
print("Summary Statistics:\n", df.describe())

# 3. Data Cleaning
# Rename columns for easier access
df.columns = ['Month', '1958', '1959', '1960']
print("Renamed Columns DataFrame:\n", df.head())

# Handling missing values
df = df.dropna()
print("DataFrame after dropping missing values:\n", df.head())

# 4. Basic Analysis
print("Total passengers in 1958:\n", df['1958'].sum())
print("Average passengers per month in 1960:\n", df['1960'].mean())
