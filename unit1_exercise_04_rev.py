# 1.4 Temperature Converter
celsius_value = float(input("Enter temperature in Celsius: "))
fahrenheit_value = (celsius_value * 9 / 5) + 32
kelvin_value = celsius_value + 273.15
print(f"Temperature in Fahrenheit: {fahrenheit_value:.2f}°F")
print(f"Temperature in Kelvin: {kelvin_value:.2f}K")
