# 3.3 List Comprehension Lab

# (a) Squares of 1-20
squares_value = [x_value**2 for x_value in range(1, 21)]

# (b) Even numbers 1-50
evens_value = [x_value for x_value in range(1, 51) if x_value % 2 == 0]

# (c) Words longer than 4 characters
sample_sentence = "Python list comprehension makes writing clear and readable code easy"
long_words_value = [word_value for word_value in sample_sentence.split() if len(word_value) > 4]

# (d) Cubes of odd numbers 1-15
odd_cubes_value = [x_value**3 for x_value in range(1, 16) if x_value % 2 != 0]

print(f"(a) Squares (1-20)     : {squares_value}")
print(f"(b) Evens (1-50)       : {evens_value}")
print(f"(c) Words > 4 chars    : {long_words_value}")
print(f"(d) Odd Cubes (1-15)   : {odd_cubes_value}")