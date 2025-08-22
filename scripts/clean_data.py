import pandas as pd

# 1. CSV file load karo
df = pd.read_csv("data/sales_data.csv")

print("🔹 Raw Data:")
print(df.head())  # Pehle 5 rows dikhayega

# 2. Missing values check karo
print("\n🔹 Missing Values:")
print(df.isnull().sum())

# 3. Duplicates check karo
print("\n🔹 Duplicate Rows:", df.duplicated().sum())

# 4. Data types check karo
print("\n🔹 Data Types:")
print(df.dtypes)

# 5. Cleaning steps
# - Missing values drop karna (agar hote)
df = df.dropna()

# - remove null values
print(df.isnull().sum(),"detect the null values")

# - Duplicates drop karna
df = df.drop_duplicates()

# - Date ko proper datetime format me convert karna
df['Date'] = pd.to_datetime(df['Date'])

# - Quantity & Price ko numeric ensure karna
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['Price'] = pd.to_numeric(df['Price'])

# 6. Cleaned file save karna
df.to_csv("data/cleaned_sales_data.csv", index=False)

print("\n✅ Data cleaning complete! Cleaned file saved as cleaned_sales_data.csv")
