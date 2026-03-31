# Car Price Prediction

A machine learning project that predicts the **selling price of a used car** based on features such as year of manufacture, fuel type, transmission, and kilometers driven. The model is trained using historical car data to provide accurate price estimates and help buyers and sellers determine fair market value.Built using Python and a Random Forest Regressor model.

---

## Table of Contents

- [Overview]
- [Theory & Concepts]
- [Project Structure]
- [Requirements]
- [How to Run]
- [Features Used]
- [Dataset]
- [Built With]

---

## Overview

When someone wants to sell their used car, figuring out a fair price is not straightforward. The price depends on several factors — how old the car is, how many kilometers it has been driven, the fuel type, transmission type, and more.

This project uses historical car sales data to train a machine learning model that can predict the expected selling price of a used car. The workflow is divided into three clean steps — data analysis, model training, and price prediction.

---

## Theory & Concepts

### 1. Exploratory Data Analysis (EDA)
Before building any model, it is important to understand the data. EDA involves examining the dataset for patterns, missing values, and relationships between variables.

In this project, two key visualizations were created:
- **Age vs. Price** — shows that older cars generally sell for lower prices
- **Fuel Type vs. Price** — shows that diesel cars tend to have a higher average selling price

### 2. Feature Engineering
The original dataset contained a `Year` column (e.g., 2015, 2018), which is not directly useful for a model. Instead, **car age** is a more meaningful feature. A new column `Age` was derived as:

```
Age = 2024 - Year
```

This process of transforming raw data into more informative features is called **Feature Engineering**.

### 3. One-Hot Encoding
Machine learning models work with numbers, not text. Categorical columns like `Fuel_Type` and `Transmission` were converted into binary (0/1) columns using **One-Hot Encoding**.

For example, `Fuel_Type` becomes:
- `Fuel_Type_Diesel` → 1 if Diesel, else 0
- `Fuel_Type_Petrol` → 1 if Petrol, else 0

This was handled using `pd.get_dummies()` in pandas.

### 4. Train-Test Split
The dataset was divided into two parts:
- **80% Training set** — the model learns patterns from this data
- **20% Test set** — used to evaluate the model on unseen data

This split is essential to detect **overfitting** — a situation where a model performs well on training data but poorly on new, real-world data.

### 5. Random Forest Regressor
The core algorithm used in this project is a **Random Forest Regressor**. Here's how it works:

- A **Decision Tree** is a flowchart-like model that splits data based on conditions (e.g., *Is the car older than 5 years? → Is kms driven > 80,000?*) until it reaches a predicted price.
- A **Random Forest** builds **100 such decision trees**, each trained on a slightly different random subset of the data.
- The final prediction is the **average** of all 100 trees, which makes it more stable and accurate than a single tree.

This technique of combining multiple models to improve accuracy is called **Ensemble Learning**.

### 6. Model Persistence
After training, the model was saved using `joblib` as a `.pkl` file. This allows the model to be **loaded and reused** for future predictions without retraining from scratch.

---

## Project Structure

```
car-price-prediction/
│
├── data/
│   ├── car_data.csv               # Original dataset
│   └── car_data_cleaned.csv       # Auto-generated after Step 1
│
├── charts/
│   ├── age_vs_price.png           # Scatter plot — Age vs Selling Price
│   └── fuel_vs_price.png          # Bar chart — Fuel Type vs Selling Price
│
├── 1_eda_and_charts.py            # Data analysis and chart generation
├── 2_model_training.py            # Model training and saving
├── 3_predict_price.py             # Price prediction using saved model
│
├── car_price_model.pkl            # Saved trained model 
├── model_columns.pkl              # Saved feature columns
└── README.md
```

---

## ⚙️ Requirements

Install the required libraries using:

```bash
pip install pandas scikit-learn matplotlib seaborn joblib
```

---

## How to Run

> **Important:** Run the scripts in order. Each step depends on the previous one.

**Step 1 — EDA & Chart Generation**
```bash
python 1_eda_and_charts.py
```
Performs exploratory data analysis, generates charts, and saves the cleaned dataset.

**Step 2 — Model Training**
```bash
python 2_model_training.py
```
Trains the Random Forest model and saves it as `car_price_model.pkl`.

**Step 3 — Price Prediction**
```bash
python 3_predict_price.py
```
Loads the saved model, takes user inputs, and predicts the car's selling price in lakhs.

---

## Features Used

| Feature | Description |
|---|---|
| Present Price | Current market price of the car (in lakhs) |
| Kms Driven | Total kilometers driven |
| Age | Age of the car (derived from Year) |
| Fuel Type | Petrol / Diesel / CNG |
| Seller Type | Dealer / Individual |
| Transmission | Manual / Automatic |

---

## Dataset

- **Source:** [Vehicle Dataset from Cardekho — Kaggle](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)
- Place `car_data.csv` inside the `data/` folder before running Step 1.

---

## Built With

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and encoding |
| Scikit-learn | Model training and evaluation |
| Matplotlib & Seaborn | Data visualization |
| Joblib | Model saving and loading |

---

