import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Ecommerce_sales.csv", encoding="latin1")

# Sales by Segment
segment_sales = data.groupby("Segment")["Sales"].sum()
print("\nSales by Segment:\n", segment_sales)

segment_sales.plot(kind="bar", color="teal", figsize=(6,4))
plt.title("Sales by Customer Segment")
plt.ylabel("Sales")
plt.show()

# Top 10 Cities by Sales
city_sales = data.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Cities by Sales:\n", city_sales)

plt.figure(figsize=(10,5))
city_sales.plot(kind="bar", color="brown")
plt.title("Top 10 Cities by Sales")
plt.ylabel("Sales")
plt.xticks(rotation=75)
plt.show()
