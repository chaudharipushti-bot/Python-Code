# 3.1 List Statistics
numbers_value = [23, 89, 12, 45, 67, 90, 34]

print(f"(a) Original List : {numbers_value}")
print(f"(b) Sorted List   : {sorted(numbers_value)}")
print(f"(c) Reversed List : {list(reversed(numbers_value))}")
print(f"(d) Maximum       : {max(numbers_value)}")
print(f"(e) Minimum       : {min(numbers_value)}")
print(f"(f) Sum           : {sum(numbers_value)}")
print(f"(g) Average       : {sum(numbers_value) / len(numbers_value):.2f}")