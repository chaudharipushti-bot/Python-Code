# 3.4 Multi-Return Function

def stats_value(first_value, second_value, third_value):
    total_sum_value = first_value + second_value + third_value
    average_value = total_sum_value / 3.0
    min_value = min(first_value, second_value, third_value)
    max_value = max(first_value, second_value, third_value)
    return total_sum_value, average_value, min_value, max_value

# Unpacking the returned tuple
text_value, first_value, mn_value, mx_value = stats_value(15, 42, 8)

print(f"Sum: {text_value}")
print(f"Average: {first_value:.2f}")
print(f"Minimum: {mn_value}")
print(f"Maximum: {mx_value}")
