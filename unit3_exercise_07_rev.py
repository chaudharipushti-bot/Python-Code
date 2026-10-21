# 3.7 Set Operations Lab
set1_value = {x_value for x_value in range(1, 16) if x_value % 2 != 0}   # Odd numbers 1-15
set2_value = {x_value for x_value in range(1, 16) if x_value % 3 == 0}   # Multiples of 3 up to 15

print(f"Set 1 (Odds 1-15)         : {set1_value}")
print(f"Set 2 (Multiples of 3)     : {set2_value}")
print("-" * 50)
print(f"Union (Set1 | Set2)        : {set1_value | set2_value}")
print(f"Intersection (Set1 & Set2) : {set1_value & set2_value}")
print(f"Difference (Set1 - Set2)   : {set1_value - set2_value}")
print(f"Difference (Set2 - Set1)   : {set2_value - set1_value}")
print(f"Symmetric Difference       : {set1_value ^ set2_value}")