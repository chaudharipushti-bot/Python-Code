# 1.3 Simple Interest Calculator
P_value = float(input("Enter Principal amount (P): "))
R_value = float(input("Enter Rate of Interest (R): "))
T_value = float(input("Enter Time in years (T): "))
SI_value = (P_value * R_value * T_value) / 100
total_amount_value = P_value + SI_value
print(f"Simple Interest: {SI_value:.2f}")
print(f"Total Amount: {total_amount_value:.2f}")
