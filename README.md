# car-price-prediction
A machine learning project that predicts the price of used cars based on features such as year of manufacture, fuel type, transmission, and kilometers driven. The model is trained using historical car data to provide accurate price estimates and help buyers and sellers determine fair market value.

# 🚗 Car Price Prediction

hey so this is my ML project where you can predict the selling price of a used car. built this using python and random forest. pretty cool ngl

---

## 🧠 What is this project actually doing?

okay so basically the idea is — when someone wants to sell their old car, how do you figure out a fair price for it? you can't just guess. the price depends on a lot of things like how old the car is, how many kms it's been driven, what fuel it uses, etc.

so what this project does is — it looks at data from hundreds of used car sales, finds patterns in that data, and then uses those patterns to predict what price a car *should* sell for. that's machine learning in a nutshell honestly

---

## 📚 Theory / Concepts Used

### 1. Exploratory Data Analysis (EDA)
before building any model, you gotta *understand* your data first. EDA is basically just poking around the dataset — checking for missing values, weird outliers, understanding how different columns relate to each other

in this project i made two charts:
- **age vs price** → older cars = lower price (makes sense right)
- **fuel type vs price** → diesel cars tend to be priced higher on average

### 2. Feature Engineering
the dataset had a `Year` column (like 2015, 2018) but that's not very useful directly. what actually matters is *how old* the car is. so i created a new column called `Age` by doing:

```
Age = 2024 - Year
```

this is called feature engineering — turning raw data into something more meaningful for the model

### 3. One-Hot Encoding
machine learning models only understand numbers, they can't read text like "Petrol" or "Manual". so we convert categorical columns into 0s and 1s using a technique called **one-hot encoding**

for example, Fuel_Type becomes:
- `Fuel_Type_Diesel` → 1 if diesel, else 0
- `Fuel_Type_Petrol` → 1 if petrol, else 0

`pd.get_dummies()` handles this automatically which is nice

### 4. Train-Test Split
we split the dataset into two parts:
- **80% Training data** → the model learns from this
- **20% Testing data** → we check how well the model performs on data it's never seen

this is important because if you test on the same data you trained on, the model will just memorize it and look good but fail on real data. that's called **overfitting**

### 5. Random Forest Regressor 🌲
this is the actual ML model used here. let me explain it simply —

a **Decision Tree** is like a flowchart. it asks questions like:
- is the car older than 5 years? → yes → is kms > 80000? → ...
- and so on until it gives a price

a **Random Forest** is just *many decision trees* working together (100 trees in this project). each tree looks at a slightly different random subset of the data, and at the end all the trees vote and the average becomes the final prediction

why is this better than one tree? because one tree can overfit, but when 100 trees all slightly disagree and you average them out, you get a much more stable and accurate result. this is called **ensemble learning**

### 6. Model Persistence (saving the model)
after training, i used `joblib` to save the model as a `.pkl` file. this means you don't have to retrain every time — you just load the saved model and use it directly for predictions

---

## 📁 Project Structure

```
car-price-prediction/
│
├── data/
│   ├── car_data.csv               # original dataset 
│   └── car_data_cleaned.csv       # this gets auto generated after step 1
│
├── charts/
│   ├── age_vs_price.png           # scatter plot
│   └── fuel_vs_price.png          # bar chart
│
├── 1_eda_and_charts.py            # data analysis + chart generation
├── 2_model_training.py            # trains and saves the model
├── 3_predict_price.py             # use this to actually predict prices
│
├── car_price_model.pkl            # saved model (auto generated)
├── model_columns.pkl              # saved columns (auto generated)
└── README.md                      
```

---

## ⚙️ Requirements

make sure you have these installed —

```
pip install pandas scikit-learn matplotlib seaborn joblib
```

---

## 🚀 How to Run

run the files **in order**, don't skip steps or it'll break

**Step 1 — EDA & Charts**
```bash
python 1_eda_and_charts.py
```
this cleans the data and saves two charts in the `charts/` folder

**Step 2 — Train the Model**
```bash
python 2_model_training.py
```
trains a Random Forest model and saves it as `car_price_model.pkl`

**Step 3 — Predict Price**
```bash
python 3_predict_price.py
```
it'll ask you some inputs and then predict the car's selling price in lakhs

---

## 📊 Features Used

- Present Price (in lakhs)
- Kms Driven
- Car Age
- Fuel Type (Petrol / Diesel / CNG)
- Seller Type (Dealer / Individual)
- Transmission (Manual / Automatic)

---

## 📌 Note

> make sure to put `car_data.csv` inside the `data/` folder before running step 1, otherwise it throws an error

dataset used → [Vehicle Dataset from Cardekho](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho) (from Kaggle)

---

## 🛠️ Built With

- Python
- Pandas
- Scikit-learn
- Matplotlib & Seaborn
- Joblib

---
