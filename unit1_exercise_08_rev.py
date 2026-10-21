# 1.8 Unit Converter
km_value = float(input("Enter distance in kilometres: "))
metres_value = km_value * 1000
centimetres_value = km_value * 100000
miles_value = km_value * 0.621371
feet_value = km_value * 3280.84

print(f"Metres: {metres_value:.2f} m")
print(f"Centimetres: {centimetres_value:.2f} cm")
print(f"Miles: {miles_value:.4f} mi")
print(f"Feet: {feet_value:.2f} ft")
