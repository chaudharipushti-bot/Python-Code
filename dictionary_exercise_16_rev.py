# Initializing with default values and resetting dictionary
keys_value = ["a", "b", "c"]
default_dict_value = dict.fromkeys(keys_value, 0)
print("Default Dict:", default_dict_value)

default_dict_value.clear()
print("Cleared Dict:", default_dict_value)