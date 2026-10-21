# 1.11 Percentage Calculator
m1_value = float(input("Enter marks for Subject 1: "))
m2_value = float(input("Enter marks for Subject 2: "))
m3_value = float(input("Enter marks for Subject 3: "))
m4_value = float(input("Enter marks for Subject 4: "))
m5_value = float(input("Enter marks for Subject 5: "))
total_value = m1_value + m2_value + m3_value + m4_value + m5_value
percentage_value = (total_value / 500.0) * 100
average_value = total_value / 5.0
print(f"\nTotal Marks: {total_value:.2f}/500")
print(f"Percentage: {percentage_value:.2f}%")
print(f"Average Marks: {average_value:.2f}")
