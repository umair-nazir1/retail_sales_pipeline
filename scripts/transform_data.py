import pandas as pd

# 1. Load cleaned data
df = pd.read_csv("data/cleaned_sales_data.csv")

print("🔹 Data Before Transformation:")
print(df.head())

# 2. Convert Date column to datetime (important for extracting Month)
df['Date'] = pd.to_datetime(df['Date'])

# 3. Create new column: TotalAmount = Quantity × Price
df['TotalAmount'] = df['Quantity'] * df['Price']

# 4. Extract Month name from Date
df['Month'] = df['Date'].dt.month_name()

print("\n🔹 Data After Transformation:")
print(df.head())

# 5. Save transformed data
df.to_csv("data/transformed_sales_data.csv", index=False)

print("\n✅ Data transformation complete! File saved as transformed_sales_data.csv")
