import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sales.csv")

# Basic info
print("First 5 rows:")
print(df.head())

# Total revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Group by product
product_sales = df.groupby("Product")["Revenue"].sum()
print("\nRevenue by Product:")
print(product_sales)

# Plot revenue by product
plt.figure(figsize=(6,4))
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

# Group by date
daily_sales = df.groupby("Date")["Revenue"].sum()

plt.figure(figsize=(6,4))
daily_sales.plot(kind="line", marker="o")
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("daily_trend.png")
plt.show()
