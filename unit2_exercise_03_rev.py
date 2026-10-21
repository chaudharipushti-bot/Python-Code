# 3.3 Factorial Function

def factorial_value(n_value):
    fact_value = 1
    for i_value in range(1, n_value + 1):
        fact_value *= i_value
    return fact_value

# Printing table headers with left-alignment
# :<10
# : mean format start
#  < mean left alignment
#  10 mean 10 spaces

print(f"{'Number':<10} | {'Factorial':<15}")
print("-" * 28)

# Displaying factorials for numbers 1 to 10
for i_value in range(1, 11):
    print(f"{i_value:<10} | {factorial_value(i_value):<15}")
