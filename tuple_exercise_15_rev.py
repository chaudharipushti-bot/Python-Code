t_value = (45,12,78,34,99,10,67)

max_value = t_value[0]
min_value = t_value[0]

for i_value in t_value:

    if i_value > max_value:
        max_value = i_value

    if i_value < min_value:
        min_value = i_value

print("Maximum =", max_value)
print("Minimum =", min_value)