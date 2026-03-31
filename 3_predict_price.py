import joblib
import os

if not os.path.exists('car_price_model.pkl'):
    print(" ERROR: Train the model first!")
    exit()

model = joblib.load('car_price_model.pkl')

print("\n Used Car Price Predictor\n")

# input
present_price = float(input("Enter present price (in lakhs): "))
kms = int(input("Enter kms driven: "))
age = int(input("Enter car age: "))

fuel_diesel = int(input("Diesel? (1=yes, 0=no): "))
fuel_petrol = int(input("Petrol? (1=yes, 0=no): "))
seller_individual = int(input("Individual seller? (1=yes, 0=no): "))
transmission_manual = int(input("Manual? (1=yes, 0=no): "))

# prediction
data = [[present_price, kms, 0, age,
         fuel_diesel, fuel_petrol,
         seller_individual, transmission_manual]]

prediction = model.predict(data)

print(f"\n Predicted Price: {prediction[0]:.2f} Lakhs")