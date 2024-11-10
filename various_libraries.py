# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Create a simulated sales dataset
data = {
    'CustomerID': np.arange(1001, 1051),
    'Product': np.random.choice(['Product A', 'Product B', 'Product C'], 50),
    'Quantity': np.random.randint(1, 20, 50),
    'Price': np.random.uniform(10.0, 100.0, 50).round(2),
    'PurchaseDate': pd.date_range(start='2023-01-01', periods=50, freq='W')
}

# Load the data into a pandas DataFrame
df = pd.DataFrame(data)

# Step 2: Calculate total sales per transaction
df['TotalSales'] = df['Quantity'] * df['Price']

# Step 3: Analyze and summarize data
# Total sales by product
total_sales_by_product = df.groupby('Product')['TotalSales'].sum()
print("Total Sales by Product:\n", total_sales_by_product)

# Average price per product
average_price_by_product = df.groupby('Product')['Price'].mean()
print("\nAverage Price by Product:\n", average_price_by_product)

# Step 4: Visualize the data
plt.figure(figsize=(12, 8))

# Subplot 1: Bar chart of total sales by product
plt.subplot(2, 2, 1)
sns.barplot(x=total_sales_by_product.index, y=total_sales_by_product.values, palette="Blues_d")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")

# Subplot 2: Boxplot of prices by product
plt.subplot(2, 2, 2)
sns.boxplot(x='Product', y='Price', data=df, palette="Pastel1")
plt.title("Price Distribution by Product")
plt.xlabel("Product")
plt.ylabel("Price ($)")

# Subplot 3: Time series of total sales
df['Month'] = df['PurchaseDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalSales'].sum()
plt.subplot(2, 1, 2)
monthly_sales.plot(kind='line', marker='o', color='teal')
plt.title("Monthly Total Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.grid(True)

# Step 5: Display the plot
plt.tight_layout()
plt.show()

# Step 6: Additional Insights
# Identify the best customer based on total sales
best_customer = df.groupby('CustomerID')['TotalSales'].sum().idxmax()
best_customer_sales = df.groupby('CustomerID')['TotalSales'].sum().max()
print(f"\nBest Customer ID: {best_customer} with Total Sales: ${best_customer_sales:.2f}")
