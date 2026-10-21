# 1.10 BMI Calculator
weight_value = float(input("Enter weight in kg: "))
height_value = float(input("Enter height in metres: "))
bmi_value = weight_value / (height_value ** 2)
if bmi_value < 18.5:
    category_value = "Underweight"
elif 18.5 <= bmi_value <= 24.9:
    category_value = "Normal"
elif 25 <= bmi_value <= 29.9:
    category_value = "Overweight"
else:
    category_value = "Obese"
print(f"BMI: {bmi_value:.2f}")
print(f"Category: {category_value}")
