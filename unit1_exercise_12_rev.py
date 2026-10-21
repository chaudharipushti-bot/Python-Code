# 1.12 Electric Bill Calculator
prev_reading_value = float(input("Enter previous meter reading: "))
curr_reading_value = float(input("Enter current meter reading: "))
units_consumed_value = curr_reading_value - prev_reading_value
fixed_charge_value = 100.0
total_bill_value = (units_consumed_value * 5.50) + fixed_charge_value
print(f"Units Consumed: {units_consumed_value:.2f}")
print(f"Total Electric Bill: ₹{total_bill_value:.2f}")

