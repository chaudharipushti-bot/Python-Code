# 1.18 Fibonacci Series
n_terms_value = int(input("Enter the number of terms: "))

first_value, second_value = 0, 1
item_count = 0

print("Fibonacci Series:")
while item_count < n_terms_value:
    print(first_value, end=" ")
    first_value, second_value = second_value, first_value + second_value
    item_count += 1
print()