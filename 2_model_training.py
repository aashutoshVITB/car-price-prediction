import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

file_path = 'data/car_data_cleaned.csv'

if not os.path.exists(file_path):
    print(" ERROR: Run 1_eda_and_charts.py first!")
    exit()

# Load data
df = pd.read_csv(file_path)

# Prepare data
df_model = df.drop(['Car_Name', 'Year', 'Current_Year'], axis=1)

# encoding
df_encoded = pd.get_dummies(df_model, drop_first=True)

# Split
X = df_encoded.drop('Selling_Price', axis=1)
y = df_encoded['Selling_Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'car_price_model.pkl')
joblib.dump(list(X.columns), 'model_columns.pkl')

print("Model trained & saved successfully!")