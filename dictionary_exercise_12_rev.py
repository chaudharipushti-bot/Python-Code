# Sorting dictionary items by keys and values
marks_data = {"Rahul": 85, "Aniket": 92, "Bhavik": 78}

# Sort by keys
sorted_by_key_value = dict(sorted(marks_data.items()))
# Sort by values descending
sorted_by_val_value = dict(sorted(marks_data.items(), key=lambda item_value: item_value[1], reverse=True))

print("Sorted by Name:", sorted_by_key_value)
print("Sorted by Marks (Desc):", sorted_by_val_value)