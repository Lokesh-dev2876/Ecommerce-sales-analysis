import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Ecommerce_sales.csv", encoding="latin1")

# Total Sales & Profit
print(f"Total Sales: {data['Sales'].sum():,.2f}")
print(f"Total Profit: {data['Profit'].sum():,.2f}")

# Top 10 Products by Sales
top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Sales:\n", top_products)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top 10 Products by Sales")
plt.ylabel("Sales")
plt.xticks(rotation=75)

plt.show()

# Top 10 Customers by Profit
top_customers = data.groupby("Customer Name")["Profit"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Profit:\n", top_customers)

plt.figure(figsize=(10,5))
top_customers.plot(kind="bar", color="orange")
plt.title("Top 10 Customers by Profit")
plt.ylabel("Profit")
plt.xticks(rotation=75)
plt.show()
