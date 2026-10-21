text_value = input("Enter String: ")

new_value = ""

for ch_value in text_value:

    if ch_value == 'o':
        new_value += "@"

    else:
        new_value += ch_value

print(new_value)