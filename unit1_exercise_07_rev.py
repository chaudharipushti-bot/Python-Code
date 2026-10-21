# 1.7 Digit Extractor
num_value = int(input("Enter a 3-digit number: "))
hundreds_value = num_value // 100
tens_value = (num_value // 10) % 10
units_value = num_value % 10
digit_sum_value = hundreds_value + tens_value + units_value
digit_product_value = hundreds_value * tens_value * units_value
print(f"Hundreds Digit: {hundreds_value}")
print(f"Tens Digit: {tens_value}")
print(f"Units Digit: {units_value}")
print(f"Sum of Digits: {digit_sum_value}")
print(f"Product of Digits: {digit_product_value}")

