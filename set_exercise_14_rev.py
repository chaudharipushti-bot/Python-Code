# Modifying sets directly in place
s1_value = {1, 2, 3, 4}
s2_value = {3, 4, 5, 6}

s1_value.intersection_update(s2_value)  # s1 now contains only elements common to both
print("s1 after intersection_update:", s1_value)