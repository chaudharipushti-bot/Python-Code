# Checking subset/superset relationships
first_value = {1, 2}
second_value = {1, 2, 3, 4}

print("Is A subset of B?", first_value.issubset(second_value))
print("Is B superset of A?", second_value.issuperset(first_value))
print("Are A and B disjoint?", first_value.isdisjoint({5, 6}))