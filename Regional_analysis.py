import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Ecommerce_sales.csv", encoding="latin1")

# Sales by Country
country_sales = data.groupby("Country")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Countries by Sales:\n", country_sales)

plt.figure(figsize=(10,5))
country_sales.plot(kind="bar", color="skyblue")
plt.title("Top 10 Countries by Sales")
plt.ylabel("Sales")
plt.show()

# Sales by Region
region_sales = data.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n", region_sales)

region_sales.plot(kind="pie", autopct="%.1f%%", figsize=(6,6))
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()
