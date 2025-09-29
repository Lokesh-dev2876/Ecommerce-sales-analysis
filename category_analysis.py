import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Ecommerce_sales.csv", encoding="latin1")

# Sales by Category
category_sales = data.groupby("Category")["Sales"].sum()
print("\nSales by Category:\n", category_sales)

category_sales.plot(kind="bar", color="purple", figsize=(6,4))
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()

# Profit by Sub-Category
subcategory_profit = data.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Sub-Category:\n", subcategory_profit)

plt.figure(figsize=(12,6))
subcategory_profit.plot(kind="bar", color="green")
plt.title("Profit by Sub-Category")
plt.ylabel("Profit")
plt.xticks(rotation=75)
plt.show()
