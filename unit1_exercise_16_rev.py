# 1.16 Factorial Finder
n_value = int(input("Enter a non-negative integer: "))
fact_value = 1

if n_value < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i_value in range(1, n_value + 1):
        fact_value *= i_value
    print(f"{n_value}! = {fact_value}")