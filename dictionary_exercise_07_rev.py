# Checking if keys or values exist in a dictionary
user_data = {"username": "admin", "role": "editor", "active": True}

print("Is 'role' a key?", "role" in user_data)
print("Is 'email' a key?", "email" in user_data)
print("Is 'editor' a value?", "editor" in user_data.values())