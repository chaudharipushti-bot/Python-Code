# Generating sets using comprehensions
numbers_value = range(1, 11)

even_squares_value = {x_value**2 for x_value in numbers_value if x_value % 2 == 0}
print("Even Squares Set:", even_squares_value)