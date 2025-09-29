import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Ecommerce_sales.csv", encoding="latin1")

# Convert date column
data["Order Date"] = pd.to_datetime(data["Order Date"], dayfirst=True)

# Sales by Year
data["Year"] = data["Order Date"].dt.year
yearly_sales = data.groupby("Year")["Sales"].sum()
print("\nYearly Sales:\n", yearly_sales)

yearly_sales.plot(marker="o", figsize=(8,5))
plt.title("Yearly Sales Trend")
plt.ylabel("Sales")
plt.show()

# Sales by Month
data["Month"] = data["Order Date"].dt.month
monthly_sales = data.groupby("Month")["Sales"].sum()
print("\nMonthly Sales:\n", monthly_sales)

monthly_sales.plot(kind="bar", figsize=(8,5), color="orange")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.show()
