import pandas as pd

# Load data
df = pd.read_csv("sales.csv")

# Create Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]
print("\n💰 Data with Total Sales:")
print(df)

# 1. Top Products
top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

# 2. City Sales
city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False)

# 3. Category Sales
category_sales = df.groupby("Category")["Total_Sales"].sum()

# OUTPUT
print("="*40)
print("TOP PRODUCTS")
print(top_products)

print("\n"+"="*40)
print("CITY WISE SALES")
print(city_sales)

print("\n"+"="*40)
print("CATEGORY WISE SALES")
print(category_sales)