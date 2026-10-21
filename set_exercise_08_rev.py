# Elements present in first set but not second
set_a_value = {1, 2, 3, 4, 5}
set_b_value = {4, 5, 6, 7}

diff_a_b_value = set_a_value - set_b_value
diff_b_a_value = set_b_value - set_a_value

print("Set A - Set B:", diff_a_b_value)
print("Set B - Set A:", diff_b_a_value)