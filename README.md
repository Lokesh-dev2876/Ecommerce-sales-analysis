# 📊 E-commerce Sales Analysis

## 📌 Project Overview

This project analyzes an **E-commerce sales dataset** to uncover insights on sales performance, customer behavior, product categories, and regional trends.
The project combines **Python (VS Code)** for data cleaning & analysis and **Power BI** for building an interactive dashboard.

## 🎯 Objectives

* Analyze overall sales performance over time
* Identify top-performing product categories and regions
* Understand customer behavior and purchasing patterns
* Provide KPIs to support business decision-making

## 🛠 Tools & Technologies

* **Python** – Data cleaning, preprocessing, and analysis
* **Pandas, Matplotlib** – Data manipulation & visualization
* **Power BI** – Dashboard & interactive reports
* **Excel/CSV** – Raw data storage

## 📂 Project Structure

```
ecommerce-sales-analysis/
│── data/
│   └── Ecommerce_sales.csv        # dataset
│
│── scripts/
│   ├── Load_data.py               # loads and preprocesses data
│   ├── sales_analysis.py           # overall sales performance
│   ├── category_analysis.py        # category-level insights
│   ├── Regional_analysis.py        # region-wise analysis
│   ├── time_analysis.py            # time-series trends
│   ├── Customer_analysis.py        # customer behavior insights
│   └── visualizations.py           # data visualization functions
│
│── dashboard/
│   └── ecommerce_sales.pbix        # Power BI dashboard
│
│── README.md                       # project documentation
```

## 📊 Dashboard Features

* **Sales Trends**: Revenue & profit over time
* **Regional Insights**: Sales performance by region
* **Category Analysis**: Top-performing categories & products
* **Customer Analysis**: Repeat customers & order distribution
* **KPIs**: Total sales, profit margin, order count

## 📷 Dashboard Preview

(Add screenshots of your Power BI dashboard inside `images/` folder)

![Dashboard Overview](images/dashboard_overview.png)

## 🚀 How to Use

1. Clone this repository
2. Navigate to `scripts/` and run the Python files for analysis

   ```bash
   python Load_data.py
   python sales_analysis.py
   ```
3. Open `dashboard/ecommerce_sales.pbix` in **Power BI Desktop**
4. Connect the dashboard to `data/Ecommerce_sales.csv` (if required)
5. Explore the interactive dashboard

## 📈 Key Insights (Example – replace with your findings)

* 📌 The **Western region** generated the highest revenue
* 📌 **Category X** was the most profitable in Q2
* 📌 **Repeat customers** contributed ~40% of total sales
* 📌 Sales peaked during the **festival season** (Oct–Dec)

## 🔮 Future Improvements

* Automate data refresh using Power BI Service
* Add predictive analytics with Python/ML models
* Build an interactive web dashboard

---

👤 **Author:** Lokesh Kl
🔗 Connect with me on [LinkedIn](your-linkedin-url)
