# 1.6 Salary Calculator
basic_salary_value = float(input("Enter basic salary: "))
hra_value = 0.20 * basic_salary_value
da_value = 0.10 * basic_salary_value

pf_value = 0.12 * basic_salary_value
gross_salary_value = basic_salary_value + hra_value + da_value
net_salary_value = gross_salary_value - pf_value
print(f"HRA: {hra_value:.2f}")
print(f"DA: {da_value:.2f}")
print(f"PF Deduction: {pf_value:.2f}")
print(f"Gross Salary: {gross_salary_value:.2f}")
print(f"Net Salary: {net_salary_value:.2f}")
