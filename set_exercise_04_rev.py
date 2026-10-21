# Removing elements safely and unsafely
numbers_value = {10, 20, 30, 40, 50}

numbers_value.remove(20)       # Raises KeyError if not found
numbers_value.discard(99)      # Safe: Does nothing if element doesn't exist
popped_value = numbers_value.pop()   # Removes and returns an arbitrary element

print("Popped Element:", popped_value)
print("Remaining Set:", numbers_value)