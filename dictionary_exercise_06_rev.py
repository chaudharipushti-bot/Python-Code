# Removing items using different deletion methods
data_value = {"a": 1, "b": 2, "c": 3, "d": 4}

removed_val_value = data_value.pop("b")  # Removes key 'b' and returns its value
last_item_value = data_value.popitem()  # Removes the last inserted key-value pair
del data_value["a"]               # Deletes key 'a'

print("Removed Val:", removed_val_value)
print("Last Item Removed:", last_item_value)
print("Remaining Dict:", data_value)