# Merging two dictionaries using update() and union operator
dict1_value = {"a": 1, "b": 2}
dict2_value = {"b": 20, "c": 30}

# Method 1: update()
merged1_value = dict1_value.copy()
merged1_value.update(dict2_value)
print("Merged using update():", merged1_value)

# Method 2: '|' Operator
merged2_value = dict1_value | dict2_value
print("Merged using '|':", merged2_value)