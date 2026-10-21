# 1.23 Sum of Series
N_value = int(input("Enter N: "))

sum_natural_value = 0
sum_squares_value = 0
sum_cubes_value = 0

for i_value in range(1, N_value + 1):
    sum_natural_value += i_value
    sum_squares_value += i_value**2
    sum_cubes_value += i_value**3

print(f"Sum of first {N_value} natural numbers: {sum_natural_value}")
print(f"Sum of squares of first {N_value} natural numbers: {sum_squares_value}")
print(f"Sum of cubes of first {N_value} natural numbers: {sum_cubes_value}")