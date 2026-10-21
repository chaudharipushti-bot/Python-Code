# Pairing two lists into a dictionary using zip()
keys_value = ["name", "age", "city"]
values_value = ["Priya", 22, "Surat"]

profile_value = dict(zip(keys_value, values_value))
print("Zipped Dictionary:", profile_value)