# Working with immutable sets
regular_set = {1, 2, 3}
frozen_items = frozenset([3, 4, 5])

print("Frozenset:", frozen_items)
# Useful as dictionary keys or set elements
frozen_lookup = {frozen_items: "Immutable Key"}
print(frozen_lookup)