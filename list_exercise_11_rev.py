L_value = ['a','b','e','f','i','o','u','k']

item_count = 0

for i_value in L_value:
    if i_value in "aeiouAEIOU":
        item_count += 1

print("Vowels =", item_count)