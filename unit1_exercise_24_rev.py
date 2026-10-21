# 1.24 Number Pattern
rows_value = 5

print("Ascending Pattern:")
for i_value in range(1, rows_value + 1):
    for j_value in range(1, i_value + 1):
        print(j_value, end=" ")
    print()

print("\nDescending Pattern:")
for i_value in range(rows_value, 0, -1):
    for j_value in range(1, i_value + 1):
        print(j_value, end=" ")
    print()