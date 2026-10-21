vowel_chars = ('a','e','i','o','u','A','E','I','O','U')

text_value = input("Enter String: ")

item_count = 0

for ch_value in text_value:

    if ch_value in vowel_chars:
        item_count += 1

print("Vowels =", item_count)