# 3.8 2D Matrix (Nested List)
matrix_value = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# (a) Display in tabular format
print("3x3 Matrix:")
for row_value in matrix_value:
    print(" ".join(f"{val_value:3d}" for val_value in row_value))

# (b) Calculate sum of each row
print("\nRow Sums:")
for idx_value, row_value in enumerate(matrix_value, start=1):
    print(f"  Row {idx_value} Sum: {sum(row_value)}")

# (c) Calculate sum of main diagonal
diagonal_sum_value = sum(matrix_value[i_value][i_value] for i_value in range(len(matrix_value)))
print(f"\nMain Diagonal Sum: {diagonal_sum_value}")