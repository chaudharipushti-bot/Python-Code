# 3.10 Duplicate Remover
nums_list1_value = [10, 20, 30, 20, 40, 10, 50, 30, 60]
nums_list2_value = [30, 40, 70, 80]

print(f"List 1: {nums_list1_value}")
print(f"List 2: {nums_list2_value}")

# (a) Remove duplicates using set
unique_list_value = list(set(nums_list1_value))
print(f"\n(a) Duplicates Removed (List 1): {unique_list_value}")

# (b) Elements in List 1 but not List 2
diff_elements_value = list(set(nums_list1_value) - set(nums_list2_value))
print(f"(b) In List 1 but not List 2   : {diff_elements_value}")

# (c) Count occurrences of each number in List 1
counts_value = {num_value: nums_list1_value.item_count(num_value) for num_value in set(nums_list1_value)}
print("(c) Element Occurrences (List 1):")
for num_value, item_count in sorted(counts_value.items()):
    print(f"    Element {num_value:2d} -> Appears {item_count} time(s)")