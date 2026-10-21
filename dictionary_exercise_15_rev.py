# Swapping keys and values
original_data = {"a": 1, "b": 2, "c": 3}
reversed_data = {v_value: k_value for k_value, v_value in original_data.items()}

print("Original:", original_data)
print("Inverted:", reversed_data)