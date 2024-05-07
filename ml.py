import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
# Fetch dataset
online_retail = fetch_ucirepo(id=352)

# Convert data to DataFrame
df = pd.DataFrame(online_retail.data.features, columns=online_retail.variables['name'])

# Identify 10 unique quantity values
unique_quantities = df['Quantity'].unique()[:10]

# Initialize lists to store descriptions, unit prices, and transaction amounts
descriptions = []
unit_prices = []
transaction_amounts = []

# Loop through unique quantities
for quantity in unique_quantities:
    # Filter dataframe for the current quantity
    filtered_df = df[df['Quantity'] == quantity]
    # Get description and unit price for the first row (assuming they are consistent for the same quantity)
    description = filtered_df.iloc[0]['Description']
    unit_price = filtered_df.iloc[0]['UnitPrice']
    # Calculate transaction amount
    transaction_amount = quantity * unit_price
    # Append to lists
    descriptions.append(description)
    unit_prices.append(unit_price)
    transaction_amounts.append(transaction_amount)

# Create DataFrame for visualization
transaction_df = pd.DataFrame({
    'Description': descriptions,
    'TransactionAmount': transaction_amounts
})
# Display the first few rows of the DataFrame
print(df.head())
# Define custom colors for each category
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'cyan', 'magenta', 'lime', 'pink']

# Plot a chart of Product Category (Description Selected) against the Transaction Amount
plt.figure(figsize=(12, 6))
plt.bar(transaction_df['Description'], transaction_df['TransactionAmount'], color=colors)
plt.xlabel('Product Category (Description)')
plt.ylabel('Transaction Amount (Sterling Pounds)')
plt.title(' Retail Store: Distribution of transaction amounts across different product categories')
plt.xticks(rotation=90)
plt.show()
