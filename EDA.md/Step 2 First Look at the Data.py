print("=== FIRST LOOK AT TITANIC DATA ===")

# 1. Display first 5 rows to understand data structure
print("\n1. First 5 rows:")
print(df.head())

# 2. Get dataset information including column types and non-null counts
print("\n2. Dataset Info:")
print(df.info())

# 3. Show basic statistical summary for numerical columns
print("\n3. Basic Statistics:")
print(df.describe())

# 4. Count missing values in each column
print("\n4. Missing Values Count:")
print(df.isnull().sum())

# 5. Display data types of each column
print("\n5. Data Types:")
print(df.dtypes)