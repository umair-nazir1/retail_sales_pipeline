import pandas as pd
import sqlite3

# 1. Load transformed data
df = pd.read_csv("data/transformed_sales_data.csv")

print("🔹 Transformed Data:")
print(df.head())

# 2. Connect to SQLite database (file will be created if it doesn’t exist)
conn = sqlite3.connect("data/retail_sales.db")

# 3. Save DataFrame to database table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("\n✅ Data loaded successfully into SQLite database (retail_sales.db) → sales table")

# 4. Test query
query = "SELECT Month, SUM(TotalAmount) as MonthlySales FROM sales GROUP BY Month"
result = pd.read_sql(query, conn)
print("\n🔹 Monthly Sales Summary:")
print(result)

# 5. Close connection
conn.close()
