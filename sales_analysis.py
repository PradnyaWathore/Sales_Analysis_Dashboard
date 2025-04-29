import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_csv('sales_data.xlsx.csv')


# Clean up whitespace in column names
df.columns = df.columns.str.strip()

# Group by month
monthly_sales = df.groupby('Month')['Sales'].sum()
print("Monthly Sales:")
print(monthly_sales)

# Group by region
region_sales = df.groupby('Region')['Sales'].sum()

# Visualization
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
monthly_sales.plot(kind='bar', title='Monthly Sales')

plt.subplot(1, 2, 2)
region_sales.plot(kind='pie', autopct='%1.1f%%', title='Region-wise Sales')

plt.tight_layout()
plt.show()
