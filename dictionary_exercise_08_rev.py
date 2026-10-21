# Looping through keys, values, and key-value pairs
scores_value = {"Math": 90, "Science": 85, "English": 88}

print("Keys:")
for k_value in scores_value.keys():
    print(k_value, end=" ")

print("\nValues:")
for v_value in scores_value.values():
    print(v_value, end=" ")

print("\nItems:")
for k_value, v_value in scores_value.items():
    print(f"{k_value}: {v_value}")