# 1.13 Number Classifier
num_value = float(input("Enter a number: "))

# (a) Positive/Negative/Zero
if num_value > 0:
    pos_neg_value = "Positive"
elif num_value < 0:
    pos_neg_value = "Negative"
else:
    pos_neg_value = "Zero"

# (b) Even or Odd
even_odd_value = "Even" if num_value % 2 == 0 else "Odd"

# (c) Divisible by 5
div_by_5_value = "Divisible by 5" if num_value % 5 == 0 else "Not divisible by 5"

print(f"Result: {pos_neg_value}, {even_odd_value}, {div_by_5_value}")