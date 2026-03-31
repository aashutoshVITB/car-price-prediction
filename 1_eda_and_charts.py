import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = "data/car_data.csv"

if not os.path.exists(file_path):
    print("ERROR: 'car_data.csv' not found inside 'data' folder")
    print("Please create a folder named 'data' and put the dataset inside it")
    exit()

# Load data
df = pd.read_csv(file_path)
print("Data loaded successfully!")

# Feature Engineering
df['Current_Year'] = 2024
df['Age'] = df['Current_Year'] - df['Year']

# Create charts folder
os.makedirs('charts', exist_ok=True)

# Plot 1
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Selling_Price')
plt.title('Impact of Age on Car Price')
plt.savefig('charts/age_vs_price.png')
print("Saved: charts/age_vs_price.png")

# Plot 2
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Fuel_Type', y='Selling_Price')
plt.title('Average Price by Fuel Type')
plt.savefig('charts/fuel_vs_price.png')
print(" Saved: charts/fuel_vs_price.png")

# Save cleaned data
os.makedirs('data', exist_ok=True)
df.to_csv('data/car_data_cleaned.csv', index=False)
print("Cleaned data saved!")