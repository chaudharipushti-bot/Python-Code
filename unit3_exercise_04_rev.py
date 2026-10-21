# 3.4 Tuple Operations
marks_data = (85, 92, 78, 65, 90)

print(f"Original Tuple: {marks_data}")
print(f"Indexing (First Element): {marks_data[0]}")
print(f"Slicing (Middle 3)      : {marks_data[1:4]}")
print(f"Length                  : {len(marks_data)}")

# Demonstrating Immutability (TypeError)
print("\nAttempting to modify tuple element:")
try:
    marks_data[0] = 95
except TypeError as e:
    print(f"  TypeError caught successfully: {e}")

# Modifying via List conversion
temp_list_value = list(marks_data)
temp_list_value[0] = 95
marks_data = tuple(temp_list_value)
print(f"Tuple after modification via List conversion: {marks_data}")