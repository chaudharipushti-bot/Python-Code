# Generating dictionaries using comprehension
numbers_value = [1, 2, 3, 4, 5]

# Squares dictionary
squares_value = {x_value: x_value**2 for x_value in numbers_value}
# Even squares only
even_squares_value = {x_value: x_value**2 for x_value in numbers_value if x_value % 2 == 0}

print("Squares:", squares_value)
print("Even Squares:", even_squares_value)