# 1.20 Star Pattern Collection
rows_value = 5

print("(a) Right-angled Triangle:")
for i_value in range(1, rows_value + 1):
    for j_value in range(i_value):
        print("*", end="")
    print()

print("\n(b) Inverted Triangle:")
for i_value in range(rows_value, 0, -1):
    for j_value in range(i_value):
        print("*", end="")
    print()

print("\n(c) Diamond Pattern:")
# Upper part
for i_value in range(1, rows_value + 1):
    for j_value in range(rows_value - i_value):
        print(" ", end="")
    for k_value in range(2 * i_value - 1):
        print("*", end="")
    print()
# Lower part
for i_value in range(rows_value - 1, 0, -1):
    for j_value in range(rows_value - i_value):
        print(" ", end="")
    for k_value in range(2 * i_value - 1):
        print("*", end="")
    print()