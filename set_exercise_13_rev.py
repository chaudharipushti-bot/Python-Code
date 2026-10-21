# Cleaning duplicate values using list -> set conversion
duplicates_list_value = [10, 20, 10, 30, 20, 40, 50, 40]

unique_set_value = set(duplicates_list_value)
cleaned_list_value = list(unique_set_value)

print("Original List:", duplicates_list_value)
print("Cleaned List :", cleaned_list_value)